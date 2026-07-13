import numpy as np

nodes = ["A", "B", "C", "D", "E"]

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D"),
    ("D", "E"),
]

node_to_index = {
    node: index for index, node in enumerate(nodes)
}

print("ノード番号")
print(node_to_index)

adjacency_matrix = node_to_index

node_features = np.array([
    1.0,
    2.0,
    3.0,
    4.0,
    5.0,
])

print("特徴量")
print(node_features)

neighbor_sum = adjacency_matrix @ node_features

print("隣接ノードの特徴量合計")
print(neighbor_sum)

identity_matrix = np.eye(len(nodes))

print("単位行列")
print(identity_matrix)

adjacency_with_self_loop = adjacency_matrix + identity_matrix

print("自己ループ付き隣接行列")
print(adjacency_with_self_loop)

updated_features = adjacency_with_self_loop @ node_features

print("更新前")
print(node_features)

print("更新後")
print(updated_features)

for index, node in enumerate(nodes):
    print(node, "の更新後の特徴量:", updated_features[index])