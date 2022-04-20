#/usr/bin/env python3.10

import pandas as pd
import networkx as nx

def get_graph(data:pd.DataFrame, cut:int, direction=""):
    DG = nx.from_pandas_edgelist(data, source='package', target='requirement',\
                                 create_using=nx.DiGraph())
    DG.remove_nodes_from(['.', 'NaN'])
    if direction == "":
        to_remove = [n[0] for n in DG.degree() if n[1] <= cut]
        DG.remove_nodes_from(to_remove)
    elif direction == "in":
        to_remove = [n[0] for n in DG.in_degree() if n[1] <= cut]
        DG.remove_nodes_from(to_remove)
    elif direction == "out":
        to_remove = [n[0] for n in DG.in_degree() if n[1] <= cut]
        DG.remove_nodes_from(to_remove)
    return DG
