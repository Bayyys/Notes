import React, { useEffect, useState } from "react";
import { Card, Table, Button, Tag, Space, Popconfirm, message } from "antd";
import { PlusOutlined } from "@ant-design/icons";
import { reqCategorys } from "../../api/api";

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
        <Popconfirm title="确认修改?">
          <a>修改分类</a>
        </Popconfirm>
        <Button type="link">查看子分类</Button>
      </>
    ),
  },
];

export default function Category() {
  const [categorys, setCategorys] = useState([]); // 一级分类列表
  const [loading, setLoading] = useState(true); // 是否正在获取数据中
  const title = "一级分类列表";
  const extra = (
    <Button type="primary" icon={<PlusOutlined />}>
      添加
    </Button>
  );

  useEffect(() => {
    // 初始化表格数据
    reqCategorys("0")
      .then((res) => {
        setCategorys(res.data);
      })
      .catch((err) => {
        message.error(err.message);
      });
    setLoading(false);
  }, []);

  return (
    <Card title={title} extra={extra}>
      <Table
        columns={columns}
        dataSource={categorys}
        bordered
        loading={loading}
        pagination={{ defaultPageSize: 5, showQuickJumper: true }}
        rowKey={(record) => record._id}
      />
    </Card>
  );
}
