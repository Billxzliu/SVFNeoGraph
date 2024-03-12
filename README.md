# SVFNeoGraph
Here are two scripts that convert the SVF-generated Constraint Graph in .dot format into CSV format and import it into Neo4j to form a graph database. If you want to know more about SVF and Constraint Graph, please follow the [Technical documentation](https://github.com/svf-tools/SVF/wiki/Technical-documentation) of [SVF](https://github.com/SVF-tools/SVF).

We will be updating more SVF on Neo4j extension projects, please follow us if you are interested in our projects😺!

# How to use
1. Modify the file path in **dot2csv.py**
2. Run **dot2csv.py**
3. Put the generated nodes.csv and edges.csv into the **import** folder of your database's local folder, and modify the database-related information in **import2neo4j.py**
4. Run **import2neo4j.py**

