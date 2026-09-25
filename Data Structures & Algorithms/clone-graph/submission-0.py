class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        copy = Node(node.val, [])

        visited = {node: copy}
        
        def dfs(node, copyNode):
            for n in node.neighbors:
                if n in visited:
                    copyNode.neighbors.append(visited[n])
                    continue

                newNode = Node(n.val, [])
                visited[n] = newNode
                copyNode.neighbors.append(newNode)
                dfs(n, newNode)

        dfs(node, copy)

        return copy