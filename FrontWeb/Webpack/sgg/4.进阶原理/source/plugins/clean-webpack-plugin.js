class CleanWebpackPlugin {
  apply(compiler) {
    // 2. 获取打包输出的目录
    const outputPath = compiler.options.output.path;
    const fs = compiler.outputFileSystem;
    // 1. 注册钩子：在打包输出之前 emit
    compiler.hooks.emit.tap("CleanWebpackPlugin", (compilation) => {
      // 3. 通过fs删除打包输出的目录下的所有文件
      this.removeFiles(fs, outputPath);
    });
  }

  removeFiles(fs, filepath) {
    // 想要删除打包输出目录下所有资源，需要先将目录下的资源删除，才能删除这个目录
    // 1. 读取当前目录下所有资源
    const files = fs.readdirSync(filepath);
    // console.log(files); // [ 'images', 'index.html', 'js' ]
    // 2. 遍历一个个删除
    files.forEach((file) => {
      // 2.1 遍历所有文件，判断是文件夹还是文件
      const path = `${filepath}/${file}`;
      const fileStat = fs.statSync(path);
      // console.log(fileStat);
      if (fileStat.isDirectory()) {
        // 2.2 是文件夹，就得删除下面所有文件，才能删除文件夹
        this.removeFiles(fs, path);
      } else {
        // 2.3 是文件，直接删除
        fs.unlinkSync(path);
      }
    });
  }
}

module.exports = CleanWebpackPlugin;
