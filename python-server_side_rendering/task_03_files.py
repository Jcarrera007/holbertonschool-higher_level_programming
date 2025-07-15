from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except FileNotFoundError:
        items_list = []
    except json.JSONDecodeError:
        items_list = []
    
    return render_template('items.html', items=items_list)

def read_json_data(file_path):
    """Read data from JSON file"""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv_data(file_path):
    """Read data from CSV file"""
    try:
        products = []
        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert id and price to appropriate types
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except (FileNotFoundError, ValueError, KeyError):
        return []

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Check for valid source parameter
    if source not in ['json', 'csv']:
        return render_template('product_display.html', 
                             error_message="Wrong source")
    
    # Read data based on source
    if source == 'json':
        products = read_json_data('products.json')
    else:  # source == 'csv'
        products = read_csv_data('products.csv')
    
    # Filter by ID if provided
    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products if p.get('id') == product_id]
            if not filtered_products:
                return render_template('product_display.html', 
                                     error_message="Product not found")
            products = filtered_products
        except ValueError:
            return render_template('product_display.html', 
                                 error_message="Product not found")
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)