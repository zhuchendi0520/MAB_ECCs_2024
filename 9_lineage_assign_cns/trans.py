import sys

if len(sys.argv) != 3:
    print("用法: python replace_lines.py <输入文件.txt> <输出文件.txt>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        # 跳过空行
        if not line.strip():
            continue

        parts = line.strip().split()

        # 如果是标题行，直接写出
        if parts[0].lower() == "position":
            outfile.write("\t".join(parts) + "\n")
            continue

        # 检查是否为合法的三列格式
        if len(parts) != 3:
            print(f"跳过格式错误行: {line.strip()}")
            continue

        # 替换第三列中的 "."
        if parts[2] == ".":
            parts[2] = parts[1]

        outfile.write("\t".join(parts) + "\n")

