from flask import Flask, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from models import db

app = Flask(__name__)

# Flask configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
migrate = Migrate(app, db)

# Initialize the database
db.init_app(app)

@app.route('/movies', methods=['GET'])
def movies():
    response_dict = {"text": "Movies will go here"}
    return make_response(jsonify(response_dict), 200)

if __name__ == '__main__':
    app.run(port=5555)
