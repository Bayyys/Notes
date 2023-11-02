/* global use, db */
// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

const database = 'server_db2';
const collection = 'NEW_COLLECTION_NAME';

use(database);

/*
 Navicat Premium Data Transfer

 Source Server         : mongodb-localhost
 Source Server Type    : MongoDB
 Source Server Version : 30204
 Source Host           : localhost:27017
 Source Schema         : server_db2

 Target Server Type    : MongoDB
 Target Server Version : 30204
 File Encoding         : 65001

 Date: 04/08/2021 15:43:46
*/


// ----------------------------
// Collection structure for categorys
// ----------------------------
db.getCollection("categorys").drop();
db.createCollection("categorys");

// ----------------------------
// Documents of categorys
// ----------------------------
db.getCollection("categorys").insert([ {
    _id: ObjectId("5e12b8bce31bb727e4b0e348"),
    parentId: "0",
    name: "家用电器",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5e130ec7e31bb727e4b0e34c"),
    parentId: "0",
    name: "洗衣机",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5e130e60e31bb727e4b0e34b"),
    parentId: "0",
    name: "手机",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5e1346533ed02518b4db0cd7"),
    parentId: "0",
    name: "图书",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5e13467e3ed02518b4db0cd8"),
    parentId: "0",
    name: "杯具",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5e144dc7297c1138787e96ab"),
    parentId: "0",
    name: "服装",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5e1346c83ed02518b4db0cd9"),
    parentId: "0",
    name: "纸",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5e144de1297c1138787e96ac"),
    parentId: "0",
    name: "玩具",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5e16e37e49dc6b38d018fe28"),
    parentId: "0",
    name: "手机",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5e16e38949dc6b38d018fe29"),
    name: "三星",
    __v: NumberInt("0"),
    parentId: "0"
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5fc0bf33eb957f1b94f4a959"),
    parentId: "0",
    name: "医药",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5fc0bfa4eb957f1b94f4a95a"),
    parentId: "0",
    name: "食品",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5fc0bfcdeb957f1b94f4a95b"),
    parentId: "0",
    name: "发型",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5fc0bfd7eb957f1b94f4a95c"),
    parentId: "0",
    name: "水果",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5fc0bfdeeb957f1b94f4a95d"),
    parentId: "0",
    name: "发饰",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5fc30a1833fe4221c4546275"),
    parentId: "5e12b8bce31bb727e4b0e348",
    name: "冰箱",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5fc0bfe6eb957f1b94f4a95e"),
    parentId: "0",
    name: "图纸",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5fc30a4133fe4221c4546276"),
    parentId: "5e12b8bce31bb727e4b0e348",
    name: "微波炉",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5fc30a6533fe4221c4546279"),
    parentId: "5e12b8bce31bb727e4b0e348",
    name: "消毒碗柜",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5fc30a5133fe4221c4546278"),
    parentId: "5e12b8bce31bb727e4b0e348",
    name: "洗衣机",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5fc30a4a33fe4221c4546277"),
    parentId: "5e12b8bce31bb727e4b0e348",
    name: "电饭煲",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5fc30a6f33fe4221c454627a"),
    parentId: "5e12b8bce31bb727e4b0e348",
    name: "电视",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5fc30a7a33fe4221c454627b"),
    parentId: "5e12b8bce31bb727e4b0e348",
    name: "抽油烟机",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5fc5a5ff4870c82a702c5efd"),
    parentId: "0",
    name: "bbb",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5fc5b24b4870c82a702c5f05"),
    parentId: "0",
    name: "2",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5fc5b2ae4870c82a702c5f06"),
    parentId: "0",
    name: "34",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5fc5b2b84870c82a702c5f07"),
    parentId: "5fc5b2ae4870c82a702c5f06",
    name: "222",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5fc74b650dd9b10798413162"),
    parentId: "5e12b8bce31bb727e4b0e348",
    name: "电脑",
    __v: NumberInt("0")
} ]);
db.getCollection("categorys").insert([ {
    _id: ObjectId("5fc9e7cc618171388c09b7eb"),
    parentId: "0",
    name: "哈哈哈",
    __v: NumberInt("0")
} ]);

// ----------------------------
// Collection structure for products
// ----------------------------
db.getCollection("products").drop();
db.createCollection("products");

