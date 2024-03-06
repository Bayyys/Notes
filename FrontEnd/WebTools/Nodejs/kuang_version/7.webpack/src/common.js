exports.info = function (str) {
    // 向控制台输出信息
    console.log('common.js==>info:' + str);
    // 向页面输出信息
    document.write('common.js==>info:' + str + '<br/>');
}