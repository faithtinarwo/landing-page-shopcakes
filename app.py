from flask import Flask, render_template
import os


app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the cake shop page
@app.route('/shop')
def shop():
    # Add logic to fetch available cakes from a database (if needed)
    cakes = [
        {'name': 'Chocolate Cake', 'price': 15, 'image': 'https://via.placeholder.com/300x200'},
        {'name': 'Vanilla Cake', 'price': 12, 'image': 'https://via.placeholder.com/300x200'},
        {'name': 'Strawberry Cake', 'price': 18, 'image': 'https://via.placeholder.com/300x200'},
        {'name': 'Lemon Cake', 'price': 14, 'image': 'https://via.placeholder.com/300x200'}
    ]
    return render_template('shop.html', cakes=cakes)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
