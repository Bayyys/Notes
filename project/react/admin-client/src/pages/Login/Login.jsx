import React from "react";
import { useNavigate } from "react-router-dom";
import { LockOutlined, UserOutlined } from "@ant-design/icons";
import { Button, Form, Input, message } from "antd";

import "./index.css";
import logo from "./images/logo.png";
import { reqLogin } from "../../api";

export default function Login() {
  const navigate = useNavigate();

  const onFinish = async (values) => {
    const { username, password } = values;
    try {
      const res = await reqLogin(username, password); // 成功: {statys:0,data:user} 失败: {statys:1,msg:'xxx'}
      if (res.status === 0) {
        message.success("登录成功");
        navigate("/admin", { replace: true });
      } else {
        message.error("用户名或密码错误, 登录失败!");
      }
    } catch (error) {
      console.log("-----");
    }
  };

  const onFinishFailed = (errorInfo) => {
    console.log("Failed:", errorInfo);
  };

  const pwdRule = [
    { required: true, message: "请输入密码!" },
    { max: 12, message: "密码最大长度为12位" },
    { min: 4, message: "密码最小长度为4位" },
    {
      validator: (_, value) => {
        return /^[a-zA-Z0-9_]+$/.test(value)
          ? Promise.resolve()
          : Promise.reject("密码必须是英文、数字或下划线组成");
      },
    },
  ];

  return (
    <div className="login">
      <header className="login-header">
        <img src={logo} alt="logo" />
        <h1>后台管理系统</h1>
      </header>
      <section className="login-content">
        <h2>用户登录</h2>
        <Form
          name="login"
          className="login-form"
          initialValues={{ remember: true }}
          onFinish={onFinish}
          onFinishFailed={onFinishFailed}
        >
          <Form.Item
            name="username"
            initialValue={"admin"}
            rules={[
              { required: true, message: "请输入用户名!" },
              { max: 12, message: "用户名最大长度为12位" },
              { min: 4, message: "用户名最小长度为4位" },
              {
                pattern: /^[a-zA-Z0-9_]+$/,
                message: "用户名必须是英文、数字或下划线组成",
              },
            ]}
            validateFirst
            validateDebounce={100}
            hasFeedback
          >
            <Input
              prefix={<UserOutlined className="site-form-item-icon" />}
              placeholder="用户名"
            />
          </Form.Item>
          <Form.Item
            name="password"
            initialValue={"admin"}
            rules={pwdRule}
            hasFeedback
            validateDebounce={100}
            validateFirst
          >
            <Input
              prefix={<LockOutlined className="site-form-item-icon" />}
              type="password"
              placeholder="密码"
            />
          </Form.Item>
          <Form.Item>
            <Button
              type="primary"
              htmlType="submit"
              className="login-form-button"
              style={{ width: "100%" }}
            >
              登录
            </Button>
          </Form.Item>
        </Form>
      </section>
    </div>
  );
}
