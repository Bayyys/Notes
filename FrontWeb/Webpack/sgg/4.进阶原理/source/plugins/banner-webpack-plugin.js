class BannerWebpackPlugin {
  constructor(options = {}) {
    this.options = options;
  }

  apply(compiler) {
    // 在资源输出之前触发
    compiler.hooks.emit.tap("BannerWebpackPlugin", (compilation) => {
      // debugger;
      const extensions = ["css", "js"];
      // 1. 获取即将输出的资源文件：compilation.assets
      // 2. 过滤只保留js和css资源
      const assets = Object.keys(compilation.assets).filter((assetPath) => {
        // 将文件名切割 ['xxxx', 'js'] ['xxxx', 'css']
        const splitted = assetPath.split(".");
        // 获取最后一个文件扩展名
        const extension = splitted[splitted.length - 1];
        // 判断是否保护
        return extensions.includes(extension);
      });

      const prefix = `/*
* Author: ${this.options.author}
*/
`;
      // 3. 遍历剩下资源添加上注释
      // console.log(assets);
      assets.forEach((asset) => {
        // 获取原来内容
        const source = compilation.assets[asset].source();
        // 拼接上注释
        const content = prefix + source;

        // 修改资源
        compilation.assets[asset] = {
          // 最终资源输出时，调用source方法，source方法的返回值就是资源的具体内容
          source() {
            return content;
          },
          // 资源大小
          size() {
            return content.length;
          },
        };
      });
    });
  }
}

module.exports = BannerWebpackPlugin;
