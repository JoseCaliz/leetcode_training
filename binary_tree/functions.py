from graphviz import Digraph
from IPython.display import Image
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def create_tree(nums:list) -> TreeNode:
    """
    :type nums: List[int]
    :rtype: TreeNode 
    """
    t = TreeNode(nums[0])
    curr = t
    slow, fast = 0, 1
    stack = deque([t])
    
    def attach(head:TreeNode, val=0, is_left=True): 
        if is_left:
            head.left = TreeNode(val)
        else:
            head.right = TreeNode(val)
            
    while fast < len(nums):
        curr = stack.popleft()
        
        if fast < len(nums):
            attach(curr, nums[fast], True)
            stack.append(curr.left)
            
        if fast + 1 < len(nums):
            attach(curr, nums[fast+1], False)
            stack.append(curr.right)
            
        fast += 2    
        
    return t    

def visualize_tree(tree):
    """
    :type tree: TreeNode
    :rtype dot: Dot
    """
    def add_nodes_edges(tree, dot=None):
        # Create Digraph object
        if dot is None:
            dot = Digraph()
            dot.node(name=str(tree), label=str(tree.val))

        # Add nodes
        if tree.left:
            dot.node(name=str(tree.left) ,label=str(tree.left.val))
            dot.edge(str(tree), str(tree.left))
            dot = add_nodes_edges(tree.left, dot=dot)
            
        if tree.right:
            dot.node(name=str(tree.right) ,label=str(tree.right.val))
            dot.edge(str(tree), str(tree.right))
            dot = add_nodes_edges(tree.right, dot=dot)

        return dot
    
    # Add nodes recursively and create a list of edges
    dot = add_nodes_edges(tree)

    # Visualize the graph
#     display(dot)
    
    return dot