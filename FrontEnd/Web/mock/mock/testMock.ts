const mock = require("mockjs");

// 140000199412185622
const id = mock.mock("@id");

// { id: '140000199412185622' }
const idObj = mock.mock({
  id: "@id",
});

const obj = mock.mock({
  id: "@id",
  username: "@cname",
  date: "@date",
  avatar: "@image('200x100', '#50B347', '#FFF', 'Avatar')",
  description: "@paragraph",
  ip: "@ip",
  email: "@email",
  url: "@url",
});
console.log("🚀 ~ obj:", obj);
