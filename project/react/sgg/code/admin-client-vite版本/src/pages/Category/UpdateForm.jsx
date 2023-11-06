import React from "react";
import { Form, Input } from "antd";
const { Item } = Form;

export default function UpdateForm({ form, category, categorys }) {
  return (
    <Form
      form={form}
      preserve={false} // 表单重置后清除表单项的值
    >
      <Item
        label="品类名称"
        name="name"
        initialValue={category.name}
        rules={[
          {
            validator: (_, value) =>
              value.trim()
                ? Promise.resolve()
                : Promise.reject("分类名称不能为空"),
          },
          {
            validator: (_, value) => {
              if (value.trim() === category.name) return Promise.resolve();
              const result = categorys.find(
                (item) => item.name === value.trim()
              );
              return result
                ? Promise.reject("分类名称已存在")
                : Promise.resolve();
            },
          },
        ]}
        validateFirst
        hasFeedback
      >
        <Input placeholder="请输入分类名称"></Input>
      </Item>
    </Form>
  );
}
