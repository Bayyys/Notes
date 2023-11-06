import React, { useCallback, useEffect, useState } from "react";
import { Card, Table, Button, message, Modal, Form } from "antd";
import { ArrowRightOutlined } from "@ant-design/icons";
import { PlusOutlined } from "@ant-design/icons";
import { reqCategorys, reqAddCategory, reqUpdateCategory } from "../../api/api";
import UpdateForm from "./UpdateForm";
import AddForm from "./AddForm";

export default function Category() {
  const [categorys, setCategorys] = useState([]); // 一级分类列表
  const [subCategorys, setSubCategorys] = useState([]); // 二级分类列表
  const [loading, setLoading] = useState(true); // 是否正在获取数据中
  const [parentId, setParentId] = useState("0"); // 当前需要显示的分类列表的父分类ID
  const [parentName, setParentName] = useState(""); // 当前需要显示的分类列表的父分类名称
  const [mTitle, setMTitle] = useState(""); // Card的标题
  const [mContent, setMContent] = useState(""); // Card的内容
  const [mOpen, setMOpen] = useState(false); // Card的打开状态
  const [category, setCategory] = useState({}); // 当前需要修改的分类
  const [form] = Form.useForm();

  // 获取一级/二级分类列表
  const showCategorys = useCallback(
    async (new_parentId) => {
      setLoading(false);
      // 等待一秒后执行后续代码
      new_parentId = new_parentId ? new_parentId : parentId;
      setParentId(new_parentId);
      try {
        const res = await reqCategorys(new_parentId);
        if (new_parentId === "0") setCategorys(res.data);
        else setSubCategorys(res.data);
      } catch (error) {
        message.error(error.message);
      }
      setLoading(false);
    },
    [parentId]
  );

  // 获取二级分类列表
  const showSubCategory = (parent) => {
    setLoading(false);
    setParentName(parent.name);
    setParentId(parent._id);
    showCategorys(parent._id);
  };

  // 更新分类
  const updateCategory = async (_id, name) => {
    try {
      const res = await reqUpdateCategory({
        categoryId: _id,
        categoryName: name,
      });
      if (res.status === 0) {
        message.success("更新分类成功");
        showCategorys();
      }
    } catch (error) {
      message.error("更新分类失败");
    }
  };

  // 添加分类
  const addCategory = async (kind, name) => {
    const addPId =
      kind === "一级分类"
        ? "0"
        : categorys.find((item) => item.name === kind)._id;
    try {
      const res = await reqAddCategory(name, addPId);
      if (res.status === 0) {
        message.success("添加分类成功");
        showCategorys();
      }
    } catch (error) {
      message.error("添加分类失败");
    }
    if (addPId !== parentId) {
      if (addPId === "0") {
        showCategorys("0");
      } else {
        showSubCategory(categorys.find((item) => item._id === addPId));
      }
    }
  };

  // 显示添加/修改分类的对话框
  const showCategoryModal = (category) => {
    setMTitle(category ? `修改<${category.name}>分类` : "添加分类");
    setMContent(
      category ? (
        <UpdateForm
          form={form}
          category={category}
          categorys={parentId === "0" ? categorys : subCategorys}
        />
      ) : (
        <AddForm form={form} categorys={categorys} parentId={parentId} />
      )
    );
    setMOpen(true);
    setCategory(category);
  };

  // 点击对话框的确定按钮
  const handlerOnOk = () => {
    form
      .validateFields()
      .then((values) => {
        const { kind, name } = form.getFieldsValue();
        category ? updateCategory(category._id, name) : addCategory(kind, name);
        setMOpen(false);
      })
      .catch((err) => {});
  };

  // 表格列的配置
  const columns = [
    {
      title: "分类名称",
      dataIndex: "name",
      key: "name",
    },
    {
      title: "operation",
      dataIndex: "operation",
      key: "operation",
      width: "25%",
      render: (_, record) => (
        <>
          <Button type="link" onClick={() => showCategoryModal(record)}>
            修改分类
          </Button>
          {
            parentId === "0" ? (
              <Button
                type="link"
                onClick={() => {
                  showSubCategory(record);
                }}
              >
                查看子分类
              </Button>
            ) : null // 如果是二级分类列表, 不显示"查看子分类"按钮
          }
        </>
      ),
    },
  ];

  // Card的标题
  const title =
    parentId === "0" ? (
      "品类列表"
    ) : (
      <span>
        <Button
          type="link"
          style={{ fontSize: 16 }}
          onClick={() => showCategorys("0")}
        >
          品类列表
        </Button>
        <ArrowRightOutlined style={{ marginRight: "5px" }} />

        <span>{parentName}</span>
      </span>
    );

  // Card的右侧
  const extra = (
    <Button
      type="primary"
      icon={<PlusOutlined />}
      onClick={() => {
        showCategoryModal();
      }}
    >
      添加
    </Button>
  );

  useEffect(() => {
    // 初始化表格数据
    showCategorys("0");
  }, [showCategorys]);

  return (
    <Card title={title} extra={extra}>
      <Table
        columns={columns}
        dataSource={parentId === "0" ? categorys : subCategorys}
        bordered
        loading={loading}
        pagination={{ defaultPageSize: 5, showQuickJumper: true }}
        rowKey={(record) => record._id}
      />
      <Modal
        destroyOnClose={true}
        okButtonProps={{ disabled: false }}
        open={mOpen}
        title={mTitle}
        onOk={handlerOnOk}
        onCancel={() => {
          setMOpen(false);
        }}
      >
        {mContent}
      </Modal>
    </Card>
  );
}
