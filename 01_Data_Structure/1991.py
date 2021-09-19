"""
- 트리 순회
트리를 만들고 재귀를 활용해 출력
"""


class Tree:
    index = None
    left = None
    right = None

    def __init__(self, index, left=".", right="."):
        self.index = index
        if left != ".":
            self.left = Tree(left)
        if right != ".":
            self.right = Tree(right)

    def insert(self, index, left, right):
        if self.index == index:
            self.left = Tree(left)
            self.right = Tree(right)
        if self.left is not None:
            self.left.insert(index, left, right)
        if self.right is not None:
            self.right.insert(index, left, right)

    def preorder(self):
        if self.index != ".":
            print(self.index, end="")
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        if self.index != ".":
            print(self.index, end="")
        if self.right is not None:
            self.right.inorder()

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        if self.index != ".":
            print(self.index, end="")


tree = Tree("A")
for _ in range(int(input())):
    tmp = input().split()
    tree.insert(*tmp)

tree.preorder()
print()
tree.inorder()
print()
tree.postorder()
print()
