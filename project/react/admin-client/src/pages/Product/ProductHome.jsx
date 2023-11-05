import React, { useEffect, useState } from "react";
import { Button, Card, Input, Select, Table, message } from "antd";
import { PlusOutlined } from "@ant-design/icons";
import { Outlet } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import { PAGE_SIZE } from "../../utils/constants";
import { reqProducts, reqSearchProducts, reqUpdateStatus } from "../../api/api";
const Option = Select.Option;

export default function ProductHome() {
  const [products, setProducts] = useState([]); // 商品的数组
  const [columns, setColumns] = useState([]); // 商品的数组
  const [total, setTotal] = useState(0); // 商品的总数量
  const [loading, setLoading] = useState(false); // 是否正在加载中
  const [searchName, setSearchName] = useState(""); // 搜索的关键字
  const [searchType, setSearchType] = useState("productName"); // 根据哪个字段搜索
  const [pageNum, setPageNum] = useState(1); // 当前显示第几页的数据
  const navigate = useNavigate();

  // 获取指定页码的列表数据显示
  const getProducts = async (pageNum) => {
    setPageNum(pageNum); // 保存pageNum, 让其它方法可以看到
    setLoading(true);
    let result;
    try {
      if (searchName) {
        result = await reqSearchProducts(
          pageNum,
          PAGE_SIZE,
          searchName,
          searchType
        );
      } else {
        result = await reqProducts(pageNum, PAGE_SIZE);
      }
      if (result.status === 0) {
        const { total, list } = result.data;
        setProducts(list);
        setTotal(total);
      }
    } catch (error) {
      // message.error("获取商品列表失败");
    }
    setLoading(false);
  };

  // 更新指定商品的状态
  const updateStatus = async (productId, status) => {
    try {
      const res = await reqUpdateStatus(productId, status);
      if (res.status === 0) {
        getProducts(pageNum);
      }
    } catch (error) {}
  };

  // 初始化table的列的数组
  const initColumns = () => {
    getProducts(pageNum);
    setColumns([
      {
        title: "商品名称",
        dataIndex: "name",
      },
      {
        title: "商品描述",
        dataIndex: "desc",
      },
      {
        title: "价格",
        dataIndex: "price",
        render: (price) => "￥" + price, // 当前指定了对应的属性，传入的是对应的属性值
      },
      {
        title: "状态",
        dataIndex: "status",
        width: 150,
        render: (status, record) => {
          return (
            <span>
              <span>{status === 1 ? "在售" : "已下架"}</span>
              <Button
                type="link"
                onClick={() => {
                  updateStatus(record._id, status === 1 ? 2 : 1);
                }}
              >
                {status === 1 ? "下架" : "上架"}
              </Button>
            </span>
          );
        },
      },
      {
        title: "操作",
        render: (product) => {
          return (
            <span>
              <Button
                type="link"
                onClick={() =>
                  navigate("/product/detail", { state: { product } })
                }
              >
                详情
              </Button>
              <Button
                type="link"
                onClick={() =>
                  navigate("/product/addupdate", { state: { product } })
                }
              >
                修改
              </Button>
            </span>
          );
        },
      },
    ]);
  };

  const title = (
    <span>
      <Select
        defaultValue={searchType}
        onChange={(value) => {
          setSearchType(value);
        }}
      >
        <Option value="productName">按名称搜索</Option>
        <Option value="productDesc">按描述搜索</Option>
      </Select>
      <Input
        placeholder="关键字"
        style={{ width: 150, margin: "0 15px" }}
        onChange={(e) => {
          setSearchName(e.target.value);
        }}
      />
      <Button
        type="primary"
        onClick={() => {
          getProducts(1);
        }}
      >
        搜索
      </Button>
    </span>
  );

  const extra = (
    <span>
      <Button
        type="primary"
        icon={<PlusOutlined />}
        onClick={() => navigate("/product/addupdate")}
      >
        添加商品
      </Button>
    </span>
  );

  useEffect(() => {
    initColumns();
  }, []);

  return (
    <Card title={title} extra={extra}>
      <Table
        rowKey="_id"
        dataSource={products}
        columns={columns}
        pagination={{
          defaultPageSize: PAGE_SIZE,
          showQuickJumper: true,
          total: total,
        }}
        onChange={(page) => {
          getProducts(page.current);
        }}
        loading={loading}
      />
      <Outlet />
    </Card>
  );
}
