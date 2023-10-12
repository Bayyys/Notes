class BannerWebpackPlugin {
  constructor(options = {}) {
    this.options = options;
  }

  apply(compiler) {
    // 在 emit(资源即将输出) 阶段添加钩子函数
    compiler.hooks.emit.tapAsync(
      "BannerWebpackPlugin",
      (compilation, callback) => {
        // debugger;
        const exts = ["js", "css"];
        // 1. 获取即将输出的资源列表 compilation.assets
        // 2. 过滤只保留 js/css 文件
        const assets = Object.keys(compilation.assets).filter((assetPath) => {
          // 切割文件
          const splitted = assetPath.split(".");
          // 获取最后一个文件扩展名
          const ext = splitted[splitted.length - 1];
          // 判断是否在扩展名数组中
          return exts.includes(ext);
        });
        // 3. 为每个文件添加头部注释信息
        const prefix = `/*
* Author: ${this.options.author}
*/
`;

        assets.forEach((asset) => {
          // 3.1 获取文件内容
          const source = compilation.assets[asset];
          compilation.assets[asset] = {
            source: () => {
              return prefix + source.source();
            },
            size: () => {
              return prefix.length + source.size();
            },
          };
        });

        callback(); // 异步钩子函数必须调用 callback
      }
    );
  }
}

module.exports = BannerWebpackPlugin;
