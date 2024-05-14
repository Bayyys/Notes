## Linux 命令

## echo 打印字符

> - print given arguments
> - 打印给定字符

#### 基本使用

```shell
$ echo hello	# 默认带换行符
$ echo "hello"	# 引号是可选的
> hello

$ echo -n hello	# 不打印尾随的换行
> hello

$ name=bayyy
$ echo $name	# 打印变量
> bayyy

$ echo $?	# 打印上条命令执行结果
## : success
# other: failed

$ echo '$name'	# 单引号不进行解析
> $name

$ echo -e "column1\ncolumn"	# 转义字符 -e escape 启用反斜杠转义
> column1
> column2

$ echo > file.txt	# 文件清空
```

> :warning:
>
> - 反斜杠 `\` 会被认为是续行符，如果要打印此符号，需要加双引号 `""`
> - 多个空格会默认保留一个空格，如果要保留需要加双引号 `""`
> - `echo lx` 会搜索历史命令中以 `x` 开头最近的指令，并执行
>   - `$echo "hello world!"` 双引号中的感叹号 `!`，会自动匹配上述说明，因此此条命令可能会报错
> - `!!` 会执行上条命令

#### ANSI 转义序列

> - In computing, ANSI escape codes (or escape sequences) are a method using in-band signaling to control theformatting, color, and other output options on video text terminals.To encode this formatting information, certain sequences of bytes are embedded into the text,which the terminal looks for and interprets as commands, not ascharacter codes.
>
> - 在计算机系统中，ANSI转义码(或转义序列)是一种使用带内信号控制视频文本终端的格式、颜色和其他输出选项的方法。为了编码这种格式化信息，特定的字节序列被嵌入到文本中，终端将查找并将其解释为命令，而不是字符代码。

- **ANSI转义序列**

  - 是终端上通用的通信控制协议，我们可以在命令行下显示粗体、斜体、下划线字符，也可以显示不同的颜色，甚至还能显示简单的动画
  - ANSI序列是在二十世纪七十年代引入的标准，用以取代特定终端供应商的序列，并在二十世纪八十年代早期开始在计算机设备市场上广泛使用。与早期缺少光标移动功能的系统相比，新生的电子公告板系统（BBS）使用ANSI序列改进其显示。正是因为这个原因，ANSI序列变成了所有制造商共同采用的标准。

- 序列具有不同的长度

  - 所有序列都以ASCII字符**ESC**（十进制的27 ，或十六进制 0x1B，或八进制的033，或转义字符\e）开头，第二个字节则是0x40–0x5F（ASCII 的@A–Z[]^_）范围内的字符

- 除ESC之外的其他C0代码（通常是BEL，BS，CR，LF，FF，TAB，VT，SO和SI）在输出时也可能会产生与某些控制序列相似或相同的效果

  <img src="https://s2.loli.net/2023/11/06/Hz3PS6x8DlZGTyF.webp" alt="在这里插入图片描述" style="zoom:50%;" />

- 转义序列C1不完整列表

  <img src="https://s2.loli.net/2023/11/06/mcLtD86bTuGJYkX.webp" alt="在这里插入图片描述" style="zoom:50%;" />

#### SGR(Set graphics mode)

```shell
# 识别 \e[xxxm
$ echo -e "\e[xxxmhello world\e[0m"
```

![image-20231106130701983](https://s2.loli.net/2023/11/06/kq3ZvUpAWo4hwiP.png)

<img src="https://s2.loli.net/2023/11/06/FlHfavqb1kByiUt.webp" alt="在这里插入图片描述" style="zoom: 67%;" />

![在这里插入图片描述](https://s2.loli.net/2023/11/06/pKRY7AUGjBNn8xv.webp)

![image-20231106130815449](https://s2.loli.net/2023/11/06/QV93NGyWndRqCvY.png)

## cd 改变路径

> - Change the current working directory
> - 改变当前工作路径

```shell
$ cd dirname	# 进入dirname目录

$ cd test1/test2/...	# 进入深级目录

$ cd ~	# 进入当前用户的 home 目录
$ cd		# 同上

$ cd ~{{username}}	# 进入指定用户的 home 目录

$ cd /	# 进入根目录

$ cd - # 返回上次所在的目录
```

## apt 安装

> - Debian and Ubuntu package management utility.Search for packages using apt-cache
>
> > :hotsprings: apt、apt-get
> >
> > apt 命令的引入就是为了解决命令过于分散的问题，它包括了 apt-get 命令出现以来使用最广泛的功能选项，以及 apt-cache 和 apt-config 命令中很少用到的功能

```shell
$ sudo apt update	# 升级可用包及版本

$ apt seaarch {{package}}	# 搜索包

$ apt show {{package}}	# 展示包的信息

$ apt install {{package}}	# 安装

$ apt remove {{package}}	# 移除

$ apt list	# 列出安装的包

$ apt list --installed 	# 列出安装的包

$ apt reinstall {{package}}	# 重新安装

$ apt autoremove	{{package}} # 自动移除、
```

## find 递归查找

> - Find files or directories under the given directory tree, recursively
> - ==递归地==查找给定目录树下的文件或目录
>
> - `find {{root_path}} -name '{{*.ext}}'`

```shell
$ find . -name "test1.txt"
> ./test1.txt

$ find . -name "*.txt"	# 正则匹配
> ./test1.txt ./test2.txt ...

$ find . -iname "*.txt"	# 忽略大小写
> ./test1.txt ./test2.txt ./test3.TXT ...

$ find . -type f	# 按照类型查找文件 (f 普通文件 d 目录 l 链接 b 块设备 c 字符设备)

$ find . -mtime -1 # 根据修改时间查找文件
# (-mtime 天 -mmin 分钟)
# (-1 1分钟之内 +1 1分钟之外)
# (-m 修改时间 -a 访问时间 -c 变更时间)

$ find . -user root # 根据用户查找文件	(-nouser 不属于用户)
$ find . -group root  # 根据用户组查找文件	(-nogoup 不属于组)

$ find . -maxdepth 1 "test.txt" # 设置递归深度

$ find . -size +5k -size -10M	# 根据文件大小查找
	
$ find . -path "*/code/*"	# 匹配路径规则

$ find . -perm 644 # 根据权限查找

$ find . -name "*.txt" -exec cat {} \;	# 根据查找到的文件递归执行命令 ({} 指代了查找到的内容 \; 作为命令参数结束的标志)
$ find . -name "*.txt" -ok cat {} \;	# 同上，但是其会询问用户

# 其他
-mount                            #查文件时不跨越文件系统mount点
-follow                            #如果遇到符号链接文件，就跟踪链接所指的文件
-prune                            #忽略某个目录
```

> :key: 使用技巧
>
> - 多条件查找
>
>   - `-or/-o` 或
>
>   - `-not/!` 排除规则
>   - `-and/-a` 与
>
> - 可以使用 `-empty` 查找空文件
>
> - 可以使用 `-dekete` 删除查找到的文件
>
> - `-exec` 等效指令 `find . -type f | xargs cat`
>
> - 控制输出格式 `find ./ -name "*.txt" -printf "%f %a %M %s\n"`
>
>   - ```shell
>     %f	文件名
>     %a 访问时间
>     %c	修改时间
>     %M	权限信息
>     %m	权限位信息
>     %s	文件大小、以字节为单位
>     %d	文件所在目录层级
>     %u	文件所属用户
>     %p	带相对路径的完整名
>     %y	文件类型
>     ```

## mkdir 新建目录

> - Create directories and set their permissions
> - 创建目录并设置其权限

```shell
$ mkdir testdir1

$ mkdir -p t1/t2/t3	# 递归创建文件夹

$ mkdir -v testdir	# 显示创建过程
> mkdir: created directory 'testdir'

$ mkdir -m 700 testdir	# 指定权限 (700 wxr------)
```

## cp 复制

> - Copy files and directories
> - 复制文件/目录

```shell
$ cp file.txt copy,txt	# 复制 (默认覆盖)
$ cp -v ...							# -v 显示操作过程
> 'file.txt' -> 'copy.txt'

$  cp -r testdir testdir2	# -r 复制文件夹

$ cp file.txt ./testdir		# 复制到其他文件夹

$ cp -r testdir testdir2 # 将testdir文件夹整个复制到其他目录下

$  cp -t ../testdir a.txt b.txt	# 将多个文件复制到 testdir 文件夹中

$  cp -i {{*.txt}} testdir	# 以交互模式将文本文件复制到另一个位置
```

## cat 打印

> - Print and concatenate files
> - 打印并连接文件

```shell
$ cat file.txt	# 打印文件内容

$ cat -n file.txt # 显示行号
$ cat -b file.txt	# 显示行号(跳过空行)

$ cat -s file.txt # 多个连续空行合并显示

$ cat -E file.txt # 以 $ 符号显示换行符
$ cat -T file.txt	# 以 ^I 符号显示 tab
$ cat -A file.txt	# 同时实现以上两个的显示 (-E -T)

$ cat f1.txt f2.txt	# 同时输出多个文件

$ cat f1 > f2	# 将 f1 内容 覆盖 f2
$ cat f1 >> f2	# 将 f1 内容 追加到 f2
$ cat -u f1 > f2	# 不带缓冲的复制

$ cat - > file	# 以接下来连续的输入形式复制到 file 中 (exit退出)
```

## rm 删除

> - Remove files or directories
> - 删除文件或文件夹

```shell
$ rm file				# 删除文件
$ rm -r testdir	# 删除文件夹

$ rm -i file		# 删除前询问

$ rm -f file		# 强制删除

$ rm -v file		# 显示删除操作信息
```

## wc 计数

> - Count lines, words, and bytes.
> - 计算行数、字数和字节数

```shell
$ wc file	# 基本计数	(行数 单词数 字节数)
> 8 5 25 file

$ wc --lines file	# 行数 -l
$ wc --words file	# 单词数 -w
$ wc --chars file	# 字符数 -c
$ wc --bytes file # 字节数 -m
```

## tar 解压/压缩

> - Archiving utility.Often combined with a compression method, such as gzip or bzip2
> - 归档实用程序。通常与压缩方法结合使用，例如 gzip 或 bzip2

```shell
$ tar -cf target.tar files	# 将 files 打包并命名为 target.tar

$ tar -xf target.tar	# 解包

$ tar -zcf target.tar.gz files	# 使用gzip处理打包文件

$ tar -zvcf target.tar.gz files	# 列出执行过程
```

| args | 说明                                   | args    | 说明                                                         |
| ---- | -------------------------------------- | ------- | ------------------------------------------------------------ |
| -f   | 指定备份内容                           | -Z      | 通过compress处理备份文件                                     |
| -t   | 列出备份文件的内容                     | -u      | 仅置换较备份文件内的文件更新的文件                           |
| -v   | 显示指令执行过程                       | -U      | 解开压缩文件还原文件之前，先解除文件的连接                   |
| -w   | 遇到问题进行询问                       | -V      | 建立使用指定的卷册名称的备份文件                             |
| -x   | 从备份中还原                           | -W      | 写入备份文件后，确认文件正确无误                             |
| -c   | 建立新的备份文件                       | -X      | 指定范本文件，其内含有一个或多个范本样式，让ar排除符合设置条件的文件 |
| -z   | 通过gzip处理备份文件(*.tar.gz)         | -backup | 移除文件前先进行备份                                         |
| -j   | 通过bzip2处理备份文件(*.tar.bz2/.tbz2) |         |                                                              |

## zip 压缩

> - 包和压缩(存档)文件到zip文件
> - :key: 需要安装 `zip unzip`

```shell
# --- 压缩 ---
$ zip -r target.zip {{file...}}	# 压缩
$ zip -r target.zip {{file...}} -x {{e_files...}}	# 排除指定文件

$ zip -d target.zip {{d_files..}}	# 从 zip 中移除指定文件
$ zip -r -{{0-9}} target.zip {{files...}}	# 以指定压缩等级进行压缩 0<9
$ zip -r -e target.zip {{files...}} # 以指定密码打包
$ zip -r -s {{3g}} target.zip {{files}}	# 超过3GB进行划分
$ zip -sf target.zip	# 打印压缩包内容

