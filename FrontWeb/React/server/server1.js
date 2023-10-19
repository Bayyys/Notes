const express = require("express");

const app = express();

app.use((req, res, next) => {
  console.log(req.get("Host") + " --- " + req.ip + ": 请求服务器1...");
  next();
});

app.get("/cars", (req, res) => {
  const cars = [
    { id: "001", name: "BMW", price: 1000 },
    { id: "002", name: "Benz", price: 1200 },
    { id: "003", name: "Audi", price: 1100 },
  ];
  res.send(cars);
});

app.listen(5000, (err) => {
  if (!err)
    console.log("服务器1启动成功了,请求车辆地址为: http://localhost:5000/cars");
});
