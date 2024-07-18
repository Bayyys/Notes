## 项目初始化

### 项目结构

#### 完整项目结构

<img src="https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/06/28/截屏2024-06-25-14.49.16-1719555615.png" alt="截屏2024-06-25 14.49.16" style="zoom:33%;" />

| 文件(夹)名           | 功能介绍                         |
| -------------------- | -------------------------------- |
| .gradle和.idea       | Android Studio自动生成的一些文件 |
| **app**              | **项目的代码、资源**             |
| build                | 编译生成文件                     |
| gradle               | gradle wrapper配置文件           |
| .gitignore           | 版本控制忽略文件                 |
| **build.gradle**     | 项目全局的gradle构建脚本         |
| gradle.properties    | 全局gradle配置文件               |
| gradlew和gradlew.bat | gradle命令行执行文件(linux/win)  |
| local.peopertirs     | 指定本机中的Android SDK路径      |
| setting.gradle       | 指定项目引入模块                 |

#### 主要文件夹(app)

<img src="https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/06/28/截屏2024-06-25-14.57.39-1719555615.png" alt="截屏2024-06-25 14.57.39" style="zoom:33%;" />

| 文件(夹)名          | 功能介绍                           |
| ------------------- | ---------------------------------- |
| build               | 编译生成文件                       |
| src                 | 资源+代码目录                      |
| andriodTest         | Android Test测试用例               |
| main                | 主要资源+代码目录                  |
| java                | 主要代码目录                       |
| res                 | 主要资源目录                       |
| AndroidManifest.xml | 项目配置文件(组件注册、权限设置等) |
| test                | 单元测试用例                       |
| .gitignore          | 版本控制忽略配置                   |
| build.gradle        | app模块的gradle构建脚本            |
| progurad-rules.pro  | 指定项目代码的混淆规则             |

#### 资源文件夹(res)

| 文件(夹)名    | 功能介绍                      |
| ------------- | ----------------------------- |
| drawable      | 图片                          |
| mipmap-(*)dpi | 应用图标                      |
| values(-*)    | 存放设定值                    |
| xml           | xml格式(会被编译为二进制文件) |
| raw           | 不进行编译的源文件            |

### 相关特性

#### 四大组件

- 活动（Activity）
- 服务（Service）
- 广播接收器（Broadcast Receiver）
- 内容提供器（Content Provider）

#### 项目资源引用

- 代码 `R.string.mystr`、`R.style.mystyle`
- XML `@string/mystr`、`@style/mystyle`

#### Build.gradle

> **Gradle** 使用基于 **Groovy** 的领域特定语言（DSL）来声明项目设置

```groovy
// 指定模块类型
// application - 应用程序(可直接运行)
// library - 库模块(依赖其他模块)
plugins {
  alias(libs.plugins.android.application)
}

// android 闭包
// 配置项目构建的各种属性
android {
  namespace 'com.bayyy.start'
  compileSdk 34	// 指定项目的编译版本

  // 细节哦配置
  defaultConfig {
      applicationId "com.bayyy.start"	// 指定项目包名
      minSdk 24	// 最低兼容 Android 系统版本
      targetSdk 34	// 最佳目标版本
      versionCode 1	// 版本号
      versionName "1.0"	// 版本名

      testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
  }
	
  // 指定生产安装文件的相关配置
  // 一般有 release 和 debug(可忽略) 两个闭包
  buildTypes {
      release {
          minifyEnabled false	// 是否启用代码混淆
          proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'	// 指定混淆规则文件 (Android SDK目录下/当前项目根目录下)
      }
  }
  compileOptions {
      sourceCompatibility JavaVersion.VERSION_1_8
      targetCompatibility JavaVersion.VERSION_1_8
  }
}

// 指定项目的依赖关系
// 本地依赖、库依赖、远程依赖
dependencies {
  implementation libs.appcompat
  implementation libs.material
  implementation libs.activity
  implementation libs.constraintlayout
  testImplementation libs.junit
  androidTestImplementation libs.ext.junit
  androidTestImplementation libs.espresso.core
}
```

#### 日志工具 Log

> 日志工具类 `android.util.Log`

- `Log.v(tag, msg)`
- `Log.d()`
- `Log.i()`
- `Log.w()`
- `Log.e()`

## 活动 Activity

> 活动是包含用户界面的组件，主要用于和用户交互

### 创建

#### 手动创建空活动

- `Generate a Layout File`  自动为该活动创建一个对应的布局
- `Launcher Activity` 设置为当前项目的主活动

<img src="https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/06/28/截屏2024-06-25-15.40.40-1719555615.png" alt="截屏2024-06-25 15.40.40" style="zoom:33%;" />

```java
// com.bayyy.activity.FirstActivity.java
public class FirstActivity extends AppCompatActivity {
  @Override
  protected void onCreate(Bundle savedInstanceState) {
      super.onCreate(savedInstanceState);
  }
}
```

#### 创建和加载布局

- `app/src/main/res/layout -> Layout resource file` 

![截屏2024-06-25 15.45.22](https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/06/28/截屏2024-06-25-15.45.22-1719555615.png)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
  android:layout_width="match_parent"
  android:layout_height="match_parent">

  <Button
      android:id="@+id/btn_1"
      android:layout_width="match_parent"
      android:layout_height="wrap_content"
      android:text="@string/btn_1" />

</LinearLayout>
```

- 效果展示

<img src="https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/06/28/截屏2024-06-25-15.48.06-1719555615.png" alt="截屏2024-06-25 15.48.06" style="zoom: 25%;" />

- 引入布局

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.first_layout);	// 引入布局
}
```

#### 活动注册

- 所有的活动都需要在 `AndroidManifest.xml` 中注册才能够生效

```xml
  <!-- name: 指定启动的Activity -->
  <!-- exported: 是否允许其他应用启动该Activity -->
  <!-- label: 显示在应用启动器中的名称 -->
  <activity
      android:name="com.bayyy.activity.FirstActivity"
      android:exported="true"
      android:label="My First Activity">
      <!-- intent-filter: 指定Activity的启动方式 -->
      <intent-filter>
          <!-- action: 指定Activity的启动方式(MAIN: 主Activity, VIEW: 浏览器) -->
          <action android:name="android.intent.action.MAIN" />
          <!-- category: 指定Activity的启动方式(LAUNCHER: 主Activity, DEFAULT: 默认Activity) -->
          <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
  </activity>
```

<img src="https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/06/28/截屏2024-06-25-16.01.52-1719555615.png" alt="截屏2024-06-25 16.01.52" style="zoom:25%;" />

### 基本使用

#### 使用Toast

> 消息通知类

- 可以通过 `findViewById()` 获取现在布局文件中定义的元素
  - 默认返回 `View` 对象

```java
Button btn_1 = (Button) findViewById(R.id.btn_1);
btn_1.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View view) {
        Toast.makeText(FirstActivity.this, "You clicked Button 1", Toast.LENGTH_SHORT).show();
    }
})
```

<img src="https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/06/28/截屏2024-06-25-16.06.35-1719555615.png" alt="截屏2024-06-25 16.06.35" style="zoom:33%;" />

#### 修改Menu项

- 创建menu项
  - `res -> menu -> main.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android">
  <item
      android:id="@+id/add_item"
      android:title="Add" />
  <item
      android:id="@+id/remove_item"
      android:title="Remove" />
</menu>
```

- 重写目录项相关代码

```java
@Override
public boolean onCreateOptionsMenu(Menu menu) {
    getMenuInflater().inflate(R.menu.main, menu);
    return super.onCreateOptionsMenu(menu);
}

@Override
public boolean onOptionsItemSelected(@NonNull MenuItem item) {
    if (item.getItemId() == R.id.add_item) {
        Toast.makeText(this, "You clicked Add", Toast.LENGTH_SHORT).show();
    } else if (item.getItemId() == R.id.remove_item) {
        Toast.makeText(this, "You clicked Remove", Toast.LENGTH_SHORT).show();
    } else {
        return false;
    }
    return true;
}
```



<img src="https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/06/28/截屏2024-06-25-16.19.24-1719555615.png" alt="截屏2024-06-25 16.19.24" style="zoom:25%;" />

### 活动切换

> 使用Intent在活动间进行切换
>
> - Intent 是 Android 程序中各组件之间进行交互的一种重要方式
>   - 可以指明当前组件的执行动作
>   - 还可以在不同组件间传递数据
> - 一般用于启动活动、启动服务、发送广播等场景

#### 使用显式的Intent

- `new Intent(Context packageContext, Class<?> cls);`
  - `Context` 传入启动活动的上下文
  - `Class<?>` 指定想要启动的目标活动

- `startActivity(intent)`
  - 启动切换活动意图

```java
findViewById(R.id.btn_3).setOnClickListener(
    View -> {
        Intent intent = new Intent(FirstActivity.this, SecondActivity.class);
        startActivity(intent);
    }
);
```

<img src="https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/06/28/截屏2024-06-25-16.53.22-1719555615.png" alt="截屏2024-06-25 16.53.22" style="zoom:33%;" />

#### 使用隐式Intent

- 隐式Intent通过指定一系列的`action`和`category`，来筛选合适的活动
  - 注意：必须制定一个默认的 `”android.intent.category.DEFAULT“`

```xml
  <activity
      android:name="com.bayyy.activity.SecondActivity"
      android:exported="true">
      <intent-filter>
          <action android:name="com.bayyy.activity.SECOND_ACTIVITY" />

          <category android:name="android.intent.category.DEFAULT" />
          <category android:name="com.bayyy.activity.MY_CATEGORY" />
      </intent-filter>
  </activity>
```

```java
findViewById(R.id.btn_3).setOnClickListener(
      View -> {
          Intent intent = new Intent("com.bayyy.activity.SECOND_ACTIVITY");
          intent.addCategory("com.bayyy.activity.MY_CATEGORY");
          startActivity(intent);
      }
);
```

#### 更多隐式Intent用法

- 进行多程序之间的功能共享：使用浏览器打开百度
  1. 指定 Intent 的 action 为 `Intent.ACTION_VIEW`
     - 内置常量值 `android.intent.action.VIEW`
  2. 将网址字符串解析为 Uri 对象
  3. 将 Uri 对象传递给 intent

```java
// btn_4: 跳转到百度
findViewById(R.id.btn_4).setOnClickListener(View -> {
    Intent intent = new Intent(Intent.ACTION_VIEW);
    intent.setData(Uri.parse("https://www.baidu.com"));
    startActivity(intent);
});
```

> - 本质是跳转到所有 `<intent-filter> - <data>` 内容包含网址的活动
>
>   - `android:scheme` 数据协议部分，如 http
>
>   - `android:host` 主机名部分，如 www.baidu.com
>
>   - `android:port` 端口部分，紧跟在主机名后
>
>   - `android:path` 主机名和端口之间的部分，域名之后的内容
>
>   - `android:mimeType` 可处理的数据类型
>
> - 将某个活动 标注
>   - `<action android:name="android.intent.action.VIEW" />`
>   - `<data android:scheme="http" />`
>
> <img src="https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/06/28/截屏2024-06-25-17.41.42-1719555615.png" alt="截屏2024-06-25 17.41.42" style="zoom:25%;" />

- 其他功能
  - `geo:xxx` 地理位置 
  - `Intent.ACTION_DIAL -> tel:xxx` 拨打电话

#### 向活动传递数据

> - 使用 `putExtra()` 重载方法进行数据暂存
> - 跳转活动即可获取数据

- ` putExtra(String name, @Nullable String value)`
  - 键 - 值

```java
  // btn_5: 发送数据到 ThirdActivity
  findViewById(R.id.btn_5).setOnClickListener(View -> {
      Intent intent = new Intent(FirstActivity.this, ThirdActivity.class);
      intent.putExtra("extra_data", "Hello ThirdActivity");
      startActivity(intent);
  });
```

- `intent.getxxx`

```java
Intent intent = getIntent();
String data = intent.getStringExtra("extra_data");
```

<img src="https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/06/28/image-20240625175417823-1719555615.png" alt="image-20240625175417823" style="zoom:25%;" />

#### 返回数据

- 使用 `startActivityForResult(intent: Intent, requestCode: Int)` 表明通知发送并接受数据

  - 指定 Intent

  - 请求码，可以用来确认请求

```java
// btn_6: 发送并接受返回数据
findViewById(R.id.btn_6).setOnClickListener(View -> {
    Intent intent = new Intent(FirstActivity.this, ThirdActivity.class);
    startActivityForResult(intent, 1);
});
```

- 返回数据
  - 构建一个无 “intent” 的 Intent
  - 载入数据
  - 调用 `setResult()`  
    - 向前活动返回处理结果
    - 设置带有数据的 intent

```java
findViewById(R.id.btn_3).setOnClickListener(
    View -> {
        Intent intent1 = new Intent();
        intent1.putExtra("data_return", "Hello FirstActivity");
        setResult(RESULT_OK, intent1);
        finish();
    }
);
```

- 重写 `onActivityResult` 来获取返回数据
  - `protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {}`
  - `请求码, 返回码, 返回数据`

```java
@Override
protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    if (requestCode == 1 && resultCode == RESULT_OK) {
        assert data != null;
        String returnedData = data.getStringExtra("data_return");
        Toast.makeText(this, returnedData, Toast.LENGTH_SHORT).show();
    }
}
```

- 可以通过重写 `onBackPressed()` 来修改 Back 键的效果

```java
@Override
public void onBackPressed() {
    Intent intent = new Intent();
    intent.putExtra("data_return", "Hello FirstActivity, via Back Pressed.");
    setResult(RESULT_OK, intent);
    super.onBackPressed();
}
```

#### registerForActivityResult

- `onActivityResult()` 方法废弃 -> `registerForActivityResult()`
  - 旧方法存在问题
    1. 在启动 activity 以获取结果时，可能会出现进程和 activity 因内存不足而被销毁的情况
    2. onActivityResult 回调方法嵌套耦合严重，逻辑混乱导致难以维护

##### 注册回调

```java
registerForActivityResult(
    contract: ActivityResultContract<I, O>,
    callback: ActivityResultCallback<O>
): ActivityResultLauncher<I> {
    return registerForActivityResult(contract, activityResultRegistry, callback)
}
```

- `ActivityResultContract` 定义生成结果所需的输入类型以及结果的输出类型
  - 这些 API 可为拍照和请求权限等基本 intent 操作提供默认协定，同时还可以创建自定义协定。
- `ActivityResultCallback` 是单一方法接口，带有 `onActivityResult()` 方法，可接受 `ActivityResultContract` 中定义的输出类型的对象

```java
// btn_7: 使用 registerForActivityResult 进行消息发送+接收
ActivityResultLauncher<Intent> launcher = registerForActivityResult(new ActivityResultContracts.StartActivityForResult(),
  new ActivityResultCallback<ActivityResult>() {
      @Override
      public void onActivityResult(ActivityResult result) {
          if (result.getResultCode() == FirstActivity.RESULT_OK) {
              Log.d("data_return", result.getData().getStringExtra("data_return"));
          }
      }
});
findViewById(R.id.btn_7).setOnClickListener(
  View -> {
      Intent i = new Intent(FirstActivity.this, ThirdActivity.class);
      launcher.launch(i);
});
```

### Activity 活动周期

#### 返回栈

<img src="https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/06/28/image-20240625185514591-1719555615.png" alt="image-20240625185514591" style="zoom: 33%;" />

#### 活动状态

1. **运行状态** 活动处于栈顶
2. **暂停状态** 活动不处于栈顶，但仍然可见
   - 对话框等不占用完整屏幕
3. **停止状态** 不处于栈顶，且完全不可见
4. **销毁状态** 从返回栈中移除

#### 活动生命周期

<img src="https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/06/28/119921-1719555615.png" alt="Android四大组件之Activity详解" style="zoom: 50%;" />

| 回调方法      | 说明                                                         |
| ------------- | ------------------------------------------------------------ |
| `onCreate()`  | 开启activity的第一个方法，这个方法会初始化setContentLayout()方法（屏幕绘制），作用是进行Activity的一些初始化工作，比如使用setContentView加载布局，对一些控件和变量进行初始化等，此时Activity还在后台，不可见 |
| `onStart()`   | 表示Activity正在被启动，已经从不可见到可见状态（不是指用户可见，指Activity在后台运行，没有出现在前台），但还是无法与用户进行交互 |
| `onResume()`  | Activity已经变为可见状态了，并且出现在前台工作了，也就是指用户可见了。此阶段可以打开独占设备 |
| `onPause()`   | Activity正在暂停，但Activity依然可见，可以执行一些轻量级操作，但一般不会进行太多操作，因为这样会影响用户体验。通常用于确认对于持久性的数据保存更改，动画的停止以及任何其他可能消耗cpu的内容， |
| `onStop()`    | Activity即将暂停，此时Activity工作在后台，已经不可见了，可以与onPause方法一样做一些轻量级操作，但依然不能太耗时。比如可能是被另一个Activity覆盖，或者退回到桌面，在onStop方法下系统内存紧张时，有可能会被系统回收 |
| `onDestroy()` | 即将被销毁，当Activity结束或者被系统销毁Activity实例的时候，会被调动该方法 |
| `onRestart()` | 被重新启动的时，调用此方法。比如从桌面回到应用中时           |

#### 回收时临时消息存储

- `onSaveInstanceState()` 保存临时数据
  - 此方法保证活动回收前被调用

```java
@Override
public void onSaveInstanceState(@NonNull Bundle outState, @NonNull PersistableBundle outPersistentState) {
    String tmpData = "This is a temp msg.";
    outState.putString("tmpData", tmpData);
    super.onSaveInstanceState(outState, outPersistentState);
    Log.d(TAG, "onSaveInstanceState");
}
```

- `onCreate(Bundle outState)` 中获取临时数据

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    Log.d(TAG, "onCreate");
    setContentView(R.layout.main_layout);
    if (savedInstanceState != null) {
        String tmpData = savedInstanceState.getString("tmpData");
        Log.d(TAG, "get tmpData: " + tmpData);
    }
}
```

### 活动启动模式

- 模式区分

  - `standard`

  - `singleTop`

  - `singleTask`

  - `singleInstance`

- 指定方式

  - 通过 `<activity>` 标签指定 `android:launchMode` 选择启动模式

| 模式                  | 说明                                                         |      |
| --------------------- | ------------------------------------------------------------ | ---- |
| standard              | 默认类型，每次使用时创建一个新的活动对象                     |      |
| singleTop             | 类似singleInstance，不同点在于会复用，栈顶只会存在唯一的Activity |      |
| singleTask            | singleTop的增强版，会有Intent.FLAG_ACTIVITY_BROUGHT_TO_FRONT的标记，若在栈顶，则不会 |      |
| singleInstance        | 目标Activity独占一个任务栈，且只会创建一次，只允许一个活动实例运行，每次加载会将其带到前台，同时调用Activity的`onNewIntent`方法进行通知；若尝试启动新的Activity，新创建必须为不同的任务栈 |      |
| singleInstancePerTask | singleInstance的增强版，Activity只能作为任务栈的根结点       |      |

### 简单应用

#### 提供创建日志

- 新建 `BaseActivity` 继承 `AppCompatActivity` 作为工程的基类

```java
public class BaseActivity extends AppCompatActivity {
  @Override
  public void onCreate(@Nullable Bundle savedInstanceState, @Nullable PersistableBundle persistentState) {
      super.onCreate(savedInstanceState, persistentState);
      Log.d("BaseActivity", getClass().getSimpleName());
  }
}
```

#### 实现直接退出程序

- 新建 `ActivityCollector` 类作为活动管理器，对所有活动进行管理

```java
public class ActivityCollector {
  public static List<Activity> activities = new ArrayList<>();

  public static void addActivity(Activity activity) {
      activities.add(activity);
  }

  public static void removeActivity(Activity activity) {
      activities.remove(activity);
  }

  public static void finishAll() {
      for (Activity activity : activities) {
          if (!activity.isFinishing()) {
              activity.finish();
          }
      }
  }
}
```

- `onCreate()/onDestory()` 中增加增删操作
  - 关闭操作可以直接执行 `ActivityCollector.finishAll()`

```java
public class BaseActivity extends AppCompatActivity {
  @Override
  public void onCreate(@Nullable Bundle savedInstanceState, @Nullable PersistableBundle persistentState) {
      super.onCreate(savedInstanceState, persistentState);
      Log.d("BaseActivity", getClass().getSimpleName());
      ActivityCollector.addActivity(this);
  }

  @Override
  protected void onDestroy() {
      super.onDestroy();
      ActivityCollector.removeActivity(this);
  }
}
```

#### 活动启动预留传值

- 若某Activity需要其他进行传值，可以预留函数，其他活动使用时可以直接进行唤醒+传值

```java
public static void actionStart(Context context, String data1, String data2) {
    Intent intent = new Intent(context, ThisActivity.class);
    intent.putExtra("param1", data1);
    intent.putExtra("param2", data2);
    context.startActivity(intent);
}
```

- 其他活动调用

```java
ThisActivity.actionStart(MainActivity.this, "data1", "data2");
```

## 程序界面 UI

> 编写 UI 界面通过编写 XML 代码

### 常用控件的使用方法

#### TextView

- `android:layout_width/android:layout_height`
  - `match_parent`
  - `fill_parent`
  - `wrap_content` 

- `android:text` 指定显示文字
- `gravity` 指定文字对齐方式
- `layout_gravity` 指定布局对齐方式

```xml
<TextView
    android:id="@+id/text_view"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:layout_gravity="top"
    android:gravity="center"
    android:text="This is TextView"
    android:textColor="#ff0000"
  	android:textSize="24sp" />
```

#### Button

- `textAllCaps` 英文字母是否自动进行大写转换

```xml
  <Button
      android:id="@+id/btn_demo"
      android:layout_width="wrap_content"
      android:layout_height="wrap_content"
      android:layout_gravity="center_horizontal"
      android:text="Show text in EditText" />
```

- 事件注册方式
  1. 匿名类

```java
findViewById(R.id.btn_demo).setOnClickListener(
    new View.OnClickListener() {
      @Override
      public void onClick(View view) {
        Toast.makeText(CustomWidget.this, "Clicked a Button.", Toast.LENGTH_SHORT).show();
      }
    }
);

// lambda 表达式方式
findViewById(R.id.btn_demo).setOnClickListener(
    v -> Toast.makeText(this, "Clicked a Button.", Toast.LENGTH_SHORT).show();
);
```

2. 接口实现

```java
public class CustomWidget extends AppCompatActivity implements View.OnClickListener {
  @Override
  protected void onCreate(Bundle savedInstanceState) {
    // ...
    findViewById(R.id.btn_demo).setOnClickListener(this);
  }
  @Override
  public void onClick(View view) {
    switch (view.getId()) {
      case R.id.btn_demo:
        Toast.makeText(this, "Clicked a Button.", Toast.LENGTH_SHORT).show();
        break;
    }
  }
}
```

#### EditText

- `hint` 提示文字
- `maxLines` 最大行数

```xml
<EditText
          android:id="@+id/et_text"
          android:layout_width="match_parent"
          android:layout_height="wrap_content"
          android:gravity="center_horizontal"
          android:hint="请输入文字..."
          android:maxLines="2" />
```

- 获取其中文字

```java
String inputTxt = ((EditText) findViewById(R.id.et_text)).getText().toString();
Toast.makeText(this, inputTxt, Toast.LENGTH_SHORT).show();
```

#### ImageView

```xml
<ImageView
           android:id="@+id/img_view"
           android:layout_width="match_parent"
           android:layout_height="match_parent"
           <!-- 自动调整尺寸 -->
           android:adjustViewBounds="true"
           android:contentDescription="This is ImageView"
           android:src="@drawable/img" />
```

```java
((ImageView) findViewById(R.id.img_view)).setImageResource(R.drawable.img);
```

#### ProgressBar

```xml
<ProgressBar
             android:id="@+id/progress_bar"
             style="?android:attr/progressBarStyleHorizontal"
             android:layout_width="match_parent"
             android:layout_height="match_parent"
             android:layout_gravity="center_horizontal"
             android:max="100"
             android:min="0"
             android:visibility="visible" />
```

```java
ProgressBar progressBar = findViewById(R.id.progress_bar);

findViewById(R.id.p_visiable).setOnClickListener(
  v -> progressBar.setVisibility(progressBar.getVisibility() == ProgressBar.VISIBLE ? ProgressBar.INVISIBLE : ProgressBar.VISIBLE));
findViewById(R.id.p_style).setOnClickListener(
  v -> progressBar.setScrollBarStyle(progressBar.getScrollBarStyle() == ProgressBar.SCROLLBARS_INSIDE_OVERLAY ? ProgressBar.SCROLLBARS_INSIDE_INSET : ProgressBar.SCROLLBARS_INSIDE_OVERLAY));
findViewById(R.id.p_add).setOnClickListener(v -> progressBar.setProgress(progressBar.getProgress() + 10));
findViewById(R.id.p_add).setOnClickListener(v -> progressBar.setProgress(progressBar.getProgress() - 10));
```

#### AlertDialog

```java
new AlertDialog.Builder(this)
  .setTitle("Alert Dialog")
  .setMessage("This is an alert dialog")
  .setPositiveButton("OK", (dialog, which) -> {
    Toast.makeText(this, "OK", Toast.LENGTH_SHORT).show();
  })
  .setNegativeButton("Cancel", (dialog, which) -> {
    Toast.makeText(this, "Cancel", Toast.LENGTH_SHORT).show();
  })
  .show();

```

#### ProgressDialog

```java
ProgressDialog progressDialog = new ProgressDialog(this);
progressDialog.setTitle("Progress Dialog");
progressDialog.setMessage("This is a progress dialog");
progressDialog.setCancelable(true);
progressDialog.show();
```

### 基本布局

#### LinearLayout 线性布局

- `orientation` 排列方向

```xml
<LinearLayout
              android:layout_width="match_parent"
              android:layout_height="wrap_content"
              android:orientation="vertical">

  <Button
          android:layout_width="match_parent"
          android:layout_height="wrap_content"
          android:text="Button1" />
	<!-- ... -->
  
</LinearLayout>
```

- 内部组件属性
  - `layout_gravity` 指定控件在布局中的对齐方式
  - `layout_weight` 以比例形式指定控件尺寸
    - 此时 `layout_width:0dp`

#### RelativeLayout 相对布局

- 相对于父控件
  - `layout_alignParentLeft/Top/Right/Bottom/centerInParent`

![image-20240628165439190](https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/06/28/image-20240628165439190-1719564880.png)

```xml
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
                android:layout_width="match_parent"
                android:layout_height="match_parent">

  <Button
          android:id="@+id/button1"
          android:layout_width="wrap_content"
          android:layout_height="wrap_content"
          android:layout_alignParentStart="true"
          android:layout_alignParentLeft="true"
          android:layout_alignParentTop="true"
          android:text="Button 1" />

  <Button
          android:id="@+id/button2"
          android:layout_width="wrap_content"
          android:layout_height="wrap_content"
          android:layout_alignParentTop="true"
          android:layout_alignParentEnd="true"
          android:layout_alignParentRight="true"
          android:text="Button 2" />
