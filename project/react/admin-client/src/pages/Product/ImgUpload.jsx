import React, { useCallback, useEffect, useState } from "react";
import { Modal, Upload, message } from "antd";
import { PlusOutlined } from "@ant-design/icons";
import { reqDeleteImg, reqCheckImg } from "../../api/api";

const getBase64 = (file) =>
  new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => resolve(reader.result);
    reader.onerror = (error) => reject(error);
  });

export default function ImgUpload(props) {
  const [messageApi, messageContextHolder] = message.useMessage();
  const [previewOpen, setPreviewOpen] = useState(false); // 是否显示大图预览
  const [previewImage, setPreviewImage] = useState(""); // 大图的url
  const [previewTitle, setPreviewTitle] = useState(""); // 大图的标题
  const [fileList, setFileList] = useState([]); // 所有已上传图片的数组
  const [hasErrorImg, setHasErrorImg] = useState(false); // 是否有错误图片
  const { imgs } = props;

  const handlePreview = async (file) => {
    if (!file.url && !file.preview) {
      file.preview = await getBase64(file.originFileObj);
    }
    setPreviewImage(file.url || file.preview);
    setPreviewOpen(true);
    setPreviewTitle(
      file.name || file.url.substring(file.url.lastIndexOf("/") + 1)
    );
  };

  /**
   * file: 当前操作的图片文件(上传/删除)
   * fileList: 所有已上传图片文件对象的数组
   */
  const handleChange = async ({ file, fileList }) => {
    if (file.status === "done") {
      const { status } = file.response;
      if (status === 0) {
        messageApi.success("上传图片成功");
        const { name, url } = file.response.data;
        file.name = name; // 最新版中, file 与 fileList 中的文件对象是同一个
        file.url = url;
        if (hasErrorImg) {
          // 有错误图片, 则删除错误图片
          const newList = fileList.filter((file) => file.name !== "error.jpg");
          fileList = newList;
        }
      } else {
        messageApi.error("上传图片失败");
      }
    } else if (file.status === "removed") {
      if (file.name !== "error.jpg") {
        try {
          const response = await reqDeleteImg(file.name);
          if (response.status === 0) {
            messageApi.success("删除图片成功");
          } else {
            messageApi.error("删除图片失败");
          }
        } catch (error) {
          messageApi.error("删除图片失败");
        }
      }
    }
    setFileList(fileList);
    props.onChange(fileList); // 将fileList传递给父组件
  };

  const initImgList = useCallback(async () => {
    if (imgs && imgs.length > 0) {
      const fileList = imgs.map((name, index) => {
        let newName = name;
        try {
          const response = reqCheckImg(name); // 检查图片是否存在
          if (response.status !== 0) {
            newName = "error.jpg"; // 不存在则显示默认图片
            setHasErrorImg(true); // 标记有错误图片
          }
        } catch (error) {
          newName = "error.jpg"; // 不存在则显示默认图片
          setHasErrorImg(true); // 标记有错误图片
        }
        return {
          uid: -index,
          name: newName,
          status: "done",
          url: `http://localhost:5000/upload/${newName}`,
        };
      });
      // 过滤, 只保留1份 error.jpg
      const newFileList = fileList.filter(
        (file) => file.name !== "error.jpg" || fileList.length === 1
      );
      setFileList(newFileList);
    }
  }, [imgs]);

  useEffect(() => {
    initImgList();
  }, [initImgList]);

  return (
    <>
      {messageContextHolder}
      <Upload
        action="/api/manage/img/upload" // 上传图片的接口地址
        accept="image/*" // 只接收图片格式
        name="image" // 请求参数名
        listType="picture-card"
        fileList={fileList}
        onChange={handleChange}
        onPreview={handlePreview}
      >
        {fileList.length >= 3 ? null : (
          <div>
            <PlusOutlined />
            <div style={{ marginTop: 8 }}>Upload</div>
          </div>
        )}
      </Upload>
      <Modal
        title={previewTitle}
        footer={null}
        onCancel={() => {
          setPreviewOpen(false);
        }}
        open={previewOpen}
      >
        <img src={previewImage} alt="example" style={{ width: "100%" }} />
      </Modal>
    </>
  );
}
