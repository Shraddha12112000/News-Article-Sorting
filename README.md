# 📰 News Article Sorting
This project is part of ineuron.ai internship. 
A machine learning project to classify news articles into predefined categories like business, 
technology, politics, sports, and entertainment. The project uses a Random Forest Classifier 
and Flask to build a web application that predicts the category of a given news article.
# 📜 Table of Contents
1. About the Project
2. Features
3. Technologies Used
4. Setup and Installation
5. Usage Instructions
6. Deployment
7. Future Enhancements
8. Acknowledgments
# 🌟 About the Project
This project demonstrates a simple text classification model to sort news articles into five categories.
It incorporates:
1. Text preprocessing
2. Feature extraction using CountVectorizer 
3. Model training and evaluation
4. Deployment using Flask for a user-friendly interface.
# ✨ Features
1. Preprocessing: Remove special characters, stopwords, and perform lemmatization.
2. Model Training: Random Forest Classifier for high accuracy.
3. Web Interface: Predict news categories using a simple input form.
4. Modular Structure: Easy to understand and extend.
# 🛠️ Technologies Used
1. Programming Languages: 
Python
2. Libraries:
Flask, scikit-learn, nltk, pandas, numpy, matplotlib
3. Frontend: 
HTML, CSS
4. Deployment: 
Gunicorn, Render
# ⚙️ Setup and Installation
1. Step 1: Clone the Repository
 git clone https://github.com/yourusername/news-article-sorting.git

2. Step 2: Create a Virtual Environment
  i. For Windows write following command :
      $python -m venv myenv
      $myenv\Scripts\activate
3. Step 3: Install Dependencies
  Command : pip install -r requirements.txt
# 🚀 Usage Instructions
1. Start the Flask application:
  Command : python app.py
# 🌍 Deployment
To deploy this project on a cloud platform like Render:
1. Set up your project files on a GitHub repository.
2. Create a Render Web Service.
3. Add the gunicorn command to deploy your Flask app
  Command : gunicorn app:app
# 🚧 Future Enhancements
1. Implement additional classification models.
2. Optimize the preprocessing pipeline for better performance.
3. Improve the UI/UX of the web application.
4. Add more news categories for classification.
5. Deploy on other cloud platforms like AWS or Google Cloud.
# 🙏 Acknowledgments
Special Thanks To Ineuron For This Amazing Opportunity Which Helped Me To Enhance My Skills.
