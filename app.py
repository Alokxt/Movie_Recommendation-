from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import difflib

app = Flask(__name__)

# Load the trained model
model_path = 'model.pkl'
similarity_mats = 'top_k_similar.pkl'
movies_path = 'movies.pkl'

with open(model_path, 'rb') as file:
    xgb = pickle.load(file)

with open(movies_path,'rb') as f:
    movies = pickle.load(f)

with open(similarity_mats,'rb') as f:
    similarity_mat = pickle.load(f)


def predict(budget,score,year):

    try:
        int_features2 = np.array([float(budget),float(score),int(year)]).reshape(1,-1)
        print(int_features2)
        prediction = xgb.predict(int_features2)
        output = f"On the basis of this features, This movie can generate a total revenue of {prediction}"

        return {
                "success": True,
                "prediction": float(prediction[0]),
                "message": f"This movie can generate a total revenue of {prediction[0]}"
            }
    except Exception as e:
        return {"success": False, "error": str(e)}


def recommend(movie):
    try:

        all_movies = movies['names'].to_list()
        close_movies = difflib.get_close_matches(movie , all_movies)

        movie_found = close_movies[0]
        print(movie_found)
        idx = movies[movies['names'] == movie_found]
        if idx.empty:
            return "movie not found"
        idx1 = idx.index[0]

        l = similarity_mat[idx1][:6]
        k = []
        for j in l:
            k.append(movies.iloc[j[0]]['names'])

        return {
            "success": True,
            "Top recommendations": k,
        }
    except Exception as e:
        return {"success": False, "error": str(e)}

def recommend_by_genre(genre):
    try:

        filtered_movies = movies[movies['genre'].apply(lambda x: genre in x)]['names'][:6].values

        l = filtered_movies.tolist()

        return l
    except Exception as e:
        return {"success": False, "error": str(e)}

@app.route('/',methods=["GET", "POST"])
def home():
    movies_by_name = []
    revenue = None
    genre_recommendations = []

    if request.method == "POST":
        if "movie" in request.form:   # Search recommendations
            movie = request.form["movie"]
            recommendations = recommend(movie)

            movies_by_name = recommendations["Top recommendations"]

        if "genre" in request.form:        # Genre recommendations
            genre = request.form["genre"]
            genre_recommendations = recommend_by_genre(genre)

        if "budget" in request.form:  # Revenue prediction
            budget = request.form["budget"]
            score =  request.form["score"]
            year = request.form["year"]
            if score is None:
                score = 40
            if year is None:
                year = 2021

            revenue_cal = predict(budget,score,year)

            if revenue_cal["success"] == True:
                revenue = revenue_cal["prediction"]


    return render_template(
        "index.html",
        recommendations=movies_by_name,
        genre_recommendations=genre_recommendations,
        revenue=revenue
    )



if __name__ == "__main__":
    app.run(debug=True)