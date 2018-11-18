# KGKitchen

## This repository is used for code sharing for inf558_2018 project Knowledge Graph in the Kitchen; group members are Muxin Liang and Yuqiu He.

### 1. Collecting recipes from allrecipe
Task: retrive name, steps, ingredient from ALLRECIPE

Now we have recipes and the extraction results of ingredient, catorized by (val, unit, entity).
TODO: 1. creating mapper that map(teasponn -> .01 gram, etc.) 


Task: generate a set of all(or most of:)) category of food used in recipe
### 2. Crawling food from food list
Task: retrive name, price, count_unit, save food by categor(probably one json file for each kind of food).

### 3. Defining Ontology
Muxin's initial definition of Ontology:

Ontology:recipe:
  URI:\_url\_of\_recipe;
  INGEDRENTS:Str, ingredients
  TYPE:food_type
  NAME:food_name
 
Ontology:food:
  URI:\_url\_of\_food;
  TYPE:food_type;
  MEARUREMENTS:(teaspoons, gram, cups, etc.);

Ontology:USED_BY:
  domian:food
  range:recipe
  AMOUNT:val
  UNIT:unit
  
 PADA:
 > just initial thinking, we can discuss later.
 > looking for some walk around method with extraction of food since food list looks huge
  