# --- 解压缩 ---
$ unzip {{archive.zip ...}}	# 解压缩

$ unzip {{*.zip}} -d {{path}}	# 解压至指定路径

$ unzip -l {{*.zip}}	# 列出压缩包内容


$ unzip -c {{*.zip}}	# 打印压缩包内容 (文件内容也会同时打印)
$ unzip -O {{gbk}} {{path/to/archive1.zip path/to/archive2.zip ...}}	# 以指定字符集打印
$  unzip -j {{path/to/archive.zip}} {{path/to/file_in_archive1 path/to/file_in_archive2 ...}} # 从存档中提取特定文件
```

## tail / head 展示部分

> - Display the last part of a file
> - 展示文件的后部分

```shell
$ tail file.txt	# 默认展示最后10行

$ tail --lines 10 file.txt	# 指定展示最后n行	(-n)

$ tail -n +10 file.txt	# 从第n行开始打印到最后

$ tail --bytes file.txt	# 打印最后 n bytes	(-c)

$ tail --fllow file.txt			# 持续监视改文件，改变后输出改变内容 (-f)
$ tail --retry --fllow file.txt	# 如果无法访问，会尝试打开文件 (-F)
# 如果文件删除后重建，-f会自动断开，-F会重新连接并输出

$ tail --sleep-interval 60 -f file.txt	# 监视过程会每隔60s进行打印
```

```shell
$ head file.txt	# 默认打印前10行
$ head -n -10 file.txt	# 打印到倒数第n行
```

## grep 文件查找

> - Find patterns in files using regular expressions
> - 使用正则表达式查找文件中的模式串

```shell
$ grep hello file.txt	# 打印包含hello的字符串(区分大小写)

$ grep -i hello file.txt	# 模糊匹配

$ grep -w hello file.txt	# 精确匹配字符串

$ grep -e hello -e today file.txt	# 允许匹配多个

$ grep -n hello file.txt	# 匹配并打印行号

$ grep -v hello file.txt	# 打印不包含该串的文本

$ grep -r hello dir/				# 递归目录输出包含该串的文本

$ grep -lr hello dir/			# 递归输出包含该串的文件名

$ grep -E 'hello|today' file.txt	# 使用正则表达式进行匹配
```

## sed 编辑文本

> - Edit text in a scriptable manner
> - 以可编写脚本的方式编辑文本

```shell
$ sed -e '1i\a new line' file	# 在文件 file 第一行前插入 a new line, 展示最终效果(不会修改文件) [-e可以省略]
## 第一行 i 插入 \作为分割

$ sed -i '1i\a new line' file	# 执行并修改文件
$ sed -ixxx '1i\a new line' file	# 执行并修改文件，同时复制原文件, 并在文件名后添加xxx，以作备份

$ sed -e '1a\aaa' file	# 行后追加操作
$ sed -e '2d' file	# 删除操作
$ sed -e '1c\line' file	# 覆盖操作
$ sed -e '1p'	file	# 重复第一行操作
$ sed -n '2p' file	# 只打印经过编辑的内容

$ sed -e 's/old/new/' file	# 替换操作，用new替换old的内容 (可以使用正则表达式) [同一行存在多个匹配只替换第一个]
$ sed -e 's/old/new/g' file	# 全局替换

$ sed -e '1a\aaa' -e '1p' file	# 执行多个脚本
$ sed -f op.sh file	# 使用文件脚本进行打印命令
$ cat op.sh
> 1a\aaa
> 2p
```

## 管道符号

> - “|”是Linux管道命令操作符，简称管道符
> - “|”左边命令的输出就会作为“|”右边命令的输入
>   - 输出转输入

```shell
$ cat file.txt | wc -l	# 将 file.txt 文本内容作为输入传给 wc 进行行数统计

$ ls -l | less					# 显示文件，并逐页查看
```

## 输入/出重定向

> :key: *文件描述符 0 通常是标准输入（STDIN），1 是标准输出（STDOUT），2 是标准错误输出（STDERR）*
>
> - 输出重定向 `>`
> - 输入重定向 `<`

```shell
$ cat file1 > file2	# 将 file1 输出到文件 file2 (存在则覆盖)
$ catt file1 | grep hello > file2	# 查找 file1 中包含hello的行 输出到文件 file2

$ cat file1 >> file2	# 将 file1 输出追加到 file2

$ cat file1 2> file2 # 将 执行结果中的 标准错误输出 到 file2 (默认是标准输出 1>)
$ cat file1 file2 > file3 2>& 1	# 将标准错误输出(2) 绑定到标准输出(1) 同时输出结果
$ cat file1 file2 &> file3			# 同上

$ cat file1 > /etc/null				# 将结果输出 空设备，丢弃一切写入其中的数据
```

```shell
$ cat < file		# 将 file1 作为标准输入传给 cat, cat 会输出所给内容
$ cat << EOF		# 追加内容，直到遇见 EOF (该符号可自定义, 一般用EOF)
heredoc> hello
heredoc> world
heredoc> EOF
> hello
> world

$ cat > file << EOF	# 将标准输入到file, 输入直到遇见EOF
heredoc> hello
heredoc> world
heredoc> EOF
# 此时不会有输出结果，已经被重定向到file
```

## printf 格式化打印

> - Format and print text
> - 格式化和打印文本

```shell
$ name=bayyy
$ printf "$name"	# 解析并打印变量 (默认不会换行)
> bayyy%

$ printf '$name\n' # 不解析打印
> bayyy

$ printf "\e[5;31m$name\e[0m"		# 使用SGR进行美化

# %-5s   左对齐 长度5 字符串
$ printf "%-5s %2d %5d %10d\n" "BAY" "12" "13" "14" && \
> printf "%-5s %2d %5d %10d\n" "bayyy" "12" "1212" "123"	# 格式化字符串
> BAY   12    13         14
> bayyy 12  1212        123

$ print '1'	# 不会进行格式化，同时不打印换行符
```

## awk 文件处理

> - A versatile programming language for working on files
> - 一种用于处理文件的通用编程语言
> - 相关概念
>   - 每行 record 记录
>   - 每个间隔符分开 field 字段 

#### 基本使用

```shell
# --- 内置指令 ---
$ awk  []         'BEGIN{}   	//   		{}   	END{} '   	 []
## 操作  2.脚本部分 前操作  匹配规则 	循环操作 	后操作      3.文件名
$ awk -F: {print $1,$2...} file	# -F 指定分割符, 默认为空格



# --- 基本使用 ---
$ awk '{print $1}' file	# 流式读取每一行，打印第一个字段
$ awk '{print $NF}' file	# 打印最后一个字段 (以此类推 %NF-1 倒数第二个字段)

$ awk '{OFS="#";$1=$1;print $0}' file	# 流式打印一行所有字段，并以#进行分隔
# 整行输出模式下, 需要使用, $1=$1 是进行刷新分隔符替换操作, 不进行任何刷新不生效
$ awk -v OFS="#" '{$1=$1;print $0}' file	# 同上, -v赋值一个用户定义变量
$ awk -v '{OFS="#";print $1,$2,$3,$4}' file	 # 同上
$ awk 'BEGIN{OFS="#"} {print $1,$2,$3,$4}' file	# 同上

$ awk '{printf "%-5s %3d %5d %10d\n",$1,$2,$3,$4}' 1.txt
> bayyy 111    12  546153165
> BAY     1    19          1
> C      12  4516     451456

$ awk '{if(NR==3){print $0} else {print "不是第三行"}}' 1.txt	# 可以使用函数
> 不是第三行
> 不是第三行
> C 12 4516 451456
$ awk 'NR==3{print $0}' 1.txt	# 直接进行模式的设置 (第三行数据)
$ awk 'NR==1||NR==3{print $0}' 1.txt	# 第一和第三行

# --- 内置函数 ---
$ awk '/ba/ {print index($1, "y")}' 1.txt	# 查找字符的索引位置 index
$ awk '{print length($1)}' 1.txt					# 长度 length

# --- BEGIN/END ---
$ awk 'BEGIN{x=0} {x++} END{print x}' 1.txt	# 记录行数
$ awk 'BEGIN{x=0} /ba/ {x++} END{print x}' 1.txt	# 统计以ba开头的行数

# --- 脚本文件 ---
$ awk -f awk.sh file
```

```sh
# awk.sh
BEGIN{
        printf "----- start awk -----\n"
        printf "%2s %2s %2s %2s %2s\n","姓名","语文","数学","英语","总分"
}

{
        total=0
        i=2
        while(i<=NF){
                total+=$i
                i++
        }
        printf "%-4s %-4d %-4d %-4d %-4d\n",$1,$2,$3,$4,total
        if(total>max){
                max=total
        }
}

END{
        printf "最高分为: %-4d\n",max
}
```

#### 内置变量

| 变量        | 描述                                                  |
| ----------- | ----------------------------------------------------- |
| $n          | **当前记录的第n个字段，字段间由FS分隔**               |
| $0          | **完整的输入记录**                                    |
| ARGC        | 命令行参数的数目                                      |
| ARGIND      | 命令行中当前文件的位置(从0开始算)                     |
| ARGV        | 包含命令行参数的数组                                  |
| CONVFMT     | **数字转换格式**(默认值为%.6g)ENVIRON环境变量关联数组 |
| ERRNO       | 最后一个系统错误的描述                                |
| FIELDWIDTHS | 字段宽度列表(用空格键分隔)                            |
| FILENAME    | **当前文件名**                                        |
| FNR         | 各文件分别计数的行号                                  |
| **FS**      | **字段分隔符(默认是任何空格)**                        |
| IGNORECASE  | 如果为真，则进行忽略大小写的匹配                      |
| NF          | 一条记录的字段的数目                                  |
| NR          | 已经读出的记录数，就是行号，从1开始                   |
| OFMT        | **数字的输出格式(默认值是%.6g)**                      |
| **OFS**     | **输出字段分隔符，默认值与输入字段分隔符一致。**      |
| **ORS**     | **输出记录分隔符(默认值是一个换行符)**                |
| RLENGTH     | 由match函数所匹配的字符串的长度                       |
| **RS**      | **记录分隔符(默认是一个换行符)**                      |
| RSTART      | 由match函数所匹配的字符串的第一个位置                 |
| SUBSEP      | 数组下标分隔符(默认值是/034)                          |

#### 选项参数

| 参数                                                     | 说明                                                         |
| -------------------------------------------------------- | ------------------------------------------------------------ |
| `-F --field-separator`                                   | 指定输入文件折分隔符，一个字符串或者是一个正则表达式(默认以空格作为分隔符) |
| `-v --asign`                                             | 用户定义变量赋值                                             |
| `-f --file`                                              | 脚本文件中读取awk命令                                        |
| `-W compat --compat`<br />`-W tradtional --tradtional`   | compact 兼容模式；traditional 传统模式                       |
| `-W copyleft --copyleft`<br />`-W copyright --copyright` | copyleft copyright 版权信息                                  |
| `-W helo --help`<br />`-W usage --usage`                 | help usage 全部选项或每个选项的简短说明                      |

#### 处理规则

| 规则    | 说明                           |
| ------- | ------------------------------ |
| BEGIN{} | 文本处理之前运行               |
| / /     | 使用的匹配规则                 |
| {}      | 循环(每次只处理一行数据)       |
| END{}   | 全部执行完毕后，执行的相关操作 |

## touch 创建

> - Create files and set access/modification times
> - 创建文件并设置访问/修改时间

```shell
$ touch file1 file2	# 创建空文件

$ touch -c file	# 修改访问/修改时间为最新, 如果文件不存在也不会重新创建

$ touch -a|-m -d 20080101 file	# 修改访问/修改时间, 不会改变 Change/Birth 属性
# 如果不加 -a|-m 则均会被修改

$ touch [-a|-m] -t 200801011200.00 file	# 以固定格式进行修改 YYYYMMDDHHMM.SS

