"""
https://leetcode.com/problems/find-if-path-exists-in-graph/description/
"""

class Solution(object):
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        def depthFirstSearch(adj, source, destination):
            stack_dfs = [ source ]
            Lookup = set(stack_dfs)
            while stack_dfs:
                pos = stack_dfs.pop()
                if pos == destination: return True
                for nei in reversed(adj[pos]):
                    if nei in Lookup:
                        continue
                    Lookup.add(nei)
                    stack_dfs.append(nei)
            return False
        
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return depthFirstSearch(adj, source, destination)