// ----------------------------
// Documents of products
// ----------------------------
db.getCollection("products").insert([ {
    _id: ObjectId("5e12b97de31bb727e4b0e349"),
    status: NumberInt("2"),
    imgs: [
        "1578588737108-index.jpg"
    ],
    name: "联想ThinkPad 翼4809",
    desc: "年度重量级新品，X390、T490全新登场 更加轻薄机身设计9",
    price: NumberInt("6300"),
    pCategoryId: "5e12b8bce31bb727e4b0e348",
    categoryId: "5fc74b650dd9b10798413162",
    detail: "<p><span style=\"color: rgb(228,57,60);background-color: rgb(255,255,255);font-size: 12px;\">想你所需，超你所想！精致外观，轻薄便携带光驱，内置正版office杜绝盗版死机，全国联保两年！</span></p>\n<p><span style=\"color: rgb(102,102,102);background-color: rgb(255,255,255);font-size: 16px;\">联想（Lenovo）扬天V110 15.6英寸家用轻薄便携商务办公手提笔记本电脑 定制【E2-9010/4G/128G固态】 2G独显 内置</span></p>\n<p><span style=\"color: rgb(102,102,102);background-color: rgb(255,255,255);font-size: 16px;\"></span></p>\n",
    __v: NumberInt("0")
} ]);
db.getCollection("products").insert([ {
    _id: ObjectId("5e12b9d1e31bb727e4b0e34a"),
    status: NumberInt("1"),
    imgs: [
        "image-1559402448049.jpg",
        "image-1559402450480.jpg"
    ],
    name: "华硕(ASUS) 飞行堡垒",
    desc: "15.6英寸窄边框游戏笔记本电脑(i7-8750H 8G 256GSSD+1T GTX1050Ti 4G IPS)",
    price: NumberInt("6799"),
    pCategoryId: "5e12b8bce31bb727e4b0e348",
    categoryId: "5fc74b650dd9b10798413162",
    detail: "<p><span style=\"color: rgb(102,102,102);background-color: rgb(255,255,255);font-size: 16px;\">华硕(ASUS) 飞行堡垒6 15.6英寸窄边框游戏笔记本电脑(i7-8750H 8G 256GSSD+1T GTX1050Ti 4G IPS)火陨红黑</span>&nbsp;</p>\n<p><span style=\"color: rgb(228,57,60);background-color: rgb(255,255,255);font-size: 12px;\">【4.6-4.7号华硕集体放价，大牌够品质！】1T+256G高速存储组合！超窄边框视野无阻，强劲散热一键启动！</span>&nbsp;</p>\n",
    __v: NumberInt("0")
} ]);
db.getCollection("products").insert([ {
    _id: ObjectId("5e145c55d9ba8f39dc5f879f"),
    status: NumberInt("2"),
    imgs: [
        "image-1559402396338.jpg"
    ],
    name: "联想ThinkPad 翼4809",
    desc: "年度重量级新品，X390、T490全新登场 更加轻薄机身设计9",
    price: "65999",
    pCategoryId: "5e12b8bce31bb727e4b0e348",
    categoryId: "5fc74b650dd9b10798413162",
    __v: "0"
} ]);
db.getCollection("products").insert([ {
    _id: ObjectId("5e145c5ed9ba8f39dc5f87a1"),
    status: "1",
    imgs: [
        "image-1559402396338.jpg"
    ],
    name: "联想ThinkPad 翼4809",
    desc: "年度重量级新品，X390、T490全新登场 更加轻薄机身设计9",
    price: "65999",
    pCategoryId: "5e12b8bce31bb727e4b0e348",
    categoryId: "5fc74b650dd9b10798413162",
    __v: "0"
} ]);
db.getCollection("products").insert([ {
    _id: ObjectId("5e146b3cd9ba8f39dc5f87a2"),
    status: "1",
    imgs: [
        "image-1559402396338.jpg"
    ],
    name: "联想ThinkPad 翼4809",
    desc: "年度重量级新品，X390、T490全新登场 更加轻薄机身设计9",
    price: "65999",
    pCategoryId: "5e12b8bce31bb727e4b0e348",
    categoryId: "5fc74b650dd9b10798413162",
    detail: "",
    __v: "0"
} ]);
db.getCollection("products").insert([ {
    _id: ObjectId("5e146b40d9ba8f39dc5f87a3"),
    status: NumberInt("2"),
    imgs: [
        "image-1559402396338.jpg"
    ],
    name: "联想ThinkPad 翼4809",
    desc: "年度重量级新品，X390、T490全新登场 更加轻薄机身设计9",
    price: "65999",
    pCategoryId: "5e12b8bce31bb727e4b0e348",
    categoryId: "5fc74b650dd9b10798413162",
    detail: "",
    __v: "0"
} ]);
db.getCollection("products").insert([ {
    _id: ObjectId("5e146b44d9ba8f39dc5f87a4"),
    status: "1",
    imgs: [
        "image-1559402396338.jpg"
    ],
    name: "联想ThinkPad 翼4809",
    desc: "年度重量级新品，X390、T490全新登场 更加轻薄机身设计9",
    price: "65999",
    pCategoryId: "5e12b8bce31bb727e4b0e348",
    categoryId: "5fc74b650dd9b10798413162",
    detail: "",
    __v: "0"
} ]);
db.getCollection("products").insert([ {
    _id: ObjectId("5e17045939c375286459fc82"),
    imgs: [
        "image-1559402396338.jpg"
    ],
    name: "测试一号",
    desc: "哈哈哈哈哈哈",
    price: NumberInt("99999"),
    detail: "<p>少时诵诗书所所所</p>\n",
    pCategoryId: "5e12b8bce31bb727e4b0e348",
    categoryId: "5fc74b650dd9b10798413162",
    status: NumberInt("1"),
    __v: NumberInt("0")
} ]);
db.getCollection("products").insert([ {
    _id: ObjectId("5fc7096f0dd9b10798413160"),
    status: NumberInt("1"),
    imgs: [
        "image-1559402396338.jpg"
    ],
    name: "美的(Midea) 213升-BCD-213TM",
    desc: "爆款直降!大容量三口之家优选! *节能养鲜,自动低温补偿,36分贝静音呵护",
    price: NumberInt("1388"),
    pCategoryId: "5e12b8bce31bb727e4b0e348",
    categoryId: "5fc30a1833fe4221c4546275",
    detail: "<p style=\"text-align:start;\"><span style=\"color: rgb(102,102,102);background-color: rgb(255,255,255);font-size: 16px;font-family: Arial, \"microsoft yahei;\">美的(Midea) 213升 节能静音家用三门小冰箱 阳光米 BCD-213TM(E)</span></p>\n<p><span style=\"color: rgb(228,57,60);background-color: rgb(255,255,255);font-size: 12px;font-family: tahoma, arial, \"Microsoft YaHei\", \"Hiragino Sans GB\", u5b8bu4f53, sans-serif;\">【4.8美的大牌秒杀日】爆款直降!大容量三口之家优选! *节能养鲜,自动低温补偿,36分贝静音呵护! *每天不到一度电,省钱又省心!</span>&nbsp;</p>\n",
    __v: NumberInt("0")
} ]);
db.getCollection("products").insert([ {
    _id: ObjectId("5fc9ea2b1cb7c416c4fb7edc"),
    status: NumberInt("1"),
    imgs: [ ],
    categoryId: "5e12b8bce31bb727e4b0e348",
    pCategoryId: "0",
    name: "测试1",
    price: NumberInt("1000"),
    __v: NumberInt("0")
} ]);
db.getCollection("products").insert([ {
    _id: ObjectId("5e146b4dd9ba8f39dc5f87a5"),
    status: NumberInt("2"),
    imgs: [
        "image-1559402396338.jpg"
    ],
    name: "联想ThinkPad 翼4809",
    desc: "年度重量级新品，X390、T490全新登场 更加轻薄机身设计9",
    price: "65999",
    pCategoryId: "5e12b8bce31bb727e4b0e348",
    categoryId: "5fc74b650dd9b10798413162",
    detail: "",
    __v: "0"
} ]);
db.getCollection("products").insert([ {
    _id: ObjectId("5fc9eca01cb7c416c4fb7ee1"),
    status: NumberInt("1"),
    imgs: [ ],
    name: "123",
    desc: "213",
    price: NumberInt("213"),
    pCategoryId: "0",
    categoryId: "5e130e60e31bb727e4b0e34b",
    __v: NumberInt("0")
} ]);
db.getCollection("products").insert([ {
    _id: ObjectId("5fc74fe10dd9b10798413163"),
    status: NumberInt("2"),
    imgs: [
        "image-1559402436395.jpg"
    ],
    name: "你不知道的JS（上卷）",
    desc: "图灵程序设计丛书： [You Don't Know JS:Scope & Closures] JavaScript开发经典入门图书 打通JavaScript的任督二脉",
    price: NumberInt("35"),
    pCategoryId: "0",
    categoryId: "5e1346533ed02518b4db0cd7",
    detail: "<p style=\"text-align:start;\"><span style=\"color: rgb(102,102,102);background-color: rgb(255,255,255);font-size: 16px;\">图灵程序设计丛书：你不知道的JavaScript（上卷）</span> <span style=\"color: rgb(102,102,102);background-color: rgb(255,255,255);font-size: 16px;\"><strong>[You Don't Know JS:Scope &amp; Closures]</strong></span></p>\n<p style=\"text-align:start;\"><span style=\"color: rgb(227,57,60);background-color: rgb(255,255,255);font-size: 12px;\">JavaScript开发经典入门图书 打通JavaScript的任督二脉 领略语言内部的绝美风光</span>&nbsp;</p>\n",
    __v: NumberInt("0")
} ]);
db.getCollection("products").insert([ {
    _id: ObjectId("5fc709a00dd9b10798413161"),
    status: NumberInt("1"),
    imgs: [
        "image-1554638676149.jpg",
        "image-1554638683746.jpg"
    ],
    name: "联想ThinkPad X1 Carbon",
    desc: "英特尔酷睿i5 14英寸轻薄笔记本电脑（i5-8250U 8G 256GSSD FHD）黑色",
    price: NumberInt("9999"),
    pCategoryId: "5e12b8bce31bb727e4b0e348",
    categoryId: "5fc74b650dd9b10798413162",
    detail: "<p style=\"text-align:start;\"><span style=\"color: rgb(102,102,102);background-color: rgb(255,255,255);font-size: 16px;font-family: Arial, \"microsoft yahei;\">联想ThinkPad X1 Carbon 2018（09CD）英特尔酷睿i5 14英寸轻薄笔记本电脑（i5-8250U 8G 256GSSD FHD）黑色</span></p>\n<p><span style=\"color: rgb(228,57,60);background-color: rgb(255,255,255);font-size: 12px;font-family: tahoma, arial, \"Microsoft YaHei\", \"Hiragino Sans GB\", u5b8bu4f53, sans-serif;\">年度重量级新品，X390、T490全新登场 更加轻薄机身设计，全面的配置升级，让工作更便捷，让生活更轻松</span><a href=\"https://pro.jd.com/mall/active/2M4o7NTzHH6jEJXS7VbpbTAANQB9/index.html\" target=\"_blank\"><span style=\"color: rgb(94,105,173);background-color: rgb(255,255,255);font-size: 12px;font-family: tahoma, arial, \"Microsoft YaHei\", \"Hiragino Sans GB\", u5b8bu4f53, sans-serif;\">4月9日京东震撼首发，火爆预约</span></a>&nbsp;</p>\n",
    __v: NumberInt("0")
} ]);