$ touch -r ref_file file	# 以 ref_file 参考修改 file
```

## stat 状态

> - Display file and filesystem information
> - 显示文件和文件系统信息

```shell
$ stat file.txt
File: file.txt
Size: 12              Blocks: 8          IO Block: 4096   regular file
Device: 820h/2080d      Inode: 29637       Links: 1
Access: (0644/-rw-r--r--)  Uid: ( 1000/   bayyy)   Gid: ( 1000/   bayyy)
Access: 2023-11-07 17:10:12.948666601 +0800
Modify: 2023-11-07 17:11:53.868629243 +0800
Change: 2023-11-07 17:11:53.868629243 +0800
Birth: 2023-11-07 17:09:40.158676218 +0800

$ stat --terse(-t) file.txt	# 不显示label 以简洁的形式打印信息
file.txt 12 8 81a4 1000 1000 820 29637 1 0 0 1699348212 1699348313 1699348313 1699348180 4096

$ stat --file-system(-f) file.txt	# 显显示文件系统状态，而不是文件状态
File: "1.txt"
ID: 59b42ad3d70d1f0d Namelen: 255     Type: ext2/ext3
Block size: 4096       Fundamental block size: 4096
Blocks: Total: 263940717  Free: 263510537  Available: 250084669
Inodes: Total: 67108864   Free: 67060321

$ stat --format(-c)="%a %n" file.txt	# 使用指定的格式 权限+文件名
> 644 file.txt
# %a 权限 %n 文件名 %U 拥有者 %G 组 %s 文件大小
# 也可以使用 --printf=FORMAT
# 类似于——format，但解释反斜杠转义，并且不输出强制的尾随换行符
```

## xargs 输入转参数

> - Execute a command with piped arguments coming from another command, a file, etc.The input is treated as a single block of text and split into separate pieces on spaces, tabs, newlines and end-of-file
> - 执行带有来自另一个命令(文件等)的管道参数的命令。输入被视为单个文本块，并在空格、制表符、换行符和文件结束符上分割成不同的部分
>   - ==捕获一个命令的输出，然后传递给另外一个命令==
>   - 将标准输入转化为参数
>   - 某些命令不接受标准输入，只接受参数 (echo touch rm...)

```shell
# --- 基本格式 ---
$ xargs [OPTION]... COMMAND [INITIAL-ARGS]...

# --- 基本参数 ---
$ echo hello | xargs echo	# 将 echo 的输出通过 管道符号 转为输入, 再通过 xargs 转化为参数， 使用echo输出
$ echo hello | xargs 			# 同上, xargs 默认命令为 echo
> hello

$ echo "hello world" | xargs -n1	# 每次只操作一个argument -n
> hello
> world

$ echo "hello world" | xargs -d o	# 设置分隔符 -d
hell  w rld

$ echo -n "hello world" | xargs -d o -p -n 1	# 运行前询问 -p
echo hell?...y
> hell
echo ' w'?...y
> w
echo rld?...y
> rld

$  echo -n "hello world" | xargs -t -n 1	# 运行前打印commond

$ echo | xargs -r echo	# 空参数则不执行 -r

# --- 使用技巧 ---
$ cat file.txt | xargs	# 将文本转化到一行(\会被认为是保护字符)

$ echo "1 2 3 4 5 6" | xargs -I {} touch {}.txt	# 批量创建文件
```

- 参数 ` xargs [OPTION]... COMMAND [INITIAL-ARGS]...`

| 参数                       | 说明                                                         |
| -------------------------- | ------------------------------------------------------------ |
| `-a/--arg-file=FILE`       | 从文件中读入作为 stdin                                       |
| `-e/-eof flag`             | 设置逻辑EOF字符串                                            |
| `-o/--open-tty`            | 在执行命令之前，在子进程中将stdin重新打开为/dev/tty;用于运行交互式应用程序 |
| `-p/--interactive`         | 当每次执行一个argument的时候询问一次用户                     |
| `-n/--max-args=MAX-ARGS`   | 表示命令在执行的时候一次用的argument的个数，默认是用所有的   |
| `-t/--verbose`             | 在执行命令之前打印命令                                       |
| `-i/-I/--replace[=R]`      | 将INITIAL-ARGS中的R替换为从标准输入读取的名称，以换行符分隔;如果R未指定，则假定{} |
| `-r no-run-if-empty`       | 当xargs的输入为空的时候则停止xargs，不用再去执行了(不指定时，即使为空也会执行至少一次) |
| `-s/--max-chars=MAX-CHARS` | 命令行的最大字符数，指的是 xargs 后面那个命令的最大命令行字符数 |
| `-L/--max-lines=MAX-LINES` | 从标准输入一次读取 num 行送给 command 命令                   |
| `-l[MAX-LINES]`            | 同上                                                         |
| `-d/--delimiter delim`     | 分隔符，默认的xargs分隔符是回车，argument的分隔符是空格，这里修改的是xargs的分隔符 |
| `-x/--exit`                | 如果超出大小(参见-s)，退出                                   |
| `-P/--max-procs=MAX-PROCS` | 行运行最多进程数(默认为1，如果为0则使用尽可能多的进程)       |
| `-0/--null`                | 项之间用空分隔，而不是空白                                   |

## ls 目录内容

> - List directory contents
> - 列出目录内容

```shell
$ ls	# 简短形式列出

$ ls -a	# 包含隐藏文件

$ ls -A # 不包含 . ..

$ ls -l	# 列出较详细信息 类型 权限 链接数 所有者 所有组 大小 修改时间 文件名
> -rw-r--r-- 1 bayyy bayyy   21 Nov  7 21:36 file.txt

$ ls -R # 递归形式列出
.:
file.txt  history

./history:
awk

./history/awk:
1.txt  awk.sh

$ ls -S	# 排序(-S 大小 -t 修改时间 -v 版本 -X 扩展名 -u 访问时间 -c 修改时间)

$ ls -i # 显示文件的 inode

$ ls -Z	# 查看上下文 -Z/--context
```

## du 文件尺寸

> - 磁盘使用情况:估计和汇总文件和目录的空间使用情况

```shell
$ du -{{b|k|m}} {{path}}	# 以指定单位列出文件及目录尺寸
$ du -h {{path}}	# 以易读形式

$ du -sh {{path}}	# 列出单个指定内容, 不进行递归
$ du -sh *				# 当前目录
4.0K 1.txt
12K d.tar
4.0K d.tar.gz
4.0K d.zip
24K d1
40K history
4.0K test.txt

$ du -ah {{path}}	# 递归展示

$ du -h --max-depth=N {{path}}	# 指定递归层数

