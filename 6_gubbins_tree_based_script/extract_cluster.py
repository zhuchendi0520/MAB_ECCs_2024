import sys
from Bio import Phylo
import os
import csv

def get_terminals_under_clade(clade):
    """获取给定节点下的所有末端节点"""
    return list(clade.find_clades(terminal=True))

def select_nodes(tree, node_info, threshold):
    all_terminals = set(tree.get_terminals())
    selected_nodes = {}
    covered_terminals = set()
    cluster_id = 1

    # 记录每个cluster包含的菌株数量
    cluster_counts = {}

    # 选择小于阈值的节点，并按覆盖的末端节点数量排序
    eligible_nodes = [(node, info) for node, info in node_info.items() if info[0] < threshold]
    sorted_nodes = sorted(eligible_nodes, key=lambda x: -x[1][2])

    for node, _ in sorted_nodes:
        if covered_terminals == all_terminals:
            break
        node_terminals = set(get_terminals_under_clade(node))
        if not node_terminals.issubset(covered_terminals):
            for terminal in node_terminals:
                selected_nodes[terminal.name] = cluster_id
            covered_terminals.update(node_terminals)
            cluster_counts[cluster_id] = len(node_terminals)
            cluster_id += 1

    # 查找只有一个菌株的cluster
    single_member_clusters = [cluster_id for cluster_id, count in cluster_counts.items() if count == 1]
    for terminal, cluster_id in selected_nodes.items():
        if cluster_id in single_member_clusters:
            selected_nodes[terminal] = "others"

    return selected_nodes

def calculate_distances_terminals_and_count(input_file, threshold):
    tree = Phylo.read(input_file, "newick")
    node_info = {}

    for clade in tree.find_clades():
        max_distance = 0
        terminal_names = []
        terminals = get_terminals_under_clade(clade)
        for terminal in terminals:
            distance = tree.distance(clade, terminal)
            max_distance = max(max_distance, distance)
            terminal_names.append(terminal.name)
        node_info[clade] = (max_distance, terminal_names, len(terminal_names))

    # 选择节点
    selected_nodes = select_nodes(tree, node_info, threshold)

    # 输出信息
    output_file = os.path.splitext(input_file)[0] + "_selected_node_info.csv"
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Strains', 'Cluster'])
        for terminal, cluster_id in selected_nodes.items():
            writer.writerow([terminal, cluster_id])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py input_file threshold")
        sys.exit(1)

    input_file_path = sys.argv[1]
    threshold = float(sys.argv[2])
    calculate_distances_terminals_and_count(input_file_path, threshold)
