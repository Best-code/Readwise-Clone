from flask import Flask, request, jsonify

app = Flask(__name__)


import getNotes

# Read (GET) all items
@app.route('/notes/<string:title>', methods=['GET'])
def get_items(title):
    args = request.args
    amt = args.get("amt", default=5, type=int)
    items = getNotes.getRandomNotes(title, amt)
    return jsonify(items.to_json())


# Delete (DELETE) an item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    items.remove(item)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
