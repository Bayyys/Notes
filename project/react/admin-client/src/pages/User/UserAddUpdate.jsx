import React from "react";
import { Modal, Form, Input, Select } from "antd";
const { Item } = Form;
const { Option } = Select;

export default function UserModal({ open, setOpen, roles, user, handleForm }) {
  const [form] = Form.useForm();

  const handleAddOk = () => {
    form
      .validateFields()
      .then((values) => {
        handleForm({ ...user, ...values });
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <Modal
      destroyOnClose={true}
      open={open}
      onCancel={() => {
        setOpen(false);
      }}
      onOk={handleAddOk}
      title="添加角色"
    >
      <Form
        form={form}
        preserve={false}
        labelCol={{ span: 4 }}
        initialValues={user}
      >
        <Item
          label="用户名"
          name="username"
          rules={[
            {
              required: true,
              message: "用户名必须输入",
            },
          ]}
        >
          <Input placeholder="请输入用户名"></Input>
        </Item>
        {user._id ? null : (
          <Item
            label="密码"
            name="password"
            rules={[{ required: true, message: "密码必须输入" }]}
          >
            <Input.Password placeholder="请输入密码"></Input.Password>
          </Item>
        )}
        <Item
          label="手机号码"
          name="phone"
          rules={[{ required: true, message: "手机号码必须输入" }]}
        >
          <Input placeholder="请输入手机号码"></Input>
        </Item>
        <Item
          label="邮箱"
          name="email"
          rules={[{ required: true, message: "邮箱必须输入" }]}
        >
          <Input placeholder="请输入邮箱"></Input>
        </Item>
        <Item
          label="角色"
          name="role_id"
          rules={[
            {
              required: true,
              message: "角色必须选择",
            },
          ]}
        >
          <Select placeholder="请选择角色">
            {roles.map((role) => {
              return (
                <Option key={role._id} value={role._id}>
                  {role.name}
                </Option>
              );
            })}
          </Select>
        </Item>
      </Form>
    </Modal>
  );
}
