# 🧠 Social Behavior Classifier

This project is a **Streamlit-based web application** that predicts whether a person is an **Introvert** or **Extrovert** based on their social behavior patterns. The model is trained using a **Random Forest Classifier** with features such as time spent alone, stage fear, social activity frequency, and more.

![App Screenshot](Screenshot%202025-06-29%20011144.png)

---


---

## 🖥️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/personality-predictor.git
cd personality-predictor


## 📊 Prediction Overview

The app uses the following features to predict personality:

| Feature                     | Description                                             |
|-----------------------------|---------------------------------------------------------|
| `Time_spent_Alone`          | Average hours per day spent alone                      |
| `Stage_fear`                | Stage fright (0 = No, 1 = Yes)                         |
| `Social_event_attendance`   | Number of events attended per month                    |
| `Going_outside`             | Times per week the person goes outside                 |
| `Drained_after_socializing`| Drained after socializing? (0 = No, 1 = Yes)           |
| `Friends_circle_size`       | Size of the social/friends circle                      |
| `Post_frequency`            | Weekly social media post frequency                     |

The model outputs:

- `Introvert` if the prediction is 0  
- `Extrovert` if the prediction is 1

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** for the web interface
- **Scikit-learn** for ML model and preprocessing
- **Pandas** for data manipulation
- **Pickle** for saving/loading model and scaler

---

## 📁 Project Structure

personality-predictor/
├── app.py # Streamlit application script
├── model.pkl # Trained Random Forest model
├── scaler.pkl # StandardScaler object used during training
├── features.pkl # List of input features
├── personality.ipynb # Jupyter notebook for training the model
├── personality_datasert.csv # Original dataset used for training
├── Screenshot 2025-06-29 011144.png # UI screenshot for demo
└── README.md # This file

🙋‍♀️ Author
Amal ROy
📧 amal.roy2100@gmail.com
🔗 github.com/amalroy2003
