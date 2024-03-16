from neo4j import GraphDatabase
import dot2csv as dot
import sys
#********Need change: The info of your target database***********

# Your Neo4j's uri
uri = "bolt://localhost:7687"
# your database's user name
username = "neo4j"
# your database's password
password = "12345678"
# The /import file of your Neo4j database
target_path = r"D:\neo4j\relate-data\dbmss\dbms-422fcd92-2201-46d2-b297-da19fa31fff5\import".replace("\\","/")

#*****************************************************************

dot_file = sys.argv[1]
dot.main(dot_file, target_path)

driver = GraphDatabase.driver(uri, auth=(username, password))

def import_nodes(session):
    with open("nodes.csv", "r") as file:
        next(file)
        for line in file:
            graph_id, label, svf_id = line.strip().split(',')
            svf_id = int(svf_id)
            cypher_query = f"CREATE (n:{label} {{graph_id: $graph_id, svf_id: $svf_id}})"
            session.run(cypher_query, graph_id=graph_id, svf_id=svf_id)

def import_relationships(session):
    with open("edges.csv", "r") as file:
        next(file)  
        for line in file:
            source_id, target_id, relationship_type = line.strip().split(',')
            cypher_query = f"""
                MATCH (source {{graph_id: $source_id}}), (target {{graph_id: $target_id}})
                CREATE (source)-[r:{relationship_type}]->(target)
                """
            session.run(cypher_query, {"source_id": source_id, "target_id": target_id})
with driver.session(database="neo4j") as session:
    import_nodes(session)
    import_relationships(session)
driver.close()