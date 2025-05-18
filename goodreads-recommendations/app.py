from flask import Flask, jsonify, render_template
from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALSModel
import pandas as pd

app = Flask(__name__)

# Initialize Spark
spark = SparkSession.builder \
    .appName("BookRecs") \
    .config("spark.driver.memory", "2g") \
    .getOrCreate()

# Load model and data
model = ALSModel.load("als_model")
books = pd.read_csv("books.csv")

@app.route('/')
def home():
    """Render the beautiful homepage"""
    return render_template('index.html')

@app.route('/recommend/<int:user_id>')
def recommend(user_id):
    """API endpoint for recommendations (unchanged)"""
    try:
        user_df = spark.createDataFrame([(user_id,)], ["user_id"])
        recs = model.recommendForUserSubset(user_df, 5).collect()[0].recommendations
        
        result = []
        for r in recs:
            book = books[books["book_id"] == r.book_id].iloc[0]
            result.append({
    'book_id': r.book_id,
    'title': book.get('title', 'Unknown Title'),
    'author': book.get('authors', 'Unknown Author'),
    'rating': round(r.rating, 2),
    'image_url': book.get('image_url', ''),
    'year': book.get('original_publication_year', ''),
    'description': book.get('description', ''),
    'url': f"https://www.goodreads.com/book/show/{book.get('goodreads_book_id', '')}"
})
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)