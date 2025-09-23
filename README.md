Student Math Score Prediction!

📖 Overview
This project aims to predict students' mathematics scores based on a variety of demographic, socio-economic, and academic factors. By leveraging machine learning, specifically Bagging and Boosting ensemble techniques, we can uncover how different attributes correlate with student performance and build a robust predictive model.

The dataset includes features such as parental education level, gender, race/ethnicity, and performance in other subjects like reading and writing.

🎯 Problem Statement
The goal is to build an accurate regression model that can predict a student's final math score given a set of personal and academic background features. This can help educators identify students who may need extra support and understand the key factors that influence academic success in mathematics.

✨ Features
The model is trained on the following input features:

Gender: Male / Female

Race/Ethnicity: Group A, B, C, D, E

Parental Level of Education: Bachelor's Degree, Master's Degree, High School, etc.

Lunch: Standard or Free/Reduced

Test Preparation Course: None or Completed

Reading Score: Student's score on the reading test

Writing Score: Student's score on the writing test

Target Variable:

Math Score: The student's score on the math test (the value to be predicted).

🛠️ Methodology
The project follows a standard machine learning workflow:

Data Cleaning & Preprocessing: Handled missing values and encoded categorical features (like gender, race, etc.) into a numerical format suitable for modeling.

Exploratory Data Analysis (EDA): Analyzed the relationships between different features and the target variable (math score) using visualizations to gain insights.

Model Training: Implemented and trained two powerful types of ensemble models:

Bagging: A RandomForestRegressor was used to reduce variance and improve stability.

Boosting: A GradientBoostingRegressor (or XGBoost) was used to build a strong predictive model by sequentially correcting errors from previous models.

Model Evaluation: The performance of both models was evaluated using standard regression metrics to determine the most effective approach.

💻 Technologies Used
Language: Python 3.x

Libraries:

Pandas: For data manipulation and analysis.

NumPy: For numerical operations.

Scikit-learn: For data preprocessing and implementing machine learning models.

Matplotlib & Seaborn: For data visualization.

Environment: Jupyter Notebook

🚀 How to Run this Project
To get a local copy up and running, follow these simple steps.

Prerequisites
Python 3.8 or higher

pip (Python package installer)

Installation
Clone the repository:

git clone [https://github.com/your-username/your-repository-name.git](https://github.com/2k23csaiml2313622-code/mlproject.git)
cd mlproject

Create and activate a virtual environment (recommended):

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

Install the required packages:

pip install -r requirements.txt

(Note: You will need to create a requirements.txt file by running pip freeze > requirements.txt in your terminal.)

Usage
Open the Jupyter Notebook:

jupyter notebook

In the browser window that opens, navigate to and open the main project notebook (e.g., student_performance.ipynb).

Run the cells in the notebook sequentially to see the data analysis, model training, and evaluation.

📈 Results
The models were evaluated based on their ability to predict math scores accurately. The following metrics were used:

Best Model Accuracy Score-

R² Score= 0.8824

Conclusion:
[Briefly state which model performed better and why. For example: "The Gradient Boosting model provided a slightly higher R² score, indicating it was better at explaining the variance in the students' math scores."]

A feature importance analysis revealed that Reading Score and Writing Score were the most significant predictors of a student's performance in math.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

📧 Contact
Aishwarya Mishra - 2k23.csaiml2313622@gmail.com

Project Link: https://github.com/2k23.csaiml2313622-code/mlproject