</RelativeLayout>
```

- 相对于其他控件
  - `layout_above/layout_below` 使被控组件位于另一组件上方/下方
  - `layout_toLeftOf/layout_toRightOf` 使被控组件位于另一组件左侧/右侧
  - `layout_alignTop/Bottom/Left/Right` 使被控组件与另一组件边缘对齐

![image-20240628165516659](https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/06/28/image-20240628165516659-1719564917.png)

```xml
<RelativeLayout
                android:layout_width="match_parent"
                android:layout_height="300dp">

  <Button
          android:id="@+id/btn_2_center"
          android:layout_width="wrap_content"
          android:layout_height="wrap_content"
          android:layout_centerInParent="true"
          android:text="Center" />

  <Button
          android:layout_width="wrap_content"
          android:layout_height="wrap_content"
          android:layout_above="@+id/btn_2_center"
          android:layout_toLeftOf="@+id/btn_2_center"
          android:text="above+toLeft" />

  <Button
          android:layout_width="wrap_content"
          android:layout_height="wrap_content"
          android:layout_below="@id/btn_2_center"
          android:layout_toRightOf="@+id/btn_2_center"
          android:text="below+toRight" />

  <Button
          android:layout_width="wrap_content"
          android:layout_height="wrap_content"
          android:layout_above="@id/btn_2_center"
          android:layout_alignLeft="@id/btn_2_center"
          android:text="above+alignLeft" />

  <Button
          android:layout_width="wrap_content"
          android:layout_height="wrap_content"
          android:layout_below="@id/btn_2_center"
          android:layout_alignRight="@id/btn_2_center"
          android:text="below+alignRight" />
</RelativeLayout>
```

#### FrameLayout 帧布局

- 默认左对齐，根据图层顺序依次排列
  - 可以使用 `gravity` 进行排序

![image-20240628170932463](https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/06/28/image-20240628170932463-1719565772.png)

```xml
<FrameLayout
             android:layout_width="match_parent"
             android:layout_height="match_parent">

  <TextView
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="hello world!" />

  <Button
          android:layout_width="wrap_content"
          android:layout_height="wrap_content"
          android:text="button" />
</FrameLayout>
```

#### PercentXXXLayout 百分比布局

- 需要添加额外依赖
  - `implementation 'com.android.support:percent:28.0.0'`
- 需要给定完整包路径
- 需要定义app命名空间

![image-20240628172744582](https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/06/28/image-20240628172744582-1719566865.png)

```xml
<androidx.percentlayout.widget.PercentFrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
                                                  xmlns:app="http://schemas.android.com/apk/res-auto"
                                                  android:id="@+id/main"
                                                  android:layout_width="match_parent"
                                                  android:layout_height="match_parent">

  <Button
          android:layout_width="wrap_content"
          android:layout_height="wrap_content"
          android:layout_gravity="left|start"
          android:text="Button1"
          app:layout_heightPercent="20%"
          app:layout_widthPercent="50%" />

  <Button
          android:layout_width="wrap_content"
          android:layout_height="wrap_content"
          android:layout_gravity="right|end"
          android:text="Button2"
          app:layout_heightPercent="20%"
          app:layout_widthPercent="50%" />

</androidx.percentlayout.widget.PercentFrameLayout>
```

### 自定义控件

<img src="https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/06/28/image-20240628172906965-1719566947.png" alt="image-20240628172906965" style="zoom: 33%;" />

- 新建布局 `my_layout.xml`
- 引入
  1. 简单引入 `<include layout="@layout/my_layout>"`
  2. 自定义化引入：重写类

```java
public class MyLayout extends LinearLayout {
  public MyLayout(Context context, @Nullable AttributeSet attrs) {
    super(context, attrs);
    LayoutInflater.from(context).inflate(R.layout.my_layout, this);
  }
}
```

```xml
<com.bayyy.ui.MyLayout
                       android:layout_width="match_parent"
                       android:layout_height="wrap_content" />
```

- 此时若有公共组件的公共方法, 可以在自定义组件类中进行定义

```java
public class MyLayout extends LinearLayout {
  public MyLayout(Context context, @Nullable AttributeSet attrs) {
    super(context, attrs);
    LayoutInflater.from(context).inflate(R.layout.my_layout, this);
    findViewById(R.id.btn_back).setOnClickListener(v -> Toast.makeText(context, "Back", Toast.LENGTH_SHORT).show());
    findViewById(R.id.btn_exit).setOnClickListener(v -> Toast.makeText(context, "Exit", Toast.LENGTH_SHORT).show());
  }
}
```

### ListView

#### 简单用法

```xml
  <ListView
      android:id="@+id/list_view"
      android:layout_width="match_parent"
      android:layout_height="wrap_content" />
```

- 需要使用 **适配器** 实现数据的传入

```java
private String[] data = {"北京", "上海", "广州", "深圳", "杭州", "南京", "苏州", "成都", "重庆", "武汉};
  // ...
ArrayAdapter<String> adapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, data);
((ListView) findViewById(R.id.list_view)).setAdapter(adapter);
```

#### 自定义界面

- 定义实体类

```java
public class Fruit {
  private String name;
  private int imageId;

  public Fruit(String name, int imageId) {
    this.name = name;
    this.imageId = imageId;
  }

  public int getImageId() {
    return imageId;
  }

  public String getName() {
    return name;
  }
}
```

- 定义自定义布局

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
              android:layout_width="match_parent"
              android:layout_height="match_parent"
              android:orientation="vertical">

  <ImageView
             android:id="@+id/fruit_image"
             android:layout_width="wrap_content"
             android:layout_height="wrap_content" />

  <TextView
            android:id="@+id/fruit_name"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_marginLeft="10dp" />

</LinearLayout>
```

- 自定义适配器
  - 继承 `ArrayAdapter`
  - 重写 构造方法 和`getView()`
    - 确保子项滚动到屏幕中时能够获取到数据

```java
public class FruitAdapter extends ArrayAdapter<Fruit> {

  private int resourceId;

  public FruitAdapter(@NonNull Context context, int resource, @NonNull List<Fruit> objects) {
    super(context, resource, objects);
    resourceId = resource;
  }

  @NonNull
  @Override
  public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
    Fruit fruit = getItem(position);
    View view = LayoutInflater.from(getContext()).inflate(resourceId, parent, false);
    TextView fruitName = (TextView) view.findViewById(R.id.fruit_name);
    ImageView fruitImage = (ImageView) view.findViewById(R.id.fruit_image);
    fruitImage.setImageResource(fruit.getImageId());
    fruitName.setText(fruit.getName());
    return view;
  }
}

```

#### 运行优化

- `getView()` 中 `convertView` 会缓存布局

```java
@NonNull
@Override
public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
  Fruit fruit = getItem(position);
  View view;
  if (convertView == null) {
    view = LayoutInflater.from(getContext()).inflate(resourceId, parent, false);
  } else {
    view = convertView;
  }
  TextView fruitName = (TextView) view.findViewById(R.id.fruit_name);
  ImageView fruitImage = (ImageView) view.findViewById(R.id.fruit_image);
  fruitImage.setImageResource(fruit.getImageId());
  fruitName.setText(fruit.getName());
  return view;
}
```

- 使用 `ViewHolder` 缓存数据

```java
@Override
public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
  Fruit fruit = getItem(position);
  View view;
  ViewHolder viewHolder;
  if (convertView == null) {
    view = LayoutInflater.from(getContext()).inflate(resourceId, parent, false);
    viewHolder = new ViewHolder();
    viewHolder.fruitImage = (ImageView) view.findViewById(R.id.fruit_image);
    viewHolder.fruitName = (TextView) view.findViewById(R.id.fruit_name);
    view.setTag(viewHolder);
  } else {
    view = convertView;
    viewHolder = (ViewHolder) view.getTag();
  }
  viewHolder.fruitImage.setImageResource(fruit.getImageId());
  viewHolder.fruitName.setText(fruit.getName());
  return view;
}

class ViewHolder {
  ImageView fruitImage;
  TextView fruitName;
}
```

- 降低 `findByID()` 的调用次数

#### 点击事件

```java
FruitAdapter fruitAdapter = new FruitAdapter(this, R.layout.fruit_item, fruitList);
ListView listView = (ListView) findViewById(R.id.list_view);
listView.setAdapter(fruitAdapter);
listView.setOnItemClickListener((parent, view, position, id) -> {
  Fruit fruit = fruitList.get(position);
  Toast.makeText(MyListView.this, fruit.getName(), Toast.LENGTH_SHORT).show();
});
```

### RecyclerView

> 增强版的 `ListView，又花了效率和布局问题

- 需要增加 `support:recyclerview` 包

#### 基本用法

- 包含完整路径

```xml
<androidx.recyclerview.widget.RecyclerView
                                           android:id="@+id/recycler_view"
                                           android:layout_width="match_parent"
                                           android:layout_height="match_parent" />
```

- 重写适配器 继承 `RecyclerView.Adapter`
  - 内部类 `ViewHolder` 继承自 `RecyclerView.ViewHolder`
  - 构造参数建立数据
  - 重写
    - `onCreateViewHolder()` 创建 `ViewHolder` 实例
    - `onBindViewHolder()` 对子项进行赋值
    - `getItemCount()` 计算子项数量

```java
public class ReFruitAdapter extends RecyclerView.Adapter {
  private List<Fruit> mFruitList;

  static class ViewHolder extends RecyclerView.ViewHolder {
    ImageView fruitImage;
    TextView fruitName;

    public ViewHolder(@NonNull View itemView) {
      super(itemView);
      fruitImage = itemView.findViewById(R.id.fruit_image);
      fruitName = itemView.findViewById(R.id.fruit_name);
    }

  }

  public ReFruitAdapter(List<Fruit> fruitList) {
    mFruitList = fruitList;
  }

  @NonNull
  @Override
  public RecyclerView.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
    View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.fruit_item, parent, false);
    ViewHolder holder = new ViewHolder(view);
    return holder;
  }


  @Override
  public void onBindViewHolder(@NonNull RecyclerView.ViewHolder holder, int position) {
    Fruit fruit = mFruitList.get(position);
    ((ViewHolder) holder).fruitImage.setImageResource(fruit.getImageId());
    ((ViewHolder) holder).fruitName.setText(fruit.getName());

  }

  @Override
  public int getItemCount() {
    return mFruitList.size();
  }
}
```

- 加载布局
  - 需要 `layoutManager` 指定布局方式
  - 需要 `adapter` 指定列表适配器

```java
RecyclerView recyclerView = (RecyclerView) findViewById(R.id.recycler_view);
LinearLayoutManager linearLayoutManager = new LinearLayoutManager(this);
recyclerView.setLayoutManager(linearLayoutManager);
ReFruitAdapter fruitAdapter = new ReFruitAdapter(fruitList);
recyclerView.setAdapter(fruitAdapter);
```

#### 横向滚动和瀑布流布局

- 横向滚动
  - 设置布局管理器 `LayoutManager` 为 `HORIZONTAL`

```java
LinearLayoutManager linearLayoutManager = new LinearLayoutManager(this);
linearLayoutManager.setOrientation(LinearLayoutManager.HORIZONTAL);
recyclerView.setLayoutManager(linearLayoutManager);
```

- 瀑布流布局

```java
StaggeredGridLayoutManager manager = new StaggeredGridLayoutManager(3, StaggeredGridLayoutManager.VERTICAL);
recyclerView.setLayoutManager(manager);
```

#### 点击事件

- 由子项 View 注册点击事件
  - 修改 `ViewHolder` 增加 `View` 保存布局的实例
  - 对子项的内容注册点击事件

```java
public class ReFruitAdapter extends RecyclerView.Adapter {
  private List<Fruit> mFruitList;

  static class ViewHolder extends RecyclerView.ViewHolder {
    View fruitView;	// 保存布局实例
    ImageView fruitImage;
    TextView fruitName;

    public ViewHolder(@NonNull View itemView) {
      super(itemView);
      fruitView = itemView;
      fruitImage = itemView.findViewById(R.id.fruit_image);
      fruitName = itemView.findViewById(R.id.fruit_name);
    }
  }

  // ...
  
  @NonNull
  @Override
  public RecyclerView.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
    View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.fruit_item, parent, false);
    // 提取 ViewHolder, 并注册点击事件
    final ViewHolder holder = new ViewHolder(view);
    holder.fruitView.setOnClickListener(v ->
        {
          int position = holder.getAdapterPosition();
          Fruit fruit = mFruitList.get(position);
          Toast.makeText(v.getContext(), "You clicked view " + fruit.getName(), Toast.LENGTH_SHORT).show();
        }
    );
    holder.fruitImage.setOnClickListener(v -> {
      int position = holder.getAdapterPosition();
      Fruit fruit = mFruitList.get(position);
      Toast.makeText(v.getContext(), "You clicked image " + fruit.getName(), Toast.LENGTH_SHORT).show();
    });
    return holder;
  }
  
  // ...
}
```

## Fragment

> **Fragment** 是一种嵌入在 Activity 中的 UI 片段
>
> - 更加适配大屏使用

### 简单应用

- 创建左右布局 `left_fragment.xml / right_fragment.xml`
- 分别创建左右布局子类，并实现 `Fragment`

```java
public class LeftFragment extends Fragment {
  @Override
  public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
    View view = inflater.inflate(R.layout.left_fragment, container, false);
    return view;
  }
}

