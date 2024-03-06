class AnalyzeWebpackPlugin {
  apply(compiler) {
    // 1. 注册钩子: 打包输之前 emit
    compiler.hooks.emit.tap("AnalyzeWebpackPlugin", (compilation) => {
      // 2. 遍历所有即将输出的文件, 得到其大小
      let content = `| 资源名称 | 资源大小(kb) |\n| --- | --- |\n`;
      const assets = Object.entries(compilation.assets);
      assets.forEach(([filename, stat]) => {
        content += `| ${filename} | ${Math.ceil(stat.size() / 1024)} |\n`;
      });

      // 3. 将内容输出到 dist/analyze.md
      compilation.assets["analyze.md"] = {
        source: () => {
          return content;
        },
        size: () => {
          return content.length;
        },
      };
    });
  }
}

module.exports = AnalyzeWebpackPlugin;
