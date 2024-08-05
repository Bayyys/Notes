---
title: Flask 服务端框架使用
description: Flask是一个使用 Python 编写的轻量级 Web 应用框架
created: 08/05/2024
tags: ['python' 'web']
---

## 简介及安装

- Flask是一个使用Python编写的轻量级Web应用框架，它简洁而灵活，适用于开发小型至中型的Web应用
  - Flask 依赖于 Werkzeug WSGI 工具包、Jinja 模板引擎和 Click CLI 工具包
  - Flask是基于Werkzeug和Jinja2库构建的，它遵循了MVC（模型-视图-控制器）的设计模式

> **WSGI** 一套接口规范。一个WSGI程序用以接受客户端请求，传递给应用，再返回服务器的响应给客户端

- 特点
  - 简洁轻量
  - 易于扩展
  - 模板引擎支持: Jinja2
  - 多种数据库支持
  - 自动化测试
- 安装
  - `pip install flask`
- 自动安装依赖项
  - `Werkzeug` 一个WSGI工具库，他可以作为一个Web框架的底层库
  - `Jinja` Jinja 模板只是一个文本文件，可以 基于模板生成任何基于文本的格式（HTML、XML、CSV、LaTeX 等），一般用在前端的项目中，渲染 HTML 文件
  - `MarkupSafe` 用于确保字符串在插入 HTML 时的安全性, 防止潜在的安全漏洞
  - `ItsDangerous` 是Python中一个轻量级的库，旨在提供安全且简单的数据传输和签名功能
  - `Click`
  - `Blinker`

- 注意点
  - `python≥3.8`
  - 虚拟环境 `python3 -m venv .venv`

## 快速入门

### 最小应用程序

```python
# main.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
```

- 导入 **Flask** 类, 该实例作为 WSGI 应用程序
- app 为创建的实例, 首个参数为应用程序的模块或包的名称
- **route()** 指明 URL 的触发对象
- 函数返回浏览器的显示消息, 默认内容为 HTML

### 程序运行

