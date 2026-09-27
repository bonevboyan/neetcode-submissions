class Node:
  def __init__(self, i, inEdges, outEdges):
    self.i = i
    self.inEdges = inEdges
    self.outEdges = outEdges

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = []

        for i in range(numCourses):
            node = Node(i, set(), set())
            nodes.append(node)

        for prer in prerequisites:
            course = prer[0]
            pre = prer[1]

            courseNode = nodes[course]
            preNode = nodes[pre]

            nodes[course].inEdges.add(preNode)
            nodes[pre].outEdges.add(courseNode)

        queue = []

        count = 0

        for node in nodes:
            if len(node.inEdges) == 0:
                count = count + 1
                queue.append(node)

        while len(queue) != 0:
            current = queue.pop()
            out = current.outEdges.copy()

            for node in out:
                current.outEdges.remove(node)
                node.inEdges.remove(current)

                if len(node.inEdges) == 0:
                    count = count + 1
                    queue.append(node)


        return count == numCourses




        
            
            
        