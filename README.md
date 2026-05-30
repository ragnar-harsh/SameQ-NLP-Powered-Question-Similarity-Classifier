# SameQ- A - NLP-Powered Question Similarity Classifier


A powerful Machine Learning project that detects whether two questions are **semantically similar (duplicates)** or not. This project leverages **Natural Language Processing (NLP)** techniques and **supervised learning models** to understand textual similarity.

---

## 🚀 Project Overview

Duplicate questions are common in platforms like Quora, Stack Overflow, and forums. Identifying them helps in:

* Improving user experience
* Reducing redundant content
* Enhancing search efficiency

This project builds an intelligent system that predicts whether two questions have the **same intent**, even if they are phrased differently.

---

## 🧠 Key Features

* 📊 **Exploratory Data Analysis (EDA)** to understand patterns in question pairs
* 🧹 **Data Preprocessing** (cleaning, stopword removal, normalization)
* 🧬 **Feature Engineering** with custom NLP-based features
* 🔗 **Correlation Analysis** between features
* 🧾 **Bag of Words (BoW) Vectorization** for text representation
* 🤖 Multiple ML models with **Hyperparameter Tuning**
* 📈 Model comparison based on **Accuracy & Precision**
* 🎯 Final model selection based on **higher precision**

---

## 🏗️ Tech Stack

* **Programming Language:** Python 🐍
* **Libraries & Tools:**

  * NumPy
  * Scikit-learn
  * NLTK
  * FuzzyWuzzy
  * BeautifulSoup
  * Distance
  * Streamlit (for UI)

---

## ⚙️ Machine Learning Models Used

| Model                       | Performance      |
| --------------------------- | ---------------- |
| Random Forest Classifier 🌲 | ✅ ~80% Accuracy  |
| XGBoost Classifier ⚡        | Compared & Tuned |

✔️ Final model selected based on **higher precision score**

---

## 📊 Workflow

1. **Data Collection**
2. **EDA (Exploratory Data Analysis)**
3. **Text Preprocessing**

   * Lowercasing
   * Removing stopwords
   * Cleaning HTML tags
4. **Feature Engineering**

   * Common words
   * Token-based similarity
   * Fuzzy matching scores
5. **Vectorization**

   * Bag of Words (BoW)
6. **Model Training**

   * Random Forest
   * XGBoost
7. **Hyperparameter Tuning**
8. **Model Evaluation**
9. **Deployment with Streamlit UI**

---

## 🎯 Results

* Achieved **~80% accuracy** using Random Forest
* Improved prediction quality using **precision-based model selection**
* Successfully detects semantic similarity between question pairs

---

## 💻 Demo UI

A clean and interactive UI built using **Streamlit**:

* Input two questions
* Click on **Validate**
* Get instant prediction:

  * ✅ Duplicate
  * ❌ Not Duplicate

---

## Screenshots

![alt text](<Datasets/Screenshot 2026-05-30 211226.png>)


![alt text](<Datasets/Screenshot 2026-05-30 211244.png>)

---

## 📦 Installation

```bash
git clone https://github.com/ragnar-harsh/SameQ-NLP-Powered-Question-Similarity-Classifier.git
cd SameQ-NLP-Powered-Question-Similarity-Classifier
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
├── Notebook/
│   ├── model.pkl
│   └── EDA & Training Notebooks
├── helper.py
├── app.py
├── requirements.txt
└── README.md
```

---

## 🔮 Future Improvements

* 🚀 Use advanced NLP models like **BERT / Sentence Transformers**
* 📊 Add probability/confidence score
* 🌐 Deploy on cloud (Streamlit Cloud / Azure / AWS)
* ⚡ Improve accuracy with deep learning

---

## 🙌 Acknowledgements

* Open-source NLP libraries
* Machine Learning community
* Dataset inspired by real-world duplicate question problems

---

## 👨‍💻 Author

**Harsh Singh**
💼 Software Engineer | ML Enthusiast

---

⭐ If you like this project, don’t forget to **star the repository!**
