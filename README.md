i.	Problem statement
College students often struggle to balance academic performance, personal well-being, and lifestyle habits. Managing attendance, organizing daily schedules, tracking study hours, and maintaining productivity while avoiding distractions can become overwhelming without a centralized, data-driven tool. There is a need for a unified platform that not only tracks these metrics but also leverages Artificial Intelligence to provide actionable insights, predict performance, and optimize daily routines.

ii.	Objective
•	To develop an AI-powered web application that acts as a comprehensive academic productivity and lifestyle dashboard.
•	To utilize Machine Learning models to predict student marks, final grades, stress levels, and productivity based on lifestyle and academic data.
•	To integrate an OCR-based system for automated attendance tracking from university ERP portal screenshots.
•	To provide a dynamic day planner that integrates the student's timetable with real-time predictions to optimize their schedule.


iii.	Proposed Methodology
•	Data Collection & Preprocessing: Gather datasets related to student performance, lifestyle, and productivity. Clean and preprocess the data for model training.
•	Model Training: Develop and train four Machine Learning models (Linear Regression, Random Forest, Decision Tree) to predict outcomes like marks, grades, stress, and productivity.
•	Backend Development: Build a robust Flask-based RESTful backend to serve API endpoints and handle routing.
•	Frontend Development: Design an intuitive, responsive, and glassmorphic UI using Bootstrap 5, Jinja2 templates, and Plotly.js for data visualization.
•	Feature Integration: Implement the OCR attendance parser using Tesseract and OpenCV, and integrate the dynamic planner module.
•	Testing & Refinement: Test the application locally, refine model accuracies, and ensure seamless user experience across the dashboard.

iv.	Expected Outcome
A fully functional web application running locally on a Flask server that allows students to view their timetables, track their attendance using OCR, log their daily habits, and receive AI-driven predictions regarding their academic performance and stress levels. The dashboard will visually present data analytics to help students make informed decisions about their study routines.

v.	Future-scope and Limitations
•	Future Scope: Integration with external APIs (like Google Calendar), cloud deployment (e.g., AWS or Heroku), mobile application development, and adding a personalized chatbot for study tips.
•	Limitations: The OCR system heavily depends on the image quality and specific format of the university's ERP portal. The machine learning predictions are based on historical datasets which may not fully capture individual psychological factors. The application currently stores data in local CSV files rather than a scalable relational database.
