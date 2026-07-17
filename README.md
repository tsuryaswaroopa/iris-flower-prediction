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
├── .gitignore
├── README.md
│
├── static/
│   ├── smallflower.png
│   ├── irissetosa.png
│   ├── irisversicolor.png
│   └── irisvirginica.png
│
├── templates/
│   └── index.html
│
└── images/
    ├── output1.png
    ├── output2.png
    └── output3.png
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
## 💻 Output

<img width="1800" height="1000" alt="output1" src="https://github.com/user-attachments/assets/215953e9-82f8-471a-9d2d-d5b86b42bdac" />

<img width="1800" height="1000" alt="output2" src="https://github.com/user-attachments/assets/042f4983-1367-45a6-997b-96702df15a96" />

<img width="1800" height="1000" alt="output3" src="https://github.com/user-attachments/assets/cf759441-0374-4ca7-b3e8-011611d5cade" />


## 📷 User Interface

The application displays:

- Images of all three Iris flower species
- Input form for measurements
- Predicted flower species

---

## 👩‍💻 Author

**Thotakura Surya Swaroopa**

BCA (Data Science)

GitHub: https://github.com/tsuryaswaroopa

---

## ⭐ Future Improvements

- Improve UI design
- Deploy the application online
- Add prediction confidence score
- Support mobile-friendly layout

---

## 📄 License

This project is created for educational and learning purposes.
