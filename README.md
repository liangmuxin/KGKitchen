# KGKitchen

## This repository is used for code sharing for inf558_2018 project Knowledge Graph in the Kitchen; group members are Muxin Liang and Yuqiu He.

### 1. Collecting recipes from allrecipe
FINISHED

### 2. Crawling food from food list
FINISHED

### 3. Ontologies
Definition of ontologies


For every recipes:

**Ontology:recipe:**
  
    rdfs:value str recipe_name

    URL: str, url_of_recipe
  
    INGEDRENTS:String version of ingredients
  
    TYPE: str, recipe_type
    
    
  
 
**Ontology:food:**

    URL: str, url_of_food;
  
    TYPE: str, food_type;
  
    DEFINITION\_TOPCLASS: str, definitions of topclass in extration of food, used for direct mapping with recipe when generating a used_by instance ;
  
    DEFINITION\_SUBCLASS: str, definitions of the exact extracting word for searching food, we calculate the jaro-winkler distance and sorted with best result to connect with food used in recipe
  
    UNIT: str, the unit of food used by the recipe
  
    PRICE: float, the exact total price of the food
  
    UNIT_PRICE: float, the unit price of the food
  
 
**Ontology:used_by:**

    domian: food ;
  
    range: recipe ;
  
    AMOUNT: val ;
  
    UNIT: unit ;
    
    UNIT_PRICE: unit_price .
