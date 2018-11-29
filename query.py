from SPARQLWrapper import SPARQLWrapper, JSON



class QUERY:
    def __init__(self, sparql: SPARQLWrapper, return_format, selection: list, *args, **args_val):
        self.sparql = sparql
        self.return_format = return_format
        self.SELECTION_LIST = list(map(lambda x: "?"+x, selection))
        if "distinct" in args_val:
            self.DISTINCT = "distinct"
        else:
            self.DISTINCT = ""
        if "limit" in args_val:
            self.LIMIT = "LIMIT" + str(args_val["limit"])
        else:
            self.LIMIT = ""
        if "_filter" in args_val:
            self.FILTER = list(map(lambda x: "?"+x[0]+"="+"\""+str(x[1])+"\"", args_val["_filter"]))
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
                schema:recipe_type ?recipe_type ;
                schema:type_url ?type_url ;
                schema:ingredient ?ingredient ;
                rdf:value ?recipe_name ;
        """
    def run_query(self, verbose = False):
        SELECTION = """
            SELECT {}
        """.format(self.DISTINCT + " ".join(self.SELECTION_LIST))
        if not self.FILTER:
            FILTER = ""
        else:
            FILTER = ""
            for f in self.FILTER:
                tmp = "filter("+f+")"
                FILTER += tmp
        self.sparql.setQuery(self.PREFIX+SELECTION+self.STRUCTURE+"\n"+FILTER+"\n"+"}"+"{}".format(self.LIMIT))
        if verbose:
            print(self.PREFIX+SELECTION+self.STRUCTURE+"\n"+FILTER+"\n"+"}"+"{}".format(self.LIMIT))
        self.sparql.setReturnFormat(JSON)
        return self.sparql.query().convert()


def main():
    sparql = SPARQLWrapper("http://localhost:3030/test/sparql")
    query1 = QUERY(sparql, JSON, ["ingredient", "recipe_name"], limit=10)
    # print(query1.run_query())
    query2 = QUERY(sparql, JSON, ["food_name", "topclass", "unit_price"], limit=10)
    # print(query2.run_query())
    query3 = QUERY(sparql, JSON, ["recipe_name", "ingredient", "recipe_url"], _filter=[("topclass", "milk")], limit=10)
    query4 = QUERY(sparql, JSON, ["food_name", "amount", "unit_price", "food_unit", "topclass"], _filter=[("recipe_url", "https://www.allrecipes.com/recipe/75194/fresh-veggie-bagel-sandwich/")])
    query5 = QUERY(sparql, JSON, ["food_name", "food_unit_price", "food_unit", "food_price"], _filter=[("topclass", "chicken")], distinct=True)
    query6 = QUERY(sparql, JSON, ["recipe_type", "recipe_name", "food_unit", "food_unit_price"], _filter=[("topclass", "salt")], limit=10)
    query7 = QUERY(sparql, JSON, ["food_name", "food_unit"], _filter=[("food_unit", "tablespoon")])
    # estimating cost
    # res = query4.run_query()
    # for v in res["results"]["bindings"]:
    #     for k in v.keys():
    #         print(v[k]["value"])
    res1 = query5.run_query()
    # import pdb
    # pdb.set_trace()
    for v in res1["results"]["bindings"]:
        for k in v.keys():
            print(v[k]["value"])
    # res2 = query6.run_query()

    # for v in res2["results"]["bindings"]:
    #     for k in v.keys():
    #         print(v[k]["value"])

    print("finished")



if __name__ == "__main__":
    main()