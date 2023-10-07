//1、导入模块
const fs = require('fs');
//2、创建Promise实例化对象
new Promise((resolve, reject) => {
    fs.readFile('./resource/1.txt', (err, data) => {
        if (err) reject(err);
        resolve(data);
    })
}).then(value => {
    return new Promise((resolve, reject) => {
        fs.readFile('./resource/2.txt', (err, data) => {
            if (err) reject(err);
            resolve([value, data]);
        })
    })
}).then(value => {
    return new Promise((resolve, reject) => {
        fs.readFile('./resource/3.txt', (err, data) => {
            if (err) reject(err);
            value.push(data)
            resolve(value);
        })
    })
}).then(value => {
    console.log(value.toString());
})