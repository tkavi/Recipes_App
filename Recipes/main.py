from flask import Flask,request,jsonify
from Recipes import test

app = Flask(__name__)

recipes_list = test.recipe

@app.route('/recipes',methods=["GET"])
def get_recipes():
    if request.method == "GET":
        json_data = jsonify(recipes_list)
        return json_data

@app.route('/recipes/<int:id>',methods=["GET"])
def get_recipeById(id):
    if request.method == "GET":
        for i in recipes_list:
            if i["id"]==id:
                return jsonify(i)
        else:
            return "Recipe not found"

@app.route('/recipes/<int:id>',methods=["DELETE"])
def delete_recipeById(id):
    if request.method == "DELETE":
        for i in recipes_list:
            if i["id"] == id:
                recipes_list.remove(i)
                return recipes_list
        else:
            return "Recipe not found"

@app.route('/recipes/<int:id>',methods=["PUT"])
def update_recipeById(id):
    if request.method == "PUT":
        for i in recipes_list:
            if i["id"] == id:
                data = request.get_json()
                i['description'] = data
            return recipes_list
        else:
            return "Recipe not found"

@app.route('/recipes',methods=["POST"])
def add_recipe():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        recipes_list.append(data)
        return recipes_list

app.run()