$ du -ch {{*/*.jpg}}	# 在一级目录下的*.jpg文件
```

## 常用快捷键

- 上下键	历史记录(根据已有输入搜索)

- Ctrl-A/Ctrl-E  移至行首/行尾
- Ctrl-W   删除单词
- Ctrl-U    光标前删除
- Ctrl-K    光标前删除
- Ctrl-Y     复制删除内容
- Ctrl-L    清屏
- Ctrl-R    搜索命令

## ln 链接

> - Creates links to files and directories
> - 创建到文件和目录的链接

```shell
# --- 基本语法 ---
$ ln [OPTION]... TARGET... DIRECTORY

$ ln file.txt tlink	# 创建 file.txt 的硬链接 tlink (对应inode为同一个, 删除后硬链接仍旧可以使用)
$ ln -s file.txt slink	# 创建 file.txt 的软链接 slink (对应inode不同, 删除后找不到源文件)
$ ls -il
33172 -rw-r--r-- 2 bayyy bayyy   21 Nov  7 21:36 file.txt
  851 lrwxrwxrwx 1 bayyy bayyy    8 Nov  8 15:32 slink -> file.txt
33172 -rw-r--r-- 2 bayyy bayyy   21 Nov  7 21:36 tlink

$ ln file.txt ./testdir/hardlink	# 在其他目录下创建硬链接
```

## pwd 路径

> - Print name of current/working directory
> - 打印当前/工作路径

```shell
$ pwd		# 打印当前路径

$ pwd -L	# 打印当前逻辑路径，不解析符号链接 (默认)
$ pwd -P	# 打印当前目录，并解析所有符号链接(即显示“物理”路径):
```

## mv 移动

> - Move or rename files and directories
> - 移动或重命名文件和目录

```shell
# --- 基本指令 ---
$ mv [OPTION]... SOURCE... DIRECTORY

$ mv file.txt testdir	# 移动
$ mv file.txt testdir/new.txt	# 移动并重命名
$ mv file.txt new.txt	# 重命名

$ mv -v file.txt testdir/new.txt	# 移动、重命名并显示过程	-v/--verbose
> renamed './file.txt' -> 'testdir/file.txt'

$ mv -vb file.txt testdir	# 存在同名则进行备份 (结尾加~)	-b/--backup[=CONTROL] 注: -b默认~,且无法修改控制符, --backup可以修改控制类型 
# none, off			不进行备份, 及时加--backup
# numbered, t		数字备份 ,~1~
# existing, nil	当数字备份存在时以数字, 否则以简单模式
# simple, never	以简单类型备份 ~


renamed 'file.txt' -> 'testdir/file.txt' (backup: 'testdir/file.txt~')
$ mv -vf file.txt testdir	# 存在同名则直接覆盖	-f/--force

$ mv -fiv file.txt testdir/file.txt	# 如果要覆盖则提醒	-i/--interactive
mv: overwrite 'testdir/file.txt'? n

$ mv -nv file.txt testdir/file.txt	# 如果同名则不进行覆盖, 直接跳过 -n/--no-clobber

$ mv -t testdir 1.txt 2.txt...	# 移动所有文件到目录中 -t/--target-directory=DIRECTORY

$ mv -u file.txt new.txt			# 仅在比目标文件更新或者目标不存在时复制 -u/--update
```

## 用户及权限

#### 用户

- root用户、系统用户、普通用户

  - `/etc/passwd`

  - ![image-20231108160330084](https://s2.loli.net/2023/11/08/hPlFEt5Q7SY4Ric.png)

  - ```shell
    # bayyy : x : 1000 : 1000 :,,,:    /home/bayyy:  /bin/zsh
    # 用户名   密码  uid    gid  用户描述    home目录      shell
    ```

  - 密码

    - ` /etc/shadow` (需要管理员权限)

    - ```shell
      # bayyy:xxx:19667:0:99999:7:::
      # 用户 密码 创建时间戳 时间间隔 有效天数 失效前提醒天数 过期后准许使用天数 失效日期 保留字段
      #     */!! 代表未设置密码
      ```

- 登录默认配置项 ` /etc/login.defs`

- 新建用户默认配置项 `/etc/default/useradd`

#### 组

- 组信息

  - `/ect/group`

  - ```shell
    # bayyy:x:1000:
    # 用户 密码 id 其他成员
    ```

  - 密码

    - `/etc/gshadow`

    - ```shell
      # bayyy:!::
      # 用户 密码 组管理员 组成员
      ```

#### 权限

```shell
# d   r w x r - x r - x 
# 类型 d读 w写 x执行
#       用户 组 其他
```

#### useradd 新增用户

> :key: useradd 和 adduser 类型 一般`useradd`，对其进行更好的封装

```shell
$ useradd test1	# 新建用户
$ cat /etc/passwd | grep test1
> test1:x:1001:1001::/home/test1:/bin/sh

$ passwd test1	# 设置密码 
> New password:
> Retype new password:
> passwd: password updated successfully

# --- 设置加密密码 ---
$ useradd -p '$1$bTPcgJ/u$tYW2GPSNNbyv22NYR8FsP0' test2	# -p设置密码 (需要是加密后的算法, 并且因为系统默认是md5, 所以使用md5进行加密)
$ openssl passwd -1 '123456'	# -1 指定md5
$ cat /ect/shadow | grep test2
> test2:$1$bTPcgJ/u$tYW2GPSNNbyv22NYR8FsP0:19669:0:99999:7:::

$ useradd -b /tmp test3	# 修改基础目录	(/tmp/test3)
$ useradd -d /tmp/tt4	test4	# 修改home目录 (/tmp/tt4)

$ useradd -c '测试用户' test5	# 描述信息

$ useradd -G root,root1 test6	# 增加附属组	-G/--groups

$ useradd -s /bin/sh test7	# 修改命令行	-s/--shell

$ useradd -u 753 test	# 修改uid

$ useradd -D	# 查看默认信息
> GROUP=100
> HOME=/home
> INACTIVE=-1
> EXPIRE=
> SHELL=/bin/sh
> SKEL=/etc/skel
> CREATE_MAIL_SPOOL=no
$ useradd -D -b /temp	# 修改默认信息 -b HOME -s /bin/sh...

$ useradd -r test8	# 创建系统用户 -r/--system
```

#### usermod 修改用户

```shell
$ usermod -c '测试用户' test	# 修改描述信息

$ usermod -G group1 test	# 将test所属附属组改为group1(原信息清空, 覆盖操作)
$ usermod -aG group2,group3 test	# 增加附属组 (保留原附属组信息)

$ usermod -l newname test	# 用户重命名

$ usermod -L test	# 用户锁定
$ usermod -U test	# 用户解锁

$ usermod -p 123456 test	# 修改密码
```

#### userdel 删除用户

```shell
$ userdel test	# 删除用户 (但是不会删除 home目录及 mail目录)
$ userdel -r test	# 完全删除 (组内包含其他成员则不会删除)
```

#### 组管理

```shell
# --- 新增 ---
$ groupadd test
$ group -g 1010 test	# 指定组id

# --- 修改 ---
$ groupmod -g 1111 test	# 修改组id
$ groupmod -n newname test	# 修改组名

# --- 删除 ---
$ groupdel test
```

## chown 修改用户/组

> - Change user and group ownership of files and directories
> - 更改文件和目录的用户和组所有权

```shell
$ chown user file	# 修改文件所属用户
$ chown :group file	# 修改文件所属组
$ chown user:group file	# 同时修改

$ chown -R user testdir/	# 递归遍历文件夹修改用户或组

$ chown -h user file	# 修改符号链接的用户或组
```

## chmod 修改权限

> - Change the access permissions of a file or directory
> - 修改文件或目录的权限

- 用户
  - u 文件所有者
  - g 文件所有者同组
  - o 其他用户
- 权限
  - r 读 4
  - w 写 2
  - x 执行 1

```shell
# --- 基本使用 ---
$ chmod [OPTION]... MODE[,MODE]... FILE...

$ chmod 760 file	# 修改权限 rwxrw----
$ chmod g+wx file	# 组 增加权限
$ chmod o-rwx file	# 其他用户 移除读写执行权限
$ chmod a-w file	# 修改所有对象 的写权限

$ chmod -R 760 testdir/	# 递归文件夹, 修改权限 -R/--recursive

$ chmod -cR 760 testdir/	# 权限发生变化, 打印执行结果
$ chmod -vR 760 testdir/	# 打印执行效果 (权限未改变也会变化)
```

## su 切换用户

> - Switch shell to another user
> - 将shell切换到其他用户

```shell
$ su user	# 切换用户

$ su			# 切换到root

$ su -c {{commond}} user	# 以指定用户执行该命令

$ su -l user	# 登录 user 用户，且切换到其shell -l/-/--login

$ sudo -k	# 使sudo有效期单词后过期
$ sudo -v # 延长有效期
$ sudo -u bayyy ls	# 指定用户执行sudo命令
```

## hostname 临时操作用户名

> - Show or set the system's host name
> - 显示或设置系统的主机名

```shell
$ hostname	# 显示用户名
$ hostname newname	# 设置临时用户名 (reboot 后恢复)

$ cat /etc/hostname	# 用户名位置
> bayyy

$ hostname -i	# 显示网络地址
$ hostname -I	# 显示host网络地址
$ hostname --fqdn	# 显示全称域名

$ hostnamectl set-hostname newname	# 永久修改用户名
```

## hostnamectl 永久操作主机名

> - Query or change system hostname
> - 查询或修改系统主机名

```shell
$ hostnamectl			# 查看用户信息
 Static hostname: bayyy
       Icon name: computer-container
         Chassis: container
      Machine ID: 37691082dc0040319785f18abea4c01b
         Boot ID: c528066922374ad78be434881170b83a
  Virtualization: wsl
Operating System: Ubuntu 22.04.3 LTS
          Kernel: Linux 5.15.90.1-microsoft-standard-WSL2
    Architecture: x86-64

$ hostnamectl status		# 内容命令
# status	当前用户设置
# hostname [NAME]	系统用户名 (获取/设置)
# icon-name	[NAME]	icon 名
# chassis	[NAME]	chassis类型
# deployment [NAME] 部署环境
# location [NAME] 位置
    
$ sudo hostnamectl set-hostname "{{hostname}}"	# 永久修改主机名
# 修改后可用 bash/zsh 进行刷新

$ sudo hostnamectl set-hostname --static "{{hostname.example.com}}" && sudo hostnamectl set-hostname --pretty "{{hostname}}"	# 设置 static及pretty主机名

$ sudo hostnamectl set-hostname --pretty ""	# 恢复默认设置
```

## who 登录信息

> - Display who is logged in and related data (processes, boot time)
> - 显示登录者和相关数据(进程、引导时间)

```shell
$ who	# 展示用户名 操作命令 以及最近一次登录时间
> bayyy    pts/1        2023-11-09 09:52

$ who -a # 展示所有信息 -a/--all
>            system boot  2023-11-09 09:52
>            run-level 5  2023-11-09 09:52
> LOGIN      tty1         2023-11-09 09:52               223 id=tty1
> LOGIN      console      2023-11-09 09:52               220 id=cons
> bayyy    - pts/1        2023-11-09 09:52 10:54         386
>            pts/3        2023-11-09 12:24              3524 id=ts/3  term=0 exit=0

$ who -H	# 展示题头	-H/--heading
> NAME     LINE         TIME             COMMENT
> bayyy    pts/1        2023-11-09 09:52

$ who -q	# 所有用户名+用户计数	-q/--count
> bayyy
> #  users=1
```

## w 登录信息

> - Show who is logged on and what they are doing.Print user login, TTY, remote host, login time, idle time, current process
> - 显示谁登录了，他们在做什么。打印用户登录，TTY，远程主机，登录时间，空闲时间，当前进程
>
> > :key: TTY (显示终端机连接标准输入设备的文件名称) (Teletype 或 Teletypewriter)
> >
> > - 泛指计算机的终端(terminal)设备

```shell
$ w
>  21:05:55 up 11:13,  1 user,  load average: 0.08, 0.02, 0.01
> USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
> bayyy    pts/1    -                09:52   11:13m  0.06s  0.06s -zsh

$ w -h	# 不展示表头
> bayyy    pts/1    -                09:52   11:14m  0.06s  0.06s -zsh
```

## id 用户及组标识

> - Display current user and group identity
> - 显示当前用户和组标识

```shell
$ id
> uid=1000(bayyy) gid=1000(bayyy) groups=1000(bayyy)

$ id -u	# 用户信息

$ id -g	# 用户组标识

$ id {{username}}	# 展示指定用户内容
```

## alias 别名

> - Creates aliases -- words that are replaced by a command string.Aliases expire with the current shell session unless defined in the shell's configuration file, e.g. ~/.bashrc
> - 创建别名——由命令字符串替换的单词。除非在shell的配置文件中定义了别名，否则别名会在当前shell会话中过期，例如~/.bashrc

```shell
$ alias		# 查看所有设置的别名

$ alias {{word}}="{{command}}"	# 设置别名

$ alias {{word}}		# 查看该条别名对应的命令

$ unalias {{word}}	# 取消别名
```

## cut 截取

> - Cut out fields from stdin or files
> - 从标准输入或文件中删除字段

```shell
# cut OPTION... [FILE]...

$ cut -b 1 file		# 截取字节	-b/--bytes=LIST
$ cut -b 1- file	# 截取从第一个字符开始到最后
$ cut -b -5	file	# 截取直到第5个字符
$ cut -b 1,3,5	file	# 截取指定字节数
$ cut -b 1-5	file	# 截取字节范围

$ cut -c 1 file		# 截取字符 	-c/--characters=LIST

$ cut -d , -f 1 file	# 将tab分隔符替换为其他 -d/--delimiter=DELTM (只能为单字符)
											# 按照字段分割 -f/--fields=LIST
											
$ cut -f 1 -s file		# 忽略不包含分隔符的行	-s/--only-delimiterd
$ cut -d " " -f 1- -s --output-delimiterd	file	# 指定输出分隔符 --output-delimiterd

$  cut -d " " -f 1 -s --complement file.txt	# 输出内容的补集 --complement

$ cat /etc/passwd | grep bayyy | cut -d ":" -f -2 --output-delimiter="&&"	# 结合管道符使用
```

## tr 标准输入转换

> - Translate, squeeze, and/or delete characters from standard input,
>   writing to standard output
> - 从标准输入中翻译、压缩和/或删除字符， 写入标准输出

```shell
# tr [OPTION]... SET1 [SET2]

$  echo 'abcabc' | tr 'a' 'z'
> zbczbc

$ echo 'abcabc' | tr 'ab' 'z'	# tr 为单字符匹配 (此条分别将a和b替换成z)
> zzczzc

$ echo 'abcabc' | tr -t 'ab' 'z'	# 指定匹配对应 (a替换z， b未指定)
> zbczbc -t/--truncate-set1

$ echo 'abcabc123' | tr -d '0-9'	# 删除 -d/--delete
> abcabc
$ echo 'abcabc123' | tr -cd '0-9'	# 反选 -c/-C/--complement

$ echo 'aaabbbccc' | tr -s 'a'		# 重复压缩 -s/--squeeze-repeats
> abc

$ echo 'abc\nabc' | tr '\n' '\t'	# 替换转义字符
> abc     abc     %
> 123%

$ echo 'abc\nabc' | tr 'a-z' 'A-Z'	# 集合替换
> ABCABC

$ echo 'abcabc' | tr '[:lower:]' '[:upper:]'	# 小写替换为大写
# [:alnum:]	字符和数字   [:aplha:] 字符   [:blank:] 空字符
# [:cntrl:] 控制字符     [:digit:] 数字   [:print:] 所有打印字符, 不包括space
# [:punct:]	标点符号		 [:space:] 空字符 	[:upper:] 大写
# [:xdigit:] 16进制数字  [=CHAR=] 所有与CHAR等价的字符
```

## sort 排序

> - Sort lines of text files
> - 对文本文件行进行排序
>   - 如果未指定文件, 则对标准输入进行排序

```shell
# sort [OPTION]... [FILE]...

$ sort file	# 文件排序 (首字符, 字典序升序)

$ sort -r file	# 降序 -r/--reverse

$ sort -t ":" -k 3 file	# 指定分隔符 :  (默认 space) -t/--field-separator=SEP
												# 按照第三列进行排序 (默认第一列) -k/--key=KEYDEF

$ sort -n file	# 按照数值大小排序	-n/--numeric-sort

$ sort -h file	# 可以对单位进行归一 -h/--human-numeric-sort

$ sort file -o output.txt	# 指定文件输出 -o/--output=FILE

$ sort file -u 			# 重复行去重 -u/--unique

$ sort -c file			# 检查是否完成排序 (否: 则输出导致非排序的第一行) -c/--check
> sort: file:3: disorder: 3
$ sort -C file			# 不进行输出, 可以根据退出状态码判断
```

## uniq 去重

> - Output the unique lines from the given input or file.Since it does not detect repeated lines unless they are adjacent, we need to sort them first
> - 输出来自给定输入或文件的唯一行。因为它不会检测到重复的行，除非它们是相邻的，所以我们需要先对它们进行排序

```shell
$ uniq file	# 去重 (仅操作相邻行重复项, 不改变源文件)
$ uniq file file2	# 保存文件

$ uniq -c file	# 统计重复次数	-c/--count
$ uniq -d file	# 仅打印重复项  -d/--repeated
$ uniq -D file	# 打印重复项(所有重复项, 重复几次打印几次) -D
$ uniq -u file	# 仅打印非重复项 -u/--uniq

$ uniq -i file	# 忽略大小写	-i/--ignore-case

$ uniq -f 1 file	# 指定跳过字段进行查重 (跳过第一个字段, 默认space分隔) -f/--skip-fields=N
$ uniq -s 1 file	# 跳过字符查重	-s/--skip-chars=N
$ uniq -w 1 file	# 按照第1个字符查重 -w/--check-chars=N
```

## watch 监控

> - Execute a program periodically, showing output fullscreen
> - 周期性执行程序，全屏显示输出

```shell
# watch [OPTION] command

$ watch 'tail file'	# 监视文件变化

$ watch -d 'tail file'	# 高亮单次变化内容	-d/--differences[=<permanent>]

$ watch -t 'tail file'	# 关闭 header -t/--no-title

$ watch -n 5 'tail file'	# 秒数间隔时间 -n/--interval <secs>

$ watch -g 'tail file'	# 监测到变化后退出 -g/--chgexit

$ watch -e 'tail file'	# 监测到错误时, 按任意键退出 -e/--errexit
```

- 测试结果：<img src="C:/Users/bayyy/AppData/Roaming/Typora/typora-user-images/image-20231109105528132.png" alt="image-20231109105528132" style="zoom:33%;" />

## top 进程

> - Display dynamic real-time information about running processes.
> - 显示运行进程的动态实时信息

#### 默认窗口

![image-20231109111834316](https://s2.loli.net/2023/11/09/ZtXgwnCPBDF5bmV.png)

```shell
# 负载均衡
运行指令 当前时间   已运行时间  登录用户数    平均负载    1min 10min 15min
 top - 11:03:29 up  1:11,  1 user,  load average: 0.00, 0.00, 0.00
 
# task.cpu
进程数    总进程数       运行         睡眠          停止           僵尸进程
Tasks:  38 total,   1 running,  36 sleeping,   1 stopped,   0 zombie
cpu信息    没有修改过   内核态进程   修改过nice值			idle			等待io操作		硬件中断    软中断		  虚拟化层调用虚拟机

以%为单位		用户态的							 即修改过优先级		空闲占比		的进程
					优先级进程							 的用户态进程
%Cpu(s):   0.0 us,    0.0 sy,    0.0 ni,       100.0 id,  0.0 wa,      0.0 hi,   0.0 si,    0.0 st

# 内存信息
物理内存信息     总量             空闲             使用中          用作缓存的内存总量
MiB Mem :   7791.1 total,   6875.0 free,    496.4 used,    419.7 buff/cache

虚拟内存																												可用内存总量
MiB Swap:   2048.0 total,   2048.0 free,      0.0 used.   7064.4 avail Mem


  PID		有效用户	优先级			虚拟内存				共享内存        CPU使用时间占比      物理内存   总使用CPU时间      命令
  			用户名				 NICE值				驻留内存		    状态   (从上次统计至今)
    PID USER      PR  NI    VIRT    RES    SHR     S          %CPU         %MEM     TIME+            COMMAND
    460 root      20   0   44208  37636  10136     S           0.3          0.5   0:04.89            python3
      1 root      20   0  165732  11060   8196     S           0.0          0.1   0:00.35            systemd
      2 root      20   0    2324   1260   1148     S           0.0          0.0   0:00.00            init-systemd(Ub
      5 root      20   0    2352     68     68     S           0.0          0.0   0:00.01            init
     40 root      19  -1   47736  14912  13900     S           0.0          0.2   0:00.09            systemd-journal
     60 root      20   0   21960   5740   4272     S           0.0          0.1   0:00.12            systemd-udevd
```

#### 指令

- x 高亮排序项
- b 显示当前指令

- g 跳转窗口
  1. 默认窗口 (%CPU排序)
  2. job窗口 (PID排序)
  3. MEM窗口 (%MEM排序)
  4. USER窗口 (USER排序)
- A 更改交互模式
  - a/w 其他换下一个窗口
  - -/_ 显示/隐藏 (-当前，_其余全部)
  - i  更改尺寸 (默认/只一行 切换)
  - n 更改尺寸 (输入显示行数)
    - = 当前窗口
    - \+ 所有窗口
  - ![image-20231109111936223](https://s2.loli.net/2023/11/09/TJdMbvy2gISprP8.png)

#### help文档

```shell
# 交互模式的文档 版本
Help for Interactive Commands - procps-ng 3.3.17

# 当前窗口     累计模式状态(默认关闭)       刷新间隔								 安全模式状态(默认关闭)
Window 1:Def: Cumulative mode Off.  System: Delay 3.0 secs;    Secure mode Off.

  Z,B,E,e   Global: 'Z' 颜色配置;
  									'B' 加粗;
  									'E'/'e' 总览/任务列表 单位(k,m,g,t,p,e)
  
  l,t,m,I   Toggle: 'l' 负载均衡(SUMMARY中首行);
  									't' 任务/cpu(轮询切换);
  									'm' 内存信息(轮询切换);
  									'I' Irix模式(使用率显示效果: 默认会除以总数)
  
  0,1,2,3,4 Toggle: '0' 0值是否显示;
  									'1/2/3' cpu/numa节点 显示;
  									'4' cpus 两行显示
  									
  f,F,X     Fields: 'f'/'F' 配置字段管理面板;
  									'X' 增加固定宽度(8+n) [-1默认, 0auto]

  L,&,<,> . Locate: 'L'/'&' 寻找; 移动:
  									'<'/'>' left/right 排序字段
  									
  R,H,J,C . Toggle: 'R' 更改排序方式(升序降序)
  								'H' 进程/线程
  								'J' 数字对齐方式
  								'C' Coordinates
  								
  c,i,S,j . Toggle: 'c' command 目录显示内容 名称/完整命令;
  									'i' 是否显示从上次更新到现在没有更新的任务
  									'S' 累积模式开关
  									'j' 字符字段的对齐方式
  									
  x,y     . Toggle highlights: 'x' 排序字段高亮显示开关;
  															'y' 运行任务高亮显示开关
  															
  z,b     . Toggle: 'z' 颜色显示开关;
  									'b' 粗体显示开关 (only if 'x' or 'y')
  									
  u,U,o,O . Filter by: 'u'/'U' 展示用户;
  											'o'/'O' other criteria
  											
  n,#,^O  . Set: 'n'/'#' max tasks displayed; Show: Ctrl+'O' other filter(s)
  
  V,v     . Toggle: 'V' 森林视图
  									'v' 显示/隐藏子节点

  k,r       Manipulate tasks: 'k' kill; 'r' renice
  d or s    Set update interval
  W,Y,!     Write config file 'W'; Inspect other output 'Y'; Combine Cpus '!'
  q         Quit
          ( commands shown with '.' require a visible task display window )
Press 'h' or '?' for help with Windows,
Type 'q' or <Esc> to continue
```

##### 颜色配置

<img src="https://s2.loli.net/2023/11/09/OJKI4QrgBcyEjPf.png" alt="image-20231109115233956" style="zoom:50%;" />

```shell
基本设置: 'B': 全局是否加粗显示 'z': 彩色/单色显示  'b': 任务列表加粗

1) 区域选择: 'S' 总结区域	'M' 信息区	'H' 标题区 'T' 任务信息
2) 颜色 单独设置某区域颜色
3) 退出及切换
		q: 退出
		a/w: 提交和改变
		ENTER: 提交和退出
