class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes = []
        
        for i in range(n):
          nodes.append([])

        for edge in edges:
          fromVal = edge[0]
          toVal = edge[1]
          nodes[fromVal].append(toVal)
          nodes[toVal].append(fromVal)

        stack = []
        stack.append((0, None))
        visited = set()

        while len(stack) != 0:
          current = stack.pop()

          i = current[0]
          parent = current[1]

          visited.add(i)

          neighbors = nodes[i]

          for nb in neighbors:
            if nb == parent:
              continue
            if parent != nb and nb in visited:
              return False

            stack.append((nb, i))

        print(visited)
        print(len(visited))
        print(n)
        return len(visited) == n




          






        