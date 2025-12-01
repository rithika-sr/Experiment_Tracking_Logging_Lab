# 🫀 MLOps Logging Lab – Heart Disease Dataset Analysis

This project is my custom implementation of the **MLOps Logging Lab**, where I built a complete Python logging pipeline using a real-world dataset (`heart.csv`).  
The goal of this lab is to demonstrate **professional logging practices**, modular project structure, safe data loading, and step-by-step analysis with detailed debug tracking.


## 🚀 Project Overview

This lab implements:

- Custom logger configuration  
- Console + file logging using handlers  
- Exception-safe CSV loading  
- Modular architecture (`app/` folder)  
- Automatic log file creation  
- Numeric column analysis with detailed debug logs  
- Clean and reproducible project flow  

The project analyzes the **Heart Disease dataset**, performing mean and max calculations on all numeric columns, while logging every step of execution.

---

## 📁 Project Structure


```
Experiment_Tracking_Logging_Lab/
│
├── app/
│   ├── logger_config.py      # Logger setup with console+file handlers
│   ├── data_loader.py        # Safe CSV loading with exception logging
│   └── analyzer.py           # Numeric column analysis with debug logs
│
├── logs/
│   └── app.log               # Automatically generated log file
│
├── heart.csv                 # Heart disease dataset (real dataset)
├── main.py                   # Application entry point
└── Starter.ipynb             # Reference notebook from course
```


---

## 🔧 How to Run

1. Install dependencies:
```bash
pip install pandas
````

2. Run the application:

```bash
python main.py
```

3. Logs will appear both in the console and inside:

```
logs/app.log
```

---

## 📊 Example Output
<img width="1906" height="822" alt="image" src="https://github.com/user-attachments/assets/c4ed167b-32e7-4ee5-b2f7-abf8502dfeda" />

```
age -> mean: 54.366, max: 77.000
sex -> mean: 0.683, max: 1.000
cp -> mean: 0.967, max: 3.000
...
target -> mean: 0.545, max: 1.000
```

### The log file includes:

* Dataset loading steps
* Column detection
* Debug logs for each analyzed column
* Summary of results
* Errors (if any occur)

---

## 🧠 What This Lab Demonstrates

* How to configure a **real logging pipeline** in Python
* How to structure code in a clean, modular way
* How to track data pipeline execution with INFO + DEBUG logs
* How to catch and log exceptions safely
* How to work with real datasets in MLOps contexts

---

## 📘 Dataset Information

**Dataset:** Heart Disease Data
**Features include:**

* Age, sex, chest pain type
* Resting blood pressure, cholesterol
* Maximum heart rate
* Oldpeak, slope, ca, thal
* Target (heart disease presence)

The analyzer automatically detects **all numeric columns** and computes their summary statistics.

---

## ✔ Summary

This project showcases a complete end-to-end logging workflow, implemented cleanly and professionally.
It reflects real MLOps practices such as structured modules, robust exception handling, and detailed pipeline visibility.


