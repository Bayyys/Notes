const express = require("express");
const app = express();

//专门指定静态资源，必须
app.use(express.static(__dirname + "/static"));

app.get("/person", (request, response) => {
  const resp = {
    id: 123,
    users: "users",
  };
  response.send(JSON.stringify(resp));
});

app.

app.listen(5000, (err) => {
  if (!err)
    console.log("服务器启动成功了,请求地址为: http://localhost:5000/person");
});
