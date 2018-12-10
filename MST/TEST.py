
import time


def benchmark(f):
    """
    Декоратор @benchmark для вычисления времени работы функции f
    """
    def _benchmark(*args, **kw):
        t = time.clock()
        rez = f(*args, **kw)
        t = time.clock() - t
        print('{0} time elapsed {1:.8f}'.format(f.__name__, t))
        return rez
    return _benchmark


class WeightedGraph:
    def __init__(self, n):
        self.graph = [[0 for _ in range(n)]for _ in range(n)]
        self.vertices = n

    def __getitem__(self, item):
        return self.graph[item]

    def __setitem__(self, key, value):
        self[key] = value

    def addEdge(self, v1, v2, w):
        self[v1][v2] = w

# Union find data structure for quick kruskal algorithm
class UF:
    def __init__(self, N):
        self._id = [i for i in range(N)]

    # judge two node connected or not
    def connected(self, p, q):
        return self._find(p) == self._find(q)

    # quick union two component
    def union(self, p, q):
        p_root = self._find(p)
        q_root = self._find(q)
        if p_root == q_root:
            return
        self._id[p_root] = q_root

    # find the root of p
    def _find(self, p):
        while p != self._id[p]:
            p = self._id[p]
        return p


# prim algorithm
@benchmark
def prim(G):
    # initialize the MST and the set X
    MST = set()
    X = set()

    # select an arbitrary vertex to begin with
    X.add(0)
    while len(X) != G.vertices:
        crossing = set()
        # for each element x in X, add the edge (x, k) to crossing if
        # k is not in X
        for x in X:
            for k in range(G.vertices):
                if k not in X and G[x][k] != 0:
                    crossing.add((x, k))
        # find the edge with the smallest weight in crossing
        edge = sorted(crossing, key=lambda e: G[e[0]][e[1]])[0]
        # add this edge to MST
        MST.add(edge)
        # add the new vertex to X
        X.add(edge[1])
    return MST


# kruskal algorithm
def kruskal(G):
    # initialize MST
    MST = set()
    edges = set()
    # collect all edges from graph G
    for j in range(G.vertices):
        for k in range(G.vertices):
            if G[j][k] != 0 and (k, j) not in edges:
                edges.add((j, k))
    # sort all edges in graph G by weights from smallest to largest
    sorted_edges = sorted(edges, key=lambda e: G[e[0]][e[1]])
    uf = UF(G.vertices)
    for e in sorted_edges:
        u, v = e
        # if u, v already connected, abort this edge
        if uf.connected(u, v):
            continue
        # if not, connect them and add this edge to the MST
        uf.union(u, v)
        MST.add(e)
    return MST
kruskal = benchmark(kruskal)

if __name__ == '__main__':
    WG = WeightedGraph(4)
    WG.addEdge(0, 1, 2)
    WG.addEdge(2, 1, 3)
    WG.addEdge(1, 3, 1)
    WG.addEdge(0, 2, 5)
    print("================USING PRIM ALGORITHM================")
    MST = prim(WG)
    # print the edges of the MST
    for edge in MST:
        print(edge)
    print("================USING KRUSKAL ALGORITHM================")
    MST = kruskal(WG)
    # print the edges of the MST
    for edge in MST:
        print(edge)
    WG = WeightedGraph(4)
    WG.addEdge(0, 1, -2)
    WG.addEdge(2, 1, -3)
    WG.addEdge(1, 3, -1)
    WG.addEdge(0, 2, -5)
    print("================MAX PRIM ALGORITHM================")
    MST = prim(WG)
    # print the edges of the MST
    for edge in MST:
        print(edge)
    print("================MAX KRUSKAL ALGORITHM================")
    MST = kruskal(WG)
    # print the edges of the MST
    for edge in MST:
        print(edge)

