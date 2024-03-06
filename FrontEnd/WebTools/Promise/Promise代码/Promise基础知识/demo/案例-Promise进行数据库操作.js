//1、导入模块
const mongoose = require('mongoose');
//2、创建Promise实例化对象
new Promise((resolve, reject) => {
    //3、链接数据库
    mongoose.connect('mongodb://127.0.0.1:27017/project1');
    mongoose.connection.on('open', () => {
        //连接成功的情况
        resolve();
    })
    mongoose.connection.on('error', () => {
        //连接失败的情况
        reject();
    })
}).then(value => {
    //创建结构
    const noteSchema = new mongoose.Schema({
        title: String,
        content: String
    })

    //创建模型
    const nodeModel = mongoose.model('notes', noteSchema);

    //读取操作
    nodeModel.find().then(value => {
        console.log(value);
    }, reason => {
        console.log(reason);
    })
}, reason => {
    console.log('链接数据库失败');
})