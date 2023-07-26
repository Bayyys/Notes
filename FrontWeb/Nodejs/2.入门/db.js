// 导入(require)mysql依赖包, 其属于第三方模块, 需要先安装 npm install mysql
var mysql = require('mysql');

// 1. 创建一个mysql的Connection对象
// 2. 配置数据库连接参数
var connection = mysql.createConnection({
    host: 'localhost',  // 数据库所在的服务器域名或者IP地址
    user: 'root',       // 登录数据库的账号
    port: 3306,         // 数据库的端口号
    password: '123456', // 登录数据库的密码
    database: 'testdb'    // 操作的数据库
});

// 3. 连接数据库
connection.connect();

// 4. 执行SQL语句 CURD
connection.query('SELECT * FROM `testtable`', function (error, results, fields) {
    if (error) throw error;
    console.log('The solution is: ', results);
});

// 5. 关闭数据库连接
connection.end();