import sys
from Bio import Phylo
import os
import csv

def get_terminals_under_clade(clade):
    """获取给定节点下的所有末端节点"""
    return list(clade.find_clades(terminal=True))

def calculate_distances_terminals_and_count(input_file):
    # 读取系统发育树文件
    tree = Phylo.read(input_file, "newick")

    # 初始化字典来存储每个节点下面的最远末端节点的距离、所有末端节点的名称和数量
    node_info = {}

    # 遍历树中的所有节点
    for clade in tree.find_clades():
        # 如果当前节点是末端节点，跳过
        if clade.is_terminal():
            continue

        # 初始化最大距离为0
        max_distance = 0
        terminal_names = []

        # 使用自定义函数获取当前节点下的所有末端节点
        terminals = get_terminals_under_clade(clade)

        # 遍历当前节点下的所有末端节点
        for terminal in terminals:
            # 计算当前节点到末端节点的距离
            distance = tree.distance(clade, terminal)
            # 更新最大距离
            max_distance = max(max_distance, distance)
            # 收集末端节点名称
            terminal_names.append(terminal.name)

        # 存储最大距离、末端节点名称和数量
        node_info[clade] = (max_distance, terminal_names, len(terminal_names))

    # 生成CSV文件名
    output_file = os.path.splitext(input_file)[0] + "_distance_terminals_count.csv"

    # 将每个节点下的最远末端节点的距离、所有末端节点名称和数量保存到CSV文件
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Node', 'Max Distance to Terminal', 'Terminal Names', 'Number of Terminals'])  # 写入标题行
        for node, (distance, terminals, count) in node_info.items():
            terminals_str = '; '.join(terminals)
            writer.writerow([str(node), distance, terminals_str, count])    # 写入数据行

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py input_file")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    calculate_distances_terminals_and_count(input_file_path)
