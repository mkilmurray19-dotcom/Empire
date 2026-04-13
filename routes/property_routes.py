from flask import Blueprint, jsonify, request

# Create a Blueprint for property routes
property_routes = Blueprint('property_routes', __name__)

# Sample data:
properties = []  # This would usually be a database call
favorites = []

@property_routes.route('/properties/<int:property_id>', methods=['GET'])
def get_property(property_id):
    """ Get an individual property by ID """
    property = next((prop for prop in properties if prop['id'] == property_id), None)
    if property:
        return jsonify(property), 200
    else:
        return jsonify({'message': 'Property not found'}), 404

@property_routes.route('/favorites', methods=['POST'])
def manage_favorites():
    """ Add or remove from favorites """
    data = request.get_json()
    action = data.get('action')
    property_id = data.get('property_id')
    if action == 'add':
        if property_id not in favorites:
            favorites.append(property_id)
            return jsonify({'message': 'Property added to favorites'}), 200
    elif action == 'remove':
        if property_id in favorites:
            favorites.remove(property_id)
            return jsonify({'message': 'Property removed from favorites'}), 200
    return jsonify({'message': 'Invalid action or property not found'}), 400

@property_routes.route('/compare', methods=['POST'])
def compare_properties():
    """ Compare two or more properties """
    data = request.get_json()
    property_ids = data.get('property_ids', [])
    selected_properties = [prop for prop in properties if prop['id'] in property_ids]
    if len(selected_properties) < 2:
        return jsonify({'message': 'At least two properties required for comparison'}), 400
    return jsonify(selected_properties), 200
