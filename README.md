**Movie Recommendation System** 📽️🎬✨
Welcome to the Movie Recommendation System! This project uses data science and machine learning to recommend movies based on their content and predict their box office revenue.
Below is an overview of the complete workflow, including Exploratory Data Analysis (EDA), data preprocessing, feature engineering for recommendations, 
and regression modeling for revenue prediction.

📚 **Dataset**
The dataset comprises more than 10,000 movies, with fields like:

names: Movie titles

date_x: Release dates

score: IMDb or similar ratings

genre: List of genres

overview: Movie plot summaries

crew: Main actors, directors, etc.

country: Production country

budget_x: Movie budget (in USD)

revenue: Box office revenue (in USD)

Year: Year of release

🔍 **1. Exploratory Data Analysis (EDA)**
Various techniques were used to understand the distribution and relationships in the dataset:

Head & Info: Previewed the top rows to check for nulls and data types.

Distribution Plots: Used histograms and count plots to visualize ratings (score), budget_x, revenue, and Year.

Bar Charts: For most frequent genres and top-grossing movies.

Correlation Heatmaps: Checked relationships between numerical columns, such as budget, score, and revenue.

Missing Value Analysis: Identified columns with NaNs and applied imputation/cleaning where needed.

🛠️ **2. Data Preprocessing**
Before modeling and recommendations, the following preprocessing steps were applied:

Date Parsing: Transformed string dates into datetime format and extracted release years.

Genre Encoding: Processed genres as lists and encoded them for further analysis.

Overview & Tags Cleaning: Removed stopwords and punctuation in text fields for content modeling.

Numerical Feature Scaling: Scaled and normalized budget, score, and revenue for regression tasks.

Null Handling: Filled missing values with suitable defaults or dropped incomplete rows, depending on analysis requirements.

✨ **3. Content-Based Recommendation**
The core idea is to recommend movies similar in content (genre, tags, overview):

a. Feature Vectorization
Text Vectorizers: Used TF-IDF and CountVectorizer from sklearn to turn text fields (e.g., overview, genre, tags) into high-dimensional feature spaces.

Cosine Similarity: Calculated pairwise similarity between movies using cosine similarity on vector representations, enabling recommendations of "the most similar movies" for any input.

python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(data['overview'])
cos_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
Recommendation Output: On entering a movie name, the system retrieves the top N movies with the highest cosine similarity scores.

b. Genre and Tags Merge
Additional improvement by combining genres and keywords/tags for a richer similarity search.

📈 **4. Regression: Predicting Movie Revenue**
Next, the system predicts box office revenue using movie features:

a. Feature Selection
Input Features: Budget, IMDb score, release year (and more as needed).

Target Variable: revenue

b. Model
XGBoost Regression: Used the XGBRegressor model for its robustness with tabular data.

Model Parameters: Learning rate = 0.5, max_depth = 3, n_estimators = 1000 (fine-tuned via cross-validation).

Performance Metrics: Tracked R^2, RMSE to evaluate prediction accuracy.


**Run the notebook Movie_recommendation.ipynb for step-by-step outputs and plots.**


📦 **Output**
Movie Recommendations: Instant suggestions based on cosine similarity.

Revenue Prediction: Enter budget, score, and year for a predicted box office result.

Interactive Visualizations: Explore top genres, movie trends by year, and model insights.

🎯 **Conclusion**
This project showcases the full pipeline: EDA, preprocessing, content-based recommender using cosine similarity, and regression analysis for box office forecasting — all in an elegant, professional notebook!
Features: budget, score, release_year

Target: gross (revenue)

Performance: R² ≈ 0.51
