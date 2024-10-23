import sys
import csv
from Bio import Phylo

def extract_tip_distances(tree_file):
    # 读取系统发育树文件
    tree = Phylo.read(tree_file, "newick")
    
    # 获取根部节点
    root = tree.root
    
    # 定义一个字典来存储每个tip和其到根部节点的距离
    tip_distances = {}
    
    # 遍历每个tip
    for tip in tree.get_terminals():
        # 获取tip的名称
        tip_name = tip.name
        # 获取tip到根部节点的距离（节点高度）
        distance_to_root = tree.distance(tip, root)
        # 存储到字典中
        tip_distances[tip_name] = distance_to_root
    
    return tip_distances

def save_to_csv(input_file, tip_distances):
    # 获取输入文件的前缀
    file_prefix = input_file.split('.')[0]
    
    # 构建CSV文件路径
    output_csv_file = f"{file_prefix}_tips_to_root.csv"
    
    # 将结果保存到CSV文件中
    with open(output_csv_file, 'w', newline='') as csvfile:
        fieldnames = ['Tip', 'Distance to Root']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for tip, distance in tip_distances.items():
            writer.writerow({'Tip': tip, 'Distance to Root': distance})

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py tree_file.nwk")
        sys.exit(1)
    
    tree_file = sys.argv[1]
    tip_distances = extract_tip_distances(tree_file)
    save_to_csv(tree_file, tip_distances)

