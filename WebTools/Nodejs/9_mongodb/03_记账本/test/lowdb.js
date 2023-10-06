// 导入 lowdb
const low = require("lowdb");
const FileSync = require("lowdb/adapters/FileSync");  // 用于读写文件
const adapter = new FileSync("db.json");  // 申明一个适配器
const db = low(adapter);  // 获取数据库实例

// 初始化数据库
db.defaults({ posts: [], user: {} }).write();

// 添加一些数据
db.get("posts").push({ id: 1, title: "lowdb is awesome" }).write();

// db.set() 方法用于设置数据(如果数据不存在则创建, 如果存在则更新)
db.set("user.name", "typicode").write();

// 获取数据
console.log(db.get("posts").value());
const res1 = db.get("posts").find({ id: 1 }).value();  // 根据 id 查找数据

// 删除数据
db.get("posts").remove({ id: 1 }).write();
const res2 = db.get("posts").remove({ id: 3 }).write();
console.log("res", res2);  // 返回被删除的数据

// 更新数据
db.get("posts").find({ id: 2 }).assign({ title: "lowdb is awesome" }).write();