from SPARQLWrapper import SPARQLWrapper, JSON



class QUERY:
    def __init__(self, sparql: SPARQLWrapper, return_format, selection: list, *args, **args_val):
        self.sparql = sparql
        self.return_format = return_format
        self.SELECTION_LIST = list(map(lambda x: "?"+x, selection))
        if "limit" in args_val:
            self.LIMIT = "LIMIT" + str(args_val["limit"])
        else:
            self.LIMIT = ""
        if "_filter" in args_val:
            self.FILTER = list(map(lambda x: "?"+x[0]+"="+str(x[1]), args_val["_filter"]))
        else:
            self.FILTER = None
        self.query = None
        self.PREFIX = """
                    PREFIX qb: <http://purl.org/linked-data/cube#>
                    PREFIX inf558: <http://inf558.org/ns/>
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
                    PREFIX schema: <http://schema.org/>
                    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        """
        self.STRUCTURE = """
        where {
            ?u a schema:usedby; 
                schema:amount ?amount ;
                schema:unit ?using_unit ;
                schema:unit_price ?using_unit_price ;
                schema:inrecipe ?R ;
                schema:forfood ?A . 
            ?A a schema:food ;
                schema:topclass ?topclass ;
                schema:subclass ?subclass ;
                rdf:value ?food_name ;
                schema:price ?food_price ;
                schema:unit ?food_unit ;
                schema:unit_price ?food_unit_price .
            ?R a schema:recipe ;
                schema:recipe_url ?recipe_url ;
                schema:type_url ?type_url ;
                schema:ingredient ?ingredient ;
                rdf:value ?recipe_name ;
        """
    def run_query(self):
        SELECTION = """
            SELECT {}
        """.format(" ".join(self.SELECTION_LIST))
        if not self.FILTER:
            FILTER = ""
        else:
            FILTER = ""
            for f in self.FILTER:
                tmp = "filter("+f+")"
                FILTER += tmp
        self.sparql.setQuery(self.PREFIX+SELECTION+self.STRUCTURE+FILTER+"}"+"{}".format(self.LIMIT))
        self.sparql.setReturnFormat(JSON)
        return self.sparql.query().convert()


def main():
    sparql = SPARQLWrapper("http://localhost:3030/test/sparql")
    # query1 = QUERY(sparql, JSON, ["ingredient", "recipe_name"], limit=10)
    # print(query1.run_query())
    # query2 = QUERY(sparql, JSON, ["food_name", "topclass", "unit_price"], limit=10)
    # print(query2.run_query())
    query3 = QUERY(sparql, JSON, ["recipe_name", "ingredient"], filter=[{"recipe_name": "Sloppy Joe Mac and Cheese"}, {"topclass": "butter"}], limit=10)
    print(query3.run_query())




# PREFIX = """
# PREFIX qb: <http://purl.org/linked-data/cube#>
# PREFIX inf558: <http://inf558.org/ns/>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# PREFIX schema: <http://schema.org/>
# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# """
# STRUCTURE = """
# where {
#     ?u a schema:usedby; 
#         schema:amount ?amount ;
#         schema:unit ?using_unit ;
#         schema:unit_price ?using_unit_price ;
#         schema:inrecipe ?R ;
#         schema:forfood ?A . 
#     ?A a schema:food ;
#         schema:topclass ?topclass ;
#         schema:subclass ?subclass ;
#         rdf:value ?food_name ;
#         schema:price ?food_price ;
#         schema:unit ?food_unit ;
#         schema:unit_price ?food_unit_price .
#     ?R a schema:recipe ;
#         schema:recipe_url ?recipe_url ;
#         schema:type_url ?type_url ;
#         schema:ingredient ?ingredient ;
#         rdf:value ?recipe_name ;
# """
# LIMIT = """
# LIMIT 10
# """

# ENDING = "}"+"{}".format(LIMIT)



# SELECTION_LIST = ["?recipe_name", "?ingredient"]

# SELECTION = """
# SELECT {}
# """.format(" ".join(SELECTION_LIST))
# sparql.setQuery(PREFIX+SELECTION+STRUCTURE+ENDING)

# from SPARQLWrapper import SPARQLWrapper, JSON
# sparql = SPARQLWrapper("http://localhost:3030/test/sparql")
# sparql.setReturnFormat(JSON)
# results = sparql.query().convert()
# print(results)

if __name__ == "__main__":
    main()