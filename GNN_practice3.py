import numpy as np

nodes = ["A", "B", "C", "D", "E"]

edges = [
    ("A", "B"),
    ("B", "C"),
    ("B", "D"),
    ("C", "D"),
    ("D", "E"),
]

node_to_index = {
    node: index for index, node in enumerate(nodes)
}

print("ノード番号")
print(node_to_index)