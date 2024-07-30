const Mock = require("mockjs");
const Random = Mock.Random;

export const userData = Mock.mock("/user/list", "get", {
  code: 200,
  message: "success",
  "data|2-10": [
    {
      "id|+1": 1,
      username: "@cname",
      date: "@date",
      "age|18-60": 1,
      "sex|1": ["男", "女"],
      "star|1-10": "★",
      "surgery|50-100.1-10": 1,
      avatar: "@image('200x100', '#50B347', '#FFF', 'Avatar')",
      description: "@paragraph",
      ip: "@ip",
      email: "@email",
      url: "@url",
    },
  ],
});
