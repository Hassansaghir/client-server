from flask import Flask, jsonify, request
from models import db, Categories, Menu_Items
from config import Config
from flask_cors import CORS
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# API ROUTES
@app.route('/')
def home():
    return "Hello, world!"

@app.route('/category', methods=['GET'])
def get_Categories():
    categories = Categories.query.all()
    return jsonify([{'id': c.id, 'name': c.name} for c in categories])

@app.route('/items', methods=['GET'])
def get_items():
    items = Menu_Items.query.all()
    return jsonify([{
        'item_id': i.id, 
        'name': i.name, 
        'price': float(i.price),  # Convert price to float consistently
        'category_id': i.category_id
    } for i in items])

@app.route('/items/<int:id>', methods=['GET'])
def get_items_by_id(id):
    item = Menu_Items.query.get(id)
    if item:
        return jsonify({
            'item_id': item.id,
            'name': item.name,
            'price': float(item.price),  # Consistent price conversion
            'category_id': item.category_id
        }), 200
    else:
        return jsonify({'error': 'Item not found'}), 404

@app.route('/items/search', methods=['GET'])
def get_item_by_name():
    name = request.args.get('name', '')
    
    if not name:
        return jsonify({"message": "No name provided"}), 400
    
    items_by_name = Menu_Items.query.filter(Menu_Items.name.ilike(f'%{name}%')).all()
    
    if items_by_name:
        return jsonify([{
            "id": item.id,
            "name": item.name,
            "price": float(item.price),  # Convert to float for consistency
            "category": item.category_id
        } for item in items_by_name])
    else:
        return jsonify({"message": f"No items found with name: {name}"}), 404

CORS(app) 
#CORS (Cross-Origin Resource Sharing) is a security feature implemented by web browsers 
#that controls how web pages can request resources (like APIs, data, or images) 
# from a different domain (origin) than the one the web page is served from.