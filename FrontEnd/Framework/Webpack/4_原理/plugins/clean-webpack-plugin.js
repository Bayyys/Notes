class CleanWebpackPlugin {
  apply(compiler) {
    // 1. 注册钩子: 打包输之前 emit
    compiler.hooks.emit.tap("CleanWebpackPlugin", (compilation) => {
      // 2. 获取打包输出的目录
      const outputPath = compiler.options.output.path;
      const fs = compiler.outputFileSystem;
      // 3. 通过fs删除打包输出的目录下的所有文件
      this.removeFiles(fs, outputPath);
    });
  }

  removeFiles(fs, filepath) {
    // 1. 读取目录下的所有文件
    const files = fs.readdirSync(filepath); // ["images", "index.html", "js"];
    // 2. 判断是文件还是文件夹
    files.forEach((file) => {
      const _path = require("path").join(filepath, file);
      const stats = fs.statSync(_path);
      if (stats.isDirectory()) {
        // 3. 如果是文件夹, 递归调用
        this.removeFiles(fs, _path);
      } else {
        // 4. 如果是文件, 删除
        fs.unlinkSync(_path);
      }
    });
    // 3. 如果是文件夹, 递归调用
    // 4. 如果是文件, 删除
  }
}

module.exports = CleanWebpackPlugin;
