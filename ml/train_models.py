import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib
import os

# Create models directory
os.makedirs('models', exist_ok=True)
os.makedirs('dataset', exist_ok=True)

print("Starting Machine Learning Pipeline...")

# ==========================================
# 1. Performance Prediction (Random Forest) & Marks (Linear Reg)
# Uses: Student_Performance.csv
# ==========================================
try:
    print("Loading Student_Performance.csv...")
    df_perf = pd.read_csv('Student_Performance.csv')
    
    # Simple preprocessing
    # Features: study_hours, attendance_percentage
    # Targets: overall_score (for Marks Prediction), final_grade (for Performance)
    X_perf = df_perf[['study_hours', 'attendance_percentage']].fillna(0)
    
    # Train Marks Predictor (Linear Regression)
    y_marks = df_perf['overall_score'].fillna(0)
    lr_model = LinearRegression()
    lr_model.fit(X_perf, y_marks)
    joblib.dump(lr_model, 'models/marks_predictor.pkl')
    print("Marks Prediction Model saved!")

    # Train Performance Classifier (Random Forest)
    y_grade = df_perf['final_grade'].fillna('C')
    le_grade = LabelEncoder()
    y_grade_encoded = le_grade.fit_transform(y_grade)
    
    rf_perf = RandomForestClassifier(n_estimators=50, random_state=42)
    rf_perf.fit(X_perf, y_grade_encoded)
    
    joblib.dump(rf_perf, 'models/performance_classifier.pkl')
    joblib.dump(le_grade, 'models/performance_label_encoder.pkl')
    print("Performance Prediction Model saved!")

except Exception as e:
    print("Error in Performance models:", e)

# ==========================================
# 2. Stress Prediction (Random Forest)
# Uses: student_lifestyle_performance_dataset.csv
# ==========================================
try:
    print("Loading student_lifestyle_performance_dataset.csv...")
    df_life = pd.read_csv('student_lifestyle_performance_dataset.csv')
    
    # Features: Study_Hours_per_Day, Sleep_Hours, Screen_Time_Hours, Gym_Hours_per_Week
    # Target: Stress_Level_1_to_10
    X_stress = df_life[['Study_Hours_per_Day', 'Sleep_Hours', 'Screen_Time_Hours', 'Gym_Hours_per_Week']].fillna(0)
    
    # Convert stress level 1-10 into categories
    def categorize_stress(level):
        if level <= 3: return 'Low Stress'
        elif level <= 7: return 'Moderate Stress'
        else: return 'High Stress'
        
    y_stress = df_life['Stress_Level_1_to_10'].apply(categorize_stress)
    
    rf_stress = RandomForestClassifier(n_estimators=50, random_state=42)
    rf_stress.fit(X_stress, y_stress)
    
    joblib.dump(rf_stress, 'models/stress_classifier.pkl')
    print("Stress Prediction Model saved!")

except Exception as e:
    print("Error in Stress model:", e)

# ==========================================
# 3. Productivity Prediction (Decision Tree)
# Uses: student_productivity_distraction_dataset_20000.csv
# ==========================================
try:
    print("Loading student_productivity_distraction_dataset_20000.csv...")
    df_prod = pd.read_csv('student_productivity_distraction_dataset_20000.csv')
    
    # Features: phone_usage_hours, social_media_hours, breaks_per_day, exercise_minutes
    # Target: productivity_score
    features = ['phone_usage_hours', 'social_media_hours', 'breaks_per_day', 'exercise_minutes']
    X_prod = df_prod[features].fillna(0)
    
    # Convert productivity_score (numerical) to categories
    def categorize_productivity(score):
        if score < 40: return 'Low Productivity'
        elif score < 75: return 'Medium Productivity'
        else: return 'High Productivity'
        
    y_prod = df_prod['productivity_score'].apply(categorize_productivity)
    
    dt_prod = DecisionTreeClassifier(random_state=42, max_depth=5)
    dt_prod.fit(X_prod, y_prod)
    
    joblib.dump(dt_prod, 'models/productivity_classifier.pkl')
    print("Productivity Prediction Model saved!")

except Exception as e:
    print("Error in Productivity model:", e)

print("All ML Models trained successfully!")
