#!/usr/bin/evn python3.10

import matplotlib.pyplot as plt
import matplotlib.cm as cm

import plotly
import plotly.graph_objs as pgo

def get_trace_nodes_3D_legend(posG, info, color, size, legend_names = None, linewidth=0.000001, opac = 0.9):
    '''
    Get trace of nodes for plotting in 3D.
    Input:
    - posG = dictionary with nodes as keys and coordinates as values.
    - info = hover information for each node, e.g. a dictionary with node IDs and values = hover information
    - color = a dictionary of key = association name for each color (for legend) and value = hex color
    - size = a dictionary with node Ids and values=sizes of nodes
    - legend_names = list of values e.g. strings for each color
    - linewidth = float; contour of nodes
    - opac = transparency of nodes

    Return a trace for plotly graph objects plot including a legend.
    '''

    # dividing traces based on unique colors > for legend
    color_dict = {}
    for i in set(color.values()):
        sublist = []
        for k,v in color.items():
            if v == i:
                sublist.append(k)
        color_dict[i]= sublist

    d_col_pos = {}
    for i,j_list in color_dict.items():
        sub = {}
        for ix,(k,v) in enumerate(posG.items()):
            if k in j_list:
                #sub[ix] = v
                sub[k] = v
            d_col_pos[i] = sub
    d_col_pos_ordered = dict(sorted(d_col_pos.items(),reverse=True))

    # creating traces
    traces = []

    if legend_names is not None and len(legend_names) == len(set(color.values())):

        for elem,(col, dct) in enumerate(d_col_pos_ordered.items()):

            ids = list(dct.keys())
            coords = list(dct.values())

            l_info_sorted_to_ids = [(info[key]) for key in ids] #{key:info[key] for key in ids}
            #l_info_sorted_to_ids = list(info_sorted_to_ids.values())

            l_size_sorted_to_ids = [(size[key]) for key in ids] #{key:size[key] for key in ids}
            #l_size_sorted_to_ids = list(size_sorted_to_ids.values())

            trace = pgo.Scatter3d(x=[i[0] for i in coords],
                                  y=[i[1] for i in coords],
                                  z=[i[2] for i in coords],
                                  mode = 'markers',
                                  text = l_info_sorted_to_ids,
                                  hoverinfo = 'text',
                                       marker = dict(
                            color = col,
                            size = l_size_sorted_to_ids,
                            symbol = 'circle',
                            line = dict(width = linewidth,
                                    color = 'dimgrey'),
                            opacity = opac,
                        ),
                    name = "Group: "+str(list(legend_names.values())[elem])
                    )
            traces.append(trace)
        return traces

    else:
        for elem,(col, dct) in enumerate(d_col_pos_ordered.items()):

            ids = list(dct.keys())
            coords = list(dct.values())

            l_info_sorted_to_ids = [(info[key]) for key in ids] #{key:info[key] for key in ids}
            #l_info_sorted_to_ids = list(info_sorted_to_ids.values())

            l_size_sorted_to_ids = [(size[key]) for key in ids] #{key:size[key] for key in ids}
            #l_size_sorted_to_ids = list(size_sorted_to_ids.values())

            trace = pgo.Scatter3d(x=[i[0] for i in coords],
                                  y=[i[1] for i in coords],
                                  z=[i[2] for i in coords],
                                  mode = 'markers',
                                  text = l_info_sorted_to_ids,
                                  hoverinfo = 'text',
                                       marker = dict(
                            color = col,
                            size = l_size_sorted_to_ids,
                            symbol = 'circle',
                            line = dict(width = linewidth,
                                    color = 'dimgrey'),
                            opacity = opac,
                        ),
                    name = "Group: "+str(elem)
                    )
            traces.append(trace)
        return traces


def get_trace_edges_3D(G, posG, color = '#C7C7C7', opac = 0.1, linewidth=0.1):
    '''
    Get trace of edges for plotting in 3D.
    Input:
    - G = Graph
    - posG = dictionary with nodes as keys and coordinates as values.
    - color = string; hex color
    - opac = transparency of edges e.g. 1.2
    - linewidth = float;

    Return a trace for plotly graph objects plot.
    '''

    edge_x = []
    edge_y = []
    edge_z = []
    for edge in G.edges():
            x0, y0, z0 = posG[edge[0]]
            x1, y1, z1 = posG[edge[1]]
            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)
            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)
            edge_z.append(z0)
            edge_z.append(z1)
            edge_z.append(None)

    trace_edges = pgo.Scatter3d(
                                x = edge_x,
                                y = edge_y,
                                z = edge_z,
                                mode = 'lines', hoverinfo='none',
                                line = dict(width = linewidth, color = color),
                                opacity = opac,
                                name = "Links"
                        )

    return trace_edges


# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------

# P L O T T I N G

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------



def plot_3D(data,path,fname, scheme='light',annotat=None, show_leg=True):
    '''
    Create a 3D plot from traces using plotly.
    Input:
    - data = list of traces
    - filename = string
    - scheme = 'light' or 'dark'
    - annotations = None or plotly annotations

    Return plot in 3D and file, saved as html.
    '''

    fig = pgo.Figure()

    for i in data:
        fig.add_trace(i)

    if scheme == 'dark' and annotat==None:
        fig.update_layout(template='plotly_dark',
                          showlegend=show_leg, autosize = True,
                          scene=dict(
                              xaxis_title='',
                              yaxis_title='',
                              zaxis_title='',
                              xaxis=dict(nticks=0,tickfont=dict(
                                    color='black')),
                              yaxis=dict(nticks=0,tickfont=dict(
                                    color='black')),
                              zaxis=dict(nticks=0,tickfont=dict(
                                    color='black')),
                            dragmode="turntable"
                        ))

    elif scheme == 'dark':
        fig.update_layout(template='plotly_dark',
                          showlegend=show_leg, autosize = True,
                                  scene=dict(
                                      xaxis_title='',
                                      yaxis_title='',
                                      zaxis_title='',
                                      xaxis=dict(nticks=0,tickfont=dict(
                                            color='black')),
                                      yaxis=dict(nticks=0,tickfont=dict(
                                            color='black')),
                                      zaxis=dict(nticks=0,tickfont=dict(
                                            color='black')),
                                    dragmode="turntable",
                                    annotations=annotat,
                                ))

    elif scheme == 'light' and annotat==None:
        fig.update_layout(template='plotly_white',
                          showlegend=show_leg, width=1200, height=1200,
                          scene=dict(
                              xaxis_title='',
                              yaxis_title='',
                              zaxis_title='',
                              xaxis=dict(nticks=0,tickfont=dict(
                                    color='white')),
                              yaxis=dict(nticks=0,tickfont=dict(
                                    color='white')),
                              zaxis=dict(nticks=0,tickfont=dict(
                                    color='white')),
                            dragmode="turntable",
                        ))

    elif scheme == 'light':
        fig.update_layout(template='plotly_white',
                          showlegend=show_leg, width=1200, height=1200,
                          scene=dict(
                              xaxis_title='',
                              yaxis_title='',
                              zaxis_title='',
                              xaxis=dict(nticks=0,tickfont=dict(
                                    color='white')),
                              yaxis=dict(nticks=0,tickfont=dict(
                                    color='white')),
                              zaxis=dict(nticks=0,tickfont=dict(
                                    color='white')),
                            dragmode="turntable",
                            annotations = annotat
                        ))
    else:
        print('Oops, something went wrong. Please check input parameters.')

    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    fig.write_html(path+fname+'.html')

    return plotly.offline.plot(fig, filename = path+fname+'.html', auto_open=True)