// ----------------------------
// Collection structure for roles
// ----------------------------
db.getCollection("roles").drop();
db.createCollection("roles");

// ----------------------------
// Documents of roles
// ----------------------------
db.getCollection("roles").insert([ {
    _id: ObjectId("5e0d7292bd72914ee8e714d4"),
    name: "测试",
    "auth_time": NumberLong("1607481252131"),
    "auth_name": "admin",
    "create_time": NumberLong("1554639521749"),
    menus: [
        "/category",
        "/home"
    ]
} ]);
db.getCollection("roles").insert([ {
    _id: ObjectId("5e175a134bce5e36d48fb4db"),
    menus: [
        "all",
        "/home",
        "/products",
        "/category",
        "/product",
        "/user",
        "/role",
        "/charts",
        "/charts/bar",
        "/charts/line",
        "/charts/pie"
    ],
    name: "管理员",
    "create_time": NumberLong("1578588691768"),
    "auth_name": "admin",
    "auth_time": NumberLong("1578588698490")
} ]);
db.getCollection("roles").insert([ {
    _id: ObjectId("5e188bb874c89321209fedda"),
    menus: [
        "/home",
        "/charts/bar",
        "/charts",
        "/charts/line",
        "/charts/pie",
        "/role"
    ],
    name: "员工",
    "create_time": NumberLong("1578666936202"),
    "auth_name": "admin",
    "auth_time": NumberLong("1607330722391")
} ]);
db.getCollection("roles").insert([ {
    _id: ObjectId("5fcdcb428e518d46807aa485"),
    menus: [ ],
    name: "哈哈哈",
    "create_time": NumberLong("1607322434116")
} ]);
db.getCollection("roles").insert([ {
    _id: ObjectId("5fcdca798e518d46807aa484"),
    menus: [
        "/category"
    ],
    name: "你好",
    "create_time": NumberLong("1607322233401"),
    "auth_time": NumberLong("1607411041057"),
    "auth_name": "admin"
} ]);
db.getCollection("roles").insert([ {
    _id: ObjectId("5fcdcb528e518d46807aa486"),
    menus: [ ],
    name: "哈哈啊",
    "create_time": NumberLong("1607322450051")
} ]);
db.getCollection("roles").insert([ {
    _id: ObjectId("5fcdcd638e518d46807aa488"),
    menus: [ ],
    name: "123",
    "create_time": NumberLong("1607322979807")
} ]);
db.getCollection("roles").insert([ {
    _id: ObjectId("5e171d55d59eb648d4ed66a8"),
    menus: [
        "/home",
        "/products",
        "/category",
        "/product",
        "/charts/pie"
    ],
    name: "测试",
    "create_time": NumberLong("1578573141547"),
    "auth_name": "admin",
    "auth_time": NumberLong("1607406938634")
} ]);

