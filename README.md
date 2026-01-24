# 💳 Credit Card Fraud Detection – Streamlit App

This project is a **complete end-to-end machine learning–based web application** for detecting **fraudulent credit card transactions** using an interactive **Streamlit** interface. It demonstrates how a trained ML model (or simulated inference logic) can be deployed in a **real-time, user-friendly environment** to assess transaction risk instantly.


## 🎯 Project Overview

Credit card fraud detection is a critical problem in the FinTech and cybersecurity domains. This application allows users to input transaction details and instantly determine whether a transaction is **Fraudulent** or **Legitimate**, along with a visual representation of risk level.

The app accepts **30 numerical transaction features**, commonly found in anonymized fraud datasets (e.g., PCA-transformed features), making it suitable for both **academic learning** and **portfolio demonstrations**.


## 🚀 Key Features

* 📊 **Interactive Streamlit UI** for entering transaction details
* 🧮 Accepts **30 numerical input features** in a clean two-column layout
* ⚙️ **Adjustable fraud probability threshold** via sidebar
* 🔄 **Real-time prediction** with animated loading spinner
* 📈 **Visual risk-level progress bar**
* 🗂 **Prediction history tracking** using Streamlit session state
* 📱 Responsive and modern UI suitable for demos and portfolios


## 🧠 How It Works

1. **User Input**
   The user enters transaction details, including:

   * Transaction amount
   * 30 numerical features representing transaction behavior

2. **Prediction Trigger**
   When the *Predict Fraud* button is clicked:

   * Inputs are converted into a NumPy array
   * Backend simulates model inference logic *(can be replaced with a trained ML model)*
   * A fraud probability score is generated

3. **Decision Logic**

   * The predicted probability is compared with the user-defined threshold
   * Transaction is classified as **Fraudulent** or **Legitimate**

4. **Output & Visualization**

   * Fraud probability score
   * Risk-level progress indicator
   * Stored prediction history displayed on the same page


## 🛠 Technologies Used

* **Python**
* **Streamlit**
* **NumPy**
* **Pandas**
* **Time** (for UI simulation and loading effects)


## 📂 Project Structure

* `app.py` – Main Streamlit application file
* Sidebar with app information and configurable settings
* Session state management for prediction history
* Clean UI using sliders, number inputs, buttons, and progress indicators


## 🎯 Use Cases

* 📚 Academic and learning projects in **AI / Machine Learning**
* 🧪 Demonstrating **ML model deployment using Streamlit**
* 💼 Portfolio showcase for **FinTech and Cybersecurity** applications
* ⚡ Rapid prototyping of machine learning–based web apps


## 🔮 Future Enhancements

* 🤖 Integrate a trained ML/DL model (Logistic Regression, Random Forest, XGBoost)
* 📊 Add confusion matrix and performance metrics
* 🔐 Improve anomaly detection with unsupervised learning
* 🌐 Deploy on cloud platforms (Streamlit Cloud, Render)
* 📈 Add confidence intervals and explainability (SHAP)


## 👩‍💻 Developer

**Shanza Shakeel**
*AI / Machine Learning Enthusiast*


## 📌 Conclusion

This project showcases how **machine learning concepts** can be transformed into an **interactive, real-time fraud detection system** using Streamlit. It highlights best practices in ML deployment, UI design, and user interaction, making it an excellent project for **learning, experimentation, and professional portfolios**.
