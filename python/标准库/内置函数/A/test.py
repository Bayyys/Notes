import re
import os 
def remove():
    # 导入文字
    file_path = os.path.dirname(os.path.abspath(__file__))
    with open(file_path+"/test.md", "r", encoding="utf-8") as f:
        words = f.read()
    
    p1 = r'\`.+?\`'
    p2 = r'\`.+?\('
    m1 = re.findall(p1, words)
    m2 = []
    for match in m1:
        test = re.findall(p2, match)[0].replace("`", "").replace("(", "")
        test = "[`" + test + "`](#" + test + ")"
        m2.append(test)
    for i in range(len(m1)):
        words = words.replace(m1[i], m2[i])
    # 将修改后的内容写入文件
    with open(file_path+"/finish.md", "w", encoding="utf-8") as f:
        f.write(words)

def number():
    file_path = os.path.dirname(os.path.abspath(__file__))
    with open(file_path+"/form.md", "r", encoding="utf-8") as f:
        words = f.read()
    p1 = r'\`(.+?)\`'
    matches = re.findall(p1, words)
    print(matches)
    return matches

def add():
    file_path = os.path.dirname(os.path.abspath(__file__))
    with open(file_path+"/test.md", "r", encoding="utf-8") as f:
        words = f.read()
    p1 = r'\### .+?\n'
    p2 = r'###'
    matches = re.findall(p1, words)
    return matches

def change():
    list1 = number()
    list2 = add()
    list3 = []
    change_str = '<a id="#">¶</a>'
    for i in range(len(list2)):
        find_str = list2[i].strip() + '<a id="'+ list1[i] +'">¶</a>'
        list3.append(find_str)
    file_path = os.path.dirname(os.path.abspath(__file__))
    with open(file_path+"/test.md", "r", encoding="utf-8") as f:
        words = f.read()
    for i in range(len(list2)):
        words = words.replace(list2[i], list3[i])
    with open(file_path+"/finish.md", "w", encoding="utf-8") as f:
        f.write(words)


if __name__ == "__main__":
    # remove()
    change()

