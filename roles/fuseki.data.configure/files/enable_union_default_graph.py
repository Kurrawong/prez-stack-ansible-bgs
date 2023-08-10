import argparse

from rdflib import Graph, URIRef, Literal

parser = argparse.ArgumentParser()
parser.add_argument("config_file")
args = parser.parse_args()

config_file = args.config_file

graph = Graph()
graph.parse(config_file)

graph.add(
    (
        URIRef("http://base/#tdb_dataset_readwrite"),
        URIRef("http://jena.apache.org/2016/tdb#unionDefaultGraph"),
        Literal(True),
    )
)

graph.serialize(config_file)
