import React from "react";
import { Card, Form, Input, Cascader, Upload, Button, message } from "antd";
import { ArrowLeftOutlined } from "@ant-design/icons";
import { useLocation, useNavigate } from "react-router-dom";
import { useForm } from "antd/es/form/Form";
const { Item } = Form;
const { TextArea } = Input;

// 产品的添加和更新的路由组件
export default function ProductAddUpdate() {
  const navigate = useNavigate();
  const [form] = useForm();

  const {
    state: { product },
  } = useLocation();

  const validateForm = () => {
    form
      .validateFields()
      .then((values) => {
        console.log(values);
      })
      .catch((errorInfo) => {
        message.error("表单验证失败");
      });
  };

  const title = (
    <span>
      <Button
        type="link"
        icon={<ArrowLeftOutlined />}
        onClick={() => {
          navigate(-1);
        }}
      ></Button>
      <span>{product ? "修改商品" : "添加商品"}</span>
    </span>
  );

  const formItemLayout = {
    labelCol: { span: 3 }, // 左侧 label 的宽度
    labelAlign: "left", // label 文字对齐方式
    wrapperCol: { span: 8 }, // 右侧包裹的宽度
  };

  return (
    <Card title={title}>
      <Form {...formItemLayout} form={form} validateTrigger="onBlur">
        <Item
          label="商品名称"
          name="name"
          rules={[
            { required: true, message: "商品名称必须输入" },
            {
              // 自定义校验规则: 长度必须大于等于 2 小于等于 6
              validator: (_, value) => {
                if (value.length >= 2 && value.length <= 6) {
                  return Promise.resolve();
                } else {
                  return Promise.reject(
                    new Error("长度必须大于等于 2 小于等于 6")
                  );
                }
              },
            },
          ]}
          validateFirst
          hasFeedback
        >
          <Input placeholder="请输入商品名称" allowClear />
        </Item>
        <Item label="商品描述" name="desc" wrapperCol={{ span: 15 }}>
          <TextArea
            placeholder="请输入商品描述"
            autoSize={{ minRows: 3 }}
            showCount
            maxLength={100}
          />
        </Item>
        <Item
          label="商品价格"
          name="price"
          rules={[
            {
              required: true,
              message: "商品价格必须输入",
            },
            {
              validator: (_, value) => {
                if (value <= 0) {
                  return Promise.reject(new Error("价格必须大于 0"));
                } else if (value >= 9999) {
                  return Promise.reject(new Error("价格必须小于 9999"));
                } else {
                  return Promise.resolve();
                }
              },
            },
          ]}
          validateFirst
          hasFeedback
        >
          <Input type="number" defaultValue={0} addonAfter="元" />
        </Item>
        <Item label="商品分类">
          <div>图书 --{">"} 科幻</div>
        </Item>
        <Item label="商品图片">
          <div>商品图片</div>
        </Item>
        <Item label="商品详情">
          <div>商品详情</div>
        </Item>
        <Button
          type="primary"
          onClick={() => {
            validateForm();
          }}
        >
          提交
        </Button>
      </Form>
    </Card>
  );
}
