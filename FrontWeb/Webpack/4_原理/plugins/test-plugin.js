const { compilation } = require("webpack");

/**
 * 1. webpack加载webpack.config.js中所有配置, 会创建 new TestPlugin() 实例, 执行插件的 constructor 方法
 * 2. webpack 创建 compiler 对象
 * 3. 遍历所有plugins中插件, 调用插件的 apply 方法, 并传入 compiler 对象
 * 4. 执行剩下编译流程 (触发各个钩子函数)
 */
class TestPlugin {
  constructor() {
    console.log("TestPlugin constructor()");
  }
  apply(compiler) {
    console.log("compiler", compiler);
    console.log("TestPlugin apply()");

    // 由文档可知, environment 是同步(Sync)钩子, 只能使用 tap 方法注册
    // 无参数
    compiler.hooks.environment.tap("TestPlugin", () => {
      console.log("environment");
    });

    // 由文档可知, emit 是异步串行钩子(AsyncSeriesHook), 可以使用 tapAsync 或 tapPromise 方法注册
    compiler.hooks.emit.tap("TestPlugin", (compilation) => {
      console.log("emit 111");
    });

    compiler.hooks.emit.tapAsync("TestPlugin", (compilation, callback) => {
      setTimeout(() => {
        console.log("emit 222");
        callback();
      }, 2000);
    });

    compiler.hooks.emit.tapPromise("TestPlugin", (compilation) => {
      return new Promise((resolve) => {
        setTimeout(() => {
          console.log("emit 333");
          resolve();
        }, 1000);
      });
    });

    // 由文档可知, afterPlugins 异步并行钩子(AsyncParallelHook), 只能使用 tap 方法注册
    compiler.hooks.make.tapAsync("TestPlugin", (compilation, callback) => {
      // compilation 最晚需要在 make 钩子中注册
      compilation.hooks.seal.tap("TestPlugin", () => {
        console.log("seal");
      });
      setTimeout(() => {
        console.log("make 111");
        callback();
      }, 3000);
    });
    compiler.hooks.make.tapAsync("TestPlugin", (compilation, callback) => {
      setTimeout(() => {
        console.log("make 222");
        callback();
      }, 1000);
    });
    compiler.hooks.make.tapAsync("TestPlugin", (compilation, callback) => {
      setTimeout(() => {
        console.log("make 333");
        callback();
      }, 2000);
    });
  }
}

module.exports = TestPlugin;
