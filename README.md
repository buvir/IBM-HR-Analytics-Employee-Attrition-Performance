# IBM HR Analytics – Employee Attrition & Performance  

## 📌 Project Overview  
This project analyzes the **IBM HR Analytics Employee Attrition & Performance** dataset (fictional, created by IBM data scientists) to uncover factors influencing employee attrition. It combines **Exploratory Data Analysis (EDA)** with a **baseline Machine Learning model** to predict attrition.  

Attrition—when employees leave the company—can significantly impact productivity and costs. This project identifies patterns in demographics, job satisfaction, salary, and work-life balance to support HR retention strategies.  

---

## 🛠 Tools & Technologies  
- **Python**: pandas, numpy, matplotlib, seaborn  
- **scikit-learn**: preprocessing, pipelines, classification models, evaluation metrics  
- **Jupyter Notebook**: interactive data exploration  


---

## 📂 Dataset  
- **File**: `WA_Fn-UseC_-HR-Employee-Attrition.csv`  
- **Shape**: 1,470 rows × 35 columns  
- **Content**: Age, Gender, Department, Job Role, Income, Education, Work-Life Balance, Satisfaction levels, and Attrition flag.  
- **Target**: `Attrition` (Yes/No)  

---

## 🔍 Objectives  
1. **Measure turnover rate** and average employee tenure.  
2. **Analyze attrition patterns** by demographics, department, job role, income, and satisfaction indicators.  
3. **Identify key drivers** of attrition.  
4. **Build predictive models** (Logistic Regression, Random Forest) to classify attrition.  

---

## 📊 EDA Highlights  
- **Attrition Rate**: ~16% employees leave.  
- **Average Tenure**: 7 years.  
- **Age Distribution**: Majority between 30–35 years.  
- **Key Factors**:  
  - Frequent business travel ↑ attrition  
  - Low job/work-life satisfaction ↑ attrition  
  - Lower income groups more likely to leave  

---

## 🤖 Machine Learning  
- **Preprocessing**: One-hot encoding (categorical), scaling (numeric).  
- **Models**:  
  - Logistic Regression (balanced class weights)  
  - Random Forest Classifier (balanced subsample)  
- **Metrics**: Accuracy, Precision, Recall, F1, ROC-AUC  
- **Feature Importance**: Identifies top drivers of attrition.  

---

## 📈 Results  
- Baseline Random Forest achieved better **ROC-AUC** than Logistic Regression.  
- Key features influencing attrition include:  
  - **OverTime, JobRole, MonthlyIncome, WorkLifeBalance, Age**  

---
📂 Final Project Structure

IBM-HR-Attrition/
│── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│── notebooks/
│   └── IBM_HR_Attrition_EDA_Model.ipynb
│── README.md
│── requirements.txt
│── .gitignore
│── venv/        # (ignored in git)



## 🚀 How to Run  
1. Clone repo & open notebook:  
   ```bash
   git clone <repo-url>
   cd IBM-HR-Attrition
   jupyter notebook IBM_HR_Attrition_EDA_Model.ipynb
   ```  
2. Ensure requirements are installed:  
   ```bash
   pip install pandas numpy matplotlib scikit-learn
   ```  
3. Run notebook cells sequentially (top to bottom).  

---

## 📌 Next Steps  
- Hyperparameter tuning with GridSearch/RandomizedSearch.  
- Model explainability with SHAP values.  
- Deployment as a Streamlit dashboard for HR decision-makers.  

---

## 📜 License  
This project uses the **IBM HR Attrition Dataset (fictional)** provided for educational purposes.  
