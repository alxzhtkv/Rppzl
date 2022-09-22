from flask import Flask
from flask_restful import Api, Resource,reqparse

app = Flask(__name__)
api = Api()


library = {
    1: {"name": "Pride and prejudice","id":123 },
    2: {"name": "The Burden of Human Passions", "id": 666}

}
parser = reqparse.RequestParser()
parser.add_argument("name", type=str)
parser.add_argument("id", type=int)


class Main(Resource):
    def get(self,book_id):
        if book_id == 0:
            return library
        else:
            return library[book_id]

    def delete(self, book_id):
        del library[book_id]
        return library

    def post(self, book_id):

        library[book_id] = parser.parse_args()
        return library

    def put(self,book_id):
         library[book_id] = parser.parse_args()
         return library





api.add_resource(Main, f"/api/library/<int:book_id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True,port=3000,host = "127.0.0.1")