```

- 总布局引入两个布局

```xml
<LinearLayout>
  <fragment
            android:id="@+id/left_fragment"
            android:name="com.bayyy.fragment.view.LeftFragment"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1" />
  <fragment
            android:id="@+id/right_fragment"
            android:name="com.bayyy.fragment.view.RightFragment"
            android:layout_width="0dp"
            android:layout_height="match_parent"
            android:layout_weight="1" />
</LinearLayout>
```

### 添加动态碎片

#### 基本使用

- 更改 `fragment` 为 `FragmentLayout`

```xml
<FrameLayout
             android:id="@+id/right_layout"
             android:layout_width="0dp"
             android:layout_height="match_parent"
             android:layout_weight="1" />
```

- 调用 `replaceFragment()` 进行 fragment 替换
  - 创建 fragment 实例
  - 获取 `FragmentManager`  调用 `replace()` 方法
  - 启动事务并提交

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
  Button btn_jump = (Button) findViewById(R.id.btn_left_fragment);
  btn_jump.setOnClickListener(v -> {
    replaceFragment(new AnotherRightFragment());
  });
  replaceFragment(new RightFragment());
}

private void replaceFragment(Fragment fragment) {
  FragmentManager fragmentManager = getSupportFragmentManager();
  FragmentTransaction transaction = fragmentManager.beginTransaction();
  transaction.replace(R.id.right_layout, fragment);
  transaction.commit();
}
```

- 优化后的添加方式 （避免 IDE 报错）

```java
FragmentManager fragmentManager = this.getSupportFragmentManager();
LeftFragment fragment = (LeftFragment) fragmentManager.findFragmentById(R.id.left_fragment);
Button btn_jump = fragment.getView().findViewById(R.id.btn_left_fragment);
```

#### 模拟返回栈

```java
private void replaceFragment(Fragment fragment) {
  FragmentManager fragmentManager = getSupportFragmentManager();
  FragmentTransaction transaction = fragmentManager.beginTransaction();
  transaction.replace(R.id.right_layout, fragment);
  transaction.addToBackStack(null);	// 将事务添加到返回栈中，接受名字描述返回栈的状态，一般传入 null 即可
  transaction.commit();
}
```

### 通信

- 获取 Fragment 实例

```java
FragmentManager fragmentManager = this.getSupportFragmentManager();
LeftFragment fragment = (LeftFragment) fragmentManager.findFragmentById(R.id.left_fragment);
```

- 获取 Activity 实例
  - 获取到的 Activity 是一个 Context 对象

```java
MainActivity activity = (MainActivity) getActivity();
```

### 生命周期

#### 状态

| 状态     | 解释                                                         |
| -------- | ------------------------------------------------------------ |
| 运行状态 | Fragment 可见，并且所关联活动处于运行状态                    |
| 暂停状态 | 所关联活动进入暂停状态                                       |
| 停止状态 | 所关联的活动进入停止状态，或者调用 FragmentTransction 的 `remove()/replace()` 方法将 Fragment 从活动中移除，但在事务提交之前调用 `addToBackStack()` 方法 |
| 销毁状态 | 所依附的活动被销毁；或者调用 FragmentTransction 的 `remove()/replace()` 方法将 Fragment 从活动中移除，但在事务提交之前**并未**调用 `addToBackStack()` 方法 |

![Fragment 与 Activity 之间的通信_fragment activity通信-CSDN博客](https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/07/03/20201005193727278-20240703125000376-1719982200.png)

#### 回调

- 除了包括与 Activity 类似的回调以外还包括一下回调方法

| 回调                  | 解释                                         |
| --------------------- | -------------------------------------------- |
| `onAttach()`          | Fragment 和 Activity 建立关联时使用          |
| `onCreateView()`      | 为 Fragment 创建视图(加载布局时) 调用        |
| `onActivityCreated()` | 确保与 Fragment 关联的活动一定创建完毕时调用 |
| `onDestroyView()`     | 当与 Fragment 关联的视图被移除时调用         |
| `onDetach()`          | 当 Fragment 和 Activity 解除关联时调用       |

### 动态加载布局

#### 使用限定词

- `Qualifiers` 限定词
  - 使用限定词来根据 **屏幕尺寸、分辨率、方向** 等进行动态加载布局

- 相关限定词分类
  - 屏幕大小：`small/normal/large/xlarge`
  - 分辨率：`ldpi/mdpi/hdpi/xhdpi/xxhdpi`
    - `120dpi/160dpi/240dpi/320dpi/480dpi`
  - 方向：`land/port`
    - `横屏/竖屏`
- 最小宽度限定词
  - 以指定屏幕宽度的最小值进行限定（以dp为单位）

![image-20240703130456808](https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/07/03/image-20240703130456808-1719983097.png)

#### 判断时机

- 可以在 `onActivityCreated` 中进行判断

## 广播 Broadcast

### 基本概念

- Android 每个应用程序都可以对自身感兴趣的广播进行注册
  - 该程序只会接受注册的广播
  - 广播可以来自系统，也可以来自其他应用程序

- 广播类型
  - 标准广播 (Normal broadcasts)
    - 完全异步执行广播，所有广播接收器几乎同时接收到该广播消息
    - 无法被截断
  - 有序广播 (Ordered broadcasts)
    - 同步执行广播
    - 同一时间只有一个广播接收器能够接收到这条广播消息，其逻辑执行完毕后才会继续接受传递
    - 存在先后顺序 **接受优先级**
    - 可以截断正在传递的广播
- 创建广播接收器方式
  - 创建继承 `BroadcastReceiver` 的类
  - 并重写 `onReceive()`方法

### 接受系统广播

> - **动态注册** 在代码中注册
> - **静态注册** 在 AndroidManifest.xml 中注册

- `onReceive()` 中不应该进行过复杂或耗时操作，其执行过程过长会产生运行时错误

#### 动态注册监听网络变化

> 必须要在程序启动时应用

- `IntentFilter` “意图过滤器”，主要用来过滤隐式意图
- `BroadcastReceiver`广播接收器
  - 动态注册需要动态取消注册

```java
public class BaseUse extends AppCompatActivity {
  private IntentFilter intentFilter;
  private NetworkChangeReceiver networkChangeReceiver;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    intentFilter = new IntentFilter();
    // 网络状态发生变化时会发送一条值为 android.net.conn.CONNECTIVITY_CHANGE 的广播
    // 此处作过滤器，只接收值为 android.net.conn.CONNECTIVITY_CHANGE 的广播
    intentFilter.addAction("android.net.conn.CONNECTIVITY_CHANGE");
    networkChangeReceiver = new NetworkChangeReceiver();
    // 注册广播接收器
    // 此时 NetworkChangeReceiver 会接受到值为 android.net.conn.CONNECTIVITY_CHANGE 的广播
    // Notice: 动态注册的广播接收器一定要取消注册，否则会导致内存泄漏
    registerReceiver(networkChangeReceiver, intentFilter);
  }

  @Override
  protected void onDestroy() {
    super.onDestroy();
    // 取消注册广播接收器
    unregisterReceiver(networkChangeReceiver);
  }

  class NetworkChangeReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
      // 1. 简单提示网络状态发生变化
      // Toast.makeText(context, "Network is changed", Toast.LENGTH_SHORT).show());

      // 2. 获取网络连接管理器, 通过网络连接管理器获取网络连接信息
      ConnectivityManager connectivityManager = (ConnectivityManager) getSystemService(Context.CONNECTIVITY_SERVICE);
      // 访问系统等操作, 必须在 AndroidManifest.xml 中声明权限
      NetworkInfo activeNetworkInfo = connectivityManager.getActiveNetworkInfo();
      if (activeNetworkInfo != null && activeNetworkInfo.isAvailable()) {
        Toast.makeText(context, "Network is available", Toast.LENGTH_SHORT).show();
      } else {
        Toast.makeText(context, "Network is unavailable", Toast.LENGTH_SHORT).show();
      }
    }
  }
}
```

#### 静态注册实现开机启动

- 实现开机启动的功能
- 使用快速创建 `Broadcast Receiver` 来实现
  - 自动创建类并继承 `BroadcastReceiver`
  - 自动在 `Androidmanifet.xml` 进行注册
- 监听系统开关机需要进一步的权限
  - ` <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />`

![image-20240703165738732](https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/07/03/image-20240703165738732-1719997059.png)

### 自定义广播

#### 发送标准广播

- 接收器注册

```xml
<receiver
          android:name=".MyNormalReceiver"
          android:enabled="true"
          android:exported="true">
  <intent-filter>
    <action android:name="com.bayyy.MY_NORMAL" />
  </intent-filter>
</receiver>
```

- 发送标准广播
  - 从Android 8.0（API级别26）开始，该系统对声明清单的接收者施加了额外的限制
  - 如果你的应用目标是Android 8.0或更高版本，你不能使用清单为大多数隐式广播（不是专门针对你的应用的广播）声明接收器。当用户正在使用你的应用程序时，你仍然可以使用上下文注册的接收器
  - 定义的静态广播必须指定范围（应用），类似于生活中广播要在指定频道才能收到
    - 通过 `setPackage` 指定包名
    - `setComponent` 指定完整应用名+接收器名

```java
findViewById(R.id.btn_send).setOnClickListener(v -> {
  Log.d(TAG, "onCreate: send broadcast");
  Intent intent = new Intent("com.bayyy.MY_NORMAL");
  // Android 8.0 之后，静态注册的广播接收器无法接收隐式广播，需要指定包名
  intent.setPackage(getPackageName());  // 1. 指定包名, 使得广播只能被本应用接收
  intent.setComponent(new ComponentName("com.bayyy.broadcastreceiver", "com.bayyy.broadcastreceiver.OtherAppReceiver"));  // 2. 指定接收器, 完整应用名+接收器名, 适用于跨应用广播
  sendBroadcast(intent);
});
```

#### 发送有序广播

- 修改发送命令 `sendOrderedBroadcast`

```java
sendOrderedBroadcast(intent, null);	// intent, 权限相关字符串
```

- 设定先后次序 `AndroidManifest.xml` 中指定 `priority`

```xml
<intent-filter android:priority="100"> ... </intent-filter>
```

- 截断通知 `abortBroadcast()`

### 本地广播

- 使用 `LocalBroadcastManager` 进行广播管理
  - 注意及时注销

```java
private LocalBroadcastManager localBroadcastManager;
private LocalReceiver localReceiver;

@Override
protected void onCreate(Bundle savedInstanceState) {
  localBroadcastManager = LocalBroadcastManager.getInstance(this);

  findViewById(R.id.btn_send_local).setOnClickListener(v -> {
    Intent intent = new Intent("com.bayyy.MY_LOCAL");
    localBroadcastManager.sendBroadcast(intent);
  });
  localReceiver = new LocalReceiver();
  localBroadcastManager.registerReceiver(localReceiver, new IntentFilter("com.bayyy.MY_LOCAL"));
}

@Override
protected void onDestroy() {
  super.onDestroy();
  localBroadcastManager.unregisterReceiver(localReceiver);
}

class LocalReceiver extends BroadcastReceiver {
  @Override
  public void onReceive(Context context, Intent intent) {
    Toast.makeText(context, "LocalReceiver", Toast.LENGTH_SHORT).show();
  }
}
```

## 持久化技术 Storage

### 持久化技术简介

- 文件存储
- SharedPreference 存储
- 数据库存储

### 文件存储

- 不对文件进行任何格式化处理
  - 适合简单的文本数据或二进制数据

#### 将数据存储到文件中

- `Context` 类中提供了 `openFileOutput(filename, mode)` 方法
  - `filename` 文件名，不带完整路径
    - 默认存储到 `/data/data/<package name>/files`
  - `mode` 文件操作模式
    - `MODE_PRIVATE`
    - `MODE_APPEND`

```java
public class SaveData extends AppCompatActivity {
  private EditText edit;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    edit = (EditText) findViewById(R.id.et_data);
    findViewById(R.id.btn_save).setOnClickListener(v -> {
      save();
    });
  }

  public void save() {
    String inputText = edit.getText().toString();
    FileOutputStream out = null;
    BufferedWriter writer = null;
    try {
      out = openFileOutput("data", MODE_PRIVATE);
      writer = new BufferedWriter(new OutputStreamWriter(out));
      writer.write(inputText);
    } catch (Exception e) {
      e.printStackTrace();
    } finally {
      try {
        if (writer != null) {
          writer.close();
        }
      } catch (Exception e) {
        e.printStackTrace();
      }
    }
  }
}
```

![image-20240703202955401](https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/07/03/image-20240703202955401-1720009795.png)

#### 读取文件

```java
private void load() {
  FileInputStream in = null;
  BufferedReader read = null;
  StringBuilder content = new StringBuilder();  // 新建一个StringBuilder对象(content)用于存放读取的数据
  try {
    in = openFileInput("data"); // 通过openFileInput()方法获取FileInputStream对象
    read = new BufferedReader(new InputStreamReader(in)); // 通过 FileInputStream 对象构建 BufferedReader 对象
    String line = "";
    while ((line = read.readLine()) != null) {  // 逐行读取文件内容
      content.append(line);
    }
  } catch (Exception e) {
    e.printStackTrace();
  } finally {
    if (read != null) {
      try {
        read.close();
      } catch (Exception e) {
        e.printStackTrace();
      }
    }
  }
  edit.setText(content.toString());
  edit.setSelection(content.length());
}
```

### SharedPreferences 存储

- 使用键值对进行数据存储
- 支持不同的数据类型存储

