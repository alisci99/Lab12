from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self.graph = nx.Graph()
        self._idMap = {}

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
        mappa_volumi = {}
        for n in self.graph.nodes():
            somma = 0
            for a in self.graph.adj[n]:
                somma += self.graph[n][a]['weight']
            mappa_volumi[n] = somma
        return mappa_volumi


