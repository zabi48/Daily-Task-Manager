# Smart Task Priority Manager

## Team
- Muhammad Zuhaib

## Project Overview
Managing tasks efficiently is challenging. Users often struggle to decide which task to tackle first.  
This web app helps users organize tasks, predicts priority using a simple ML model, and provides a basic task manager interface.

## Features
- **Add tasks** with deadline, importance, and effort
- **Predict task priority** (High, Medium, Low) using a trained machine learning model
- **Auto-sort tasks** from highest to lowest priority
- **Mark tasks as done** → done tasks move to the bottom and are visually struck through
- **Demo tasks included** for easy testing

## How It Works
1. User fills out a form with task details (deadline, importance, effort)
2. Flask app receives the data via POST request
3. Model predicts task priority
4. Tasks are added to the list and automatically sorted
5. User can mark tasks as done, which moves them to the bottom

## Technologies Used
- **Python 3.14**
- **Flask** – web framework
- **scikit-learn** – for ML-based priority prediction
- **NumPy & Pandas** – data handling for model
- **HTML/CSS** – front-end interface

## How to Run
1. Clone the repo
2. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt