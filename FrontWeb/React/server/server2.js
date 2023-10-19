const express = require("express");

const app = express();

app.use((req, res, next) => {
  console.log(req.get("Host") + " --- " + req.ip + ": 请求服务器2...");
  next();
});

app.get("/students", (req, res) => {
  const students = [
    { id: "001", name: "Tom", age: 18 },
    { id: "002", name: "Jerry", age: 19 },
    { id: "003", name: "Jack", age: 20 },
  ];
  res.send(students);
});

app.listen(5001, (err) => {
  if (!err)
    console.log(
      "服务器2启动成功了,请求车辆地址为: http://localhost:5001/students"
    );
});
