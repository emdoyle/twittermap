import sys
import json
from SPARQLWrapper import SPARQLWrapper, JSON

STARDOG_ENDPOINT = 'http://localhost:5820/final_project/query'

QUERY = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX dby: <http://dbpedia.org/class/yago/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX ns1: <http://www.semanticweb.org/caeleanb/ontologies/twittermap#>

SELECT ?handle ?name ?type ?influence ?followers ?retweets ?lat ?long
WHERE {
	?x rdf:type ?type .
	?x ns1:hasHandle ?h .
	?h ns1:realHandle ?handle .
	?h ns1:displayName ?name .
	?h ns1:hasLocation ?l .
	?l ns1:hasLatitude ?lat .
	?l ns1:hasLongitude ?long .
	?h ns1:influenceMetric ?influence .
	?h ns1:numFollowers ?followers .
	?h ns1:numRetweets ?retweets .
}
"""

sparql = SPARQLWrapper(STARDOG_ENDPOINT)
sparql.setQuery(QUERY)
sparql.setReturnFormat(JSON)
response = sparql.query().convert()
with open("dump.json", 'w') as f:
	json.dump(response, f)
