from flask import Flask
from flask_restful import Api
from app.routes.user_routes import register_routes

app = Flask(__name__)
api = Api(app)

# Register all routes
register_routes(api)

if __name__ == '__main__':
    app.run(debug=True)