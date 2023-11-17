import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { LockOutlined, UserOutlined } from "@ant-design/icons";
import { Button, Form, Input, message } from "antd";

import "./Login.scss";
import logo from "../../assets/images/logo.png";
import { useSelector, useDispatch } from "react-redux";
import { login } from "../../redux/user";

export default function Login() {
  const [messageApi, contextHolder] = message.useMessage();
  const navigate = useNavigate();
  const user = useSelector((state) => state.user);
  const dispatch = useDispatch();

  /* ------ 表单提交功能 ------ */
  const onFinish = async (values) => {
    const { username, password } = values;
    dispatch(login(username, password)); // 发送登录的异步请求, 请求后会自动刷新页面
  };

  const onFinishFailed = (errorInfo) => {
    console.log("Failed:", errorInfo);
    messageApi.error("表单验证失败: " + errorInfo.errorFields[0].errors[0]);
  };

  /* ------ 表单验证规则 ------ */
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

  useEffect(() => {
    /* ------ 如果用户已经登录, 自动跳转到管理界面 ------ */
    if (user.user && user.user._id) {
      navigate("/", { replace: true });
    }
  }, [user, navigate, dispatch]);

  return (
    <div className="login">
      <header className="login-header">
        <img src={logo} alt="logo" />
        <h1>后台管理系统</h1>
      </header>
      <section className="login-content">
        <div className={user.msg ? "error-msg show" : "error-msg"}>
          {user.msg}
        </div>
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
      {contextHolder}
    </div>
  );
}
