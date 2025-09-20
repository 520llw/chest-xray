import os

# 定义项目根目录（可根据需要修改）
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# 需要创建的目录列表
dirs = [
    os.path.join(PROJECT_ROOT, "data/raw"),
    os.path.join(PROJECT_ROOT, "data/processed"),
    os.path.join(PROJECT_ROOT, "models"),
    os.path.join(PROJECT_ROOT, "results"),
    os.path.join(PROJECT_ROOT, "src")
]

# 创建目录（若不存在）
for dir_path in dirs:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"创建目录: {dir_path}")
    else:
        print(f"目录已存在: {dir_path}")

print("所有目录创建完成！")