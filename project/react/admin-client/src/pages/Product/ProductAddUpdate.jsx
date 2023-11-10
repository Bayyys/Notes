import React, { useCallback, useEffect, useMemo, useState } from "react";
import { Card, Form, Input, Cascader, Button, message } from "antd";
import { ArrowLeftOutlined } from "@ant-design/icons";
import { useLocation, useNavigate } from "react-router-dom";
import { useForm } from "antd/es/form/Form";
import ImgUpload from "./ImgUpload";
import { reqCategorys } from "../../api/api";

const { Item } = Form;
const { TextArea } = Input;

// 产品的添加和更新的路由组件
export default function ProductAddUpdate() {
  const [cascaderOptions, setCascaderOptions] = useState([]);
  const navigate = useNavigate();
  const [form] = useForm();
  const pIds = useMemo(() => [], []);

  const {
    state: { product },
  } = useLocation();
  const { pCategoryId, categoryId } = product;

  const validateForm = () => {
    console.log(form.getFieldsValue());
    // form
    //   .validateFields()
    //   .then((values) => {
    //     console.log(values.category);
    //   })
    //   .catch((errorInfo) => {
    //     message.error("表单验证失败");
    //   });
  };

  const getChildCategorys = useCallback(async (parentId) => {
    try {
      const result = await reqCategorys(parentId);
      if (result.status === 0) {
        return result.data;
      }
    } catch (error) {}
  }, []);

  const initCategorys = useCallback(
    async (categorys) => {
      const options = categorys.map((item) => ({
        value: item._id,
        label: item.name,
        isLeaf: false,
      }));

      if (pCategoryId !== "0") {
        const subCategorys = await getChildCategorys(pCategoryId);
        const childOptions = subCategorys.map((item) => ({
          value: item._id,
          label: item.name,
          isLeaf: true,
        }));
        options.forEach((item) => {
          if (item.value === pCategoryId) {
            item.children = childOptions;
            return;
          }
        });
      }
      setCascaderOptions(options);
    },
    [getChildCategorys, pCategoryId]
  );

  const getFirstCategorys = useCallback(
    async (parentId) => {
      try {
        const result = await reqCategorys(parentId);
        if (result.status === 0) {
          const categorys = result.data;
          initCategorys(categorys);
        }
      } catch (error) {}
    },
    [initCategorys]
  );

  const loadData = async (selectedOptions) => {
    const targetOption = selectedOptions[selectedOptions.length - 1];
    try {
      const result = await getChildCategorys(targetOption.value);
      if (result && result.length > 0) {
        targetOption.children = result.map((item) => ({
          value: item._id,
          label: item.name,
          isLeaf: true,
        }));
      } else {
        targetOption.isLeaf = true;
      }
    } catch (error) {
      message.error("加载数据失败");
    }
    setCascaderOptions([...cascaderOptions]);
  };

  const initpid = useCallback(() => {
    // 清空 pIDs
    pIds.length = 0;
    if (pCategoryId === "0") {
      pIds.push(categoryId);
    } else {
      pIds.push(pCategoryId);
      pIds.push(categoryId);
    }
  }, [categoryId, pCategoryId, pIds]);

  const normFile = (e) => {
    return e
      ?.filter((item) => item.name !== "error.jpg")
      .map((item) => item.name);
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
      <span>{product.name ? "修改商品" : "添加商品"}</span>
    </span>
  );

  const formItemLayout = {
    labelCol: { span: 3 }, // 左侧 label 的宽度
    labelAlign: "left", // label 文字对齐方式
    wrapperCol: { span: 8 }, // 右侧包裹的宽度
  };

  useEffect(() => {
    getFirstCategorys("0");
    initpid();
  }, [getFirstCategorys, initpid]);

  return (
    <Card title={title}>
      <Form
        {...formItemLayout}
        form={form}
        validateTrigger="onBlur"
        initialValues={product}
      >
        <Item
          label="商品名称"
          name="name"
          rules={[{ required: true, message: "商品名称必须输入" }]}
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
          <Input type="number" addonAfter="元" />
        </Item>
        <Item
          label="商品分类"
          name="category"
          rules={[
            {
              required: true,
              message: "商品分类必须选择",
            },
          ]}
          initialValue={pIds}
        >
          <Cascader
            options={cascaderOptions}
            loadData={loadData}
            placeholder="请选择商品分类"
          />
        </Item>
        <Item
          label="商品图片"
          name="imgs"
          valuePropName="fileList"
          getValueFromEvent={normFile}
        >
          <ImgUpload imgs={product.imgs} />
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
