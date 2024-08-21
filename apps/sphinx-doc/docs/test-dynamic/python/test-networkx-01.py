#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx
import copy
import pprint

def display_example_detals(example_details):
    """Display example details
    """

    log_prefix=f"[{example_details['function_name']}]: "

    print("")
    print(f"{log_prefix} Saving data to: {example_details['file_name']}")
    filtered_details = {k: v for k, v in example_details.items() if k not in ['function_name', 'file_name']}
    pprint.pprint(filtered_details)

def example_digraph01():
    example_details = {
        'function_name': example_digraph01.__name__,
        'file_name': 'example_digraph01.png',
        'description': 'TBU',
        'extra': 'colors, shapes, styles',
    }

    G = nx.DiGraph()
    nodes_def_attr = {
        'color'    : 'blue',
        'fillcolor': 'green',
        'fontsize' : '10',
        'shape'    : 'box',
        'style'    : 'filled',
    }

    # Define specific node attributes
    mc01_attr = {**nodes_def_attr, 'label': 'MacOS Sierra\n(Person-1)'}
    mc02_attr = {**nodes_def_attr, 'label': 'MacOS Sierra\n(Person-2)'}

    nodes_docker_attr = {**nodes_def_attr, 'fillcolor': 'cyan'}
    dd01_attr = {**nodes_docker_attr, 'label': 'Docker-Deamon01'}
    dd02_attr = {**nodes_docker_attr, 'label': 'Docker-Deamon02'}
    dd03_attr = {**nodes_docker_attr, 'label': 'Docker-Deamon03'}
    dd04_attr = {**nodes_docker_attr, 'label': 'Docker-Deamon04'}

    dcs00_attr = {**nodes_docker_attr, 'fillcolor': 'yellow', 'label': 'Ubuntu\n(official image)'}
    dcs01_attr = {**nodes_docker_attr, 'fillcolor': 'yellow', 'label': 'Ubuntu\n(In container)'}

    nodes = [
        ('systems', {}),
        ('Home', nodes_def_attr),
        ('Work', nodes_def_attr),
        ('Internet', nodes_def_attr),
        ('Person-1-laptop', nodes_def_attr),
        ('Person-1-laptop-biz', nodes_def_attr),
        ('Person-2-laptop', nodes_def_attr),
        ('Server-online', nodes_def_attr),

        ('mc01', mc01_attr),
        ('mc02', mc02_attr),
        ('OpenSUSE', nodes_def_attr),
        ('CentOS', nodes_def_attr),
        ('Windows', nodes_def_attr),

        ('Vagrant01', nodes_def_attr),
        ('Vagrant02', nodes_def_attr),

        ('dd01', dd01_attr),
        ('dd02', dd02_attr),
        ('dd03', dd03_attr),
        ('dd04', dd04_attr),
        ('docker-image', nodes_docker_attr),
        ('docker-container', nodes_docker_attr),
        ('dcs00', dcs00_attr),
        ('dcs01', dcs01_attr),
    ]
    
    edges_def_attr = {
        'splines': 'true',
        'color': 'blue',
    }
    edges = [
        ('systems', 'Home'),
        ('systems', 'Work'),
        ('systems', 'Internet'),

        ('Home', 'Person-1-laptop'),
        ('Home', 'Person-2-laptop'),
        ('Work', 'Person-1-laptop-biz'),
        ('Internet', 'Server-online'),

        ('Person-1-laptop', 'OpenSUSE'),
        ('Person-1-laptop', 'Windows'),

        ('Person-2-laptop', 'mc02'),
        ('Person-1-laptop-biz', 'mc01'),
        ('Server-online', 'CentOS'),

        ('OpenSUSE', 'Vagrant01'),
        ('mc01', 'Vagrant02'),

        ('Vagrant01', 'dd01'),
        ('Vagrant02', 'dd02'),
        ('OpenSUSE', 'dd03'),
        ('CentOS', 'dd04'),

        ('dd01', 'docker-image'),
        ('dd02', 'docker-image'),
        ('dd03', 'docker-image'),
        ('dd04', 'docker-image'),
        ('dcs00', 'docker-image'),
        ('docker-image', 'docker-container'),
        ('docker-container', 'dcs01'),
    ]
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    # print("{0}".format(G.nodes(data=True)))

    A = nx.nx_agraph.to_agraph(G)
    A.add_subgraph(['Home', 'Work', 'Internet'], rank='same')
    A.add_subgraph(['Person-1-laptop', 'Person-1-laptop-biz', 'Person-2-laptop', 'Server-online'], rank='same')
    A.add_subgraph(['Vagrant01', 'Vagrant02'], rank='same')
    A.add_subgraph(['dd01', 'dd02', 'dd03', 'dd04'], rank='same')
    A.add_subgraph(['OpenSUSE', 'mc01', 'mc02', 'CentOS', 'Windows'], rank='same')
    A.add_subgraph(['docker-container', 'docker-image', 'dcs00', 'dcs01'], rank='sink')

    display_example_detals(example_details)
    A.draw(example_details['file_name'], prog='dot')


if __name__ == '__main__':
    example_digraph01()
