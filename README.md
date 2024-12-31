# 🎥 Simple Movie Recommendation System  

A simple and interactive web-based application that recommends movies similar to a user-provided input. Built using **Streamlit** and powered by **KMeans Clustering**.  

## 🚀 Features  
- Accepts a movie title as input from the user.  
- Recommends similar movies from the dataset using clustering.  
- Dynamic assignment of clusters based on `Rating` and `Popularity` features.  
- Intuitive dark-themed user interface.  

---

## 🛠️ Technologies Used  
- **Python**  
- **Streamlit** for the web application.  
- **Pandas** for data manipulation.  
- **scikit-learn** for clustering with the KMeans algorithm.  

---

## 📁 Project Structure  
```
Simple-Movie-Recommendation/
├── app.py                 # Streamlit app for the recommendation system
├── Data/
│   └── LargeMovieDataset.csv  # Dataset without clusters
├── Model/
│   └── movie_clustering_model.pkl   # Pre-trained KMeans clustering model
├── Notebook/
│   └── model_creation.ipynb # Jupyter Notebook containing the data preprocessing, clustering model training, and evaluation steps for the KMeans-based movie recommendation system.
├── requirements.txt       # Dependencies for the project
└── README.md              # Project documentation
```

---

## 📦 Installation  

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/22AIML021VishalMehta/Simple-Movie-Recommendation-System.git
   cd Simple-Movie-Recommendation
   ```

2. **Set up a virtual environment (optional but recommended)**:  
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install the required dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**:  
   ```bash
   streamlit run app.py
   ```

5. **Open the app in your browser**:  
   Navigate to `http://localhost:8501`.

---

## 📂 Dataset  

The dataset (`original_movies.csv`) includes the following features:  
- `MovieID`  
- `Title`  
- `Genre`  
- `Rating` (scale 1-5 in floating point value)  
- `Popularity` (scale 1-100)  

Clusters are dynamically assigned using a pre-trained **KMeans model** (`kmeans_model.pkl`).  

---

## 🌐 Live Demo  
You can deploy this app online using [Streamlit Community Cloud](https://share.streamlit.io/).  

---

## 🤝 Contributing  
Contributions are welcome!  
- Fork this repository.  
- Create a feature branch.  
- Commit your changes.  
- Open a pull request.  

---

## 📜 License  
This project is licensed under the MIT License - see the [MIT](LICENSE) file for details.  

---

### 📌 Important Note  

This project utilizes **K-Means Clustering** for movie recommendation based on features such as `Rating` and `Popularity`.  

- **Dataset-Specific**: The clustering model is specifically trained and designed for the **LargeMovieDataset**.  
- **Limitations**: This model may not work as intended with other datasets due to differences in feature distributions and clustering parameters.  

---

## 💬 Contact  
For questions or suggestions, feel free to reach out:  
- **Name**: Vishal Mehta.  
- **Email**: 22aiml021@charusat.edu.in.  
- **GitHub**: [22AIML021VishalMehta](https://github.com/22AIML021VishalMehta)

---

Let me know if you'd like to modify any sections or add more details!
