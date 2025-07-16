import re
import os
import sys # 导入 sys 模块用于访问命令行参数

def modify_dockerfile(dockerfile_content):
    """
    修改 Dockerfile 内容：
    1. 在第一行前面添加 '#'。
    2. 将 XX_VERSION 的值修改为 '1.6.1'。
    3. 将 ALPINE_VERSION 的值设置为空。

    Args:
        dockerfile_content (str): 原始 Dockerfile 的内容。

    Returns:
        str: 修改后的 Dockerfile 内容。
    """
    lines = dockerfile_content.splitlines()
    modified_lines = []

    # 1. 在第一行前面添加 '#'
    if lines:
        modified_lines.append(f"#{lines[0]}")
        remaining_lines = lines[1:]
    else:
        remaining_lines = []

    # 遍历剩余行进行其他修改
    for line in remaining_lines:
        # 2. 将 XX_VERSION 的值修改为 '1.6.1'
        if line.startswith("ARG XX_VERSION="):
            modified_lines.append("ARG XX_VERSION=1.6.1")
        # 3. 将 ALPINE_VERSION 的值设置为空
        elif line.startswith("ARG ALPINE_VERSION="):
            modified_lines.append("ARG ALPINE_VERSION=")
        else:
            modified_lines.append(line)

    return "\n".join(modified_lines)

# 主执行部分
if __name__ == "__main__":
    # 检查命令行参数
    if len(sys.argv) < 2:
        print("用法: python modify_dockerfile.py <Dockerfile路径>")
        print("示例: python modify_dockerfile.py ./Dockerfile")
        sys.exit(1) # 退出程序，表示错误

    dockerfile_path = sys.argv[1] # 获取第一个命令行参数作为 Dockerfile 路径

    if not os.path.exists(dockerfile_path):
        print(f"错误: 文件 '{dockerfile_path}' 不存在。")
        sys.exit(1)
    else:
        try:
            with open(dockerfile_path, 'r', encoding='utf-8') as f:
                dockerfile_input = f.read()

            modified_content = modify_dockerfile(dockerfile_input)

            # 直接打印修改后的内容到标准输出
            print(modified_content)

            # 用户可以通过重定向来保存输出，例如：
            # python modify_dockerfile.py ./Dockerfile > ./Dockerfile.modified

        except Exception as e:
            print(f"处理文件时发生错误: {e}")
            sys.exit(1)

