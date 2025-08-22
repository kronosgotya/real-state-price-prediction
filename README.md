# 🏠 Bangalore Home Price Prediction App  

This project is a **direct implementation of the Codebasics Bangalore Home Price Prediction tutorial**.  
It was developed purely for **learning purposes**, to understand the full pipeline of building, training, and deploying a machine learning model as a web application.  

The application predicts housing prices in Bangalore based on **square footage, number of bedrooms, bathrooms, and location**.  

It consists of:  
- **Backend**: Flask (REST API endpoints for prediction and location names)  
- **Model**: Regression model trained on Bangalore housing dataset  
- **Frontend**: HTML, CSS, JavaScript (jQuery) for a simple, interactive interface  

---

## 🚀 How to Run  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/<your-repo>/bangalore-home-price.git
   cd bangalore-home-price

2. **Install dependencies**  
   Create a virtual environment (recommended) and install requirements:  
   ```bash
   pip install -r requirements.txt
3. **Start the Flask server**  

   ```
   cd server  
   python server.py  
   The server will start at http://127.0.0.1:5000  

5. **Open the frontend**  
   - Open `app.html` in your browser (located in the `frontend/` folder).  
   - Select area (sqft), bedrooms (broom), bathrooms, and location.  
   - Click *Estimate Price* → the app will call the Flask API and display the predicted price.  

## Acknowledgement  
This project is a full copy of the Codebasics tutorial on Bangalore Home Price Prediction.  
All credit for the dataset, workflow, and design belongs to Codebasics.  
My contribution was to reproduce it for educational purposes and practice an end-to-end ML deployment, and debug/refine the .py, .js, .html, and other project files to ensure correct functionality.  

