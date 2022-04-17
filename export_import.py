#!/usr/bin/env python3.10

import networkx as nx
import numpy as np

import matplotlib.cm as cm

def export_data(G:nx.DiGraph, posG3D, partition_dict, cmap, step=None):
    # make a dictonary {node: rgb_values}

    ####################################
    ## color based on node clustering ##
    ####################################
    #number_of_partitions = max(partition_dict.values())+1
    #rgb_alpha = [list(cmap.colors[i]) for i in range(0, number_of_partitions)]
    #node_partition = list(partition_dict.items())
    #node_color = {node: rgb_alpha[partition] for  node, partition in node_partition}

    ####################################
    ## color based on degree centrality ##
    ####################################
    deg = dict(G.degree())
    s_deg = list(set(deg.values()))
    cmap = cm.get_cmap('Reds', len(s_deg))
    rgb_alpha = cmap(np.arange(0, cmap.N))
    node_alpha = {node: 1 for node, L in deg.items()}
    node_color = {node: rgb_alpha[s_deg.index(degree)] for  node, degree in deg.items()}
    #node_alpha = {node: 100/max(deg.values()) * L for node, L in deg.items()}

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
        f = open(f'./data/nodes_step{step}.csv','w')
    else:
        f = open(f'./data/nodes.csv','w')

    d_node_rowID = {}
    cc = 0
    for node, xyz in sorted(posG3D.items()):
        d_node_rowID[node] = cc
        x = xyz[0]
        y = xyz[1]
        z = xyz[2]

        xn = (x-min_x)/(max_x-min_x)
        yn = (y-min_y)/(max_y-min_y)
        zn = (z-min_z)/(max_z-min_z)

        r = int(255*node_color[node][0])
        g = int(255*node_color[node][1])
        b = int(255*node_color[node][2])
        alpha = int(node_alpha[node]*node_color[node][3])
        node_size = deg[f'{node}']/max(s_deg) * 100
        name = str(node)
        f.write('%s,%s,%s,%s,%s,%s,%s,%s,%s\n' %(xn,yn,zn,r,g,b,alpha,node_size,name))
        cc += 1

    f.close()

    if step != None:
        f = open(f'./data/edges_step{step}.csv','w')
    else:
        f = open(f'./data/edges.csv','w')

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
        node_size = float(line.strip().split(',')[7])
        color = f'rgba({r}, {g}, {b}, {alpha})'
        d_nodecolors[str(cc)] = color

        hinfo = line.strip().split(',')[8]
        d_hoverinfo[str(cc)] = hinfo

        d_nodesize[str(cc)] = node_size

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
