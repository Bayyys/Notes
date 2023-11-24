module.exports = {
  // 运行环境
  env: {
    browser: true, // 浏览器环境
    es2021: true, // ES12
    node: true, // Node.js全局变量和Node.js范围
    jest: true, // Jest全局变量
  },

  // 要为特定类型的文件指定处理器
  overrides: [
    {
      files: ['.eslintrc.{js,cjs}'], // 指定文件
    },
  ],
  parser: 'vue-eslint-parser', // 指定如何解析语法
  // 优先级低于 parse 的语法解析器配置
  parserOptions: {
    ecmaVersion: 'latest', // ECMAScript版本: 最新
    parser: '@typescript-eslint/parser', // 指定解析器:
    // Esprima 默认解析器
    // Babel-ESLint babel解析器
    // @typescript-eslint/parser ts解析器
    sourceType: 'module', // 指定来源的类型: 'script'[default] | 'module' | 'unambiguous'
    jsxPragma: 'React', // 指定JSX的pragma
    ecmaFeatures: {
      jsx: true, // 启用JSX
    },
  },
  // 规则继承
  extends: [
    // 全部规则默认关闭, 通过下面的规则来开启
    // 比如: 函数不能重名、对象不能出现重复key
    'eslint:recommended', // eslint推荐规则
    'plugin:@typescript-eslint/recommended', // @typescript-eslint/eslint-plugin推荐规则
    'plugin:vue/vue3-essential', // vue3-essential推荐规则
    'plugin:prettier/recommended', // prettier推荐规则
  ],
  // ESLint支持使用第三方插件。在使用插件之前，您必须使用npm安装它
  // 该 'eslint-plugin-' 前缀可以从插件名称被省略
  plugins: ['@typescript-eslint', 'vue'],
  /** eslint规则
   * 'off' 或 0 - 关闭规则
   * 'warn' 或 1 - 开启规则，使用警告级别的错误：warn (不会导致程序退出)
   * 'error' 或 2 - 开启规则，使用错误级别的错误：error (当被触发的时候，程序会退出)
   */
  rules: {
    // eslint（https://eslint.bootcss.com/docs/rules/）
    'no-var': 'error', // 要求使用 let 或 const 而不是 var
    'no-multiple-empty-lines': ['warn', { max: 1 }], // 不允许多个空行
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off', // 生产环境禁用 console
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off', // 生产环境禁用 debugger
    'no-unexpected-multiline': 'error', // 禁止空余的多行
    'no-useless-escape': 'off', // 禁止不必要的转义字符

    // typeScript (https://typescript-eslint.io/rules)
    '@typescript-eslint/no-unused-vars': 'error', // 禁止定义未使用的变量
    '@typescript-eslint/prefer-ts-expect-error': 'error', // 禁止使用 @ts-ignore
    '@typescript-eslint/no-explicit-any': 'off', // 禁止使用 any 类型
    '@typescript-eslint/no-non-null-assertion': 'off', // 禁止使用非空断言
    '@typescript-eslint/no-namespace': 'off', // 禁止使用自定义 TypeScript 模块和命名空间。
    '@typescript-eslint/semi': 'off', // 要求或禁止使用分号代替 ASI

    // eslint-plugin-vue (https://eslint.vuejs.org/rules/)
    'vue/multi-word-component-names': 'off', // 要求组件名称始终为 “-” 链接的单词
    'vue/script-setup-uses-vars': 'error', // 防止<script setup>使用的变量<template>被标记为未使用
    'vue/no-mutating-props': 'off', // 不允许组件 prop的改变
    'vue/attribute-hyphenation': 'off', // 对模板中的自定义组件强制执行属性命名样式
  },
}
