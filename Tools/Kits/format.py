import sys
import re

# 对 markdown 标题进行修改
# 1. 标题从 二级标题 开始, 即 ##; 所有标题降一级
# 2. 去除标题后的手动命名的数字 ## 1. xxx -> ## xxx
def formatHeader(line):
  if line.startswith("#"):  # 标题行
    # 使用正则表达式去除 #数字 或者 #空格数字
    # 例如:
    # # 1. xxx -> ## xxx
    # # 1.1 xxx -> ## xxx
    # #1.xxx -> ## xxx
    line = re.sub(r'#\s*[\d\.]+\s*', '## ', line)
    return line
  else:
    return line


def main():
  file = "CSS.md"
  # 打开一个文件选择器
  with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    lines = [formatHeader(line) for line in lines ]
    with open(file, 'w', encoding='utf-8') as f:
      f.writelines(lines)

if __name__ == '__main__':
  main()