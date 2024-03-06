# Git

> Reference: 
>
> - Document
>   1. [Git - Book](https://git-scm.com/book/zh/v2)
>   2. 

# 1. 版本控制

> 版本控制是一种记录若干文件内容变化，以便将来查阅特定版本修订情况的系统.简单讲就是备份和记录。

## 1.1 版本控制发展历史

### 1.1.1 本地版本控制系统

> 版本控制是一种记录一个或若干文件内容变化，以便将来查阅特定版本修订情况的系统。
>
> 为了解决这个问题，人们很久以前就开发了许多种本地版本控制系统，大多都是采用某种简单的数据库来记录文件的历次更新差异。

![本地版本控制](https://s2.loli.net/2023/07/08/DFbvOdkzafx7MSR.png)

人们把项目拷贝到本地磁盘上进行备份，然后以命名方式来区分。这种做法好处是简单，但坏处也不少比如备份比较多或许就会混淆不同版本之间的区别。

本地版本管理就是把版本号存入数据库来记录文件的历次更新差异。

- 修订控制系统 (Revision Control System, RCS) 
  - 在硬盘上保存补丁集（补丁是指文件修订前后的变化）；通过应用所有的补丁，可以重新计算出各个版本的文件内容。

### 1.1.2 集中化版本控制系统

> 本地版本控制系统能够将不同版本的文档保存下来并且借助版本记录可以很方便定位相关文件但又引入了新的问题，如何让在不同系统上的开发者协同工作？

![集中化的版本控制](https://s2.loli.net/2023/07/08/4eh6SnGBdVsvPj1.png)

- 集中化的版本控制系统（Centralized Version Control Systems，简称CVCS)

这类系统，诸如CVS,Subversion以及Perforce等，都有一个单一的集中管理的服务器，保存所有文件的修订版本，而协同工作的人们都通过客户端连到这台服务器，取出最新的文件或者提交更新。多年以来，这已成为版本控制系统的标准做法。

这样做的好处是解决了人们开发协同的问题，但是把所有的代码提交到同一台服务器上有一个很明显的问题就是单点故障，如果这台服务器宕机了，那所有人都不能提交代码，还有如果这台服务器如果磁盘发生故障，碰巧没做备份，或者备份不够及时，就还是会有丢失数据的风险。最坏的情况是彻底丢失整个项目的所有历史更改记录，而被客户端提取出来的某些快照数据除外，但这样的话依然是个问题，你不能保证所有的数据都已经有人事先完整提电出来过。本地版本控制系统也存在类似问题，只要整个项目的历史记录被保存在单一位置，就有丢失所有历史更新记录的风险。

### 1.1.3 分布式版本控制系统

> 如何解决中央服务器的单点故障问题？

![分布式版本控制](https://s2.loli.net/2023/07/08/MmKqJa1bSBzvtwd.png)

- 分布式版本管理控制系统（Distributed Version Control System，简称DVCS)

为了解决集中化版本管理所带来的问题分布式版本管理控制系统（Distributed Version Control System，简称DVCS)就应运而生了.在这类系统中，像Git,Mercurial,Bazaar以及Darcs等，客户端不只是提取出最新版的文件快照，而是把最原始的代码仓库镜像到本地.这样一来，任何一处协同工作用的服务器发生故障，事后都可以用任何一个镜像出来的本地仓库恢复。因为每一次的提取操作，实际上都是一次对代码仓库的完整备份。

## 1.2 Git简史

> Linux 内核开源项目有着为数众多的参与者。 绝大多数的 Linux 内核维护工作都花在了提交补丁和保存归档的繁琐事务上（1991－2002年间）。 到 2002 年，整个项目组开始启用一个专有的分布式版本控制系统 BitKeeper 来管理和维护代码。
>
> 到了 2005 年，开发 BitKeeper 的商业公司同 Linux 内核开源社区的合作关系结束，他们收回了 Linux 内核社区免费使用 BitKeeper 的权力。 这就迫使 Linux 开源社区（特别是 Linux 的缔造者 Linus Torvalds）基于使用 BitKeeper 时的经验教训，开发出自己的版本系统。 他们对新的系统制订了若干目标：
>
> - 速度
> - 简单的设计
> - 对非线性开发模式的强力支持（允许成千上万个并行开发的分支）
> - 完全分布式
> - 有能力高效管理类似 Linux 内核一样的超大规模项目（速度和数据量）
>
> 自诞生于 2005 年以来，Git 日臻成熟完善，在高度易用的同时，仍然保留着初期设定的目标。 它的速度飞快，极其适合管理大项目，有着令人难以置信的非线性分支管理系统。

### 1.3 Git简介

> Git 用起来与其它的版本控制系统非常相似， 但它在对信息的存储和认知方式上却有很大差异

### 1.3.1 直接记录快照，而非差异比较

- 前类 将它们存储的信息看作是一组基本文件和每个文件随时间逐步累积的差异 （它们通常称作 **基于差异（delta-based）** 的版本控制）

- Git 像是把数据看作是对小型文件系统的一系列快照。 在 Git 中，每当你提交更新或保存项目状态时，它基本上就会对当时的全部文件创建一个快照并保存这个快照的索引。 为了效率，如果文件没有修改，Git 不再重新存储该文件，而是只保留一个链接指向之前存储的文件。 Git 对待数据更像是一个 **快照流**。

  ![区别对比](https://s2.loli.net/2023/07/08/QAIhPMlV6cTrZkB.png)

### 1.3.2 近乎所有操作都是本地执行

- 在本地磁盘上就有项目的完整历史，所以大部分操作看起来瞬间完成。

举个例子，要浏览项目的历史，Git 不需外连到服务器去获取历史，然后再显示出来——它只需直接从本地数据库中读取。 你能立即看到项目历史。如果你想查看当前版本与一个月前的版本之间引入的修改， Git 会查找到一个月前的文件做一次本地的差异计算，而不是由远程服务器处理或从远程服务器拉回旧版本文件再来本地处理。

### 1.3.3 Git 保证完整性

- Git 中所有的数据在存储前都计算校验和，然后以校验和来引用。 这意味着不可能在 Git 不知情时更改任何文件内容或目录内容。 

Git 用以计算校验和的机制叫做 SHA-1 散列（hash，哈希）。 这是一个由 40 个十六进制字符（0-9 和 a-f）组成的字符串，基于 Git 中文件的内容或目录结构计算出来。 SHA-1 哈希看起来是这样：

```markdown
24b9da6552252987aa493b52f8696cd6d3b00373
```

### 1.3.4 Git 一般只添加数据

你执行的 Git 操作，几乎只往 Git 数据库中 **添加** 数据。 你很难使用 Git 从数据库中删除数据，也就是说 Git 几乎不会执行任何可能导致文件不可恢复的操作。

### 1.3.5 三种状态

Git 有三种状态，你的文件可能处于其中之一： **已提交（committed）**、**已修改（modified）** 和 **已暂存（staged）**。

| 状态              | 描述                                                         |
| ----------------- | ------------------------------------------------------------ |
| 已提交(committed) | 数据已经安全的保存在本地数据库中                             |
| 已修改(modified)  | 修改了文件，但还没保存到数据库中                             |
| 已暂存(staged)    | 对一个已修改文件的当前版本做了标记，使之包含在下次提交的快照中 |

针对Git文件的三种状态，需要了解Git项目的三个工作区域：工作区、暂存区和Git仓库：

| 分类    | 描述                                                         |
| ------- | ------------------------------------------------------------ |
| 工作区  | 简单的理解为在电脑里能看到的目录，比如自己创建的本地项目目录 |
| 暂存区  | Git的版本库里存了很多东西，其中最重要的就是称为stage（或者叫index）的暂存区，还有Git自动创建的第一个分支master，以及指向master的一个指针叫HEAD |
| Git仓库 | 工作区有一个隐藏目录`.git`，这个不算工作区，而是Git的版本库  |

![工作区、暂存区以及 Git 目录。](https://s2.loli.net/2023/07/08/E4zowBkqOsi1nhg.png)

## 1.3 Windows安装

### 1.3.1 安装

- 官网安装：[Git](https://git-scm.com/)

  - 07/08/23: [2.37.2.windows.2(64-bit)](https://git-scm.com/download/win)
  - ![image-20230708130922459](https://s2.loli.net/2023/07/08/qj192wSt8KpxEzC.png)

- ==Git 升级==

  - ```powershell
    git update-git-for-windows
    ```

  - ![image-20230708131720133](https://s2.loli.net/2023/07/08/g3GuZcQyBt4SlI6.png)

### 1.3.2 配置

> Git 自带一个 `git config` 的工具来帮助设置控制 Git 外观和行为的配置变量。 这些变量存储在三个不同的位置：
>
> 1. `/etc/gitconfig` 文件: 包含系统上每一个用户及他们仓库的通用配置。 如果在执行 `git config` 时带上 `--system` 选项，那么它就会读写该文件中的配置变量。 （由于它是系统配置文件，因此你需要管理员或超级用户权限来修改它。）
> 2. `~/.gitconfig` 或 `~/.config/git/config` 文件：只针对当前用户。 你可以传递 `--global` 选项让 Git 读写此文件，这会对你系统上 **所有** 的仓库生效。
> 3. 当前使用仓库的 Git 目录中的 `config` 文件（即 `.git/config`）：针对该仓库。 你可以传递 `--local` 选项让 Git 强制读写此文件，虽然默认情况下用的就是它。。 （当然，你需要进入某个 Git 仓库中才能让该选项生效。）
>
> 每一个级别会覆盖上一级别的配置，所以 `.git/config` 的配置变量会覆盖 `/etc/gitconfig` 中的配置变量。
>
> - 查看所有配置以及所在文件
>
>   - ```sh
>     $ git config --list --show-origin
>     ```
>
>   - ![image-20230708132953470](https://s2.loli.net/2023/07/08/GjuAUXvThdN6BVP.png)

在使用用Git工作之前，我们需要做个==一次性的配置==。方便后续Git能跟踪到谁做了修改，我们需要设置对应的用户名与邮箱地址。

```shell
git config --global user.name "your_username"
git config --global user.email your_email@domain.com
git config --list	# 查看所有配置
```

> 注意`git config`命令的==` --global `==参数，用了这个参数，表示这台机器上所有的Git仓库都会使用这个配置，当然也可以对某个仓库指定不同的用户名和Email地址。

![image-20230708133141931](https://s2.loli.net/2023/07/08/9XelnTqWySPoL5j.png)

> 可以通过输入 `git config <key>`： 来检查 Git 的某一项配置
>
> ![image-20230708133215222](https://s2.loli.net/2023/07/08/lQJqDGuOw2seZCr.png)
>
> - Note: 由于 Git 会从多个文件中读取同一配置变量的不同值，因此你可能会在其中看到意料之外的值而不知道为什么。 此时，你可以查询 Git 中该变量的 **原始** 值，它会告诉你哪一个配置文件最后设置了该值：
>
>   - ```sh
>     $ git config --show-origin user.name
>     file:C:/Users/bayyy/.gitconfig  bayyy
>     ```

## 1.4 Help

```sh
$ git <verb> -h
```

![image-20230708133717734](https://s2.loli.net/2023/07/08/CLt3GJnsxcX9f8Y.png)

# 2. 基础操作

> 版本库又名仓库，可以简单理解成一个目录，这个目录里面的所有文件都可以被Git管理起来，每个文件的修改、删除，Git都能跟踪，以便任何时刻都可以追踪历史，或者在将来某个时刻可以“还原”。理解了Git文件状态与三种工作区域之后，通过一个例子来体验Git对于文件的基本操作。

![Git文件生命周期图](https://s2.loli.net/2023/07/08/OMSmVglpdjvJyEP.png)

## 2.1 初始化git本地仓库

通过执行`git init`命令在本地初始化一个本地仓库，执行该命令后会在本地初始化一个没有任何文件的空仓库。

![git_init](https://s2.loli.net/2023/07/08/uHQRAjWJzImvK67.png)

## 2.2 状态 status

进行一定的内容书写后，使用`git status`查看工作目录与暂存区文件状态

```sh
# 命令用于显示工作目录和暂存区的状态。使用此命令能看到那些修改被暂存到了，哪些没有，哪些文件没有被Git tracked到。
$ git status 
# 1. On branch main - 目前处在main分支

# 以简介方式查看更改
$ git status --short	# git status -s
```

![git_status](https://s2.loli.net/2023/07/08/RSnLuX2K9ysgNMf.png)

![image-20230708140806345](https://s2.loli.net/2023/07/08/FRWvCz4Q1X8NuBp.png)

## 2.3 暂存 add

```sh
$ git add path # 通常是通过git add <path>的形式把<path>添加到素引库中，<path>可以是文件也可以是目录。git不仅能判断出<path>中，修改（不包括已删除）的文件，还能判断出新添的文件，并把它们的信息添加到素引库中。
```

![image-20230708135831707](https://s2.loli.net/2023/07/08/me2AZEHrhbIStiu.png)

## 2.4 提交 commit

文件被添加到暂存区后，执行`git commit`命令提交暂存区文件到本地版本库中

```sh
$ git commit # 命令用于将更改记录（提交）到存储库。将索引的当前目录内容与描述更改的用户和日志消息一起存储在新的提交中。通常在执行提交时再用 git commit 后跟上 -m 属性，加入本次提交的记录说明，方便后续查看提交或改动记录。

# [main 32410ef] commit_desc	# 提交的: 1. 分支; 2. 校验和; 3. 信息; 4. 文件变动.
$ git commit -am 'commit_desc'	# 自动把所有已经跟踪过的文件暂存起来一并提交，从而跳过 git add 步骤

$ git commit -v --amend			# 重写最后的提交信息(覆盖之前的消息)

$ git cherry-pick [commit_id]	# 将另一个分支的一个特定提交合并到当前分支
```

![image-20230708144253896](https://s2.loli.net/2023/07/08/C4KoMbjuNdOA296.png)

## 2.5 日志信息 log

### 2.5.1 基本使用

```sh
# 按时间先后顺序列出所有的提交，最近的更新排在最上面。 正如你所看到的，这个命令会列出每个提交的 SHA-1 校验和、作者的名字和电子邮件地址、提交时间以及提交说明。
$ git log
```

![git_log](https://s2.loli.net/2023/07/08/drmgKhTYzViUkfu.png)

### 2.5.2 常用选项

```sh
$ git log -p	# -p:--patch	显示每次提交所引入的差异（按 补丁 的格式输出）
$ git log -<n>	# 显示最近 n 次的提交
$ git log --stat	# 查看提交的简略统计信息
$ git log --pretty=mode	# 使用不同于默认格式的方式展示提交历史(mode: online、short、full、fuller、format[需要添加参数])
```

![image-20230708145841383](https://s2.loli.net/2023/07/08/u3OjTyAGV9bQlgi.png)

### 2.5.3 定制显示

```sh
# 简写哈希值 - 作者名字, 修订日期(以相对时间) : 提交说明
$ git log --pretty=format:"%h - %an, %ar : %s"
32410ef - bayyy, 18 minutes ago : git_basis status diff
27028f1 - bayyy, 60 minutes ago : git_basis git commit
```

![image-20230708150003591](https://s2.loli.net/2023/07/08/rmLDoB47lcVEJMR.png)

> - format:	
>
>   - | 选项  | 说明                                          |
>     | :---- | :-------------------------------------------- |
>     | `%H`  | 提交的完整哈希值                              |
>     | `%h`  | 提交的简写哈希值                              |
>     | `%T`  | 树的完整哈希值                                |
>     | `%t`  | 树的简写哈希值                                |
>     | `%P`  | 父提交的完整哈希值                            |
>     | `%p`  | 父提交的简写哈希值                            |
>     | `%an` | 作者名字                                      |
>     | `%ae` | 作者的电子邮件地址                            |
>     | `%ad` | 作者修订日期（可以用 --date=选项 来定制格式） |
>     | `%ar` | 作者修订日期，按多久以前的方式显示            |
>     | `%cn` | 提交者的名字                                  |
>     | `%ce` | 提交者的电子邮件地址                          |
>     | `%cd` | 提交日期                                      |
>     | `%cr` | 提交日期（距今多长时间）                      |
>     | `%s`  | 提交说明                                      |
>
> - **作者**-**提交者**
>
>   - 作者指的是实际作出修改的人，提交者指的是最后将此工作成果提交到仓库的人。 所以，当你为某个项目发布补丁，然后某个核心成员将你的补丁并入项目时，你就是作者，而那个核心成员就是提交者

### 2.5.4 图形显示

```sh
$ git log --pretty=format:"%h %s" --graph	# 添加了一些 ASCII 字符串来形象地展示你的分支、合并历史
* 2d3acf9 ignore errors from SIGCHLD on trap
*  5e3ee11 Merge branch 'master' of git://github.com/dustin/grit
|\
| * 420eac9 Added a method for getting the current branch.
* | 30e367c timeout code and tests
* | 5a09431 add timeout protection to grit
* | e1193f8 support for heads with slashes in them
|/
* d6016bc require time for xmlschema
*  11d191e Merge branch 'defunkt' into local
```

### 2.5.5 更多选项

| 选项              | 说明                                                         |
| :---------------- | :----------------------------------------------------------- |
| `-p`              | 按补丁格式显示每个提交引入的差异。                           |
| `--stat`          | 显示每次提交的文件修改统计信息。                             |
| `--shortstat`     | 只显示 --stat 中最后的行数修改添加移除统计。                 |
| `--name-only`     | 仅在提交信息后显示已修改的文件清单。                         |
| `--name-status`   | 显示新增、修改、删除的文件清单。                             |
| `--abbrev-commit` | 仅显示 SHA-1 校验和所有 40 个字符中的前几个字符。            |
| `--relative-date` | 使用较短的相对时间而不是完整格式显示日期（比如“2 weeks ago”）。 |
| `--graph`         | 在日志旁以 ASCII 图形显示分支与合并历史。                    |
| `--pretty`        | 使用其他格式显示历史提交信息。可用的选项包括 oneline、short、full、fuller 和 format（用来定义自己的格式）。 |
| `--oneline`       | `--pretty=oneline --abbrev-commit` 合用的简写。              |

### 2.5.6 限制输出长度

```sh
$ git log --since=2.weeks	# 列出最近两周的所有提交
$ git log --until=1.hours	# 显示1小时之前的提交
$ git log --anthor=bayyy	# 显示指定作者的提交
$ git log --grep=basis		# 搜索提交说明中的关键字
```

> Note - 你可以指定多个 `--author` 和 `--grep` 搜索条件，这样会只输出匹配 **任意** `--author` 模式和 **任意** `--grep` 模式的提交。然而，如果你添加了 `--all-match` 选项， 则只会输出匹配 **所有** `--grep` 模式的提交。

```sh
$ git log -S <str>	# 受一个字符串参数，并且只会显示那些添加或删除了该字符串的提交
```

```sh
$ git log ... -- <path>	# 在 git log 选项的最后指定它们的路径。 因为是放在最后位置上的选项，所以用两个短划线（--）隔开之前的选项和后面限定的路径名。
```

| 选项                  | 说明                                       |
| :-------------------- | :----------------------------------------- |
| `-<n>`                | 仅显示最近的 n 条提交。                    |
| `--since`, `--after`  | 仅显示指定时间之后的提交。                 |
| `--until`, `--before` | 仅显示指定时间之前的提交。                 |
| `--author`            | 仅显示作者匹配指定字符串的提交。           |
| `--committer`         | 仅显示提交者匹配指定字符串的提交。         |
| `--grep`              | 仅显示提交说明中包含指定字符串的提交。     |
| `-S`                  | 仅显示添加或删除内容匹配指定字符串的提交。 |

### 2.5.7 历史版本记录

```sh
$ git reflog	# 显示可引用的历史版本记录,能够记录几乎所有本地仓库的改变，无论是否提交了快照
```

![image-20230708191104171](https://s2.loli.net/2023/07/08/VDMo7OXzJ9KZTB3.png)

### 2.5.8 log 使用技巧

```sh
$ git log -S'<a term in the source>'	# 按内容搜索更改

$ git log -p <file_name>	# 显示特定文件随时间的变化

$ git log --pretty=oneline --graph --decorate --all	# 打印出很酷的日志可视化
```

### 2.5.9 测试

```sh
$ git log --pretty='%h : %an - %s (%cr)' --author='bayyy' --since="2023.06.25" --before="2023.07.06" --no-merges
b41a8de : bayyy - Python-S "标准库-内置函数" bayyy-23.07.05 (3 days ago)
04575ab : bayyy - Python-S "标准库-内置函数" bayyy-23.07.05 (3 days ago)
2ba25d9 : bayyy - JavaWeb-S "JSP" bayyy-23.07.02 (6 days ago)
4c19eda : bayyy - JW-S "JavaWeb-6.7" bayyy-23.07.01 (7 days ago)
0e0d893 : bayyy - JW-S "JavaWeb-6.7" bayyy-23.07.01 (7 days ago)
2f67dd5 : bayyy - JavaWeb-A "javaweb-02-servlet" bayyy-23.07.01 (7 days ago)
200f2fd : bayyy - JavaWeb-A "javaweb-01-maven" bayyy-23.07.01 (7 days ago)
ea0b9df : bayyy - JavaWeb-A "JavaTest" bayyy-23.07.01 (7 days ago)
d95ffaf : bayyy - JavaWeb "Init Project" bayyy-23.07.01 (7 days ago)
```

> Tip - 按照你代码仓库的工作流程，记录中可能有为数不少的合并提交，它们所包含的信息通常并不多。 为了避免显示的合并提交弄乱历史记录，可以为 `log` 加上 `--no-merges` 选项

## 2.6 克隆 clone

```sh
$ gie clone https://xxx.com/xxx/<original_name> <new_name>	# 这会在当前目录下创建一个名为 “original_name” 的目录，并在这个目录下初始化一个 .git 文件夹， 从远程仓库拉取下所有数据放入 .git 文件夹，然后从中读取最新版本的文件的拷贝。
# 如果增加了 “new_name” 选项, 则可以自定义目标目录名
```

![git_clone](https://s2.loli.net/2023/07/08/BajfQoSKh26ytlD.png)

## 2.6 忽略 .gitignore

- 格式规范

  - 所有空行或者以 `#` 开头的行都会被 Git 忽略。
  - 可以使用标准的 glob 模式匹配，它会递归地应用在整个工作区中。
  - 匹配模式可以以（`/`）开头防止递归。
  - 匹配模式可以以（`/`）结尾指定目录。
  - 要忽略指定模式以外的文件或目录，可以在模式前加上叹号（`!`）取反。

- glob 模式

  > 所谓的 glob 模式是指 shell 所使用的简化了的正则表达式。 星号（`*`）匹配零个或多个任意字符；`[abc]` 匹配任何一个列在方括号中的字符 （这个例子要么匹配一个 a，要么匹配一个 b，要么匹配一个 c）； 问号（`?`）只匹配一个任意字符；如果在方括号中使用短划线分隔两个字符， 表示所有在这两个字符范围内的都可以匹配（比如 `[0-9]` 表示匹配所有 0 到 9 的数字）。 使用两个星号（``）表示匹配任意中间目录，比如 `a//z` 可以匹配 `a/z` 、 `a/b/z` 或 `a/b/c/z` 等。

> Tip -  GitHub 有一个十分详细的针对数十种项目及语言的 `.gitignore` 文件列表， 你可以在 https://github.com/github/gitignore 找到它。
>
> Note - 在最简单的情况下，一个仓库可能只根目录下有一个 `.gitignore` 文件，它递归地应用到整个仓库中。 然而，子目录下也可以有额外的 `.gitignore` 文件。子目录中的 `.gitignore` 文件中的规则只作用于它所在的目录中。 （Linux 内核的源码库拥有 206 个 `.gitignore` 文件。）

## 2.7 具体修改 diff

- 要查看尚未暂存的文件更新了哪些部分：`git diff`

```sh
$ git diff	# 已更改但未暂存内容的差异: 比较工作目录中当前文件和暂存区域快照之间的差异。 也就是修改之后还没有暂存起来的变化内容。
$ git diff --staged	# 已 commited 但尚未提交的内容的差异: 这条命令将比对已暂存文件与最后一次提交的文件差异
$ git diff --cached	# 同上
```

![image-20230708141716949](https://s2.loli.net/2023/07/08/1Mi6jJDvxzq9aT2.png)

> Notice - `git diff` 本身只显示尚未暂存的改动，而不是自上次提交以来所做的所有改动

```sh
$ git diff HEAD -- [file]	# 查看指定文件的差异
```

![image-20230708190412283](https://s2.loli.net/2023/07/08/Y1sRHENW4uxf6CF.png)

```markdown
差异比较说明：
`---`：表示变动前的文件
`+++`：表示变动后的文件
变动的位置用两个@作为起首和结束
@@ -2,4 +2,6 @@：减号表示第一个文件，“2”表示第2行，’4‘表示连续4行。同样的，“+2,6”表示变动后，成为第二个文件从第2行开始的连续6行。
```



## 2.8 移除文件 rm

```sh
$ git rm <file>	# 移除某个文件，就必须要从已跟踪文件清单中移除（确切地说，是从暂存区域移除）
$ git rm -f <file>	# 删除之前修改过或已经放到暂存区的文件	-f: force 强制删除
$ git rm --cached <file>	# 让文件保留在磁盘，但是不让 Git 继续跟踪
```

![image-20230708145237079](https://s2.loli.net/2023/07/08/ag7b8vL2W4VdFTJ.png)

## 2.9 移动文件 mv

```sh
$ git mv file_from file_to	# 中对文件改名

# ------ 相当于 --------
$ mv README.md README
$ git rm README.md
$ git add README
```

![image-20230708145307275](https://s2.loli.net/2023/07/08/KiaxQXI4uMzorbd.png)

## 2.10 撤销

### 2.10.1 修改提交说明 --amend

```sh
$ git commit --amend	# 将暂存区中的文件提交。 如果自上次提交以来你还未做任何修改（例如，在上次提交后马上执行了此命令）， 那么快照会保持不变，而你所修改的只是提交信息
```

- 提交 -> 修改 -> --amend	最终只会有依次提交(替代)

> Note - 与其说是修复旧提交，倒不如说是完全用一个 **新的提交** 替换旧的提交。从效果上来说，就像是旧有的提交从未存在过一样，它并不会出现在仓库的历史中。

### 2.10.2 取消暂存 reset

```sh
$ git reset HEAD <file_name>	# 取消暂存
```

![image-20230708152934129](https://s2.loli.net/2023/07/08/agPJTqmDxHK2iEv.png)

> Note - `git reset` 确实是个危险的命令，如果加上了 `--hard` 选项则更是如此。 在上述场景中，工作目录中的文件尚未修改，因此相对安全一些。

### 2.10.3 撤销修改

```sh
$ git checkout -- <file>	# 撤销修改
```

> Important - 请务必记得 `git checkout — <file>` 是一个危险的命令。 你对那个文件在本地的任何修改都会消失——Git 会用最近提交的版本覆盖掉它。 除非你确实清楚不想要对那个文件的本地修改了，否则请不要使用这个命令。

### 2.10.4 版本回退

```sh
$ git reset --hard HEAD^	# 一个^ 回退一个版本
$ git reset --hard HEAD~1	# 数字表示回退相对版本
$ git reset --hard <hash>	# 回退到指定校验的版本

$ git fetch --all && git reset --hard origin/master	# 抛弃本地所有的修改，回到远程仓库的状态
```

## 2.11 别名 alias

```sh
$ git config --global alias.ci commit 	# 当要输入 git commit 时，只需要输入 git ci
$ git config --global alias.unstage 'reset HEAD --'
```

## 2.12 git代码统计

```sh
# 查看指定 author 的个人代码量
$ git log --author="bayyy" --pretty=tformat: --numstat | awk \
'{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -	

# 统计每个人的增删行数
$ git log --format='%aN' | sort -u |\
  while read name; do echo -en "$name\t";\
  git log --author="$name" --pretty=tformat: --numstat | awk \
  '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -; done
  
# 查看仓库提交者排名(前10 可更改)
$ git log --pretty='%aN' | sort | uniq -c | sort -k1 -n -r | head -n 10

# 统计提交次数
$ git log --oneline | wc -l
```



# 3. 远程仓库

> Note - 你完全可以在一个“远程”仓库上工作，而实际上它在你本地的主机上。 词语“远程”未必表示仓库在网络或互联网上的其它位置，而只是表示它在别处。 在这样的远程仓库上工作，仍然需要和其它远程仓库上一样的标准推送、拉取和抓取操作。

## 3.1 查看 remote

```sh
$ git remote	# 列出指定的每一个远程服务器的简写

$ git remote -v	# 显示需要读写远程仓库使用的 Git 保存的简写与其对应的 URL
origin  git@github.com:Bayyys/temp.git (fetch)
origin  git@github.com:Bayyys/temp.git (push)

$ git remote show <remote>	# 查看某一个远程仓库的更多信息
# 会列出远程仓库的 URL 与跟踪分支的信息。 这些信息非常有用，它告诉你正处于 master 分支，并且如果运行 git pull， 就会抓取所有的远程引用，然后将远程 master 分支合并到本地 master 分支。 它也会列出拉取到的所有远程引用。
```

![image-20230708154534161](https://s2.loli.net/2023/07/08/vym48LB2oFGApQS.png)

## 3.2 添加 add

```sh
$ git remote add <shortname> <url>	# 添加一个新的远程 Git 仓库，同时指定一个方便使用的简写
$ git remote set-url origin [git_url]	# 更改 git repo 的 URL
```

![image-20230708153940311](https://s2.loli.net/2023/07/08/lkpNPa4yezWxoVQ.png)

## 3.3 抓取与拉取

```sh
$ git fetch <remote>	# 从远程仓库中获得数据

$ git clone --depth=1 https://github.com/user/repo.git
```

- 如果你使用 `clone` 命令克隆了一个仓库，命令会自动将其添加为远程仓库并默认以 “origin” 为简写
- `git fetch` 命令只会将数据下载到你的本地仓库——它并不会自动合并或修改你当前的工作，必须手动将其合并入工作
- 如果你的当前分支设置了跟踪远程分支（`git clone` 默认会执行此操作）， 那么可以用 `git pull` 命令来自动抓取后合并该远程分支到当前分支。 

## 3.4 推送 push

```sh
$ git push origin master	# 将 master 分支推送到 origin 服务器
```

## 3.5 重命名/删除

```sh
$ git remote rename <remote> <remote_new>	# 重命名 同样也会修改你所有远程跟踪的分支名字
$ git remote remove <remote>	# 删除 所有和这个远程仓库相关的远程跟踪分支以及配置信息也会一起被删除。
$ git push origin :<remote>		# 删除
$ git push origin --delete <remote>
```

## 3.6 远程仓库使用

### 3.6.1 HTTPS

```shell
echo "# git01" >> README.md
git init
git add [file]
git commit -m "first commit"
git remote add origin https://github.com/Bayyys/git01.git
git push -u origin master
```

### 3.6.2 SSH

```shell
echo "# git01" >> README.md
git init
git add [file]
git commit -m "first commit"
git remote add origin git@github.com:Bayyys/git01.git
git push -u origin master
```

### 3.6.3 申请秘钥

- 需要先申请公钥&秘钥\

  ```sh
  $ ssh-keygen -t rsa -C "475417309@qq.com"
  ```

  ![image-20220731104444471](https://s2.loli.net/2023/07/08/ch19BRMTK3wnPvZ.png)

- 到`/c/users/BAY/.ssh/id_rsa.pub`中找到公钥

- 添加公钥到SSH Keys

  ![image-20220731105042282](https://s2.loli.net/2023/07/08/vSjPxuAJHwGbm3C.png)

  ![image-20220731105337774](https://s2.loli.net/2023/07/08/7YHPkK2OyMT9urD.png)

- 检查测试链接 执行命令`ssh -T git@github.com`

  ![image-20220731105402124](https://s2.loli.net/2022/07/31/4JKWSmEALM1fzXQ.png)

# 4.  分支/标签

## 4.1 标签 tag

> Git 可以给仓库历史中的某一个提交打上标签，以示重要。 比较有代表性的是人们会使用这个功能来标记发布结点（ `v1.0` 、 `v2.0` 等等）

### 4.1.1 列出 tag

```sh
$ git tag	# 以字母顺序列出标签

$ git tag -l "v1*"
# -l:--list 列表;
# "v1*" 按照特定模式查找;

$ git show <tag>	# 查看标签信息和与之对应的提交信息
# 显示了打标签者的信息、打标签的日期时间、附注信息，然后显示具体的提交信息
```

![image-20230708155629665](https://s2.loli.net/2023/07/08/UotMpeTfEhxiVd3.png)

> Note - 如果你只想要完整的标签列表，那么运行 `git tag` 就会默认假定你想要一个列表，它会直接给你列出来， 此时的 `-l` 或 `--list` 是可选的。然而，如果你提供了一个匹配标签名的通配模式，那么 `-l` 或 `--list` 就是强制使用的。

### 4.1.2 创建标签 -a

```sh
$ git tag -a v1.0 -m 'version v1.0'
# -a 
# -m 指定了一条将会存储在标签中的信息(如果未指定, 会启动编辑器输入信息)

$ git tag v1.1	# 轻量标签, 查看不会看到额外的标签信息(没有打标者信息及打标时间、附注信息等)

$ git tag -a v1.2 <history_hash>	# 后期打标签(结尾指定提交的校验和)
```

### 4.1.3 共享标签

> 默认情况下，`git push` 命令并不会传送标签到远程仓库服务器上。 在创建完标签后你必须显式地推送标签到共享服务器上。 这个过程就像共享远程分支一样

```sh
$ git push origin v1.0	# 显式地推送标签到共享服务器上
$ git push origin --tags	# 把所有不在远程仓库服务器上的标签推送
```

![image-20230708160735829](https://s2.loli.net/2023/07/08/iqAd3clX85ZR4DW.png)

> - Note - `git push` 推送两种标签
>   - 使用 `git push <remote> --tags` 推送标签并不会区分轻量标签和附注标签， 没有简单的选项能够让你只选择推送一种标签。

### 4.1.4 删除 -d

```sh
$ git tag -d v1.0	# 删除掉你本地仓库上的标签

#  删除远程仓库标签
$ git push origin :refs/tags/v1.0	# 这种操作的含义是，将冒号前面的空值推送到远程标签名，从而高效地删除它
$ git push origin --delete v1.0		# 更直观的删除远程标签的方式
```

![image-20230708161148810](https://s2.loli.net/2023/07/08/SL1RINrc9H5iyvF.png)

### 4.1.5 检出标签

```sh
$ git checkout v1.0		# 查看某个标签所指向的文件版本, 虽然这会使你的仓库处于“分离头指针（detached HEAD）”的状态
```

![image-20230708161314598](https://s2.loli.net/2023/07/08/bsnKHSv14FPrzIk.png)

> 副作用 - 在“分离头指针”状态下，如果你做了某些更改然后提交它们，标签不会发生变化， 但你的新提交将不属于任何分支，并且将无法访问，除非通过确切的提交哈希才能访问。 因此，如果你需要进行更改，比如你要修复旧版本中的错误，那么通常需要创建一个新分支：
>
> ```console
> $ git checkout -b version2 v2.0.0
> Switched to a new branch 'version2'
> ```
>
> 如果在这之后又进行了一次提交，`version2` 分支就会因为这个改动向前移动， 此时它就会和 `v2.0.0` 标签稍微有些不同，这时就要当心了。

## 4.2 分支

### 4.2.1 分支简介

当使用 `git commit` 进行提交操作时，Git 会先计算每一个子目录（本例中只有项目根目录）的校验和， 然后在 Git 仓库中这些校验和保存为树对象。随后，Git 便会创建一个提交对象， 它除了包含上面提到的那些信息外，还包含指向这个树对象（项目根目录）的指针。 如此一来，Git 就可以在需要的时候重现此次保存的快照。

```sh
$ git add README test.rb LICENSE
$ git commit
```

在示例中:

- Git 仓库中有五个对象：三个 *blob* 对象（保存着文件快照）、一个 **树** 对象 （记录着目录结构和 blob 对象索引）以及一个 **提交** 对象（包含着指向前述树对象的指针和所有提交信息）。

![首次提交对象及其树结构](https://s2.loli.net/2023/07/08/qVx2EoDGahYZQCO.png)

- 修改后再次提交，那么这次产生的提交对象会包含一个指向上次提交对象（父对象）的指针。

![提交对象及其父对象](https://s2.loli.net/2023/07/08/2hZKz6k1vmbdLja.png)

- Git 的分支，其实本质上仅仅是指向提交对象的可变指针

### 4.2.2 分支创建 branch

```sh
$ git branch testing	# 创建名为 testing 的分支
$ git checkout -b <new_branch_name>	# 创建新分支并切换分支

$ git branch -vv	# 列出所有分支及其上游
$ git branch --all	# 列出所有分支
$ git branch -r		# 只获取所有远程分支
```

- Git 有一个名为HEAD的特殊指针, 指向当前所在的分支

![HEAD 指向当前所在的分支。](https://s2.loli.net/2023/07/08/QrSLKqouYWI3pig.png)



![image-20230708162812577](https://s2.loli.net/2023/07/08/LSV1sAyOaZcJpbF.png)

### 4.2.3 分支切换 checkout

```sh
$ git checkout <branch>	# 分支切换
$ git checkout -	# 快速切换到上一个分支
```

- 查看各个分支指向的对象

  - ```sh
    $ git log --oneline --decorate	# 查看各个分支指向的对象(decorate 装饰)
    ```

  - ![image-20230708163118753](https://s2.loli.net/2023/07/08/yi1C4QSngNTkGAV.png)

- 检出时HEAD随之移动

> Note - 在切换分支时，一定要注意你工作目录里的文件会被改变。 如果是切换到一个较旧的分支，你的工作目录会恢复到该分支最后一次提交时的样子。 如果 Git 不能干净利落地完成这个任务，它将禁止切换分支。

- 项目分叉历史

  - ```sh
    $ git log --oneline --decorate --graph --all
    ```

  - ![image-20230708163742612](https://s2.loli.net/2023/07/08/EmzIsj8wFZiNbT6.png)

  - ![项目分叉历史](https://s2.loli.net/2023/07/08/hMAIoVQbndWgpNB.png)

### 4.2.4 分支删除 -d

```sh
$ git branch -d <branch_name>	# 删除分支
$ git remote prune origin		# 删除本地存在远程不存在的分支
```

### 4.2.5 分支合并 merge

```sh
$ git merge <branch_name>	# 合并分支

$ git merge --no-ff [alias]/[branch]	# 没有快进

$ git merge --ff-only [alias]/[branch]	# 仅快进
```

- Fast-forward Merge

  ![image-20230708165227419](https://s2.loli.net/2023/07/08/AqjhSpgtdTcx4Us.png)

- 多快照 Merge

![image-20230708164844479](https://s2.loli.net/2023/07/08/pILzJk4RTYaq1HU.png)

![一次典型合并中所用到的三个快照](https://s2.loli.net/2023/07/08/p8fClXnyb5magzV.png)



### 4.2.6 分支冲突

- 如果在两个不同的分支中，对同一个文件的同一个部分进行了不同的修改，Git 就没法干净的合并它们
- Git 会暂停下来，等待你去解决合并产生的冲突。 你可以在合并冲突后的任意时刻使用 `git status` 命令来查看那些因包含合并冲突而处于未合并（==unmerged==）状态的文件
- ==HEAD -> (main|MERGING)==

![image-20230708165854508](https://s2.loli.net/2023/07/08/et1BnXrmD5L7jx6.png)

- ```sh
  $ gie merge mergetool	# 使用图形化工具来解决冲突
  
  This message is displayed because 'merge.tool' is not configured.
  See 'git mergetool --tool-help' or 'git help config' for more details.
  'git mergetool' will now attempt to use one of the following tools:
  opendiff kdiff3 tkdiff xxdiff meld tortoisemerge gvimdiff diffuse diffmerge ecmerge p4merge araxis bc codecompare smerge emerge vimdiff nvimdiff
  Merging:
  merge.txt
  
  Normal merge conflict for 'merge.txt':
    {local}: modified file
    {remote}: modified file
  Hit return to start merge resolution tool (vimdiff):
  
  ```

  - ![image-20230708171142911](https://s2.loli.net/2023/07/08/nIwx8SBYVEzUi7t.png)

### 4.2.7 分支管理

```sh
$ git branch	# 查看当前所有分支, 并且检出所在分支
$ git branch --merged	# 查看合并到当前分支的所有分支
$ git branch --no-merged	# 查看未合并到当前分支的所有分支
$ git branch --no-merged <branch_name>	# 查看其他分支的合并状态
```

![image-20230708172147084](https://s2.loli.net/2023/07/08/AQJtcKWNv7Xfy1Z.png)

### 4.2.8 分支开发工作流

#### 1）长期分支

> 许多使用 Git 的开发者都喜欢使用这种方式来工作，比如只在 `main` 分支上保留完全稳定的代码——有可能仅仅是已经发布或即将发布的代码。 他们还有一些名为 `develop` 或者 `next` 的平行分支，被用来做后续开发或者测试稳定性——这些分支不必保持绝对稳定，但是一旦达到稳定状态，就可以被合并入 `main` 分支。

- 流水线（work silos）
- 一些大型项目还有一个 `proposed`（建议） 或 `pu: proposed updates`（建议更新）分支，它可能因包含一些不成熟的内容而不能进入 `next` 或者 `master` 分支
- 目的：使你的分支具有不同级别的稳定性；当它们具有一定程度的稳定性后，再把它们合并入具有更高级别稳定性的分支中

![趋于稳定分支的工作流（“silo”）视图](https://s2.loli.net/2023/07/08/27i3h5DRAnwlLdg.png)

#### 2）主题分支

> 主题分支是一种短期分支，它被用来实现单一特性或其相关工作

![拥有多个主题分支的提交历史](https://s2.loli.net/2023/07/08/O8lwNrZbXQk13pL.png)

## 4.3 远程分支

### 4.3.1 远程引用

> 远程引用是对远程仓库的引用（指针），包括分支、标签等等

```sh
$ git ls-remote <remote>	# 显式地获得远程引用的完整列表
$ git remote show <remote>	# 获得远程分支的更多信息
```

### 4.3.2 远程跟踪分支

> 远程跟踪分支是远程分支状态的引用。
>
> 它们是你无法移动的本地引用。一旦你进行了网络通信， Git 就会为你移动它们以精确反映远程仓库的状态。请将它们看做书签， 这样可以提醒你该分支在远程仓库中的位置就是你最后一次连接到它们的位置。

- 远程跟踪分支以 `<remote>/<branch>` 的形式命名；

  - ```sh
    $ git clone <url> -o <remote_name>	# 在本地重命名远程分支名
    ```

  - 

- 远程抓取多个仓库会以`<remote>/...`进行区分

  - ![远程跟踪分支 `teamone/master`。](https://s2.loli.net/2023/07/08/hWLTx4sdPBNyES8.png)

- 推送到指定分支

  - ```sh
    $ git push <remote> <branch>	# 推送当前分支到远程 <remote> 仓库的 <branch> 分支
    $ git push <remote> <local_branch>:<remote_branch>	# 推送本地仓库的 <local_branch> 到远程 <remote> 的 <remote_branch> 分支
    ```

> Note - 避免每次重输密码
>
> 如果你正在使用 HTTPS URL 来推送，Git 服务器会询问用户名与密码。 默认情况下它会在终端中提示服务器是否允许你进行推送。
>
> 如果不想在每一次推送时都输入用户名与密码，你可以设置一个 “credential cache”。 最简单的方式就是将其保存在内存中几分钟，可以简单地运行 `git config --global credential.helper cache` 来设置它。

- 在自己的 `origin` 分支上工作，可以将其建立在远程跟踪分支之上

  - ```sh
    $ git checkout -b <my_branch> <remote>/<remote_branch>	# 建立一个本地分支，并且起点位于 <remote>/<remote_branch>
    ```

### 4.3.3 跟踪分支

#### 1）创建

- 从一个远程跟踪分支检出一个本地分支会自动创建所谓的“跟踪分支”（它跟踪的分支叫做“上游分支”），如果在一个跟踪分支上输入 `git pull`，Git 能自动地识别去哪个服务器上抓取、合并到哪个分支。

```sh
$ git checkout -b <my_branch> <remote>/<remote_branch>	# 建立一个本地分支，并且起点位于 <remote>/<remote_branch>
$ git checkout --track <remote>/<remote_branch>	# 同上
$ git checkout <remote_branch>	# 尝试检出的分支 (a) 不存在且 (b) 刚好只有一个名字与之匹配的远程分支，那么 Git 就会为你创建一个跟踪分支
```

- 需要先 `git fetch <remote_new>`

![image-20230708180447983](https://s2.loli.net/2023/07/08/njVgdpf3crsDO1z.png)

```sh
$ git checkout -b <banch_name> <remote>/<remote_branch>	# 将签出本地分支与远程分支设置为不同的名字
```

![image-20230708180814389](https://s2.loli.net/2023/07/08/7q6p4FTBEZyNmol.png)

```sh
$ git branch -u <remote>/<remote_branch>	# 设置已有的本地分支跟踪一个刚刚拉取下来的远程分支，或者想要修改正在跟踪的上游分支
# -u:--set-upstream-to
```

> Note - **上游快捷方式**
>
> 当设置好跟踪分支后，可以通过简写 `@{upstream}` 或 `@{u}` 来引用它的上游分支。 所以在 `master` 分支时并且它正在跟踪 `origin/master` 时，如果愿意的话可以使用 `git merge @{u}` 来取代 `git merge origin/master`。

#### 2）查看

```sh
$ git fetch --all	# 通常查询无法查到远程最新数据，因此首先拉取所有数据
$ git branch -vv	# 查看设置的所有跟踪分支, 会将所有的本地分支列出来并且包含更多的信息，如每一个分支正在跟踪哪个远程分支与本地分支是否是领先、落后或是都有
```

![image-20230708181314548](https://s2.loli.net/2023/07/08/qTomO8CyLiuGvgN.png)

#### 3）拉取

```sh
$ git pull	# 查找当前分支所跟踪的服务器与分支， 从服务器上抓取数据然后尝试合并入那个远程分支
# 其实现通常易出错，因此单独显式的使用 fetch 和 merge 命令会更好一点
```

#### 4）删除

```sh
$ git push origin --delet <remote_branch>	# 删除一个远程分支
```

## 4.4 变基

> 将提交到某一分支上的所有修改都移至另一分支上，就好像“重新播放”一样

### 4.4.1 简单的变基示例

![image-20230708182843087](https://s2.loli.net/2023/07/08/mGrPNFH9LQqiRg2.png)

```sh
# 检出 experiment 分支，然后将它变基到 master 分支上
$ git checkout experiment
$ git rebase master

# 合并
$ git checkout master
$ git merge experiment
```

> 一般我们这样做的目的是为了确保在向远程分支推送时能保持提交历史的整洁——例如向某个其他人维护的项目贡献代码时。 在这种情况下，你首先在自己的分支里进行开发，当开发完成时你需要先将你的代码变基到 `origin/master` 上，然后再向主项目提交修改。 这样的话，该项目的维护者就不再需要进行整合工作，只需要快进合并便可。
>
> 变基是将一系列提交按照原有次序依次应用到另一分支上，而合并是把最终结果合在一起。

### 4.4.2 复杂的变基示例

![ima](https://s2.loli.net/2023/07/08/buexTG4lBpHi3cW.png)

```sh
# 选中在 client 分支里但不在 server 分支里的修改（即 C8 和 C9），将它们在 master 分支上重放
$ git rebase --onto master server client	#  通俗的理解：取出 client 分支，找出它从 server 分支分歧之后的补丁， 然后把这些补丁在 master 分支上重放一遍，让 client 看起来像直接基于 master 修改一样

# merge client
$ git checkout master
$ git merge client

# 将主题分支（server）变基到目标分支（master）上
$ git rebase master server

# merge server
$ git checkout master
$ git merge server

# 删除额外分支, 此时提交历史只有一条
$ git branch -d client
$ git branch -d server
```

### 4.4.3 变基的风险

- 原则：**如果提交存在于你的仓库之外，而别人可能基于这些提交进行开发，那么不要执行变基。**
  - ![你将相同的内容又合并了一次，生成了一个新的提交。](https://s2.loli.net/2023/07/08/a6EBvZDr9fJe5kd.png)
  - 服务器端的变基内容被保留！
- 合并/变基的总原则：
  - **只对尚未推送或分享给别人的本地修改执行变基操作清理历史**
  - **从不对已推送至别处的提交执行变基操作**

## 4.5 分支操作

### 4.5.1 分支切换

| 命令                                         | 描述                                                         |
| -------------------------------------------- | ------------------------------------------------------------ |
| `git checkout [branch]`                      | 切换到指定分支                                               |
| `git checkout -b [new_branch`]               | 新建分支并切换到新建分支                                     |
| `git branch -d [branch`]                     | 删除指定分支                                                 |
| `git branch`                                 | 查看所有分支，并且*号标记当前所在分支                        |
| `git merge [branch]`                         | 合并分支                                                     |
| `git branch -m | -M [oldbranch] [newbranch]` | 重命名分支，如果newbranch名字分支已经存在，则需要使用-M强制重命名，否则，使用-m进行重命名。 |

- 对不关联分支的提交操作

  ```sh
  $ git push --set-upstream origin [main]	# 对不关联分支的提交
  $ git push -u origin [main]
  
  $ git ls-files	# 查看git跟踪的列表
  ```

![image-20230708192033644](https://s2.loli.net/2023/07/08/vjaJfE6NeuLsKAh.png)

### 4.5.2 分支push与pull操作

| 命令                                                    | 描述                             |
| ------------------------------------------------------- | -------------------------------- |
| `git branch -a`                                         | 查看本地与远程分支               |
| `git push origin [branch_name`]                         | 推送本地分支到远程               |
| `git push origin :[remote_branch]`                      | 删除远程分支（本地分支还在保留） |
| `git checkout -b [local_branch] origin/[remote_branch]` | 拉取远程指定分支并在本地创建分支 |

## 4.6 上传大文件

```shell
git lfs track "*.*"[files]
git add .gitattributes
git add all
……
```

# 5. 分布式Git

## 5.1 分布式工作流程

> 与传统的集中式版本控制系统（CVCS）相反，Git 的分布式特性使得开发者间的协作变得更加灵活多样。 在集中式系统中，每个开发者就像是连接在集线器上的节点，彼此的工作方式大体相像。 而在 Git 中，每个开发者同时扮演着节点和集线器的角色——也就是说， 每个开发者既可以将自己的代码贡献到其他的仓库中，同时也能维护自己的公开仓库， 让其他人可以在其基础上工作并贡献代码。

### 5.1.1 集中式工作流

> 集中式系统中通常使用的是单点协作模型——集中式工作流。 一个中心集线器，或者说 **仓库**，可以接受代码，所有人将自己的工作与之同步。 若干个开发者则作为节点，即中心仓库的消费者与中心仓库同步。

![集中式工作流](https://s2.loli.net/2023/07/08/qFDfbTMAS5iLCeY.png)

如果两个开发者从中心仓库克隆代码下来，同时作了一些修改，那么只有第一个开发者可以顺利地把数据推送回共享服务器。 第二个开发者在推送修改之前，必须先将第一个人的工作合并进来，这样才不会覆盖第一个人的修改。 

### 5.1.2 继承管理者工作流

> Git 允许多个远程仓库存在，使得这样一种工作流成为可能：每个开发者拥有自己仓库的写权限和其他所有人仓库的读权限
>
> 要为这个项目做贡献，你需要从该项目克隆出一个自己的公开仓库，然后将自己的修改推送上去。 接着你可以请求官方仓库的维护者拉取更新合并到主项目。 维护者可以将你的仓库作为远程仓库添加进来，在本地测试你的变更，将其合并入他们的分支并推送回官方仓库

![集成管理者工作流](https://s2.loli.net/2023/07/08/Pa9k3Bjt8dmyKF4.png)

- 工作方式：
  1. 项目维护者推送到主仓库。
  2. 贡献者克隆此仓库，做出修改。
  3. 贡献者将数据推送到自己的公开仓库。
  4. 贡献者给维护者发送邮件，请求拉取自己的更新。
  5. 维护者在自己本地的仓库中，将贡献者的仓库加为远程仓库并合并修改。
  6. 维护者将合并后的修改推送到主仓库。
-  GitHub 和 GitLab 等集线器式（hub-based）工具最常用的工作流程

### 5.1.3 主管与副主管工作流

> 是多仓库工作流程的变种
>
>  一般拥有数百位协作开发者的超大型项目才会用到这样的工作方式，例如著名的 Linux 内核项目。 
>
> - 被称为 **副主管（lieutenant）** 的各个集成管理者分别负责集成项目中的特定部分。 
> - 所有这些副主管头上还有一位称为 **主管（dictator）** 的总集成管理者负责统筹。 主管维护的仓库作为参考仓库，为所有协作者提供他们需要拉取的项目代码

![主管与副主管工作流](https://s2.loli.net/2023/07/08/9ZURnNwh48vtHjL.png)

- 工作流程：
  1. 普通开发者在自己的主题分支上工作，并根据 `master` 分支进行变基。 这里是主管推送的参考仓库的 `master` 分支。
  2. 副主管将普通开发者的主题分支合并到自己的 `master` 分支中。
  3. 主管将所有副主管的 `master` 分支并入自己的 `master` 分支中。
  4. 最后，主管将集成后的 `master` 分支推送到参考仓库中，以便所有其他开发者以此为基础进行变基。

- 只有当项目极为庞杂，或者需要多级别管理时，才会体现出优势。 利用这种方式，项目总负责人（即主管）可以把大量分散的集成工作委托给不同的小组负责人分别处理，然后在不同时刻将大块的代码子集统筹起来，用于之后的整合。

## 5.2 项目贡献

### 5.2.1 提交准则

1. 提交不含空白

```sh
$ git diff --check
```

2. 让每一个提交成为一个逻辑上的独立变更集
3. 在将工作发送给其他人前使用这些工具来帮助生成一个干净又易懂的历史
4.  有一个创建优质提交信息的习惯

### 5.2.2 私有小型团队

```sh
$ git fetch origin
$ git merge origin/master
$ git push origin master
```

![推送所有的改动回服务器后 Jessica 的历史](https://s2.loli.net/2023/07/08/UnjtBC1LX5S8ZWq.png)

### 5.2.3 私有管理团队

![合并了 Jessica 的两个主题分支后她的历史](https://s2.loli.net/2023/07/08/bx59Hkf8i7QraLg.png)

### 5.2.4 派生的公开项目