#### 存储

- 获取 `SharedPreferences` 对象

| 方法                                                         | 说明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `Context` 类中的 `getSharedPreferences()`                    | 参数 `文件名称, 操作模式`<br />只有 `MODE_PRIVATE` 一种模式可选 |
| `Activity` 类中的 `getPreferences()`                         | 与上述类似，只接受 `操作模式` 参数, 默认以当前活动类名作为文件名 |
| `PreferenceManager` 类中的 `getDefaultSharedPreferences().edit()` | 接受 Context 参数，自动以当前应用程序包名作为前缀命名文件    |

- 数据存储过程
  1. 调用 `edit()` 方法获取 `SharedPreferences.Editor` 对象
  2. 向该对象中添加数据，添加字符串使用 `putString()` 方法，以此类推
  3. 调用 `apply()` 方法将添加的数据提交，完成数据存储

```java
findViewById(R.id.btn_con).setOnClickListener(v -> {
  // Context 类中的 getSharedPreferences() 方法用于获取 SharedPreferences 对象
  // 可以指定包名
  SharedPreferences.Editor editor = getSharedPreferences("context_data", MODE_PRIVATE).edit();
  editor.putString("method", "Context");
  editor.putString("name", "Bay");
  editor.putInt("age", 18);
  editor.putBoolean("sex", true);
  editor.apply();
});

findViewById(R.id.btn_act).setOnClickListener(v -> {
  // Activity 类中的 getPreferences() 方法用于获取 SharedPreferences 对象
  // 自动将 Activity 的类名作为 SharedPreferences 的文件名: SharedData.xml
  SharedPreferences.Editor editor = this.getPreferences(MODE_PRIVATE).edit();
  editor.putString("method", "Activity");
  editor.putString("name", "Bay");
  editor.putInt("age", 18);
  editor.putBoolean("sex", true);
  editor.apply();
});

findViewById(R.id.btn_pre).setOnClickListener(v -> {
  // PreferenceManager 类中的 getDefaultSharedPreferences() 方法用于获取 SharedPreferences 对象
  // 自动将包名作为 SharedPreferences 的文件名: com.bayyy.storage_preferences.xml
  SharedPreferences.Editor editor = PreferenceManager.getDefaultSharedPreferences(this).edit();
  editor.putString("method", "PreferenceManager");
  editor.putString("name", "Bay");
  editor.putInt("age", 18);
  editor.putBoolean("sex", true);
  editor.apply();
});
```

![image-20240703203753144](https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/07/03/image-20240703203753144-1720010273.png)

#### 读取

```java
findViewById(R.id.btn_con_load).setOnClickListener(v -> {
  SharedPreferences preferences = getSharedPreferences("context_data", MODE_PRIVATE);
  String method = preferences.getString("method", "null");
  String name = preferences.getString("name", "null");
  int age = preferences.getInt("age", 0);
  boolean sex = preferences.getBoolean("sex", true);
  Toast.makeText(this, "Method: " + method + "\nName: " + name + "\nAge: " + age + "\nSex: " + sex, Toast.LENGTH_SHORT).show();
});

SharedPreferences preferences = this.getPreferences(MODE_PRIVATE);
SharedPreferences preferences = PreferenceManager.getDefaultSharedPreferences(this);
```

### SQLite 数据库

#### SQL 实现增删改查

- 增 `db.exec(“db.execSQL("insert into Book (name, author, pages, price) values(?, ?, ?, ?)", new String[]{"The Da Vinci Code", "Dan Brown", "454", "16.96"});`
- 删 `db.execSQL("delete from Book where pages < ?", new String[]{"500"});`
- 改 `db.execSQL("update Book set price = ? where pages > ?", new String[]{"10.99", "500"});`
- 查 `Cursor cursor = db.rawQuery("select * from Book where pages > ?", new String[]{"400"});`

#### 创建数据库

- 提供了 `SQLiteOpenHelper` 帮助类进行数据库的创建和升级
  - 实现抽象方法 `onCreate()` 和 `onUpgrade()`
  - 实例方法 `getReadableDatabase()` 和 `getWritableDatabase()`
    - 获取数据库实例时，会执行 `onCreate()` 方法
- 创建数据库一般存储在 `/data/data/<package name>/databases/` 目录下

```java
public class MyDatabaseHelper extends SQLiteOpenHelper {
  public static final String CREATE_BOOK = "create table Book ("
    + "id integer primary key autoincrement, "
    + "author text, "
    + "price real, "
    + "pages integer, "
    + "name text)";
  private Context mContext;

  public MyDatabaseHelper(@Nullable Context context, @Nullable String name, @Nullable SQLiteDatabase.CursorFactory factory, int version) {
    super(context, name, factory, version);
    mContext = context;
  }

  @Override
  public void onCreate(SQLiteDatabase db) {
    db.execSQL(CREATE_BOOK);
    Toast.makeText(mContext, "Create databases succeed!", Toast.LENGTH_SHORT).show();

  }

  @Override
  public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
  }
}

```

```java
dbHelper = new MyDatabaseHelper(this, "BookStore.db", null, 1);
findViewById(R.id.btn_create_db).setOnClickListener(v -> {
  dbHelper.getWritableDatabase();
});
```



![image-20240704193039009](/Users/bayyy/Library/Application Support/typora-user-images/image-20240704193039009.png)

#### 升级数据库

- 注意已存在数据库并不会重复创建/重写
  - 需要先drop掉已存在数据库的表
- 更新时需要更新版本号

```java
public class MyDatabaseHelper extends SQLiteOpenHelper {
  public static final String CREATE_CATEGORY = "create table Category (" +
    "id integer primary key autoincrement, " +
    "category_name text, " +
    "category_code integer)";


  @Override
  public void onCreate(SQLiteDatabase db) {
    db.execSQL(CREATE_BOOK);
    db.execSQL(CREATE_CATEGORY);
    Toast.makeText(mContext, "Create databases succeed!", Toast.LENGTH_SHORT).show();

  }

  @Override
  public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
    db.execSQL("drop table if exists Book");
    db.execSQL("drop table if exists Category");
    onCreate(db);
  }
}

// Main.java
dbHelper = new MyDatabaseHelper(this, "BookStore.db", null, 2); // 更新版本号
```

#### 添加数据

- `insert()` 进行数据插入
  - `(表名, 未指定数据自动赋值， ContentValues对象)`
  - 使用 `ContentValues` 作为数据存储对象

```java
SQLiteDatabase db = dbHelper.getWritableDatabase();
ContentValues values = new ContentValues();
// 装载第一组数据
values.put("name", "The Da Vinci Code");
values.put("author", "Dan Brown");
values.put("pages", 454);
values.put("price", 16.96);
db.insert("Book", null, values);
values.clear(); // 清空ContentValues对象
// 装载第二组数据
values.put("name", "The Lost Symbol");
values.put("author", "Dan Brown");
values.put("pages", 510);
values.put("price", 19.95);
db.insert("Book", null, values);
```

#### 更新数据

```java
SQLiteDatabase db = dbHelper.getWritableDatabase();
ContentValues values = new ContentValues();
values.put("price", 10);
db.update("Book", values, "name = ?", new String[] {"The Da Vinci Code"});
```

#### 删除数据

```java
db.delete("Book", "pages > ?", new String[] {"500"});
```

#### 查询数据

| query() 方法参数 | 对应 SQL 部分              | 描述                   |
| ---------------- | -------------------------- | ---------------------- |
| table            | from table_name            | 表名                   |
| columns          | Select column1, column2, … | 查询列，默认查询所有列 |
| selection        | where column = value       | 约束查询对象           |
| selectionArgs    | -                          | 具体约束值             |
| groupBy          | group by column            | 过滤列                 |
| having           | having column = value      | 排序约束               |
| orderBy          | order by column1, column2  | 指定排序方式           |

```java
SQLiteDatabase db = dbHelper.getWritableDatabase();
Cursor cursor = db.query("Book", null, null, null, null, null, null);
if (cursor.moveToFirst()) {
  do {
    // 遍历Cursor对象，取出数据并打印
    String name = cursor.getString(cursor.getColumnIndex("name"));
    String author = cursor.getString(cursor.getColumnIndex("author"));
    int pages = cursor.getInt(cursor.getColumnIndex("pages"));
    double price = cursor.getDouble(cursor.getColumnIndex("price"));
    System.out.println("Book name is " + name);
    System.out.println("Book author is " + author);
    System.out.println("Book pages is " + pages);
    System.out.println("Book price is " + price);
  } while (cursor.moveToNext());
}
cursor.close();
```

### LitePal

- 关系型数据库
  - 对象关系映射 ORM

#### 配置过程

- 引入依赖 `runtimeOnly group: 'org.litepal.guolindev', name: 'core', version: '3.2.3'`
  - 引入报错，无法下载
  - 解决方法：在 `settings.gradle` 加入 `jcenter()` 的库

![image-20240704203602063](https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/07/04/image-20240704203602063-1720096562.png)

- 创建 litepal 配置文件 `assets/litepal.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<litepal>
    <dbname value="BookStore" />
    <version value="1" />
    <list></list>
</litepal>
```

- 修改 `AndroidManifest.xml` 中 `Application.name`  为 `org.litepal.LitePalApplication`

![image-20240704204206681](https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/07/04/image-20240704204206681-1720096926.png) 

#### 创建和升级

- 新建实体类 Book
  - 为了实现增删改查，需要继承自 `LitePalSupport` 类

```java
public class Book extends LitePalSupport {
  @Column(unique = true)
  private int id;
  @Column(defaultValue = "unknown", nullable = false)
  private String author;
  @Column(index = true)
  private double price;
  private int pages;
  @Column(ignore = true)
  private String name;

  public int getId() {
    return id;
  }

  public void setId(int id) {
    this.id = id;
  }

  public String getAuthor() {
    return author;
  }

  public void setAuthor(String author) {
    this.author = author;
  }

  public double getPrice() {
    return price;
  }

  public void setPrice(double price) {
    this.price = price;
  }

  public int getPages() {
    return pages;
  }

  public void setPages(int pages) {
    this.pages = pages;
  }

  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }
}
```

- 添加映射模型

```xml
<?xml version="1.0" encoding="utf-8"?>
<litepal>
  <dbname value="BookStore" />
  <version value="1" />
  <list>
    <mapping class="com.bayyy.storage.pojo.Book" />
  </list>
</litepal>
```

- 只需要任意执行一次数据库操作即可创建
  - 增加实体类后进行版本更新即可

#### 增删改查

- 增

```java
Book book = new Book();
book.setAuthor("Bayyy");
book.setName("Android");
book.setPages(454);
book.setPrice(16.96);
book.save();
```

- 改

```java
Book book = new Book();
book.setPrice(14.95);
book.updateAll("name = ?", "Android");

// 设置为数据类型默认值 0,null..
book.setToDefault("prices");
```

- 删

```java
LitePal.deleteAll(Book.class, "pages < ?", "500");

// 不指定约束，即删除所有数据
```

- 查

```java
Book bookFirst = LitePal.findFirst(Book.class);  // 查询第一条数据
Book bookLast = LitePal.findLast(Book.class);  // 查询第一条数据
List<Book> books1 = LitePal.findAll(Book.class);	// 查询所有数据
List<Book> books2 = LitePal.select("name", "author").find(Book.class);
List<Book> books3 = LitePal.where("pages > ?", "400").find(Book.class);
List<Book> books4 = LitePal.order("pages desc").find(Book.class);
List<Book> books5 = LitePal.limit(3).find(Book.class);
List<Book> books6 = LitePal.limit(3).offset(1).find(Book.class);
// 完整查询语句
List<Book> books7 = LitePal.select("name", "author", "pages")
  .where("pages > ?", "400")
  .order("pages desc")
  .limit(3)
  .offset(1)
  .find(Book.class);
// 原生 SQL 查询
Cursor cursor = LitePal.findBySQL("select * from Book where pages > ?", "400");
```

## 内容提供器 Content Provider

- 提供跨应用的数据共享

### 运行时权限

#### 机制详解

| 权限分类 | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| 普通权限 | 不会直接威胁到用户的安全和隐私权限，授权后使用时系统会自动申请 |
| 危险权限 | 可能会触及到用户隐私，或者对设备安全性造成影响的权限，如获取设备联系人信息、定位设备的地理位置等，必须由用户手动点击授权 |

#### 危险权限

- 除了危险权限剩下全都是普通权限
  - 危险权限一共 **9组24个权限**
- 同意单一权限时，该权限所属权限组也会被授权

| 权限组名   | 权限名                                                       |
| ---------- | ------------------------------------------------------------ |
| CALENDAR   | READ_CALENDAR<br />WRITE_CALENDAR                            |
| CAMERA     | CAMERA                                                       |
| CONTACTS   | READ_CONTACTS<br />WRITE_CONTACTS<br />GET_ACCOUNTS          |
| LOCATION   | ACCESS_FINE_LAOCATION<br />ACCESS_COARSE_LOCATION            |
| MICROPHONE | RECORAD_AUDIO                                                |
| PHNONE     | READ_PHONE_STATE<br />CALL_PHONE<br />READ_CALL_LOG<br />WRITE_CALL_LOG<br />ADD_COICEMAIL<br />USE_SIP<br />PROCESS_OUTGOING_CALLS |
| SENSORS    | BODY_SENSORS                                                 |
| SMS        | SEND_SMS<br />RECEIVE_SMS<br />READ_SMS<br />RECEIVE_WAP_PUSH<br />RECEIVE_MMS |
| STORAGE    | READ_EXTERNAL_STORAGE<br />WRITE_EXTERNAL_STORAGE            |

