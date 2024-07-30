"use client";
import axios from "axios";
import "@/mock/index";
const xml2js = require("xml2js");

export default function Home() {
  const handlerClick = async () => {
    const res = await axios.get("/user/list");
    console.log("🚀 ~ handlerClick ~ res:", res.data.data);
  };
  // xml 虚拟数据
  const xmldata = `
    <root>
      <person>
        <name>zhangsan</name>
        <age>18</age>
      </person>
      <person>
        <name>lisi</name>
        <age>19</age>
      </person>
    </root>`;

  const parser = new xml2js.Parser();
  const data = parser
    .parseStringPromise(xmldata, {
      explicitArray: false, // 不转换为数组
      explicitRoot: false, // 不转换为根节点
    })
    .then((res: any) => {
      console.log(res);
    });

  return (
    <>
      <h1>Hello World</h1>
      <button onClick={handlerClick}>Click me</button>
    </>
  );
}
