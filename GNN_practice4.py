import numpy as np

nodes = ["A", "B", "C", "D", "E","F"]

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D"),
    ("D", "E"),
    ("E", "F"),
]

node_to_index = {
    node: index for index, node in enumerate(nodes)
}

adjacency_matrix = np.zeros(
    (len(nodes), len(nodes))
)

for node1, node2 in edges:
    index1 = node_to_index[node1]
    index2 = node_to_index[node2]

    adjacency_matrix[index1][index2] = 1
    adjacency_matrix[index2][index1] = 1

print("隣接行列")
print(adjacency_matrix)

print("隣接行列の形状")
print(adjacency_matrix.shape)

node_features = np.array([
    1.0,
    2.0,
    3.0,
    4.0,
    5.0,
    6.0,
])

identity_matrix = np.eye(len(nodes))
adjacency_with_self_loop = adjacency_matrix + identity_matrix

adjacency_without_self_loop = adjacency_matrix @ node_features

print("自己ループ追加前の隣接行列の特徴量")
print(adjacency_without_self_loop)

print("自己ループ付き隣接行列")
print(adjacency_with_self_loop)

updated_features = adjacency_with_self_loop @ node_features

print("更新前")
print(node_features)

print("更新後")
print(updated_features)

for index, node in enumerate(nodes):
    print(
        node,
        "の更新後の特徴量",
        updated_features[index]
    )

counts = adjacency_with_self_loop.sum(axis = 1)

print("自分自身を含めた接続数")
print(counts)

mean_features = updated_features / counts

print("平均集約の結果")
print(mean_features)