// ----------------------------
// Collection structure for users
// ----------------------------
db.getCollection("users").drop();
db.createCollection("users");

// ----------------------------
// Documents of users
// ----------------------------
db.getCollection("users").insert([ {
    _id: ObjectId("610a39764f93334154bb3520"),
    username: "admin",
    password: "21232f297a57a5a743894a0e4a801fc3",
    "create_time": 1628060022887,
    __v: NumberInt("0")
} ]);
db.getCollection("users").insert([ {
    _id: ObjectId("5fd06791fa244c0b10cadec9"),
    username: "Jim",
    password: "202cb962ac59075b964b07152d234b70",
    phone: "72612189",
    email: "feedback@outlook.com",
    "role_id": "5e0d7292bd72914ee8e714d4",
    "create_time": NumberLong("1552062212734"),
    __v: NumberInt("0")
} ]);
db.getCollection("users").insert([ {
    _id: ObjectId("5fd06735fa244c0b10cadec7"),
    username: "Tom",
    password: "202cb962ac59075b964b07152d234b70",
    phone: "123242434",
    email: "sd",
    "role_id": "5e188bb874c89321209fedda",
    "create_time": NumberLong("1555061512734"),
    __v: NumberInt("0")
} ]);
db.getCollection("users").insert([ {
    _id: ObjectId("5fd06aaf97daee1b6c09b1cd"),
    username: "admin",
    password: "21232f297a57a5a743894a0e4a801fc3",
    phone: "224249",
    email: "admin@outlook.com",
    "role_id": "5e175a134bce5e36d48fb4db",
    "create_time": NumberLong("1212062212734"),
    __v: NumberInt("0")
} ]);
db.getCollection("users").insert([ {
    _id: ObjectId("5fd067affa244c0b10cadeca"),
    username: "Kira",
    password: "202cb962ac59075b964b07152d234b70",
    phone: "224249",
    email: "wait@outlook.com",
    "role_id": "5fcdca798e518d46807aa484",
    "create_time": NumberLong("1252062212734"),
    __v: NumberInt("0")
} ]);
db.getCollection("users").insert([ {
    _id: ObjectId("5fd0675bfa244c0b10cadec8"),
    username: "Cindy",
    password: "202cb962ac59075b964b07152d234b70",
    phone: "12324233434",
    email: "plp",
    "role_id": "5e0d7292bd72914ee8e714d4",
    "create_time": NumberLong("1555062212734"),
    __v: NumberInt("0")
} ]);
db.getCollection("users").insert([ {
    _id: ObjectId("5fd09192efe9692bd0dd40de"),
    username: "test2",
    password: "202cb962ac59075b964b07152d234b70",
    phone: "123",
    email: "123",
    "role_id": "5e188bb874c89321209fedda",
    "create_time": NumberLong("1607504274441"),
    __v: NumberInt("0")
} ]);