#### 申请方式

```java
if (ContextCompat.checkSelfPermission(this, android.Manifest.permission.CALL_PHONE) != PackageManager.PERMISSION_GRANTED) {
  ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.CALL_PHONE}, 1);
} else {
  call();
}
```

- 设置权限申请的回调，重写 `onRequestPermissionsResult`

```java
@Override
public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
  super.onRequestPermissionsResult(requestCode, permissions, grantResults);
  switch (requestCode) {
    case 1:
      if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
        call();
      } else {
        Toast.makeText(this, "You denied the permission", Toast.LENGTH_SHORT).show();
      }
      break;
    default:
  }
}
```

### 跨应用访问数据 ContentResolver

#### 获取访问对象

- 访问内容提供器中共享的数据需要借助 `ContentResolver` 类
  - 通过 `Context` 中的 `getContentResolver()` 获取该类的实例
  - 使用 `insert()/delete()/update()/query()` 实现增删改查
- 访问对象由 `Uri` 提供
  - 由 `authority` 和 `path`  组成
  - `authority` 作为不同应用程序的区分，通常由程序包名命名
  - `path` 用作对同一应用程序中不同表进行区分，通常会添加到 `authority` 后
  - 如 `com.bayyy.oneapp/table1` 和 `com.bayyy.oneapp/table2`
- `Uri` 进行组合
  - `content://com.bayyy.oneapp/table1`

```java
Uri uri = Uri.parse("content://com.bayyy.oneapp/table1");
CUrsor cursor = getContentResolver().query(
	uri,
  projection,	// 指定查询的列名
  selection,	// 指定 where 的约束条件
  selectionArgs,	// 指定 wherre 占位符的具体值
  sortOrder	// 指定查询结果的排序方式
);
```

#### 读取系统联系人

```java
try (Cursor c = getContentResolver().query(ContactsContract.CommonDataKinds.Phone.CONTENT_URI, null, null, null, null)) {
  contactList.clear();
  if (c != null) {
    while (c.moveToNext()) {
      // 获取联系人姓名
      String displayName = c.getString(c.getColumnIndexOrThrow(ContactsContract.CommonDataKinds.Phone.DISPLAY_NAME));
      // 获取联系人手机号
      String number = c.getString(c.getColumnIndexOrThrow(ContactsContract.CommonDataKinds.Phone.NUMBER));
      contactList.add(new MyContact(displayName, number));
    }
    adapter.clear();
    adapter.addAll(contactList);
  }
} catch (Exception e) {
  e.printStackTrace();
}
```

### 自定义内容提供器

#### 创建过程

- 创建类继承 `ContentProvider` 
  - 重写其中6个方法
- `AndroidManifest.xml` 中实现注册 

```xml
<provider
          android:name=".provider.DBProvider"
          android:authorities="com.bayyy.db.provider"
          android:enabled="true"
          android:exported="true" />
```

- 标准 Uri
  - `content://com.bayyy.app/table1` table1表
  - `content://com.bayyy.app/table1/1` table1表中id为1的数据
  - `content://com.bayyy.app/table1/*` 任意长度字符
  - `content://com.bayyy.app/table1/#` 任意长度数字

| 方法       | 说明                                                         |
| ---------- | ------------------------------------------------------------ |
| onCreate() | 初始化内容提供器，可以完成创建和升级过程，返回值代表成功与否（只有在 `ContentResolver` 尝试访问数据时会被初始化 |
| query()    | 查询数据                                                     |
| Insert()   | 添加数据                                                     |
| update()   | 更新数据                                                     |
| delete()   | 删除数据                                                     |
| getType()  | 根据 Uri 返回对应的 MIME 类型                                |

#### Uri 匹配

- 使用 `UriMatcher` 进行匹配内容 `Uri` 

```java
public class MyProvider extends ContentProvider {
  public static final int TABLE1_DIR = 0;
  public static final int TABLE1_ITEM = 1;
  public static final int TABLE2_DIR = 2;
  public static final int TABLE2_ITEM = 3;
  public static UriMatcher uriMatcher;

  static {
    uriMatcher = new UriMatcher(UriMatcher.NO_MATCH);
    uriMatcher.addURI("com.bayyy.contentprovider", "table1", TABLE1_DIR);
    uriMatcher.addURI("com.bayyy.contentprovider", "table1/#", TABLE1_ITEM);
    uriMatcher.addURI("com.bayyy.contentprovider", "table2", TABLE2_DIR);
    uriMatcher.addURI("com.bayyy.contentprovider", "table2/#", TABLE2_ITEM);
  }

  @Nullable
  @Override
  public Cursor query(@NonNull Uri uri, @Nullable String[] projection, @Nullable String selection, @Nullable String[] selectionArgs, @Nullable String sortOrder) {
    switch (uriMatcher.match(uri)) {
      case TABLE1_DIR:
        break;
      case TABLE1_ITEM:
        break;
      case TABLE2_DIR:
        break;
      case TABLE2_ITEM:
        break;
      default:
        break;
    }
    return null;
  }
}

```

#### MIME 类型

- `getType()`返回 `Uri`  对象所对应的 MIMR 类型

- 格式规定
  - 必须以 `vnd` 开头
  - 若内容以路径结尾，则后接 `android.cursor.dir/`；若内容以 id 结尾，则后接 `android.cursor.item/`
  - 最后接上 `vnd.<authority>.<path>`
- 对于 `content://com.bayyy.app.provider/table1` 则对应的 MIME 类型为 `vnd.android.cursor.dir/vnd.com.bayyy.app.provider.table1`
- 对于 `content://com.bayyy.app.provider/table1/1` 则对应的 MIME 类型为 `vnd.android.cursor.item/vnd.com.bayyy.app.provider.table1`

```java
@Nullable
@Override
public String getType(@NonNull Uri uri) {
  switch (uriMatcher.match(uri)) {
    case TABLE1_DIR:
      return "vnd.android.cursor.dir/vnd.com.bayyy.contentprovider.table1";
    case TABLE1_ITEM:
      return "vnd.android.cursor.item/vnd.com.bayyy.contentprovider.table1";
    case TABLE2_DIR:
      return "vnd.android.cursor.dir/vnd.com.bayyy.contentprovider.table2";
    case TABLE2_ITEM:
      return "vnd.android.cursor.item/vnd.com.bayyy.contentprovider.table2";
    default:
      break;
  }
  return null;
}
```

#### 跨应用访问限制

- 被访问后台应用过程应该产生任何弹窗等消息，如 `Toast` 等
- 访问者需要声明访问包

```xml
<queries>
  <package android:name="com.bayyy.storage" />
</queries>
```

## 运用手机多媒体

### 通知 Notification

#### 使用通知

- `Android 8.0` 以上使用需要建立消息通道

```java
// 获取通知管理器
NotificationManager manager = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
String channelId;
// Android 8.0及以上需要建立消息通道, 否则会报错: No channel found for notification
if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
  Log.d(TAG, "onCreate: Crete Channel");
  channelId = "1";
  CharSequence channelName = "channel1";
  String channelDescription = "This is channel 1";
  int channelImportance = android.app.NotificationManager.IMPORTANCE_HIGH;
  NotificationChannel channel = new NotificationChannel(channelId, channelName, channelImportance);
  channel.setDescription(channelDescription);
  Log.d(TAG, "onCreate: Create Channel" + channel);
  manager.createNotificationChannel(channel);
}
// 创建通知
Notification notify = new NotificationCompat.Builder(this, channelId)	// 此处需要给定通知通道号
  .setContentTitle("Title")
  .setContentText("This is the content")
  .setWhen(System.currentTimeMillis())
  .setSmallIcon(R.mipmap.ic_launcher)
  .build();
manager.notify(1, notify);
```

#### 通知点击意图

- `PendingIntent` 可以理解为延时执行的 Intent

```java
PendingIntent pi = PendingIntent.getActivity(this, 0, new Intent(this, JumpPage.class), PendingIntent.FLAG_IMMUTABLE);
// 创建通知
Notification notify = new NotificationCompat.Builder(this, channelId)
  // ...
  .setContentIntent(pi)
  .build();
manager.notify(1, notify);
```

- `setAutoCancel` 点击后主动取消
- 也可以通过 `manager.cancel(notifyId)` 取消指定编号的通知

#### 进阶用法

| API                 | 描述                                                         |
| ------------------- | ------------------------------------------------------------ |
| setContentTitle     | 标题                                                         |
| setContentText      | 内容                                                         |
| setSubText          | 子标题                                                       |
| setLargeIcon        | 大图标                                                       |
| setSmallIcon        | 小图标                                                       |
| setContentIntent    | 点击时意图                                                   |
| setDeleteIntent     | 删除时意图                                                   |
| setFullScreenIntent | 全屏通知点击意图，来电、响铃                                 |
| setAutoCancel       | 点击自动取消                                                 |
| setCategory         | 通知类别，适用“勿扰模式”                                     |
| setVisibility       | 屏幕可见性，适用“锁屏状态”                                   |
| setNumber           | 通知项数量                                                   |
| setWhen             | 通知时间                                                     |
| setShowWhen         | 是否显示通知时间                                             |
| setSound            | 提示音                                                       |
| setVibrate          | 震动                                                         |
| setLights           | 呼吸灯                                                       |
| setPriority         | 优先级，7.0                                                  |
| setTimeoutAfter     | 定时取消，8.0及以后                                          |
| setProgress         | 进度                                                         |
| setStyle            | 通知样式，BigPictureStyle、BigTextStyle、MessagingStyle、InboxStyle、DecoratedCustomViewStyle |
| addAction           | 通知上的操作，10.0                                           |
| setGroup            | 分组                                                         |
| setColor            | 背景颜色                                                     |

### 调用摄像头和相册

#### 摄像头

- 调用摄像头拍摄照片 `android.media.action.IMAGE_CAPTURE`
- 存储在应用关联缓存中 `putExtra(MediaStore.EXTRA_OUTPUT, imageUri)`
  - 即指定图片的输出目录
- 文件读取，加载缓存图片

```java
public class CameraUse extends AppCompatActivity {
  public static final int TAKE_PHOTO = 1;
  private ImageView photo;
  private Button btn_take;
  private Uri imageUri;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    btn_take = (Button) findViewById(R.id.btn_take);
    photo = (ImageView) findViewById(R.id.img_show);
    btn_take.setOnClickListener(v -> {
      // 1.创建File对象，用于存储拍照后的图片
      // getExternalCacheDir()方法用于获取应用关联缓存目录 (/sdcard/Android/data/包名/cache/)
      File outputImage = new File(getExternalCacheDir(), "output_image.jpg");
      try {
        if (outputImage.exists()) {
          outputImage.delete();
        }
        outputImage.createNewFile();
      } catch (IOException e) {
        e.printStackTrace();
      }
      // 2.将File对象转换成Uri对象
      if (Build.VERSION.SDK_INT >= 24) {
        // 如果Android版本大于等于7.0, 则使用FileProvider获取Uri
        imageUri = FileProvider.getUriForFile(CameraUse.this, "com.bayyy.media.fileprovider", outputImage);
      } else {
        // 否则使用Uri.fromFile()方法获取Uri
        imageUri = Uri.fromFile(outputImage);
      }
      // 3.启动相机程序
      Intent intent = new Intent("android.media.action.IMAGE_CAPTURE");
      // 指定图片的输出地址
      intent.putExtra(MediaStore.EXTRA_OUTPUT, imageUri);
      startActivityForResult(intent, TAKE_PHOTO);
    });
  }

  @Override
  protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    switch (requestCode) {
      case TAKE_PHOTO:
        if (resultCode == RESULT_OK) {
          try {
            Bitmap bitmap = BitmapFactory.decodeStream(getContentResolver().openInputStream(imageUri));
            photo.setImageBitmap(bitmap);
          } catch (FileNotFoundException e) {
            e.printStackTrace();
          }
          // 将拍摄的照片显示出来
          photo.setImageURI(imageUri);
        }
        break;
    }
  }
}
```

- 权限声明+FileProvider声明
  - SD 权限声明是为了适配老版本机器 （4.4）
  - 此处指定了输出目录，需要额外创建

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <application>
        <provider
            android:name="androidx.core.content.FileProvider"
            android:authorities="com.bayyy.media.fileprovider"
            android:exported="false"
            android:grantUriPermissions="true">
            <meta-data
                android:name="android.support.FILE_PROVIDER_PATHS"
                android:resource="@xml/file_paths" />
        </provider>
</manifest>
```

- 文件创建 `external-path`
  - `path='.'` 表明整个SD空间

```xml
<?xml version="1.0" encoding="utf-8"?>
<paths xmlns:android="http://schemas.android.com/apk/res/android">
    <external-path
        name="my_images"
        path="." />
