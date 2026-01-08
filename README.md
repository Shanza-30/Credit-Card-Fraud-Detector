💳 Credit Card Fraud Detection – Streamlit App
This project is a complete end-to-end machine learning–based application for detecting fraudulent credit card transactions using a Streamlit web interface. It demonstrates how a trained machine learning model can be deployed in an interactive, user-friendly environment to provide real-time fraud predictions.
The application accepts 30 numerical transaction features, which typically represent anonymized credit card transaction data (such as PCA-transformed values used in common fraud datasets). These features are processed and analyzed to determine whether a transaction is Fraudulent or Legitimate.

🚀 Key Features
📊 Interactive Streamlit UI for entering transaction details
🧮 Accepts 30 numerical input features arranged in a clean two-column layout
⚙️ Adjustable Fraud Probability Threshold via sidebar
🔄 Real-time prediction with animated loading spinner
📈 Visual risk level progress bar
🗂 Prediction history tracking using Streamlit session state
📱 Responsive and clean layout suitable for demos and portfolios

🧠 How It Works
The user inputs transaction details, including:
Transaction amount
30 numerical features representing transaction behavior
On clicking Predict Fraud:
Inputs are converted into a NumPy array
The backend simulates model inference logic (can be replaced with a trained ML model)
A fraud probability score is generated
The result is classified based on the selected threshold
The prediction result is displayed instantly on the same page, along with:
Fraud probability
Risk-level progress indicator
Saved prediction history

🛠 Technologies Used
Python
Streamlit
NumPy
Pandas
Time (for UI simulation)

📂 Project Components
app.py – Main Streamlit application file
Interactive sidebar for app information and settings
Session state management for prediction history
Clean UI with sliders, number inputs, buttons, and progress indicators

🎯 Use Cases
Demonstrating ML model deployment using Streamlit
Academic and learning projects in AI/ML
Portfolio showcase for FinTech or Cybersecurity applications
Rapid prototyping of machine learning applications

👩‍💻 Developer
Shanza Shakeel
AI / Machine Learning Enthusiast