```

## man 命令手册

> - Format and display manual pages
> - 格式化和显示手册页

```shell
$ man {{command}}	# 展示命令手册

$ man {{7}} {{commond}}	# 展示命令手册第7章

$ man -f {{command}}	# 展示命令的可展示章节

$ man --path	# man的目录

$ man -w {{command}}	# 展示命令的位置

$ man -s "{{STRING}}"	# 根据字符串内容搜索命令
```

## free 内存信息

> - Display amount of free and used memory in the system
> - 显示系统中空闲和已使用内存的数量

```shell
$ free	# 展示系统内存
>                total        used        free      shared  buff/cache   available
> Mem:         7978092      534608     6740200        3204      703284     7200004
> Swap:        2097152           0     2097152

$ free -{{b|k|m|g}}	# 以某单位展示

$ free -h	# 以易读形式展示

$ free -s {{2}}	# 刷新间隔
```

## df 磁盘信息

> - Gives an overview of the filesystem disk space usage
> - 给出文件系统磁盘空间使用情况的概述

```shell
$ df
> Filesystem      1K-blocks      Used  Available Use% Mounted on
> none              3989044         4    3989040   1% /mnt/wsl
> /dev/sdc       1055762868   1895744 1000163652   1% /

$ df -h	# 易读形式
> Filesystem      Size  Used Avail Use% Mounted on
> none            3.9G  4.0K  3.9G   1% /mnt/wsl

$ df -i	# 对空闲inode的数量进行显示统计

$ df -x {{fs}}	# 显示文件系统，但不包括指定的类型

$ df -T	# 展示文件类型
```

## lscpu cpu信息

> - Displays information about the CPU architecture
> - 显示CPU架构信息

```shell
$ lscpu	# 展示所有 CPUs 信息

$ lscpu --extended	# 以表格形式查看
CPU SOCKET CORE L1d:L1i:L2:L3 ONLINE
  0      0    0 0:0:0:0          yes
  1      0    0 0:0:0:0          yes
  2      0    1 1:1:1:0          yes
  3      0    1 1:1:1:0          yes
  4      0    2 2:2:2:0          yes
  5      0    2 2:2:2:0          yes
  6      0    3 3:3:3:0          yes
  7      0    3 3:3:3:0          yes
  8      0    4 4:4:4:0          yes
  9      0    4 4:4:4:0          yes
 10      0    5 5:5:5:0          yes
 11      0    5 5:5:5:0          yes
 
$ lscpu --extended --offline	# 展示离线信息

$ cat /proc/cpuinfo	# cpu信息存储文件 (每个cpu的信息)

$ uptime # 
```

## uptime 系统运行时间

> - Tell how long the system has been running and other information
> - 告诉系统已经运行了多长时间和其他信息

```shell
$ uptime
> 21:38:30 up 11:46,  1 user,  load average: 0.03, 0.02, 0.00

$ uptime --pretty	# 运行时间
> up 11 hours, 47 minutes

$ uptime --since	# 系统booted up时间
> 2023-11-09 09:52:12
```

## uname 系统信息

> - Print details about the current machine and the operating system running on it
> - 打印有关当前计算机及其上运行的操作系统的详细信息

```shell
$ uname
> Linux

$ uname -a	# 查看所有系统信息 -a/--all
> Linux bayyy 5.15.90.1-microsoft-standard-WSL2 #1 SMP Fri Jan 27 02:56:13 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux

$ uname -m  # 系统架构 -m/--machine
> x86_64
$ uname -p	# 处理器信息 -p/--processor
> x86_64

$ uname -n	# 打印系统用户	-n/--nodename
> bayyy

