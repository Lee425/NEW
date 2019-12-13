import os
import networkx as nx
import numpy as np
from collections import defaultdict
import pickle

class DataTools:
    def __init__(self, args):
        self.args = args
        net_name = os.path.basename(self.args.input_path).split(".")[0]
        self.save_dir = os.path.join(self.args.save_path, net_name)

        self.data = self.load_data()
        self.graph = None
        self.cache_data = defaultdict()

    def load_data(self):
        return np.loadtxt(self.args.input_path, delimiter=',', skiprows=1)

    def ori_graph(self):
        graph = nx.Graph()
        for edge in self.data:
            graph.add_edge(int(edge[0]), int(edge[1]), weight=edge[2], first_node=int(edge[0]), second_node=int(edge[1]))
        return graph
    def train_graph(self, test_x):
        for e in test_x:
            self.graph.remove_edge(*(int(e[0]), int(e[1])))
        return self.graph

    def split_data(self, save_dir, train_ratio=0.9):
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        length = len(self.data)
        index = np.random.permutation(range(length))
        train_ind = np.random.choice(index, int(length * train_ratio), replace=False)
        test_ind = list(set(index) - set(train_ind))
        train_x = self.data[train_ind]
        test_x = self.data[test_ind]
        return train_x, test_x

    def _extract_feature(self, graph, e1, e2):
        n1_neighbors = list(nx.neighbors(graph, e1))
        n2_neighbors = list(nx.neighbors(graph, e2))
        common_neighbors = set(n1_neighbors) & set(n2_neighbors)
        wx = 0.
        wy = 0.
        for cn in common_neighbors:
            wxi = graph[e1][cn]['weight']
            wyi = graph[e2][cn]['weight']
            if (wxi + wyi) == 0.:
                continue
            wx += wxi / (wxi + wyi)
            wy += wyi / (wxi + wyi)
        rx = round(wx, 4)
        ry = round(wy, 4)
        return rx, ry

    def extract_feature(self, i_th):
        self.graph = self.ori_graph()

        if os.path.exists(self.save_dir) and self.args.cache:
            cache_data = self.load_split_data(i_th)
            train_X, test_X = cache_data.get('train_X'), cache_data.get('test_X')
            return train_X, test_X
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

        train_val, test_val = self.split_data(self.args.save_path, train_ratio=self.args.train_ratio)
        graph = self.train_graph(test_val)
        train_X = np.zeros((train_val.shape[0], 3))
        test_X = np.zeros((test_val.shape[0], 3))
        for i, (e1, e2, attr) in enumerate(graph.edges(data=True)):

            e1, e2 = attr['first_node'], attr['second_node']
            w = attr['weight']
            rx, ry = self._extract_feature(graph, e1, e2)
            train_X[i] = [rx, ry, w]
        for i, e in enumerate(test_val):
            rx, ry = self._extract_feature(graph, int(e[0]), int(e[1]))
            w = e[2]
            test_X[i] = [rx, ry, w]

        self.cache_data = {'train_X': train_X, 'test_X': test_X}
        self.save_split_data(i_th)
        return train_X, test_X

    def save_split_data(self, i):
        with open(os.path.join(self.save_dir, '{}_split_pkl'.format(i+1)), 'wb') as wf:
            pickle.dump(self.cache_data, wf)

    def load_split_data(self, i):
        with open(os.path.join(self.save_dir, '{}_split_pkl'.format(i+1)), 'rb') as rf:
            return pickle.load(rf)











