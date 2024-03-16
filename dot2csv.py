import pydot
import pandas as pd
import shutil
import sys

def main(dot_file, target_database):
    '''
    Need change: The /import file of your target database
    '''
    target_path = target_database

    graphs = pydot.graph_from_dot_file(dot_file)
    source_file = ['nodes.csv', 'edges.csv']

    type_dict = {'box':'ValPN','box3d':'FIObjPN','diamond':'DummyValPN',\
                'hexagon':'GepValPN','doubleoctagon':'GepObjPN','tab':'DummyObjPN','Mrecord':'RetPN',\
                'octagon':'VarArgPN','component':'ObjPN'
                }
    color_dict = {'green':'Address','blue':'Store','red':'Load','black':'Copy','purple':'octagon'}

    nodes = []
    edges = []

    for graph in graphs:
        for node in graph.get_nodes():
            attributes = node.get_attributes()
            node_id = node.get_name()
            svf_id = attributes.get('label', 'N/A').strip('"{').strip('}"')
            svf_id = int(svf_id.split(':')[0])
            node_type = type_dict[attributes.get('shape','N/A')]
            nodes.append((node_id, node_type, svf_id))
        for edge in graph.get_edges():
            source = edge.get_source()
            target = edge.get_destination()
            type = color_dict[edge.get_attributes().get('color', 'N/A')]
            edges.append((source, target, type))

    nodes_df = pd.DataFrame(nodes)
    edges_df = pd.DataFrame(edges)
    nodes_df.to_csv('nodes.csv', index=False)
    edges_df.to_csv('edges.csv', index=False)

    for file in source_file:
        destination_file = target_path + '/' + file.split('/')[-1]
        shutil.copy(file, destination_file)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please input the .dot file and the /import file of your database")
        sys.exit(1)
    main(sys.argv[1])