$ uname -o	# 操作系统 -o/--operating-system
> GNU/Linux
```

## 系统根目录

```shell
bin -> usr/bin/				# 系统指令, 存放二进制可执行文件(ls,cat,mkdir等)
boot/									# 引导目录
dev/									# 设备
etc/									# 配置文件
home/									# 目录存放所有用户文件的根目录
lib -> usr/lib/				# 存放文件系统中的程序运行所需要的共享库及内核模块
lib32 -> usr/lib32/
lib64 -> usr/lib64/		# 64位系统上存放辅助共享库文件
libx32 -> usr/libx32/
lost+found/
media/								# 目录记载可移动的外部设备信息
mnt/									# 目录系统管理员安装临时文件
opt/									# 系统外的进程安装目录
proc/									# 虚拟文件系统目录，是系统内存的映射
root/									# 超级用户（系统管理员）的主目录
run/									# 存储各种各样数据的目录
sbin -> usr/sbin/			# 存放二进制可执行文件，只有root才能访问
snap/									# 
srv/									# 存放一些服务启动之后需要提取的数据
sys/									# 记载各种物理设备信息
tmp/									# 用于存放各种临时文件
usr/									# 所有系统默认的软件都会放置到/usr
var/									# 用于存放运行时需要改变数据的文件
```

- `/var/log`	系统日志
- `/proc/`
  - `/proc/cpuinfo` 显示CPU info的信息
  - `/proc/interrupts` 显示中断
  - `/proc/meminfo` 校验内存使用
  - `/proc/swaps` 显示哪些swap被使用 
  - `/proc/version` 显示内核的版本 
  - `/proc/net/dev` 显示网络适配器及统计 
  - `/proc/mounts` 显示已加载的文件系统 

## ps 进程信息

> - Information about running processes
> - 运行进程信息

```shell
$ ps aux		# 所有进程信息	ps -ef
						# -A/-e 所有进程
						# -a 所有tty
						# a 所有tty，且包含其他用户
						# r 仅包含运行中进程
						# T 所有此terminal的进程
						# x 不包含控制ttys]
$ ps -ef		# 同上, 所有进程信息

$ ps auxww	# 包含命令的进程信息

$ ps -u {{user}}	# 查找指定用户
```

## systemctl 服务控制

> - Control the systemd system and service manager
> - 控制系统和服务管理

```shell
$ systemctl status	# 所有运行服务 (输出如下图)

$ systemctl --failed	# 查看失败单元

$ systemctl {{start|stop|restart|reload}} {{unit}}	# 运行、停止、重启、重加载服务

$ systemctl status {{unit}}	# 查看指定服务状态

