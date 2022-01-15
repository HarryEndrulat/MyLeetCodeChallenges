import queue
import networkx as nx


class Solution(object):
    def createGraph(self, arr):
        g=nx.Graph()

        for i,x in enumerate(arr):
            if i==0:
                g.add_node(i, value=x)
                g.add_node(i+1, value=arr[i+1])
                g.add_edge(i, i+1, weight=1)
            if i>0 and i<len(arr)-1:
                g.add_node(i+1, value=arr[i+1])
                g.add_edge(i-1, i, weight=1)
                g.add_edge(i, i+1, weight=1)
            if i==len(arr)-1:
                g.add_edge(i-1, i, weight=1)
        for i,x in enumerate(arr):
            for j,y in enumerate(arr):
                if x==y and i!=j:
                    g.add_edge(i, j, weight=1)
        nx.set_node_attributes(g, 'white', 'color')
        nx.set_node_attributes(g, 0, 'weight')
        return g

    def minJumps(self, arr):
        if len(arr)<2:
            return 0
        if arr[0] == arr[len(arr) - 1]:
            return 1
        g=Solution.createGraph(self,arr)
        distance=Solution.minJumpsBFS(self,g,list(g)[0])

        return distance

    def minJumpsBFS(self, g, startingV):
        distance=0
        q=queue.Queue(maxsize=0)
        q.put(startingV)
        g.nodes[startingV]['color']='gray'
        while not q.empty():
            x=q.get()
            g.nodes[x]['color'] = 'black'
            edges=g.edges(x, data=True)
            for u, v, wt in edges:
                if g.nodes[v]['color'] == 'white':
                    q.put(v)
                    g.nodes[v]['color'] = 'gray'
                    g.nodes[v]['weight'] = g.nodes[u]['weight']+1
                if v==g.number_of_nodes()-1:
                    return g.nodes[v]['weight']
        return distance
