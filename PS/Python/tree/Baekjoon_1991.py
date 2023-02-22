import sys

N = int(sys.stdin.readline())

graph = {} 

for _ in range(N):
  [root, leftChild, rightChild] = sys.stdin.readline().strip().split(' ')

  graph[root] = [leftChild, rightChild]

preorderTraversal = []
inorderTraversal = []
postorderTraversal = []

def preorderTravelTree(currentNode):
  if currentNode == '.':
    return

  [leftChild, rightChild] = graph[currentNode]

  preorderTraversal.append(currentNode)
  
  preorderTravelTree(leftChild)
  preorderTravelTree(rightChild)

def inorderTravelTree(currentNode):
  if currentNode == '.':
    return

  [leftChild, rightChild] = graph[currentNode]

  inorderTravelTree(leftChild)
  
  inorderTraversal.append(currentNode)

  inorderTravelTree(rightChild)


def postorderTravelTree(currentNode):
  if currentNode == '.':
    return

  [leftChild, rightChild] = graph[currentNode]

  postorderTravelTree(leftChild)
  postorderTravelTree(rightChild)

  postorderTraversal.append(currentNode)


preorderTravelTree('A')
inorderTravelTree('A')
postorderTravelTree('A')

print("".join(preorderTraversal))
print("".join(inorderTraversal))
print("".join(postorderTraversal))