$ systemctl {{enable|disable}	{{unit}}	# 开启/关闭boot时加载任务

$ systemctl {{mask|unmask}} {{unit}}	# 屏蔽/取消屏蔽单元以防止启用和手动激活

$ systemctl daemon-reload	# 重新装填系统，扫描新的或改变的单元

$ systemctl is-enabled {{unit}}	# 检查是否可以运行
```

![image-20231109221306555](https://s2.loli.net/2023/11/09/Tf7AIxO9RlB2WUS.png)

## which 命令文件

> - 返回在当前环境中执行的文件(或链接)的路径名

```shell
$ which [-a] filename ...

$ which {{executable}}

$ which -a {{executable}} # 匹配的多个可执行文件，显示全部
```

## whereis 搜索命令

> - Locate the binary, source, and manual page files for a command
> - 找到命令的二进制文件、源文件和手册页文件

```shell
# whereis  [options] [-BMS <dir>... -f] <name>

$ whereis ls
> ls: /usr/bin/ls /usr/share/man/man1/ls.1.gz

$ whereis -b ls	# 只显示二进制文件
> ls: /usr/bin/ls

$ whereis -m ls	# 显示手册页文件及信息
> ls: /usr/share/man/man1/ls.1.gz

$ whereis -s ls	# 显示源文件
> ls:

$ whereis -B {{/usr/bin/}} ls	# 定义二进制查询路径

$ whereis -M {{/usr/bin/}} ls	# 定义手册页查询路径

$ whereis -S {{/usr/bin/}} ls	# 定义源文件查询路径

$ whereis -u ls	# 定位不寻常的二进制文件(系统中包含多个或少于一个二进制文件的二进制文件)

$ whereis -f gcc	# 中段目录参数列表
```

## dmidecode DMI信息

> - Display the DMI (alternatively known as SMBIOS) table contents in a human-readable format.Requires root privileges
> - 以人类可读的格式显示DMI(也称为SMBIOS)表内容。需要root权限
>   - 其输出的信息包括BIOS、系统、主板、处理器、内存、缓存等等
>   - DMI (Desktop Management Interface, DMI)的主要组成部分是Management InformationFormat (MIF)数据库，这个数据库包括了所有有关电脑系统和配件的信息

```shell
$ sudo dmidecode
# dmidecode 3.3
Scanning /dev/mem for entry point.
# No SMBIOS nor DMI entry point found, sorry.

$ sudo dmidecode -s bios-version	# BIOS 版本
$ sudo dmidecode -s system-serial-number	# 系统序列码
$ sudo dmidecode -t bios	# BIOS 信息
$ sudo dmidecode -t processor	# CPU信息
$ sudo dmidecode -t memory	# 内存信息
```

## dmesg 内核信息

> - Write the kernel messages to stdout
> - 打印内核信息

```shell
$ dmesg
$ dmesg --level err	# 展示内核错误信息

$ dmesg -w	# 监视模式

$ dmesg | grep -i memory	# 查找可用物理内存

$ dmesg -T	# 展示时间戳

$ dmesg -H	# 人类可读形式

$ dmesg -L	# 颜色美化展示
```

## ip address

> - Show/manipulate routing, devices, policy routing and tunnels.Some subcommands such as ip address have their own usage documentation
>
> - 显示/操作路由、设备、策略路由和隧道。一些子命令(如ip address)有自己的使用文档
>
>   - > :key: ifconfig 需要下载 `net-tools`

```shell
$ ip address	# ip a	# 列出接口相关信息
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:15:5d:ab:d9:fa brd ff:ff:ff:ff:ff:ff
    inet 172.25.92.203/20 brd 172.25.95.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::215:5dff:feab:d9fa/64 scope link
       valid_lft forever preferred_lft forever


$ ip -brief a	# 简洁形式 网络层信息
lo               UNKNOWN        127.0.0.1/8 ::1/128
eth0             UP             172.25.92.203/20 fe80::215:5dff:feab:d9fa/64

$ ip -brief l	# ip -brief l	连接层信息
lo               UNKNOWN        00:00:00:00:00:00 <LOOPBACK,UP,LOWER_UP>
eth0             UP             00:15:5d:ab:d9:fa <BROADCAST,MULTICAST,UP,LOWER_UP>

$ ip r	# 路由信息	r/route
default via 172.25.80.1 dev eth0 proto kernel
172.25.80.0/20 dev eth0 proto kernel scope link src 172.25.92.203

$ ip n	# ARP邻居信息 n/neigh/neighbour
172.25.80.1 dev eth0 lladdr 00:15:5d:b7:c6:84 STALE

$ ip link set {{interface}} up/down	# 开启/中断连接

$  ip addr add/del {{ip}}/{{mask}} dev {{interface}}	# 增加/删除 接口上的IP

$ ip route add default via {{ip}} dev {{interface}} # 增加默认路由
```

## ifconfig 网络信息

> - Network Interface Configurator
> - 网络接口适配器

```shell
$ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.25.92.203  netmask 255.255.240.0  broadcast 172.25.95.255
        inet6 fe80::215:5dff:feab:d9fa  prefixlen 64  scopeid 0x20<link>
        ether 00:15:5d:ab:d9:fa  txqueuelen 1000  (Ethernet)
        RX packets 1505  bytes 1100847 (1.1 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 588  bytes 92312 (92.3 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

$ ifconfig eth0	# 指定网卡

$ ifconfig eth0 up/down	# 启用/停用

$ ifconfig eth0 {{ip_address}}	# 分配ip地址

$ ifconfig -s	# 简要信息
Iface      MTU    RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
eth0      1500     1534      0      0 0           589      0      0      0 BMRU
lo       65536        0      0      0 0             0      0      0      0 LRU
```

#### 内容详解

- inet：ipv4
- inet6：ipv6
- lo：回环网络接口
  - **“回环”网络接口**，“lo”是“loopback”的缩写，它不代表真正的网络接口，而是一个**虚拟的网络接口**， 其 IP 地址默认是“**127.0.0.1**”，**回环地址**通常仅用于对本机的网络测试
- br0：网桥接口 
  - 一种在**链路层实现中继**，对帧进行转发的技术，根据MAC分区块，可隔离碰撞，将网络的多个网段在数据链路层连接起来的网络设备。
  - br0可以将两个接口进行连接，如将两个以太网接口eth0进行连接，对帧进行转发
- wlan0：无线接口
  - 无线网卡对应的接口，无线网卡也需要对应的驱动程序才能工作****

```shell
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
```

- eth0             ：网卡名称
- UP                  ：表示“接口已启用”
- BROADCAST：表示“主机支持广播”
- RUNNING      ：表示“接口在工作中”
- MULTICAST  ：表示“主机支持多播”
- MTU 1500      ：（最大传输单元）：1500字节

```shell
inet 172.25.92.203  netmask 255.255.240.0  broadcast 172.25.95.255
```

- **inet**：IP地址
- **netmask**：子网掩码
- **broadcast**：广播地址

```shell
inet6 fe80::215:5dff:feab:d9fa  prefixlen 64  scopeid 0x20<link>
```

- **inet6 ::1**    ：ipv6地址
- **prefixlen 128** ：在网上只搜到说是 前缀长度，不知道对不对
- **scopeid 0x10**：global 可对外 host 本机互通

```shell
ether 00:15:5d:ab:d9:fa  txqueuelen 1000  (Ethernet)
```

- **ether**（Ethernet）           ：表示 连接类型（以太网）
- **00:50:56:28:2c:xx**（Hwaddr）：表示 硬件Mac 地址
- **txqueuelen 1000**            ：表示 网卡传送队列长度

```shell
RX packets 1505  bytes 1100847 (1.1 MB)
RX errors 0  dropped 0  overruns 0  frame 0
```

- **RX packets**     ：接受到的总包数
- **RX bytes**       ：接受到的总字节数
- **RX errors**       ：接收时，产生错误的数据包数
- **RX dropped**     ：接收时，丢弃的数据包数
- **RX overruns**    ：接收时，由于速度过快而丢失的数据包数
- **RX frame** (框架) ：接收时，发生frame错误而丢失的数据包数

```shell
TX packets 588  bytes 92312 (92.3 KB)
TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

- **TX packets**     ：发送的总包数
- **TX bytes**       ：发送的总字节数
- **TX errors**       ：发送时，产生错误的数据包数
- **TX dropped**     ：发送时，丢弃的数据包数
- **TX overruns**    ：发送时，由于速度过快而丢失的数据包数
- **TX carrier**      ：发送时， 发生carrier错误而丢失的数据包数（运输工具）
- **TX collisions**   ：发送时， 冲突信息包的数目

## wget 下载

> - Download files from the Web.Supports HTTP, HTTPS, and FTP
> - 下载文件

```shell
$ wget {{https://example.com/foo}}

$ wget -o logfile	{{https://example.com}}	# 日志信息 -o/--output-file

$ wget -O {{bar}} {{https://example.com/foo}}	# 重命名 -O/--output-document

$  wget --page-requisites --convert-links --wait=3 {{https://example.com/somepage.html}} # 以3秒的间隔下载一个网页及其所有资源(脚本、样式表、图像等)	-p -k

$ wget --mirror --no-parent {{https://example.com/somepath/}} -m -np

$ wget --limit-rate={{300k}} --tries={{100}} {{https://example.com/somepath/}}	# 限制速率及重试次数

$ wget --user={{username}} --password={{password}} {{https://example.com}}	# 下载需要用户名+密码权限的文件

$ wget --continue {{https://example.com}}	# 重连 -c

$ wget --directory-prefix {{path/to/directory}} --input-file {{URLs.txt}}	# 下载保存在文本文件中的所有url到指定目录
```

## curl 网页链接

> - Transfers data from or to a server.Supports most protocols, including HTTP, FTP, and POP3
> - 将数据从服务器传输到服务器。支持大部分协议，包括HTTP、FTP、POP3

- 用来请求 Web 服务器
  - :key: 它的名字就是客户端（client）的 URL 工具的意思

```shell
$ curl {{http://www.example/com/foo}}
# curl [options...] <url>

$ curl {{http://example.com}} --output {{path/to/file}}	# 下载并指定文件名 -o/--output=FILE

$ curl --remote-name {{http://example.com/filename}}	# 将输出保存在URL指定的文件名下 -O/--remote-name

$  curl --data {{'name=bob'}} {{http://example.com/form}}	# POST请求下载 --data @file_name 从文件 --data @'-' 从STDIN --data {{'name=bob'}} 直接输入 --data/-d <data>

$ curl --header {{'X-My-Header: 123'}} --request {{PUT}} {{http://example.com}}	# 指定 Header 及 请求方式


$ curl --user myusername:mypassword {{http://example.com}}	# 用户名+密码权限访问

$  curl --cert {{client.pem}} --key {{key.pem}} --insecure {{https://example.com}} # 客户端证书和密钥
```

#### -A/--user-agent

`-A, --user-agent <name>`

- 指定客户端用户的**用户代理标头**，即 `User-Agent` 
  - 默认用户代理字符串为: `curl/[version]`

```sh
$ curl -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36' https://baidu.com	# 指定客户端的用户代理标头

$ curl -A '' https://baidu.com	# 移除 User-Agent 标头
```

> - `-H` ：更改指定的请求标头(Header)
>
> ```sh
> curl -H "Content-Type: application/json" -H "Authorization: Bearer token123" http://example.com/api
> ```
>
> - :key: `-A` 仅仅指定 `User-Agent` 标头

#### -b/--cookie

`-b, --cookie <data|filename>` 向服务器发送 Cookie

```sh
$ curl -b 'foo=bar' https://google.com
$ curl -b cookies.txt https://google.com	# 读取本地文件cookies.txt，将其发送到服务器
```

#### -c/--cookie-jar

`-c, --cookie-jar <filename>` 将服务器设置的 Cookie 写入一个文件

```sh
$ curl -c cookies.txt https://www.google.com
```

#### -d/--data

`-d, --data <data>` 用于发送 POST 请求的数据体

- 使用 `-d` 参数以后，HTTP 请求会自动加上标头 `Content-Type : application/x-www-form-urlencoded`。并且会自动将请求转为 POST 方法，因此可以省略 `-X POST`

```sh
$ curl -d'login=emma＆password=123'-X POST https://google.com/login
# 或者
$ curl -d 'login=emma' -d 'password=123' -X POST  https://google.com/login

$ curl -d @data.txt https://google.com/login	# 读取data.txt文件的内容，作为数据体向服务器发送
```

#### --data-urlencode

`--data-urlencode <data>` 等同于`-d`，发送 POST 请求的数据体，区别在于会自动将发送的数据进行 URL 编码

```sh
$ curl --data-urlencode 'comment=hello world' https://google.com/login	# 发送的数据hello world之间有一个空格，需要进行 URL 编码
```

#### -e/--referer

`-e, --referer <URL>` 设置 HTTP 的标头 `Referer`，表示请求的来源

```sh
curl -e 'https://google.com?q=example' https://www.example.com
```

> :key: 直接通过 `-H` 参数添加
>
> ```sh
> curl -H 'Referer: https://google.com?q=example' https://www.example.com
> ```

#### -F/--form

`-F, --form <name=content>` 向服务器上传二进制文件

```sh
# 给 HTTP 请求加上标头Content-Type: multipart/form-data，然后将文件photo.png作为file字段上传
$ curl -F 'file=@photo.png' https://google.com/profile

# 指定 MIME 类型为image/png，否则 curl 会把 MIME 类型设为application/octet-stream
$ curl -F 'file=@photo.png;type=image/png' https://google.com/profile

# 指定文件名: 服务器接收到的文件名为 me.png
$ curl -F 'file=@photo.png;filename=me.png' https://google.com/profile
```

#### -G/--get

`-G, --get` 构造 URL 的查询字符串

```sh
# 发出一个 GET 请求
# 实际请求的URL为https://google.com/search?q=kitties&count=20
# 如果省略--G，会发出一个 POST 请求
$ curl -G -d 'q=kitties' -d 'count=20' https://google.com/search

# URL编码, 需要结合 --data-urlencode 参数
$ curl -G --data-urlencode 'comment=hello world' https://www.example.com
```

#### -H/--header

`-H, --header <header/@file>` 添加 HTTP 请求的标头

```sh
$ curl -H 'Accept-Language: en-US' https://google.com	# 添加 HTTP 标头Accept-Language: en-US

$ curl -d '{"login": "emma", "pass": "123"}' -H 'Content-Type: application/json' https://google.com/login	# 添加 HTTP 请求的标头是Content-Type: application/json，然后用-d参数发送 JSON 数据
```

#### -i/--include

- 打印出服务器回应的 HTTP 标头

```sh
$ curl -i https://www.example.com	# 收到服务器回应后，先输出服务器回应的标头，然后空一行，再输出网页的源码
```

![image-20240223165508420](https://s2.loli.net/2024/02/23/WoMpnBNfracXVtk.png)

#### -I/--head

- 向服务器发出 HEAD 请求，然会将服务器返回的 HTTP 标头打印出来

```sh
$ curl -I https://www.example.com	# 输出服务器对 HEAD 请求的回应
```

#### -k/--insecure

- 指定跳过 SSL 检测

```sh
$ curl -k https://www.example.com	# 不会检查服务器的 SSL 证书是否正
```

#### -L/--location

- 让 HTTP 请求跟随服务器的重定向。curl 默认不跟随重定向

```sh
$ curl -L -d 'tweet=hi' https://api.twitter.com/tweet
```

#### --limit-rate

`--limit-rate <speed> `限制 HTTP 请求和回应的带宽，模拟慢网速的环境。

```sh
$ curl --limit-rate 200k https://google.com	# 带宽限制200K字节
```

#### -o/--output

`-o, --output <file>` 将服务器的回应保存成文件，等同于`wget`命令

```sh
$ curl -o example.html https://www.example.com
```

#### -O/--remote-name

- 将服务器回应保存成文件，并将 URL 的最后部分当作文件名

```sh
$ curl -O https://www.example.com/foo/bar.html	# 文件名为bar.html
```

#### -s/--silent

- 不输出错误和进度信息

```sh
$ curl -s https://www.example.com	# 一旦发生错误，不会显示错误信息。不发生错误的话，会正常显示运行结果
```

> :key: 不输出任何结果
>
> ```sh
> $ curl -s -o /dev/null https://google.com
> ```

#### -S/--show-error

- 指定只输出错误信息，通常与`-s`一起使用

#### -u/--user

- 设置服务器认证的用户名和密码

```sh
$ curl -u 'bob:12345' https://google.com/login	# 用户名为bob，密码为12345，然后将其转为 HTTP 标头Authorization: Basic Ym9iOjEyMzQ1

$ curl https://bob:12345@google.com/login	# 识别 URL 里面的用户名和密码, 并转化为上例形式

$ curl -u 'bob' https://google.com/login	# 只设置了用户名，执行后，curl 会提示用户输入密码
```

#### -v/--verbose

- 输出通信的整个过程，用于调试

```sh
$ curl -v https://www.example.com
```

> :key: `--trace` 也可以用于调试，还会输出原始的二进制数据
>
> ```sh
> $ curl --trace - https://www.example.com
> ```

![image-20240223170421095](https://s2.loli.net/2024/02/23/ChVMwf9zEbml2Ru.png)

![image-20240223170428591](https://s2.loli.net/2024/02/23/35miMnyVwAhXZGR.png)

#### -x/--proxy

- 指定 HTTP 请求的代理

```sh
$ curl -x socks5://james:cats@myproxy.com:8080 https://www.example.com	# 指定 HTTP 请求通过myproxy.com:8080的 socks5 代理发出

$ $ curl -x james:cats@myproxy.com:8080 https://www.example.com	# 如果没有指定代理协议，默认为 HTTP
```

#### -X/--request

- 指定 HTTP 请求的方法

```sh
$ curl -X POST https://www.example.com	# 对https://www.example.com发出 POST 请求
```

## 监控工具

#### vmstat 整体监控工具

> - Report information about processes, memory, paging, block IO, traps, disks and CPU activity
> - 报告有关进程、内存、分页、块IO、陷阱、磁盘和CPU活动的信息
> - ![image-20231110142813319](https://s2.loli.net/2023/11/10/4HjZOagm8Eypd15.png)

```shell
$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 6910052  20116 528764    0    0     3     1    8   14  0  0 100  0  0

$ vnstat {{2}} {{5}}	# 每2秒查看一次，循环5次
```

#### mpstat CPU监控工具(cpu负载)

> - mpstat是Multiprocessor Statistics的缩写，是**实时系统监控工具**。其报告与==CPU==的一些统计信息，这些信息存放在`/proc/stat`文件中。在多CPUs系统里，其不但能查看所有CPU的平均状况信息，而且能够查看**特定CPU的信息**。mpstat最大的特点是：可以查看多**核心cpu中每个计算核心的统计数据**；而类似工具vmstat只能查看系统整体cpu情况
> - :key: 需要安装 `sysstat`
> - ![image-20231110143012734](https://s2.loli.net/2023/11/10/HdaYsZmgkbwELpJ.png)

```shell
$ mpstat
$ mpstat {{2}}	# 每2s刷新一次
$ mpstat {{2}} {{5}}	# 每2s刷新一次，持续5次
$ mpstat -p {{0}} {{2}} {{5}}	# 特定的进程

$ mpstat -A	# 所有cpu信息
```

#### iostat 磁盘读写信息(磁盘读写信息)

> - 统计设备和分区的CPU信息以及IO信息
> - :key: 需要安装 `sysstat`
> - ![image-20231110144117510](https://s2.loli.net/2023/11/10/z73FfMWmVNnpoDJ.png)

```shell
$ iostat

$ iostat -m	# 指定单位 -k kb/-m mb

$ iostat -c	# 展示CPU统计信息

 - Display disk statistics with disk names (including LVM):
$ iostat -N	# 展示磁盘信息 (以)

$ iostat -xN {{sda}}	# 展示扩展磁盘信息以指定磁盘名
 
$ iostat {{2}}	# 每2s更新一次

$ iostat -dxk 1 10	# -d 显示磁盘使用情况，-x 显示详细信息，-k kb单位
# 重点属性 %until 设备使用率 await 响应时间
```

- 命令
  - -x 显示详细信息
  - -C 显示CPU使用情况，与-d选项互斥
  - -d 显示磁盘使用情况，与-C选项互斥
  - -k 以 KB 为单位显示
  - -m 以 M 为单位显示
  - -N 显示磁盘阵列(LVM) 信息
  - -n 显示NFS 使用情况
  - -p[磁盘] 显示磁盘和分区的情况
  - -t 显示终端和CPU的信息
  - -V 显示版本信息
- 属性
  - cpu
    - %user：CPU处在用户模式下的时间百分比。
    - %nice：CPU处在带NICE值的用户模式下的时间百分比。
    - %system：CPU处在系统模式下的时间百分比。
    - %iowait：CPU等待输入输出完成时间的百分比。
    - %steal：管理程序维护另一个虚拟处理器时，虚拟CPU的无意识等待时间百分比。
    - %idle：CPU空闲时间百分比。
  - 磁盘
    - tps：该设备每秒的传输次数（Indicate the number of transfers per second that were issued to the device.）。“一次传输”意思是“一次I/O请求”。多个逻辑请求可能会被合并为“一次I/O请求”。“一次传输”请求的大小是未知的。
    - kB_read/s：每秒从设备（drive expressed）读取的数据量；
    - kB_wrtn/s：每秒向设备（drive expressed）写入的数据量；
    - kB_read：读取的总数据量；
    - kB_wrtn：写入的总数量数据量；

#### sar 性能分析工具(磁盘负载)

> - 统计并保存系统活动信息
> - :key: 需要安装 `sysstat`
>
> ![image-20231110154446227](https://s2.loli.net/2023/11/10/tH9hJM3PmpYNzQT.png)
>
> ![image-20231110154945084](https://s2.loli.net/2023/11/10/BqmwWpz8Z35cPfK.png)

```shell
$ sar {{2}} {{5}}	# 每2s报告一次，持续5次

$ sar -C 1 10	# 磁盘
$ sar -d 1 10	# cpu
$ sar -q 1 10	# 负载
```

#### pidstat 进程磁盘读写(进程查看)

> - 统计Linux进程的相关信息：IO、CPU、内存等
> - :key: 需要安装 `sysstat`
>
> ![image-20231110155023718](https://s2.loli.net/2023/11/10/n8J2eKGysgSdpV9.png)
>
> ![image-20231110155127620](https://s2.loli.net/2023/11/10/aLGCmqikSTwZxuK.png)

```shell
$ pidstat -d 2 10	# 磁盘读写进程

$ pidstat -r 2 10	# 分页使用及内存使用率
```

## strace 用户空间追踪器

> - Troubleshooting tool for tracing system calls.
> - 用于跟踪系统调用的故障排除工具
>   - 计算命令执行时间和效率，进行效率优化
>
> ![image-20231110155651106](https://s2.loli.net/2023/11/10/inTcyX1KNEhpkSC.png)

```shell
$ strace {{command}}	# 追踪命令的执行过程

$ strace -c {{command}}	# 统计时间、调用、错误数
1.txt  history test.txt
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
  0.00    0.000000           0         7           read
  0.00    0.000000           0         1           write
  0.00    0.000000           0        23           close
	...
------ ----------- ----------- --------- --------- ----------------
100.00    0.000000           0       148        18 total
```

## netstat 网络信息

> - Displays network-related information such as open connections, open socket ports, etc
> - 显示与网络相关的信息，如打开的连接、打开的套接字端口等

```shell
$ netstat -anptu	# 可能需要sudo权限
# -a/--all 所有端口		-n/--numeric 不解析ip地址
# -p/--program	PID及程序名		-t/--tcp TCP端口
# -u/--udp	UDP端口

Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      112/systemd-resolve
udp        0      0 127.0.0.53:53           0.0.0.0:*                           112/systemd-resolve
udp        0      0 127.0.0.1:323           0.0.0.0:*                           -
udp6       0      0 ::1:323                 :::*                                -
```

## ethtool 网卡信息

> - 显示和修改网卡参数

```shell
$ ethtool eth0
> ...
> Link detected: yes	# 重要的是连接情况
```

## ss 套接字查询

> - Utility to investigate sockets
> - 调查套接字的实用程序

```shell
$ ss -ntul	# 
# -n/--numeric 不解析服务名 -t/--tcp TCP端口	-u/--udp	UDP端口
# -l/--listening 展示监听中端口

Netid    State     Recv-Q    Send-Q        Local Address:Port         Peer Address:Port    Process
udp      UNCONN    0         0             127.0.0.53%lo:53                0.0.0.0:*
udp      UNCONN    0         0                 127.0.0.1:323               0.0.0.0:*
udp      UNCONN    0         0                     [::1]:323                  [::]:*
tcp      LISTEN    0         4096          127.0.0.53%lo:53                0.0.0.0:*

$ ss -s	# 统计连接信息
Total: 161
TCP:   1 (estab 0, closed 0, orphaned 0, timewait 0)

Transport Total     IP        IPv6
RAW       0         0         0
UDP       3         2         1
TCP       1         1         0
INET      4         3         1
FRAG      0         0         0
```

## mount 挂载信息

> - Provides access to an entire filesystem in one directory
> - 提供对一个目录中的整个文件系统的访问

```shell
$ mount # 查看所有的挂载信息

$ mount -o uid={{user_id}},gid={{group_id}} {{path/to/device_file}} {{path/to/target_directory}}	# 将设备挂载到特定用户的目录

$ unmount # 取消挂载
```

## lsblk 设备信息

```shell
$ lsblk
NAME MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda    8:0    0 363.3M  1 disk
sdb    8:16   0     2G  0 disk [SWAP]
sdc    8:32   0     1T  0 disk /snap
                               /mnt/wslg/distro
                               /
sdd    8:48   0     1T  0 disk

$ lsblk -a	# 所有信息
$ lsblk -k/-m	# 单位

$ lsblk -f	# 展示设备类型
NAME FSTYPE FSVER LABEL UUID                                 FSAVAIL FSUSE% MOUNTPOINTS
sda  ext4   1.0
sdb  swap   1           09266fbe-2cd1-4e1a-9c8f-46187eb06143                [SWAP]
sdc  ext4   1.0         5a88ab68-efaf-420c-89a2-1f31e2b04fdb  953.8G     0% /snap

$ lsblk -t	# 输出块设备拓扑信息
NAME ALIGNMENT MIN-IO OPT-IO PHY-SEC LOG-SEC ROTA SCHED RQ-SIZE  RA WSAME
sda          0    512      0     512     512    1 none      950 128    0B
sdb          0   4096      0    4096     512    1 none      950 128    0B
sdc          0   4096      0    4096     512    1 none      950 128    0B
sdd          0   4096      0    4096     512    1 none      950 128    0B
```

## fdisk 磁盘信息

> - 用于管理硬盘上的分区表和分区的程序
>
> ![image-20231110161650345](https://s2.loli.net/2023/11/10/Fnm6z3H28yo4AZ1.png)

```shell
$ sudo fdisk -l	# 所有分区信息
```

## history 命令历史记录

```shell
$ history

$ history 20	# 最新20条 (zsh中是从20开始到最后, -20为最后20条)

$ history -c	# 情况
$ history -d {{offset}} # 删除指定偏移量处的历史表项
```

## tcpdump 流量监测

> - 转储网络流量

```shell
$ tcpdump -D	# 可用的网络接口
1.eth0 [Up, Running, Connected]
2.any (Pseudo-device that captures on all interfaces) [Up, Running]
3.lo [Up, Running, Loopback]
4.bluetooth-monitor (Bluetooth Linux Monitor) [Wireless]
5.nflog (Linux netfilter log (NFLOG) interface) [none]
6.nfqueue (Linux netfilter queue (NFQUEUE) interface) [none]
7.dbus-system (D-Bus system bus) [none]
8.dbus-session (D-Bus session bus) [none]

$ tcpdump -i {{eth0}}	# 捕获指定接口的流量
```

## scp 文件传输

> - 安全的副本。使用SSH安全复制协议在主机之间复制文件

```shell
$ scp {{file}} {{remote_host}}:{{path/file_name}}
$ scp file.txt bayyy@127.0.0.1:~
```

## 防火墙与安全上下文

> 基本会关闭

#### firewalld 防火墙

#### iptables 防火墙

#### selinux 安全上下文

#### lsattr 命令用于显示文件属性

```shell
$ lsattr /ect/passwd
> --------------e----- /etc/passwd
```

#### chattr 命令放置文件被修改

```shell
$ sudo chattr +i /etc/passwd
$ lsattr /etc/passwd
$ ----i---------e----- /etc/passwd
$ sudo chattr -i /ect/passwd
```

## date 时间

```shell
$ date
> Sun Nov 12 20:20:31 CST 2023
```

## sync/rsync 同步/复制

> - sync
>   - 将所有挂起的写操作刷新到适当的磁盘。
> - rsync
>   - 默认情况下，使用SSH向远程主机传输文件或从远程主机传输文件(但不能在两个远程主机之间传输文件)。
>   - 要指定远程路径，请使用' user@host:path/ To /file or directory '。

```shell
# 同步数据
$ rsync -ar source target	# --archive/-a 以归档形式,递归传输并保持文件属性 --recursive/-r 目录递归
$ rsync -vr source target # -v 显示同步信息
$ rsync -Pr source tartget	# -P 显示进度
# --update/-u 仅在mtime更新时进行拷贝  -o/-g/-p 保持用户/组/其他的权限
# --times/-t 保持mtime属性

# 远程同步
$ rsync -av root@192.168.1.77:/etc/hosts /dir1/     #j将192.168.1.77服务器/etc/hosts文件拷贝到本地/dir1文件夹下
```

## dd 转换和复制文件

```shell
$ dd if=path/source of=/dev/dest_drive status=progress conv=noerror # 复制文件, 显示进度, 且忽略错误


$ dd if=/dev/urandom of=random_file bs=100 count=1	# 产生指定大小的随机内容文件
$ dd if=/dev/zero of=dest_file bs=1M count=100000.. # 测试磁盘读写性能,
```

## kill 结束进程

> - 向进程发送信号，通常与停止进程有关。除了SIGKILL和SIGSTOP之外的所有信号都可以被进程拦截，以执行干净的退出

```shell
$ kill process_id	# 以默认的SIGTERM信号停止程序

$ kill -l # 列出所有的信号名称
> HUP INT QUIT ILL TRAP ABRT BUS FPE KILL USR1 SEGV USR2 PIPE ALRM TERM STKFLT CHLD CONT STOP TSTP TTIN TTOU URG XCPU XFSZ VTALRM PROF WINCH POLL PWR SYS

$ kill -9|KILL id	# 立即终止程序(该程序没有机会捕获信号)
$ kill -17|STOP id	# 暂停程序，直到接收到SIGCONT ("continue")信号:
```

## md5sum md5校验

> - 计算MD5加密校验和

```shell
$ md5sum file1 file2 ...	# 计算MD5校验和
$ md5sum file > file.md5	# 计算后保存
```

## ssh-keygen 生成秘钥

> - 生成用于身份验证、无密码登录和其他操作的ssh密钥

```shell
$ ssh-keygen	# 交互式生成密钥
```

## ssh-copy-id 安装公钥

> - 在远程计算机的授权密钥中安装您的公钥

```shell
$ ssh-copy-id -i id_rsa.pub username@remote_host	# 将指定公钥安装到远程
	$ -p port	# 安装到指定端口
```

## source 执行文件

> - 从当前shell中的文件执行命令

```shell
$ source path/to/file
$ . path/to/file
```

## vim :X 加密码

- :X 添加密码
- :X 设置为空, 则取消密码

## rpm 包管理工具

```shell
$ rpm -qa		# 查看系统上安装的所有rpm包	--query/-q 查询版本 --all/-a	查询所有
$ rpm -qa | grep {{package_name}}	# 查找指定包的安装情况

$ rpm -ivh	{{package_name}}	# --install/-i 安装 --verbose/-v	展示安装细节 --hash/-h 安装时打印hash标记
$ rpm -Uvh {{package_name}}	# --upgrade/-U 升级

$ rpm -e --nodeps {{package_name}}	# --erase/-e	删除,卸载 --nodeps 不涉及其依赖包

$ rpm -ql {{package_name}}	# 查看依赖所在位置 --list/-l
```

## yum

```shell
$ yum repolist	# yum源
$ yum clean all	# 清除所有缓存及头文件
$ yum list | wc -l	# 列举源内所有包
$ yum info {{package_name}}	# 显示安装包的信息

$ yum install {{package_name}}	# 安装
$ yum groupinstall {{group_name}} # 安装程序组

$ yum remove {{package_name}}	# 卸载

$ yum update	# 全部更新
$ yum update {{package_name}}	# 更新指定包
$ yum check-update	# 检查可更新的包
$ yum upgrade {{package_name}}	# 升级指定程序包

$ yum list installed # 列举所有安装的包

$ yum deplist {{package_name}}	# 查看包的依赖
```

> - 更新 CentOS Stream仓库
>
> ```shell
> $ yum search centos-release-stream	# 搜索并查看仓库
> $ yum install -y centos-release-stream	# 安装
> $ yum repolist	# 查看所有仓库
> ```

## locate 查找文件

> - 根据文件名查找文件

```shell
$ locate pattern
```

## fsck 检查磁盘系统

> - 检查文件系统的完整性或修复它。在运行该命令时，应该卸载文件系统。

```shell
$ sudo fsck /dev/sdXN	# 检查
$ sudo fsck -r /dev/sdXN	# 检查并选择进行修复
$ sudo fsck -a /dev/sdXN	# 检查并自动修复
```

## rz/sz 上传/下载

> - 需要安装 `yum -y install lrzsz`

```shell
$ rz	# 上传(弹出对话框)
$ sz filename	# 下载
```

## mkfs 格式化文件

```shell
$ mkfs
mkfs         mkfs.ext2    mkfs.ext4    mkfs.minix   mkfs.vfat               
mkfs.cramfs  mkfs.ext3    mkfs.fat     mkfs.msdos   mkfs.xfs

$ mkfs.xfs	
```