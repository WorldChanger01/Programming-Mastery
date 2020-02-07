# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 17:45:03 2020

@author: WorldChanger
"""
import collections

def breadth_first_search(graph, root):
     visited, queue = set(), collections.deque([root])
     visited.add(root)
     
     while queue:
         vertex = queue.popleft()
         try:
             for neighbour in graph[vertex]:
                 if neighbour not in visited:
                     visited.add(neighbour) 
                     queue.append(neighbour) 
         except KeyError:
             pass
     return visited
                 
if __name__ == '__main__':
    graph = {4:[2, 6], 2: [1, 3], 6: [5,7]} 
    print(breadth_first_search(graph, 4))