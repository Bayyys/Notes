import os


# 检查所有文件输出体积大于指定大小的文件
def check_file_size(dir: str = "../..", file_size: int = 50):
    file_size = file_size * 1024 * 1024  # MB to B
    for root, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) > file_size:
                print(
                    f"File: {file_path} size is {os.path.getsize(file_path) / 1024 / 1024} MB"
                )  # 显示文件路径和大小
        for dir in dirs:
            if dir.find("node_modules") == -1:
                continue
            check_file_size(dir, file_size)


if __name__ == "__main__":
    check_file_size("../../")
