from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Start Page. Nothing to see."

@app.route("/json/books")
def list_books():
    # fetch data from the DB
    test_data = {}
    return jsonify(test_data)

@app.route("/json/book", methods=["POST"])
def add_book():
    incoming_data = request.get_json()
    # required keys: "title" (string), "authors" (list), maybe: "isbn" (string)
    # optional keys: "category" (string), "topic" (string)
    required_keys = ["title", "authors"]
    required_keys_exist = all([key in incoming_data.keys() for key in required_keys])
    if required_keys_exist:
        return "HTTP 200 OK"
    else:
        return "boo."


if __name__ == "__main__":
    app.run(debug=True)