</paths>
```

#### 加载相册

> - 最新方法：直接使用 `ImageView.setImageURI(data.getData())`

1. 动态申请访问存储器的权限 `WRITE_EXTERNAL_STORAGE`
2. 构建打开相册的意图，并等待返回结果
3. 根据 Android 4.4 版本号分割选择不同的处理方式
   - Android4.4 后，选中相册不返回真是Uri，而是进行了一定的封装
     - 被封装为 `Document`，需要取出 `document id` 进行处理
       - 若`authority`为`media`，还需要对id进行解析，分割后半部分才是真正的数字id
     - 否则，使用普通方式
     - 
   - Android4.4以前，Uri未经封装，可以直接传入获取真实路径
4. 展示图像



```java
public class CameraUse extends AppCompatActivity {
  public static final int CHOOSE_PHOTO = 2;
  public static final int REQUEST_PERMISSION_WRITE_EXTERNAL_STORAGE = 1;
  private ImageView photo;
  private Button btn_load;
  private Uri imageUri;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    btn_load = (Button) findViewById(R.id.btn_load);
    photo = (ImageView) findViewById(R.id.img_show);
    btn_load.setOnClickListener(v -> {
      // 需要动态申请权限: 读取外部存储器的权限
      if (ContextCompat.checkSelfPermission(CameraUse.this, android.Manifest.permission.WRITE_EXTERNAL_STORAGE) != PackageManager.PERMISSION_GRANTED) {
        ActivityCompat.requestPermissions(CameraUse.this, new String[]{Manifest.permission.WRITE_EXTERNAL_STORAGE}, REQUEST_PERMISSION_WRITE_EXTERNAL_STORAGE);
      } else {
        openAlbum();
      }
    });
  }

  /**
   * 打开相册, 选择图片
   */
  private void openAlbum() {
    Intent intent = new Intent("android.intent.action.GET_CONTENT");
    intent.setType("image/*");
    startActivityForResult(intent, CHOOSE_PHOTO);
  }

  @Override
  protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    switch (requestCode) {
      case CHOOSE_PHOTO:
        if (resultCode == RESULT_OK) {
          // 判断手机系统版本号
          if (Build.VERSION.SDK_INT >= 19) {
            // 4.4及以上系统使用这个方法处理图片
            handleImageOnKitKat(data);
          } else {
            // 4.4以下系统使用这个方法处理图片
            handleImageBeforeKitKat(data);
          }
        }
        break;
    }
  }

  @TargetApi(19)
  private void handleImageOnKitKat(Intent data) {
    // 1.获取图片的Uri
    String imagePath = null;
    Uri uri = data.getData();
    // 2.判断Uri的Authority是不是DocumentsContract
    if (DocumentsContract.isDocumentUri(this, uri)) {
      // 如果是Document类型的Uri, 则通过Document的Id处理
      String docId = DocumentsContract.getDocumentId(uri);
      if ("com.android.providers.media.documents".equals(uri.getAuthority())) {
        // 判断Uri的Authority是不是MediaProvider
        String id = docId.split(":")[1]; // 解析出数字格式的id
        String selection = MediaStore.Images.Media._ID + "=" + id;
        imagePath = getImagePath(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, selection);
      } else if ("com.android.providers.downloads.documents".equals(uri.getAuthority())) {
        // 判断Uri的Authority是不是DownloadsProvider
        Uri contentUri = ContentUris.withAppendedId(Uri.parse("content://downloads/public_downloads"), Long.valueOf(docId));
        imagePath = getImagePath(contentUri, null);
      }
    } else if ("content".equalsIgnoreCase(uri.getScheme())) {
      // 如果是Content类型的Uri, 则使用普通方式处理
      imagePath = getImagePath(uri, null);
    } else if ("file".equalsIgnoreCase(uri.getScheme())) {
      // 如果是File类型的Uri, 直接获取图片路径即可
      imagePath = uri.getPath();
    }
    displayImg(imagePath); // 根据图片路径显示图片
  }

  /**
   * 根据图片路径显示图片
   *
   * @param imagePath 图片路径
   */
  private void displayImg(String imagePath) {
    if (imagePath != null) {
      Bitmap bitmap = BitmapFactory.decodeFile(imagePath);
      photo.setImageBitmap(bitmap);
    } else {
      Toast.makeText(this, "Failed to get image", Toast.LENGTH_SHORT).show();
    }
  }

  /**
   * 根据Uri和selection来获取图片的真实路径
   */
  private String getImagePath(Uri uri, String selection) {
    String path = null;
    Cursor cursor = getContentResolver().query(uri, null, selection, null, null);
    if (cursor != null) {
      if (cursor.moveToFirst()) {
        path = cursor.getString(cursor.getColumnIndexOrThrow(MediaStore.Images.Media.DATA));
      }
      cursor.close();
    }
    return path;
  }

  /**
   * 4.4以下系统使用这个方法处理图片
   */
  private void handleImageBeforeKitKat(Intent data) {
    Uri uri = data.getData();
    String imagePath = getImagePath(uri, null);
    displayImg(imagePath);
  }
}
```

### 播放多媒体

#### 播放音频

- 使用 MediaPlayer 类实现
- 流程
  1. 创建 MediaPlayer 对象
  2. 调用 `getDataSource()` 方法设置播放音频路径
  3. 调用 `prepare()` 进入准备状态
  4. `start()/pause()/reset()` 分别进行开始、暂停、停止状态

```java
File file = new File(Environment.getExternalStorageDirectory(), "music.mp3");
media.setDataSource(file.getPath());
```

| 方法                          | 说明                                    |
| ----------------------------- | --------------------------------------- |
| MediaPlayer                   | 构造方法                                |
| create                        | 创建一个要播放的多媒体                  |
| getCurrentPosition            | 得到当前播放位置                        |
| getDuration                   | 得到文件的时间                          |
| getVideoHeight                | 得到视频的高度                          |
| getVideoWidth                 | 得到视频的宽度                          |
| isLooping                     | 是否循环播放                            |
| isPlaying                     | 是否正在播放                            |
| pause                         | 暂停                                    |
| prepare                       | 准备（同步）                            |
| prepareAsync                  | 准备（异步）                            |
| release                       | 释放MediaPlayer对象相关的资源           |
| reset                         | 重置MediaPlayer对象为刚刚创建的状态     |
| seekTo                        | 指定播放的位置（以毫秒为单位的时间）    |
| setAudioStreamType            | 设置流媒体的类型                        |
| setDataSource                 | 设置多媒体数据来源(位置)                |
| setDisplay                    | 设置用SurfaceHolder来显示多媒体         |
| setLooping                    | 设置是否循环播放                        |
| setOnButteringUpdateListener  | 网络流媒体的缓冲监听                    |
| setOnErrorListener            | 设置错误信息监听                        |
| setOnVideoSizeChangedListener | 视频尺寸监听                            |
| setScreenOnWhilePlaying       | 设置是否使用SurfaceHolder来保持屏幕显示 |
| setVolume                     | 设置音量                                |
| start                         | 开始播放                                |
| stop                          | 停止播放                                |

#### 播放视频

- 使用` VideoView` 实现

```java
videoView.setVideoURI(<Uri>);
```

| 方法         | 说明               |
| ------------ | ------------------ |
| setVideoPath | 设置播放视频的位置 |
| starat       | 开始               |
| pause        | 暂停               |
| resume       | 从头播放           |
| seekTo       | 从指定位置开始     |
| isPlaying    | 判断是否正在播放   |
| getDuration  | 获取载入数据的时长 |

## 网络请求

### WebView 

- 申请权限 `android.permission.INTERNET`

```java
WebView web = findViewById(R.id.web_view);
web.getSettings().setJavaScriptEnabled(true); // 设置支持JavaScript
web.setWebViewClient(new WebViewClient());  // 设置WebViewClient (网页跳转仍在当前WebView中显示)
web.loadUrl("https://www.baidu.com");
```

### HTTP 协议访问

#### HttpURLConnection

- 构建 HttpURLConnection 实例实现网络请求
  - 可以设置METHOD、TIMEOUT等
- 使用 getInputStream 将获取服务器返回的输入流
- 构建多线程操作
  - 注意：子线程无法操作UI界面，需要切换到主线程操作 `runOnUiThread()`

```java
private void sendHttpRequest() {
  new Thread(new Runnable() {
    @Override
    public void run() {
      // send http request
      HttpURLConnection connection = null;
      BufferedReader reader = null;
      try {
        URL url = new URL("https://www.baidu.com");
        connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");
        connection.setConnectTimeout(8000);
        connection.setReadTimeout(8000);
        InputStream in = connection.getInputStream();
        // read response
        reader = new BufferedReader(new InputStreamReader(in));
        StringBuilder response = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
          response.append(line);
        }
        // show response
        runOnUiThread(() -> {
          res_text.setText(response.toString());
        });
      } catch (Exception e) {
        e.printStackTrace();
      } finally {
        if (reader != null) {
          try {
            reader.close();
          } catch (IOException e) {
            e.printStackTrace();
          }
        }
        if (connection != null) {
          connection.disconnect();
        }
      }
    }
  }).start();
}
```

#### OkHttp (开源库)

- 添加依赖 `implementation("com.squareup.okhttp3:okhttp:4.12.0")`
  - 自动添加 `OkHttp + Okio` 

```java
new Thread(new Runnable() {
  @Override
  public void run() {
    try {
      // 发送GET请求
      OkHttpClient client = new OkHttpClient();
      Request req = new Request.Builder().url("https://www.baidu.com").build();
      try (Response res = client.newCall(req).execute()) {
        String data = res.body() != null ? res.body().string() : null;
        updateUI(data);
      }
    } catch (Exception e) {
      e.printStackTrace();
    }

  }
}).start();

// POST 请求
RequestBody body = new FormBody.Builder().add("username", "admin").add("password", "123456").build();
Request req_post = new Request.Builder().url("https://www.baidu.com").post(body).build();
```

### 解析XML格式数据

- Android 模拟器中 `127.0.0.1` 指代模拟器本身
- 需要通过 `10.0.2.2` 桥接到所在电脑

#### Pull 解析方式

```java
private void parseXMLWithPull(String xmlData) {
  try {
    XmlPullParserFactory factory = XmlPullParserFactory.newInstance();
    XmlPullParser xmlPullParser = factory.newPullParser();
    xmlPullParser.setInput(new StringReader(xmlData));
    int eventType = xmlPullParser.getEventType();
    String id = "";
    String name = "";
    String age = "";
    while (eventType != XmlPullParser.END_DOCUMENT) {
      String nodeName = xmlPullParser.getName();
      switch (eventType) {
          // 开始解析某个节点
        case XmlPullParser.START_TAG: {
          if ("id".equals(nodeName)) {
            id = xmlPullParser.nextText();
          } else if ("name".equals(nodeName)) {
            name = xmlPullParser.nextText();
          } else if ("age".equals(nodeName)) {
            age = xmlPullParser.nextText();
          }
          break;
        }
          // 完成解析某个节点
        case XmlPullParser.END_TAG: {
          if ("person".equals(nodeName)) {
            Log.d(TAG, "parseXMLWithPull: id = " + id);
            Log.d(TAG, "parseXMLWithPull: name = " + name);
            Log.d(TAG, "parseXMLWithPull: age = " + age);
          }
          break;
        }
        default:
          break;
      }
      eventType = xmlPullParser.next();
    }
  } catch (Exception e) {
    e.printStackTrace();
  }
}
```

#### SAX 解析方式

- 新建 `MyParserSAXHandler` 类继承 `DefaultHandler`
- 使用过程
  - 创建 `SAXParserFactory` 对象，获取 `XMLReader` 对象
  - 编写的 Handler 实例设置到 `XMLReader` 对象中
  - 调用 `parse()` 方法进行解析

```java
public class MyParseSAXHandler extends DefaultHandler {
  private String nodeName;
  private StringBuilder id;
  private StringBuilder name;
  private StringBuilder version;

  @Override
  public void startDocument() throws SAXException {
    id = new StringBuilder();
    name = new StringBuilder();
    version = new StringBuilder();
  }

  @Override
  public void startElement(String uri, String localName, String qName, Attributes attributes) throws SAXException {
    nodeName = localName;
  }

  @Override
  public void characters(char[] ch, int start, int length) throws SAXException {
    if ("id".equals(nodeName)) {
      id.append(ch, start, length);
    } else if ("name".equals(nodeName)) {
      name.append(ch, start, length);
    } else if ("version".equals(nodeName)) {
      version.append(ch, start, length);
    }
  }

  @Override
  public void endElement(String uri, String localName, String qName) throws SAXException {
    if ("app".equals(localName)) {
      System.out.println("id is " + id.toString().trim());
      System.out.println("name is " + name.toString().trim());
      System.out.println("version is " + version.toString().trim());
      // 最后要将StringBuilder清空掉
      id.setLength(0);
      name.setLength(0);
      version.setLength(0);
    }
  }

