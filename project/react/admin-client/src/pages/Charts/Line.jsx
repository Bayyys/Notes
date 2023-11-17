import React, { useCallback, useEffect, useState } from "react";
import { Line } from "@ant-design/plots";
import { Button, Card, message } from "antd";

export default function MyLine() {
  const [messageApi, contextHolder] = message.useMessage();
  const [data, setData] = useState([]);

  const updateData = () => {
    setData(
      data.map((d) => ({
        ...d,
        数量: d.name === "销量" ? d.数量 + 1 : d.数量 > 0 ? d.数量 - 1 : 0,
      }))
    );
    messageApi.loading("正在更新数据...", 0.5).then(() => {
      messageApi.success("数据更新成功！", 0.5);
    });
  };

  const title = (
    <div>
      <Button
        type="primary"
        onClick={() => {
          updateData();
        }}
      >
        刷新
      </Button>
    </div>
  );

  const initData = useCallback(() => {
    setData([
      {
        name: "销量",
        品类: "手机",
        数量: 15,
      },
      {
        name: "库存",
        品类: "手机",
        数量: 5,
      },
      {
        name: "销量",
        品类: "电视",
        数量: 3,
      },
      {
        name: "库存",
        品类: "电视",
        数量: 8,
      },
      {
        name: "销量",
        品类: "笔记本",
        数量: 11,
      },
      {
        name: "库存",
        品类: "笔记本",
        数量: 3,
      },
      {
        name: "销量",
        品类: "平板电脑",
        数量: 2,
      },
      {
        name: "库存",
        品类: "平板电脑",
        数量: 14,
      },
    ]);
  }, []);

  useEffect(() => {
    initData();
  }, [initData]);

  const config = {
    data,
    xField: "品类",
    yField: "数量",
    seriesField: "name", // 分组字段
    legend: {
      position: "top",
    },
    smooth: true,
    // @TODO 后续会换一种动画方式
    animation: {
      appear: {
        animation: "path-in",
        duration: 1000,
      },
    },
  };

  return (
    <Card title={title}>
      <Line {...config} />
      {contextHolder}
    </Card>
  );
}
