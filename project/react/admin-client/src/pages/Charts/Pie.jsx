import React, { useCallback, useEffect, useState } from "react";
import { Pie, measureTextWidth } from "@ant-design/plots";
import { Button, Card, message } from "antd";

export default function MyLine() {
  const [messageApi, contextHolder] = message.useMessage();
  const [data, setData] = useState([]);
  const [sellData, setSellData] = useState([]);
  const [stockData, setStockData] = useState([]);

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
    setSellData([
      {
        品类: "手机",
        数量: 15,
      },
      {
        品类: "电视",
        数量: 3,
      },
      {
        品类: "笔记本",
        数量: 11,
      },
      {
        品类: "平板电脑",
        数量: 2,
      },
    ]);
    setStockData([
      {
        品类: "手机",
        数量: 5,
      },
      {
        品类: "电视",
        数量: 8,
      },
      {
        品类: "笔记本",
        数量: 3,
      },
      {
        品类: "平板电脑",
        数量: 14,
      },
    ]);
  }, []);

  useEffect(() => {
    initData();
  }, [initData]);

  const sellConfig = {
    appendPadding: 10, // 图表内边距
    data: sellData,
    angleField: "数量",
    colorField: "品类",
    radius: 0.75, // 饼图半径
    legend: {
      title: {
        text: "销量", // 标题文本
        spacing: 8,
      },
    },
    label: {
      type: "spider", // 标签类型
      labelHeight: 28, // 标签高度
      content: "{name}\n{value}", // 标签内容
    },
    // interactions 交互配置
    interactions: [
      {
        type: "element-selected", // 选中元素
      },
      {
        type: "element-active", // 高亮元素
      },
    ],
  };

  // 中心统计文本
  function renderStatistic(containerWidth, text, style) {
    const { width: textWidth, height: textHeight } = measureTextWidth(
      text,
      style
    );
    const R = containerWidth / 2; // r^2 = (w / 2)^2 + (h - offsetY)^2

    let scale = 1;

    if (containerWidth < textWidth) {
      scale = Math.min(
        Math.sqrt(
          Math.abs(
            Math.pow(R, 2) /
              (Math.pow(textWidth / 2, 2) + Math.pow(textHeight, 2))
          )
        ),
        1
      );
    }

    const textStyleStr = `width:${containerWidth}px;`;
    return `<div style="${textStyleStr};font-size:${scale}em;line-height:${
      scale < 1 ? 1 : "inherit"
    };">${text}</div>`;
  }

  const stockConfig = {
    appendPadding: 10,
    data: stockData,
    angleField: "数量",
    colorField: "品类",
    radius: 1,
    innerRadius: 0.64,
    meta: {
      value: {
        formatter: (v) => `${v}`, // 格式化文本
      },
    },
    legend: {
      title: {
        text: "库存", // 标题文本
        spacing: 8,
      },
    },
    label: {
      // 饼图文本
      type: "inner",
      offset: "-50%",
      style: {
        textAlign: "center",
      },
      autoRotate: false,
      content: "{value}",
    },
    statistic: {
      title: {
        offsetY: -4,
        customHtml: (container, view, datum) => {
          // 自定义 html
          const { width, height } = container.getBoundingClientRect();
          const d = Math.sqrt(Math.pow(width / 2, 2) + Math.pow(height / 2, 2));
          const text = datum ? datum.品类 : "库存";
          return renderStatistic(d, text, {
            fontSize: 28,
          });
        },
      },
      content: {
        offsetY: 4,
        style: {
          fontSize: "32px",
        },
        customHtml: (container, view, datum, data) => {
          const { width } = container.getBoundingClientRect();
          const text = datum
            ? `${datum.数量}`
            : `${data.reduce((r, d) => r + d.数量, 0)}`;
          return renderStatistic(width, text, {
            fontSize: 32,
          });
        },
      },
    },
    // 添加 中心统计文本 交互
    interactions: [
      {
        type: "element-selected",
      },
      {
        type: "element-active",
      },
      {
        type: "pie-statistic-active",
      },
    ],
  };

  return (
    <Card title={title}>
      <span>
        <Pie {...sellConfig} />
        <Pie {...stockConfig} />
      </span>
      {contextHolder}
    </Card>
  );
}