![](https://bitiful.bayyys.cn/notes/mac/2024/08/20240805230554-1722870354.png)

#### 直接运行

- `python3 main.py`

- 或者使用命令行运行 `flask --app main run`

> 若文件名为 `app.py / wsgi.py`, 可以不指定 `--app` 
>
> - `flask run`

#### 外部可见服务器

- 使侦听所有公共 IP
  - `--host=0.0.0.0`

#### 调试模式

`flask run --debug`

- 调试器允许从浏览器执行任意 Python 代码
- 它受密码保护，但仍然存在重大的安全风险
- 不要在生产环境中运行开发服务器或调试器

## 路由

- 使用 `route()` 装饰器将函数绑定到 URL

### HTML 转义

- 返回 HTML 时 (默认响应类型), 在输出中呈现的任何用户提供的值必须通过**转义**, 以防止注入攻击
  - `escape()` 

```python
from markupsafe import escape

@app.router("/<name>")
def hello(name):
  	return f"hello, {escape(name)}!"
```

### 路由规则

- 使用 `<variable_name>` 标记部分来向 URL 添加变量部分
- 使用转换器 `<converter:variable_name>` 指定参数的类型

| 转换器 | 说明                           |
| ------ | ------------------------------ |
| string | (默认) 接受任何不带斜杠的文本  |
| int    | 接受正整数                     |
| float  | 接受正浮点数                   |
| path   | 与 `string` 类似, 但还接受斜杠 |
| uuid   | 接受 UUID 字符串               |

```python
@app.route("/user/<username>")
def show_user_profile(username):
    return f"User {username}"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post {post_id}"

@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return f"Subpath {subpath}"
```

### 唯一 URL/重定向行为

| 路径写法     | 说明                                                         |
| ------------ | ------------------------------------------------------------ |
| `/projects/` | 类似文件夹, 访问 `/projects` 会重定向到规范 URL `/projects/` |
| `/about`     | 类似文件, 访问 `/about/` 会导致 404, 有助于保持资源 URL 唯一, 避免多次搜索 |

### HTTP 方法

- 汇总 `@app.route('/login', methods=['GET', 'POST'])`

- 分别指定
  - `@app.get('/login')`
  - `@app.post('/login')`

## 静态文件

- 文件必须以 `static/style.css` 形式存储在文件系统中
- `url_for('static', filename='style.css')`

### 渲染模板

- 使用 Jinja2 模板引擎, 进行模板渲染
  - 可以生成 HTML/Markdown/Email…
  - 使用 `render_template()` 方法

```python
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

- 模板需要位于 `templates` 文件夹下, 并且处于程序同级目录下

## 请求数据

- 数据由全局 **request** 对象提供

### 请求对象

- method 属性
- form 属性

```python
from flask import request

@app.route('/login', methods=['POST', 'GET'])
def login():
  error = None
  if request.method == 'POST':
    if valid_login(request.form['username'],
                   request.form['password']):
      return log_the_user_in(request.form['username'])
    else:
      error = 'Invalid username/password'
      # the code below is executed if the request method
      # was GET or the credentials were invalid
      return render_template('login.html', error=error)
```

- args 属性

```python
searchword = request.args.get('key', '')
```

### 文件上传

```python
from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    f = request.files['the_file']
    f.save('/var/www/uploads/uploaded_file.txt')
    ...
```

### Cookie

- cookies 属性
  - `set_cookie`

```python
from flask import request

@app.route('/')
def index():
  username = request.cookies.get('username')
  # use cookies.get(key) instead of cookies[key] to not get a
  # KeyError if the cookie is missing
```

```python
from flask import make_response

@app.route('/')
def index():
  resp = make_response(render_template(...))
  resp.set_cookie('username', 'the username')
  return resp
```

### 重定向和错误

- 重定向 `redirect()`
- 终止请求 `about()`

```python
from flask import abort, redirect, url_for

@app.route('/')
def index():
  return redirect(url_for('login'))

@app.route('/login')
def login():
  abort(401)
  this_is_never_executed()
```

### 自定义错误页面

```python
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
  return render_template('page_not_found.html'), 404
```

## 响应数据

### 响应转换逻辑

| 返回值                       | 转换逻辑                                                     |
| ---------------------------- | ------------------------------------------------------------ |
| 正确类型的响应对象           | 直接从视图返回                                               |
| 字符串                       | 使用该数据和默认参数创建一个响应对象                         |
| 字符串或字节的迭代器或生成器 | 流响应                                                       |
| 字典或列表                   | 使用 **jsonify()** 创建一个响应对象                          |
| 元组                         | 元组中的项可以提供额外信息; 必须采用 `(response, status)/(response, headers)/(response, status, headers)` 的形式; status 值覆盖状态代码, headers 可以是附加标头列表或字典 |
| 非上述                       | 假定返回值为一个有效的 WSGI 应用程序, 并将其转换为响应对象   |

### 获取响应对象

```python
from flask import render_template

# 转换前
@app.errorhandler(404)
def not_found(error):
  return render_template('error.html'), 404

# 转换后
@app.errorhandler(404)
def page_not_found(error):
  return render_template('page_not_found.html'), 404
```

### JSON API

- 从视图返回一个 dict 或 list, 将转换为 JSON 响应
- 将数据传递给 jsonify() 函数的快捷方式，该函数将序列化任何受支持的 JSON 数据类型

## 高级配置

### 项目目录配置

```md
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── .venv/
├── pyproject.toml
└── MANIFEST.in
```

```ini
# .gitignore
.venv/

*.pyc
__pycache__/

instance/

.pytest_cache/
.coverage
htmlcov/

dist/
build/
*.egg-info/
```

### 引用程序工厂

- 不应该在全局范围内创建 Flask 实例, 而是应该在函数内创建
  - 即 构建应用程序工厂, 进行所需的任何配置, 注册, 以及其他设置

```python
import os

from flask import Flask


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
  )

  if test_config is None:
    # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)
  else:
    # load the test config if passed in
    app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
      os.makedirs(app.instance_path)
    except OSError:
      pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
      return 'Hello, World!'

    return app
```



## 部署生产环境

- 在使用反向代理或许多 Python 托管平台时，代理会拦截并向本地 WSGI 服务器转发所有外部请求
- HTTP 服务器应设置 X-Forwarded- 头以将真实值传递给应用程序。然后可以通过使用 Werkzeug 提供的 X-Forwarded-For Proxy Fix 中间件对其进行包装，告诉应用程序信任并使用这些值

```python
from werkzeug.middleware.proxy_fix import ProxyFix

# 仅当 flask 服务部署于代理之后采用该中间件
app.wsgi_app = ProxyFix(
  app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)
```

