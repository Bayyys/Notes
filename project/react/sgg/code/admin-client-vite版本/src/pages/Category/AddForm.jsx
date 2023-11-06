import React, { useState } from "react";
import { Form, Input, TreeSelect } from "antd";
const { Item } = Form;

export default function AddForm({ form, categorys, parentId }) {
  const treeData = [
    {
      value: "一级分类",
      title: "一级分类",
      _id: "0",
      children: [],
    },
  ];

  treeData[0].children = categorys.map((item) => {
    return {
      value: item.name,
      title: item.name,
      _id: item._id,
    };
  });

  return (
    <Form form={form} preserve={false}>
      <Item
        label="所属分类"
        name="kind"
        initialValue={
          parentId === "0"
            ? "一级分类"
            : categorys.find((item) => item._id === parentId).name
        }
      >
        <TreeSelect
          treeData={treeData}
          treeLine
          showSearch
          treeDefaultExpandAll
        />
      </Item>
      <Item
        label="品类名称"
        name="name"
        rules={[{ required: true, message: "分类名称不能为空" }]}
      >
        <Input placeholder="请输入分类名称"></Input>
      </Item>
    </Form>
  );
}
