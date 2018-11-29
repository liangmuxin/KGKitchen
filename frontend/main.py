from SPARQLWrapper import SPARQLWrapper, JSON
from flask import Flask,render_template,request
from query import QUERY

app = Flask(__name__)
dish_types = ['Appetizers & Snacks', 'Bread Recipes', 'Cake Recipes', 'Candy and Fudge', 'Casserole Recipes',
              'Christmas Cookies', 'Cocktail Recipes', 'Cookie Recipes', 'Mac and Cheese Recipes', 'Main Dishes',
              'Pasta Salad Recipes', 'Pasta Recipes', 'Pie Recipes', 'Pizza', 'Sandwiches', 'Sauces and Condiments',
              'Smoothie Recipes', 'Soups, Stew, and Chili Recipes']
def datalist_ingredients():
    ingredients = []
    for line in open('food_types.txt', 'r'):
        ingredients.append(line.strip('\n').replace('% ',''))
    return ingredients


def sparql_ingre(ingredient):
    sparql = SPARQLWrapper("http://localhost:3030/test/sparql")
    query1 = QUERY(sparql, JSON, ["food_name", "food_unit_price", "food_unit", "food_price"],
                   _filter=[("topclass", ingredient)], distinct=True)
    query2 = QUERY(sparql, JSON, ["recipe_type", "recipe_name", "recipe_url" ], _filter=[("topclass", ingredient)])

    results1 = query1.run_query()
    results2 = query2.run_query()
    return results1, results2


def sparql_dish_ingre(dishes,ingredient):
    sparql = SPARQLWrapper("http://localhost:3030/test/sparql")
    results1 = []
    flag = 1
    for ig in ingredient:
        if dishes == '' and ig != '':
            query = QUERY(sparql, JSON, ["recipe_name", "ingredient", "recipe_url"],
                          _filter=[("topclass", ig)], limit=15)
        elif dishes != '' and ig == '':
            query = QUERY(sparql, JSON, ["recipe_name", "ingredient", "recipe_url"],
                          _filter=[("recipe_type", dishes)], distinct=True, limit=15)
        elif dishes == '' and ig == '':
            query = QUERY(sparql, JSON, ["recipe_name", "ingredient", "recipe_url"], limit=15)
        else:
            query = QUERY(sparql, JSON, ["recipe_name", "ingredient", "recipe_url"],
                  _filter=[("topclass",ig),("recipe_type", dishes)], limit=15)
        results1.append(query.run_query())

    results2 = []
    url,food_name,origin_ingre = [],[],[]
    for results in results1:
        for i in range(len(results['results']['bindings'])):
            url.append(results['results']['bindings'][i]['recipe_url']['value'])
            food_name.append(results['results']['bindings'][i]['recipe_name']['value'])
            ingredients_return = results['results']['bindings'][i]['ingredient']['value'].strip('[').strip(']').replace(', ','').replace('\"','').split('\'')
            while '' in ingredients_return:
                ingredients_return.remove('')
            origin_ingre.append(ingredients_return)

            query = QUERY(sparql, JSON, ["food_name", "amount", "food_unit_price", "food_unit", "topclass"],
                   _filter=[("recipe_url",results['results']['bindings'][i]['recipe_url']['value'])], limit=15, distinct=True)
            results2.append(query.run_query())

    return results2,url,food_name,origin_ingre


@app.route('/')
def index():
    return render_template('index.html', Ingredients = datalist_ingredients(), disTypes = dish_types)


@app.route('/searchByRecipe',methods=['POST','GET'])
def searchByRecipe():
    if request.method == 'POST':
        dish_type = request.form['dishType']
        ingredient_ori = request.form['ingredient']
        ingredient = ingredient_ori.split(',')
        results2, url, food_name, origin_ingre = sparql_dish_ingre(dish_type,ingredient)

        return_dict = []
        j = 0
        for results in results2:
            ingredients, unit_price_list, food_unit, topclass, amount_list = [], [], [], [], []
            total = 0
            for i in range(len(results['results']['bindings'])):
                ingredients.append(results['results']['bindings'][i]['food_name']['value'])
                food_unit.append(results['results']['bindings'][i]['food_unit']['value'])
                unit_price = eval(results['results']['bindings'][i]['food_unit_price']['value'])
                amount = eval(results['results']['bindings'][i]['amount']['value'])
                topclass.append(results['results']['bindings'][i]['topclass']['value'])
                unit_price_list.append(unit_price)
                amount_list.append(amount)
                total += (unit_price * amount)
            total = round(total * 100)/100
            return_dict.append({"url":url[j],"food_name": food_name[j], "origin_ingre": origin_ingre[j],"ingredients_amazon": ingredients, "unit_price": unit_price_list,"food_unit":food_unit,"total":total,"topclass":topclass,"amount_list":amount_list})
            j += 1


        return render_template('searchByRecipe.html', Ingredients = datalist_ingredients(), disTypes = dish_types, returnDict = return_dict[0:15], getDishType = dish_type, getIngred = ingredient_ori)


@app.route('/searchByFood',methods=['POST','GET'])
def searchByFood():
    if request.method == 'POST':
        ingredient = request.form['ingredient']
        results1, results2 = sparql_ingre(ingredient)
        foodName,food_unit_price,food_unit,food_price,re_type,re_name,re_url = [], [], [], [], [], [], []
        return_dict,re_dict_2 = [], []

        print(results2)
        for i in range(len(results1['results']['bindings'])):
            foodName.append(results1['results']['bindings'][i]['food_name']['value'])
            food_unit_price.append(eval(results1['results']['bindings'][i]['food_unit_price']['value']))
            food_unit.append(results1['results']['bindings'][i]['food_unit']['value'])
            food_price.append(eval(results1['results']['bindings'][i]['food_price']['value']))
            return_dict.append({"foodName":foodName,"food_unit_price":food_unit_price,"food_unit":food_unit,"food_price":food_price})
        for i in range(len(results2['results']['bindings'])):
            re_type.append(results2['results']['bindings'][i]['recipe_type']['value'])
            re_name.append(results2['results']['bindings'][i]['recipe_name']['value'])
            re_url.append(results2['results']['bindings'][i]['recipe_url']['value'])
            re_dict_2.append({"re_type":re_type,"re_name":re_name,"re_url":re_url})

        return render_template('searchByFood.html', Ingredients=datalist_ingredients(), disTypes=dish_types,
                               ingredient=ingredient, returnDict=return_dict, returnDict2 = re_dict_2)


if __name__ == '__main__':
    app.run(debug=True)