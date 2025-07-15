from flask import Flask, render_template, request
import json
import csv
import sqlite3

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

def read_sql_data(product_id=None):
    """Read data from SQLite database"""
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        
        if product_id:
            cursor.execute('SELECT id, name, category, price FROM Products WHERE id = ?', (product_id,))
        else:
            cursor.execute('SELECT id, name, category, price FROM Products')
        
        rows = cursor.fetchall()
        conn.close()
        
        # Convert to list of dictionaries
        products = []
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        
        return products
    except sqlite3.Error:
        return []

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Check for valid source parameter
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', 
                             error_message="Wrong source")
    
    # Read data based on source
    if source == 'json':
        products = read_json_data('products.json')
    elif source == 'csv':
        products = read_csv_data('products.csv')
    else:  # source == 'sql'
        try:
            if product_id:
                product_id_int = int(product_id)
                products = read_sql_data(product_id_int)
            else:
                products = read_sql_data()
        except ValueError:
            return render_template('product_display.html', 
                                 error_message="Product not found")
    
    # Filter by ID if provided and source is not sql (sql filtering is done in query)
    if product_id and source != 'sql':
        try:
            product_id_int = int(product_id)
            filtered_products = [p for p in products if p.get('id') == product_id_int]
            if not filtered_products:
                return render_template('product_display.html', 
                                     error_message="Product not found")
            products = filtered_products
        except ValueError:
            return render_template('product_display.html', 
                                 error_message="Product not found")
    
    # Check if product was found when ID was provided
    if product_id and not products:
        return render_template('product_display.html', 
                             error_message="Product not found")
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)