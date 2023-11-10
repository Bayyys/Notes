import React, { useEffect, useState } from "react";
import ReactQuill from "react-quill";
import "react-quill/dist/quill.snow.css";

export default function RichTextEditor(props) {
  const [value, setValue] = useState("");
  const { value: detail } = props;
  const handleChange = (value) => {
    setValue(value);
    props.onChange(value);
  };

  const modules = {
    toolbar: [
      [{ header: [1, 2, 3, 4, false] }], // 标题
      ["bold", "italic", "underline", "strike", "blockquote", "code-block"], // 粗体 斜体 下划线 删除线 引用 代码块
      [
        { list: "ordered" }, // 有序列表
        { list: "bullet" }, // 无序列表
        { script: "sub" }, // 上标/下标
        { script: "super" },
        { indent: "-1" }, // 缩进
        { indent: "+1" },
        { align: [] }, // 对齐方式
      ],
      [{ size: ["small", false, "large", "huge"] }, { font: [] }], // 字体大小 字体
      [{ color: [] }, { background: [] }], // 字体颜色 字体背景颜色
      [("link", "image"), "code-block"], // 链接 图片 代码块
      ["clean"], // 清除字体样式
    ],
  };

  useEffect(() => {
    setValue(detail);
  }, [detail]);

  return (
    <div>
      <ReactQuill
        theme="snow"
        value={value}
        modules={modules}
        onChange={handleChange}
        style={{ height: 100 }}
      ></ReactQuill>
    </div>
  );
}
