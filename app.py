from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load your CSV data
data = pd.read_csv('data.csv')
data.columns = data.columns.str.strip()  # Remove any leading/trailing whitespace

@app.route('/')
def index():
    # Pass the food items to the index template using the correct column name
    food_items = data['name'].tolist()
    return render_template('index.html', food_items=food_items)

@app.route('/food/<food_name>')
def food(food_name):
    # Get the nutritional information for the selected food item
    # Adjusted to use the correct column name
    food_info = data[data['name'].str.lower() == food_name.lower()].squeeze()
    
    # If the food is not found, handle it gracefully
    if food_info.empty:
        return "Food not found", 404
    
    return render_template('food.html', food=food_info)

if __name__ == '__main__':
    app.run(debug=True)
