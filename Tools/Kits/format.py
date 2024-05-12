import logging
import os
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

def file_handler(file):
  with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    lines = [formatHeader(line) for line in lines ]
    with open(file, 'w', encoding='utf-8') as f:
      f.writelines(lines)

# 遍历本级目录下的所有文件, 对所有 markdown 文件进行修改
def walk_dir(dir):
  for root, dirs, files in os.walk(dir):
    for file in files:
      if file.endswith(".md"):
        file_handler(os.path.join(root, file))
        logging.info(f"处理文件 '{file}' 成功")
  logging.info("处理完成")


def main():
  # 以当前文件夹为根目录
  cur_dir = os.path.dirname(os.path.realpath(__file__))
  logging.info(f"当前目录: {cur_dir}")
  walk_dir(cur_dir)

if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO)
  main()