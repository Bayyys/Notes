// plugins/inline-chunk-webpack-plugin.js
const HtmlWebpackPlugin = require("safe-require")("html-webpack-plugin");

class InlineChunkWebpackPlugin {
  constructor(tests) {
    this.tests = tests;
  }

  apply(compiler) {
    compiler.hooks.compilation.tap(
      "InlineChunkWebpackPlugin",
      (compilation) => {
        // 1. getHooks(compilation) 获取html-webpack-plugin的钩子
        const hooks = HtmlWebpackPlugin.getHooks(compilation);
        // 2. 通过hooks获取alterAssetTagGroups钩子，该钩子在生成html之前执行
        hooks.alterAssetTagGroups.tap("InlineChunkWebpackPlugin", (assets) => {
          // 3. 将runtime文件的内容内联到html中
          assets.headTags = this.getInlineTag(
            assets.headTags,
            compilation.assets
          );
          assets.bodyTags = this.getInlineTag(
            assets.bodyTags,
            compilation.assets
          );
        });

        // 删除无用的js(runtime)文件
        hooks.afterEmit.tap("InlineChunkHtmlPlugin", () => {
          Object.keys(compilation.assets).forEach((assetName) => {
            if (this.tests.some((test) => test.test(assetName))) {
              delete compilation.assets[assetName];
            }
          });
        });
      }
    );
  }

  getInlineTag(tags, assets) {
    return tags.map((tag) => {
      if (tag.tagName !== "script") return tag;

      const filepath = tag.attributes.src;
      if (!filepath) return tag; // 如果没有src属性，直接返回

      if (!this.tests.some((test) => test.test(filepath))) return tag; // 如果是runtime文件，直接返回

      return {
        tagName: "script",
        innerHTML: assets[filepath].source(),
        closeTag: true,
      };
    });
  }
}

module.exports = InlineChunkWebpackPlugin;
