#!/usr/bin/env python3.10

import networkx as nx
import numpy as np

import matplotlib.cm as cm

def export_data_vr(G:nx.DiGraph, posG3D, chosen_nodes, path='./', step=None):
    node_color = {node: [1, 1, 1] for node in G.nodes}

    lx = [x for x,y,z in posG3D.values()]
    ly = [y for x,y,z in posG3D.values()]
    lz = [z for x,y,z in posG3D.values()]

    min_x = min(lx)
    max_x = max(lx)
    min_y = min(ly)
    max_y = max(ly)
    min_z = min(lz)
    max_z = max(lz)

    if step != None:
        f = open(path + f'nodes_{step}.csv','w')
    else:
        f = open(path + f'nodes.csv','w')

    d_node_rowID = {}
    cc = 0
#    for node, xyz in sorted(posG3D.items()):
    for node in G.nodes():
        d_node_rowID[node] = cc
        x = posG3D[node][0]
        y = posG3D[node][1]
        z = posG3D[node][2]

        xn = (x-min_x)/(max_x-min_x)
        yn = (y-min_y)/(max_y-min_y)
        zn = (z-min_z)/(max_z-min_z)

        if str(node) in chosen_nodes:
            r = int(255)
            g = int(0)
            b = int(0)
            alpha = 200
        else:
            r = int(255*node_color[node][0])
            g = int(255*node_color[node][1])
            b = int(255*node_color[node][2])
            alpha = 100

        name = str(node)
        f.write('%s,%s,%s,%s,%s,%s,%s,%s\n' %(xn,yn,zn,r,g,b,alpha,name))
        cc += 1

    f.close()

    if step != None:
        f = open(path + f'edges_{step}.csv','w')
    else:
        f = open(path + f'edges.csv','w')

    cc = 0
    for u,v in G.edges():
        row_u = d_node_rowID[u]
        row_v = d_node_rowID[v]

        edge_color = '#999999'
        r = int(255*node_color[node][0])
        g = int(255*node_color[node][1])
        b = int(255*node_color[node][2])

        f.write('%s,%s,%s,%s,%s,%s\n' %(row_u,row_v,r,g,b,100))

    f.close()
