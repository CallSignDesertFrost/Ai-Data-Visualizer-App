from flask import Flask, jsonify, render_template
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route('/api/analyze', methods=['GET'])
def analyze():
    # Retrieve data from the database
    data = Data.query.all()
    df = pd.DataFrame(data, columns=['value'])

    # Train a linear regression model
    model = LinearRegression()
    model.fit(df[['value']], df[['value']])

    # Make a prediction
    prediction = model.predict([[100]])

    # Return the prediction as JSON
    return jsonify({'prediction': prediction[0]})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)