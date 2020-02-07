class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
	
    def levelOrder(self,root):
        
        queue_list =[root] if root else []
        while queue_list:
            node = queue_list.pop()
            print(node.data, end=" ")
        
            if node.left: queue_list.insert(0,node.left)
            if node.right: queue_list.insert(0,node.right)

print("Type out your input:")
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
print(myTree.levelOrder(root))