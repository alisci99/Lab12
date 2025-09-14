import copy

from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.graph = nx.Graph()
        self._idMap = {}
        self.volumes = {}

        self.pesoM = 0
        self.cammino = []

    def fillDD(self):
        anni = DAO.get_years()
        countries = DAO.get_countries()
        return anni, countries

    def crea_grafo(self, year, country):
        self.graph.clear()
        self._idMap.clear()
        nodes = DAO.get_nodes( country)
        for node in nodes:
            self._idMap[node.Retailer_code] = node
        self.graph.add_nodes_from(nodes)

        edges = DAO.get_edges(year, country, self._idMap)
        for e in edges:
            self.graph.add_edge(e[0], e[1], weight=e[2])
        print (self.graph.number_of_nodes(), self.graph.number_of_edges())
        print (len(nodes))

    def get_graph_details(self):
        nNodes = self.graph.number_of_nodes()
        nEdges = self.graph.number_of_edges()
        return nNodes, nEdges


    def get_volume(self):
        """mappa_volumi = {}
        for n in self.graph.nodes():
            somma = 0
            for a in self.graph.adj[n]:
                somma += self.graph[n][a]['weight']
            mappa_volumi[n] = somma
        return mappa_volumi"""

        self.volumes = {}
        for node in self.graph.nodes():
            vol = sum(data.get("weight", 1) for _, _, data in self.graph.edges(node, data=True))
            self.volumes[node] = vol
        return self.volumes

    def get_cammino(self, N):
        self.pesoM=0
        self.cammino=[]

        parziale=[]

        for nodo in self.graph.nodes():
            parziale.append(nodo)
            self.ricorsione(parziale, N)
            parziale.pop(nodo)

        return self.pesoM, self.cammino

    def ricorsione(self, parziale, N):
        if len(parziale) == N :
            if self.calcolacosto(parziale) > self.pesoM:
                self.pesoM = self.calcolacosto(parziale)
                self.cammino = copy.deepcopy(parziale)


        for nodo in self.graph.neighbors(parziale[-1]):
            if len(parziale) == N-1 and nodo != parziale[0]:
                return

            if nodo not in parziale:
                parziale.append(nodo)
                self.ricorsione(parziale, N)
                parziale.pop()



    def calcolacosto(self, parziale):
        sommaPesi=0
        for nodo in parziale:
            sommaPesi += self.volumes[nodo]
        return sommaPesi
