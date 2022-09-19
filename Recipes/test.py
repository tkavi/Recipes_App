from flask import Flask,request,jsonify
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

recipe = [
    {
        'id': 1,
        'name': 'Salad',
        'description': 'This is a lovely Greek salad recipe.'
    },
    {
        'id': 2,
        'name': 'Rava Masala Dosa',
        'description': 'This is recipe for Rava Masala Dosa.'
    }
]

class allRecipes(Resource):
    def get(self):
        return jsonify(recipe)

    def post(self):
        data = request.get_json()
        recipe.append(data)
        return recipe

class oneRecipes(Resource):
    def get(self,id):
        for i in recipe:
            if i["id"] == id:
                return jsonify(i)
        else:
            return jsonify({"message":"Recipe not found"})

    def put(self,id):
        for i in recipe:
            if i["id"] == id:
                data = request.get_json()
                i['description'] = data
            return recipe
        else:
            return "Recipe not found"

    def delete(self,id):
        for i in recipe:
            if i["id"] == id:
                recipe.remove(i)
                return recipe
        else:
            return "Recipe not found"

api.add_resource(allRecipes,"/recipes")
api.add_resource(oneRecipes,"/recipes/<int:id>")
app.run()