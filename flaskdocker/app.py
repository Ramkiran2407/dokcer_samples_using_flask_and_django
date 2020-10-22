from flask import Flask, jsonify
# from flask_api import status


app = Flask(__name__)

books_data=[{"id":0,"title":"sample"},{"id":1,"title":"sggample"}]

@app.route('/books/<id>')
def books(id):
    for data in books_data:
        for key ,value in data.items():
            if value == int(id):
                return jsonify(data)
        else:
            return jsonify("status.HTTP_404_NOT_FOUND")
    
@app.route('/')
def sample():
    return "Hello docker"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)