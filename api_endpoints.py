from flask import Flask, jsonify, request

# Create the Flask app
app = Flask(__name__)

# Define a GET route
@app.route('/api/greet', methods=['GET'])
def greet():
    # Get optional query parameter ?name=
    name = request.args.get('name', 'World')
    return jsonify({"message": f"Hello, {name}!"})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)