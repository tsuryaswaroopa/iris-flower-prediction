# 🌸 Iris Flower Prediction

A Machine Learning web application built using **Flask** and **K-Nearest Neighbors (KNN)** that predicts the species of an Iris flower based on its sepal and petal measurements.

---

## 📌 Project Description

The Iris Flower Prediction project uses a trained KNN machine learning model to classify an Iris flower into one of the following species:

- 🌼 Iris Setosa
- 🌺 Iris Versicolor
- 🌸 Iris Virginica

Users enter four flower measurements through a simple web interface, and the application predicts the flower species instantly.

---

## 🚀 Features

- User-friendly Flask web application
- Predicts Iris flower species
- Uses the K-Nearest Neighbors (KNN) algorithm
- Simple and responsive interface
- Fast prediction using a saved machine learning model

---

## 🛠️ Technologies Used

- Python
- Flask
- NumPy
- Pandas
- Scikit-learn
- Pickle
- HTML
- CSS

---

## 📂 Dataset

The project uses the **Iris Dataset**, which contains four input features:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The target classes are:

- Iris Setosa
- Iris Versicolor
- Iris Virginica

---

## 📁 Project Structure

```
iris-flower-prediction/
│
├── app.py
├── model.py
├── model.pkl
├── iris.csv
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── irissetosa.png
    ├── irisversicolor.png
    └── irisvirginica.png
```

---

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/iris-flower-prediction.git
```

### 2. Install required libraries

```bash
pip install flask numpy pandas scikit-learn
```

### 3. Train the model

```bash
python model.py
```

This creates the **model.pkl** file.

### 4. Run the Flask application

```bash
python app.py
```

### 5. Open your browser

```
http://127.0.0.1:5000/
```

---

## 💻 Input

Enter the following values:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

Click **Predict** to view the flower species.

---

## 📷 User Interface

The application displays:

- Images of all three Iris flower species
- Input form for measurements
- Predicted flower species

---

## 👩‍💻 Author

**Thotakura Surya Swaroopa**

BCA (Data Science)

GitHub: https://github.com/YOUR_GITHUB_USERNAME

---

## ⭐ Future Improvements

- Improve UI design
- Deploy the application online
- Add prediction confidence score
- Support mobile-friendly layout

---

## 📄 License

This project is created for educational and learning purposes.