import React, { useCallback, useEffect, useState } from "react";
import { Button, Card, List, message } from "antd";
import { ArrowLeftOutlined } from "@ant-design/icons";
import { useLocation, useNavigate } from "react-router-dom";

import "./product.scss";
import { reqCategory } from "../../api/api";
const Item = List.Item;

// 产品详情的路由组件
export default function ProductDetail() {
  const [parentNameFirst, setParentNameFirst] = useState(""); // 一级分类列表
  const [parentNameSecond, setParentNameSecond] = useState(""); // 二级分类列表
  const navigate = useNavigate();
  const { product: p } = useLocation().state;

  const getCategory = useCallback(async () => {
    try {
      if (p.pCategoryId === "0") {
        setParentNameFirst("一级分类");
      } else {
        const first = await reqCategory(p.pCategoryId);
        if (first.status === 0) {
          setParentNameFirst(first.data.name);
        }
      }
      const second = await reqCategory(p.categoryId);
      if (second.status === 0) {
        setParentNameSecond(second.data.name);
      }
    } catch (error) {
      message.error("获取分类失败");
    }
  }, [p.pCategoryId, p.categoryId]);

  const title = (
    <span>
      <Button
        type="link"
        icon={<ArrowLeftOutlined />}
        onClick={() => {
          navigate(-1);
        }}
      ></Button>
      <span style={{ margin: "0 0px" }}>商品详情</span>
    </span>
  );

  useEffect(() => {
    getCategory();
  }, [getCategory]);

  return (
    <Card title={title} className="product-detail">
      <List>
        <Item>
          <span className="product-detail-left">商品名称:</span>
          <span className="product-detail-right">{p.name}</span>
        </Item>
        <Item>
          <span className="product-detail-left">商品描述:</span>
          <span className="product-detail-right">{p.desc}</span>
        </Item>
        <Item>
          <span className="product-detail-left">商品价格:</span>
          <span className="product-detail-right">¥{p.price}元</span>
        </Item>
        <Item>
          <span className="product-detail-left">所属分类:</span>
          <span className="product-detail-right">
            {parentNameFirst === "一级分类"
              ? parentNameSecond
              : `${parentNameFirst} --> ${parentNameSecond}`}
          </span>
        </Item>
        <Item>
          <span className="product-detail-left">商品图片:</span>
          <span className="product-detail-right">
            <img
              src="http://localhost:3000/src/assets/images/sx.jpg"
              alt="img"
              className="product-detail-img"
            />
            <img
              src="http://localhost:3000/src/assets/images/xx.jpg"
              alt="img"
              className="product-detail-img"
            />
          </span>
        </Item>
        <Item>
          <span className="product-detail-left">商品详情:</span>
          <span className="product-detail-right">
            <div
              dangerouslySetInnerHTML={{
                __html: p.detail,
              }}
            ></div>
          </span>
        </Item>
      </List>
    </Card>
  );
}
