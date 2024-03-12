import pydot
import pandas as pd

nodes = []
edges = []

graphs = pydot.graph_from_dot_file('consCG_final.dot')

type_dict = {'box':'ValPN','box3d':'FIObjPN','diamond':'DummyValPN',\
             'hexagon':'GepValPN','doubleoctagon':'GepObjPN','tab':'DummyObjPN','Mrecord':'RetPN',\
             'octagon':'VarArgPN','component':'ObjPN'
             }
color_dict = {'green':'Address','blue':'Store','red':'Load','black':'Copy','purple':'octagon'}

def get_nodes(graph):
    for node in graph.get_nodes():
        attributes = node.get_attributes()
        node_id = node.get_name()
        svf_id = attributes.get('label', 'N/A').strip('"{').strip('}"')
        svf_id = int(svf_id.split(':')[0])
        node_type = type_dict[attributes.get('shape','N/A')]
        nodes.append((node_id, node_type, svf_id))

def get_edges(graph):
    for edge in graph.get_edges():
        source = edge.get_source()
        target = edge.get_destination()
        type = color_dict[edge.get_attributes().get('color', 'N/A')]
        edges.append((source, target, type))


for graph in graphs:
    get_nodes(graph)
    get_edges(graph)

nodes_df = pd.DataFrame(nodes)
edges_df = pd.DataFrame(edges)
nodes_df.to_csv('nodes.csv', index=False)
edges_df.to_csv('edges.csv', index=False)
