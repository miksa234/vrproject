#!/usr/bin/env python3.10

import networkx as nx
import numpy as np

import matplotlib.cm as cm

def export_data(G:nx.DiGraph, posG3D, node_color, node_alpha, chosen_nodes=[], path='./', step=None):

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
            alpha = 100
        else:
            r = int(255*node_color[node][0])
            g = int(255*node_color[node][1])
            b = int(255*node_color[node][2])
            alpha = node_alpha[node]

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

def read_data(nodes_file, edges_file):
    f = open(nodes_file,'r')
    lines = f.readlines()

    posG3D = {}
    d_nodecolors = {}
    d_hoverinfo = {}
    d_nodesize = {}

    cc = 0
    for line in lines:
        x = float(line.strip().split(',')[0])
        y = float(line.strip().split(',')[1])
        z = float(line.strip().split(',')[2])
        posG3D[str(cc)] = (x,y,z)

        r = float(line.strip().split(',')[3])
        g = float(line.strip().split(',')[4])
        b = float(line.strip().split(',')[5])
        alpha = float(line.strip().split(',')[6])
        color = f'rgba({r}, {g}, {b}, {alpha})'
        d_nodecolors[str(cc)] = color

        hinfo = line.strip().split(',')[7]
        d_hoverinfo[str(cc)] = hinfo

        d_nodesize[str(cc)] = 8

        cc += 1

    f.close()

    f = open(edges_file,'r')
    lines = f.readlines()

    G = nx.Graph()

    for line in lines:
        u = line.strip().split(',')[0]
        v = line.strip().split(',')[1]
        G.add_edge(u,v)
    f.close()
    return G, d_hoverinfo, d_nodecolors, d_nodesize, posG3D