  @Override
  public void endDocument() throws SAXException {
    super.endDocument();
  }
}
```

```java
private void parseXMLWithSAX(String data) {
  try {
    SAXParserFactory factory = SAXParserFactory.newInstance();
    XMLReader xmlReader = factory.newSAXParser().getXMLReader();
    ContentHandler handler = new MyParseSAXHandler();
    // 将ContentHandler的实例设置到XMLReader中
    xmlReader.setContentHandler(handler);
    // 开始执行解析
    xmlReader.parse(new org.xml.sax.InputSource(new StringReader(data)));
  } catch (Exception e) {
    e.printStackTrace();
  }
}
```

### 解析 JSON 格式数据

#### 使用 JSONObject

```java
private void parseJSONWithJSONObject(String data) {
  try {
    JSONArray jsonArray = new JSONArray(data);
    for (int i = 0; i < jsonArray.length(); i++) {
      JSONObject jsonObject = jsonArray.getJSONObject(i);
      String id = jsonObject.getString("id");
      String name = jsonObject.getString("name");
      String age = jsonObject.getString("age");
      Log.d(TAG, "parseJSONWithJSONObject: id = " + id);
      Log.d(TAG, "parseJSONWithJSONObject: name = " + name);
      Log.d(TAG, "parseJSONWithJSONObject: age = " + age);
    }
  } catch (Exception e) {
    e.printStackTrace();
  }
}
```

#### 使用 GSON

- 添加依赖 `implementation group: 'com.google.code.gson', name: 'gson', version: '2.11.0'`
- 新建对应的实体类
- 解析单段数据 `Person person = gson.fromJson(data, Person.class)`
- 解析JSON数组 `List<Person> people = son.fromJson(data, new TypeToken<List<Person>>>())`

```java
private void parseJSONWithGSON(String data) {
  Gson gson = new Gson();
  List<Person> people = gson.fromJson(data, new TypeToken<List<Person>>() {
  }.getType());
  for (Person p : people) {
    Log.d(TAG, "parseJSONWithGSON: id = " + p.getId());
    Log.d(TAG, "parseJSONWithGSON: name = " + p.getName());
    Log.d(TAG, "parseJSONWithGSON: age = " + p.getAge());
  }
}
```

### 网络编程实践

#### 设置通用类

- 创建接口 `HttpCallbackListener` 作为线程返回数据处理
  - 成功数据在 `onFinish` 返回
  - 异常报错在 `onError` 处理

```java
public interface HttpCallbackListener {
  void onFinish(String response);
  void onError(Exception e);
}
```

- 通用类中实现网络通信

```java
public class HttpUtil {
  private static void sendHttpRequest(String address, HttpCallbackListener listener) {
    new Thread(new Runnable() {
      @Override
      public void run() {
        HttpURLConnection connection = null;
        try {
          URL url = new URL(address);
          connection = (HttpURLConnection) url.openConnection();
          connection.setRequestMethod("GET");
          connection.setConnectTimeout(8000);
          connection.setReadTimeout(8000);
          connection.setDoInput(true);  // 设置这个连接是否可以写入数据
          connection.setDoOutput(true);  // 设置这个连接是否可以输出数据
          InputStream in = connection.getInputStream();
          BufferedReader reader = new BufferedReader(new InputStreamReader(in));
          StringBuilder response = new StringBuilder();
          String line;
          while ((line = reader.readLine()) != null) {
            response.append(line);
          }
          if (listener != null) {
            listener.onFinish(response.toString());
          }
        } catch (Exception e) {
          if (listener != null) {
            listener.onError(e);
          }
        } finally {
          if (connection != null) {
            connection.disconnect();
          }
        }
      }
    }).start();
  }
}
```

- 实际使用，传入地址并重写接口两个方法即可

```java
HttpUtil.sendHttpRequest(address, new HttpCallbackListener(){
  @override
  public void onFinish(String response) { // 返回内容处理逻辑
  };

  @override
  public void onError(Exception e) { // 异常处理
  }
})
```

#### OkHttp

- OkHttp库中自带回调接口 `okhttp3.Callback`
  - 会在 `enqueue()` 中开启子线程

```java
private static void sendOkHttpRequest(String address, okhttp3.Callback callback) {
  OkHttpClient client = new OkHttpClient();
  Request request = new Request.Builder()
    .url(address)
    .build();
  client.newCall(request).enqueue(callback);
}
```

- 调用时可以使用

```java
HttpUtil.sendOkHttpRequest("http://www.baidu.com", new okhttp3.Callback() {
  @Override
  public void onResponse(@NonNull Call call, @NonNull Response response) throws IOException {
    String data = response.body() != null ? response.body().string() : null;
    updateUI(data);
  }
  @Override
  public void onFailure(@NonNull Call call, @NonNull IOException e) {
    e.printStackTrace();
  }
});
```

## 服务 Service

- 服务是 Android 中实现程序后台运行的解决方案
  - 适合执行不需要和用户交互且需要长期运行的任务
  - 不依赖任何用户界面，即便在后台，或者切换到其他应用程序
  - **注意** 其并非独立进程，而是依赖创建服务时所在的应用程序

### 多线程

#### 基本用法

```java
package com.bayyy.services.basic;

public class MyThread {
  public static void main(String[] args) {
    // Thread
    UseThread useThread = new UseThread();
    useThread.start();

    // Runnable
    new Thread(new UseRunnable()).start();

    // 匿名类
    new Thread(() -> {
      // 实现逻辑
    }).start();
  }

  static class UseThread extends Thread {
    @Override
    public void run() {
      super.run();
      // 实现逻辑
    }
  }

  static class UseRunnable implements Runnable {
    @Override
    public void run() {
      // 实现逻辑
    }
  }
}
```

#### 子线程更新UI

```java
public class UpdateUI extends AppCompatActivity {
  public static final int UPDATE_TEXT = 1;
  private TextView tv_content;

  private Handler handler = new Handler(Looper.getMainLooper()) {
    // 添加 Looper.getMainLooper() 解决隐式选择 Looper 的报错
    public void handleMessage(android.os.Message msg) {
      switch (msg.what) {
        case UPDATE_TEXT:
          tv_content.setText("Now, update the content!");
          break;
        default:
          break;
      }
    }
  };

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    tv_content = findViewById(R.id.tv_content);
    findViewById(R.id.btn_change_text).setOnClickListener(v -> {
      new Thread(() -> {
        Message message = new Message();
        message.what = UPDATE_TEXT;
        handler.sendMessage(message);
      }).start();
    });
  }
}
```

#### 异步消息处理机制

- Message 线程间传递的消息
  - 可以在内部携带少量信息
  - 其中 `arg1, arg2` 可以携带整型数据，`obj` 字段可以携带 `Object` 对象
- Handler 用于发送和处理消息
  - `sendMessage()` 发送数据
  - `handleMessage()` 处理数据
- MessageQueue 消息队列
  - 存放所有通过 Handler 发送的消息
  - 每个线程仅有一个 MessageQueue 对象
- Looper 线程中 MessageQueue 的管理对象
  - 调用 `Looper.loop()` 会进入无限循环，每当 MessageQueue 中存在消息，会取出并传递到 Handler 的 handleMessage 方法

#### 使用 AsyncTask

- AsyncTask 作为抽象类，能够方便的从子线程切换到主线程
  - 实现原理：异步消息处理机制
  - 执行`AsyncTask`的`execute`，首先触发`onPreExecute`回调，然后交给线程池`sDefaultExecutor`调度，`mFuture`配合`mWorker`开启子线程，触发`doInBackground`回调，然后交给内部单例`InternalHandler`处理返回结果并返回到主线程，最后根据`Message`处理`onProgressUpdate`或`onPostExecute`
- 三个泛型参数
  - `Params` 执行 AsyncTask 的传入参数
  - `Progress` 当前进度
  - `Result` 返回结果

- 重写方法
  - `onPreExecute()` 任务执行前调用，可以进行界面初始化，例如进度条对话框等
  - `doInBackground(Params...)` 子线程任务，可以进行 `return` 返回结果
    - **在此过程执行耗时任务**
    - 此过程无法进行UI操作
    - 更新UI需要使用 `publishProgress(Progress...)` 完成
      - 实际是启动 `onProgressUpdate(Progress...)` 方法
  - `onProgressUpdate(Progress...)` 进行UI操作
  - `onPostExecute(Result)`  子线程任务的返回值会传入该函数，可以进行收尾操作，例如关闭进度条、开启提醒任务等

```java
class SampleAsyncTask extends AsyncTask<Void, Void, Void> {
  @Override
  protected void onPreExecute() {
    super.onPreExecute();
  }
  @Override
  protected Void doInBackground(Void... voids) {
    return null;
  }
  @Override
  protected void onProgressUpdate(Void... values) {
    super.onProgressUpdate(values);
  }
  @Override
  protected void onPostExecute(Void aVoid) {
    super.onPostExecute(aVoid);
  }
}


// 启动
new SampleAsyncTask().execute();
```

> 存在问题：由于`AsyncTask`与`Activity`或`Fragment`的生命周期无关而导致的内存泄漏等
>
> 替代方法：使用 `Executor` 或 `ThreadPoolExecutor` 或 `FutureTask`

### 服务基本用法

#### 服务定义

- `New -> Service -> Service`

```java
public class MyService extends Service {
  public MyService() {
  }
  @Override
  public IBinder onBind(Intent intent) {
    // TODO: Return the communication channel to the service.
    throw new UnsupportedOperationException("Not yet implemented");
  }
}
```

- 同时在 `AndroidManifest.xml` 中注册

```xml
<service
         android:name=".MyService"
         android:enabled="true"
         android:exported="true"></service>
```

#### 服务启动和停止

- `onStart()` 仅在第一次创建时候调用
- `onStartCommand()` 每次启动都调用，多次点击启动都输出

```java
// 活动的启停
findViewById(R.id.btn_start).setOnClickListener(v -> {
  startService(new Intent(this, MyService.class));
});
findViewById(R.id.btn_stop).setOnClickListener(v -> {
  stopService(new Intent(this, MyService.class));
});

// 服务注册输出
public class MyService extends Service {
  private static final String TAG = "MyLog";

  public MyService() {
  }

  @Override
  public void onCreate() {
    super.onCreate();
    Log.d(TAG, "MyService onCreate");
  }

  @Override
  public int onStartCommand(Intent intent, int flags, int startId) {
    Log.d(TAG, "MyService onStartCommand");
    return super.onStartCommand(intent, flags, startId);
  }

  @Override
  public void onDestroy() {
    super.onDestroy();
    Log.d(TAG, "MyService onDestroy");
  }

  @Override
  public IBinder onBind(Intent intent) {
    // TODO: Return the communication channel to the service.
    throw new UnsupportedOperationException("Not yet implemented");
  }
}
```

#### 活动和服务的通信

- 创建 Binder 对象进行服务绑定管理

```java
package com.bayyy.services;

import android.app.Service;
import android.content.Intent;
import android.os.Binder;
import android.os.IBinder;
import android.util.Log;

public class MyService extends Service {
  private static final String TAG = "MyLog";
  private DownloadBinder mBinder = new DownloadBinder();

  class DownloadBinder extends Binder {
    public void startDownload() {
      Log.d(TAG, "startDownload executed");
    }

    public int getProgress() {
      Log.d(TAG, "getProgress executed");
      return 0;
    }
  }

  @Override
  public IBinder onBind(Intent intent) {
    return mBinder;
  }
  
  // ...
}
```

- 创建 ServiceConnection 类
- 重写 `onServiceConnected()` 和 `onServiceDisconnected()`
  - 分别在活动与服务绑定以及解除绑定时调用
- 可以在活动中使用 `bindService()` 以及 `unbindService()` 绑定和解除绑定服务
  - `BIND_AUTO_CREATE` 进行绑定后自动创建服务，并使 Service 中 `onCrete()` 方法得到执行， `onStartCommand()` 不执行

```java
public class StartService extends AppCompatActivity {
  private MyService.DownloadBinder downloadBinder;
  private ServiceConnection connection = new ServiceConnection() {
    @Override
    public void onServiceConnected(ComponentName name, IBinder service) {
      downloadBinder = (MyService.DownloadBinder) service;
      downloadBinder.startDownload();
      downloadBinder.getProgress();
    }
    @Override
    public void onServiceDisconnected(ComponentName name) {
    }
  };

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    findViewById(R.id.btn_bind_service).setOnClickListener(v -> {
      // 绑定服务
      // 第一个参数是Intent对象，第二个参数是ServiceConnection对象, 第三个参数是一个标志位(这里传入BIND_AUTO_CREATE表示在Activity和Service建立关联后自动创建Service)
      bindService(new Intent(this, MyService.class), connection, BIND_AUTO_CREATE);
    });
    findViewById(R.id.btn_unbind_service).setOnClickListener(v -> {
      // 解绑服务
      unbindService(connection);
    });
  }
}
```

#### 服务的生命周期

| 手动调用方法      | 作用 |
| ----------------- | ---- |
| `startService()`  | 启动 |
| `stopService()`   | 停止 |
| `bindService()`   | 绑定 |
| `unbindService()` | 解绑 |

![服务的生命周期](https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/07/10/275343c1510d1d4c4779a14be59c6d36-20240710212407185-1720617847.png)

### 服务的高级用法

#### 调用前台通知

> 具体参照 8.1 Notification

#### IntentService

- 服务中启动多线程
  - 调用 `stopService()` 或者 `stopSelf()` 进行服务停止

```java
@override
public int onStartCommand(Intent intent, int flags, int startId) {
  new Thread(new Runnable() {
    @override
    public void run() {
      // 处理逻辑
      stopSelf();
    }
  }
  ).start();
}
```

- 使用 `IntentService` 类进行自动线程处理

```java
public class MyIntentService extends IntentService {
  private static final String TAG = "MyLog";
  public MyIntentService(String name) {
    super(name);
  }

  @Override
  protected void onHandleIntent(@Nullable Intent intent) {
    Log.d(TAG, "onHandleIntent: Thread is " + Thread.currentThread().getId());
    // 该部分代码会在子线程中执行
    // 并且会自动停止服务
  }

  @Override
  public void onDestroy() {
    super.onDestroy();
    Log.d(TAG, "onDestroy");
  }
}
```

## 基于位置的服务

- LBS(Location Based Service) 基于位置的服务
- 定位技术：
  - GPS定位
  - 通过网络定位

### 百度 LBS

- 根据官网流程进行 [百度-AndroidSDK-使用准备](https://lbsyun.baidu.com/faq/api?title=androidsdk/prepare)

- 获取 SHA1
  - 调试版本和发布版本命令不同
  - 调试版： `keytool -list -v -keystore debug.keystore`
  - 发布版：`keytool -list -v -keystore release.keystore`

![image-20240711232453984](https://cdn.jsdelivr.net/gh/Bayyys/PicX/img/2024/07/11/image-20240711232453984-1720711494.png)
