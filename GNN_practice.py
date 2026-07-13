# ノードの一覧
nodes = ["A", "B", "C", "D", "E"]

# エッジの一覧
edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D"),
    ("D", "E"),
]

# 各ノードの隣接ノードを保存する辞書
adjacency = {
    node: [] for node in nodes
}

# 無向グラフなので、両方向に登録する
for node1, node2 in edges:
    adjacency[node1].append(node2)
    adjacency[node2].append(node1)

# 隣接ノードを表示する
for node in nodes:
    print(node, "の隣接ノード:", adjacency[node])

# 隣接ノード数を表示する
for node in nodes:
    print(node, "の隣接ノード数", len(adjacency[node]))

# 最も次数の大きいノードを表示する
max_degree = 0
max_node = ""

for node in nodes:
    degree = len(adjacency[node])

    if degree > max_degree:
        max_degree = degree
        max_node = node
    
print ("最も次数が大きいノード:", max_node)

node_features = {
    "A": 1.0,
    "B": 2.0,
    "C": 3.0,
    "D": 4.0,
    "E": 5.0,
}

updated_features = {}

for node in nodes:
    total = node_features[node]

    for neighbor in adjacency[node]:
        total += node_features[neighbor]

    count = 1 + len(adjacency[node])
    updated_features[node] = total

print("更新前")
print(node_features)

print("更新後")
print(updated_features)