# 🛒 MLOps-CIA1 — Online Shopper Purchase Prediction

An end-to-end **MLOps pipeline for predicting online shopping purchase intention** using the UCI Online Shoppers Purchasing Intention Dataset.

The project demonstrates the integration of **Machine Learning, MLflow, DVC, Kubeflow, Feast, Git/GitHub, and AWS SageMaker** into a reproducible MLOps workflow.

---

## 📌 Project Overview

The objective of this project is to predict whether an online shopping visitor will generate revenue (`Revenue = True`) based on browsing/session information.

The project follows an MLOps workflow covering:

```text
Dataset
   │
   ▼
DVC ───────────────► Dataset Versioning
   │
   ▼
Data Preprocessing
   │
   ▼
Model Training
   │
   ├──────────────► MLflow ──► Experiment Tracking
   │
   ├──────────────► Kubeflow ─► ML Pipeline
   │
   └──────────────► Feast ────► Feature Store
   │
   ▼
Model Evaluation
   │
   ▼
Deployment Preparation
   │
   └──────────────► AWS SageMaker
```

---

## 🎯 Objectives

- Perform preprocessing and preparation of online shopping data.
- Train and compare multiple classification models.
- Track experiments and model metrics using **MLflow**.
- Version datasets using **DVC**.
- Build a reproducible ML pipeline using **Kubeflow Pipelines**.
- Manage ML features using **Feast**.
- Prepare the trained model for cloud deployment using **AWS SageMaker**.
- Evaluate the models using Accuracy, Precision, Recall, and F1-score.

---

## 📊 Dataset

**Dataset:** UCI Online Shoppers Purchasing Intention Dataset

The dataset contains information about online shopping sessions and whether the session resulted in a purchase.

### Dataset Information

| Property | Value |
|---|---:|
| Original records | 12,330 |
| Features | 17 input features |
| Target | `Revenue` |
| Original duplicate records | 125 |
| Final records after duplicate removal | 12,205 |
| Train/Test split | 80% / 20% |
| Random state | 42 |

### Target Distribution

The target variable is:

```text
Revenue = False → No purchase
Revenue = True  → Purchase
```

The dataset is imbalanced, with substantially more non-purchase sessions than purchase sessions. Therefore, Precision, Recall, and F1-score were considered along with Accuracy.

---

## 🧹 Data Preprocessing

The following preprocessing steps were implemented:

1. Duplicate records were identified and removed.
2. `Revenue` was converted from Boolean to integer format.
3. Numerical and categorical features were separated.
4. Numerical features were standardized using `StandardScaler`.
5. Categorical features were encoded using `OneHotEncoder`.
6. A stratified 80:20 train-test split was performed.
7. The preprocessing and model were combined into a reusable scikit-learn Pipeline.

### Numerical Features

```text
Administrative
Administrative_Duration
Informational
Informational_Duration
ProductRelated
ProductRelated_Duration
BounceRates
ExitRates
PageValues
SpecialDay
OperatingSystems
Browser
Region
TrafficType
```

### Categorical Features

```text
Month
VisitorType
Weekend
```

After preprocessing, the feature representation contained **29 processed features**.

---

# 🤖 Machine Learning Models

Three classification algorithms were trained and evaluated:

### 1. Logistic Regression

Used as the baseline classification model.

### 2. Random Forest

An ensemble learning model using multiple decision trees.

### 3. XGBoost

A gradient boosting model used for comparison with the baseline and Random Forest models.

---

# 📈 Model Results

The models were evaluated on the held-out test set.

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 88.94% | 77.18% | 41.62% | 54.08% |
| Random Forest | **90.37%** | 75.26% | 57.33% | 65.08% |
| XGBoost | 90.25% | 72.50% | **60.73%** | **66.10%** |

### Observations

- Logistic Regression achieved **88.94% accuracy**.
- Random Forest achieved the highest **accuracy of 90.37%**.
- XGBoost achieved the highest **Recall (60.73%)**.
- XGBoost also achieved the highest **F1-score (66.10%)**.
- The tree-based ensemble models provided stronger overall performance than the Logistic Regression baseline.

---

# 🔬 MLflow — Experiment Tracking

MLflow was used to track the machine learning experiments.

The following information was logged for each model:

### Parameters

- Model name
- Test size
- Random state
- Model-specific hyperparameters

### Metrics

- Accuracy
- Precision
- Recall
- F1-score

### Artifacts

- Trained model files
- Confusion matrix images

### MLflow Experiment

```text
Online Shopper Purchase Prediction v2
```

The MLflow runs were programmatically verified after training.

---

# 🗂️ DVC — Dataset Versioning

DVC was used to version the dataset and maintain reproducibility.

### Version 1

The original UCI dataset was added and tracked using DVC.

```text
DVC: Version 1 of Online Shoppers dataset
```

### Version 2

Duplicate records were removed and the updated dataset was tracked as a second version.

```text
DVC: Version 2 - removed duplicate records
```

The final dataset contains:

```text
12,205 records
0 duplicate records
```

Git was used to track the DVC metadata and dataset versions.

---

# ⚙️ Kubeflow — ML Pipeline

A Kubeflow pipeline was designed to represent the ML workflow as separate components.

### Pipeline Components

```text
┌────────────────────┐
│  Preprocess Data   │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│    Train Model     │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│  Evaluate Model    │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Evaluation Metrics │
└────────────────────┘
```

### Components Implemented

**1. Preprocess Data**
- Loads dataset
- Removes duplicates
- Performs train-test split
- Applies preprocessing
- Generates processed data artifacts

**2. Train Model**
- Trains a Random Forest classifier
- Generates a model artifact

**3. Evaluate Model**
- Calculates Accuracy
- Calculates Precision
- Calculates Recall
- Calculates F1-score

The pipeline was successfully compiled into:

```text
online_shoppers_pipeline.yaml
```

---

# 🧠 Feast — Feature Store

Feast was implemented as the feature-store component of the project.

### Entity

```text
visitor
```

### Feature View

```text
online_shopper_features
```

### Feature Storage

The feature data was prepared in Parquet format and registered with Feast.

An event timestamp was added to support Feast's feature-store requirements.

### Feast Workflow

```text
Raw Dataset
     │
     ▼
Feature Preparation
     │
     ▼
Parquet Feature Data
     │
     ▼
Feast Feature View
     │
     ▼
Materialization
     │
     ▼
Online Feature Retrieval
```

The feature store was successfully applied, materialized, and tested through online feature retrieval.

---

# ☁️ AWS SageMaker — Deployment Preparation

The trained Random Forest pipeline was prepared for deployment.

### Deployment Steps Completed

1. Retrained the deployment model using a compatible scikit-learn environment.
2. Created a SageMaker inference script.
3. Packaged the model and inference code into:

```text
model.tar.gz
```

4. Uploaded the model artifact to Amazon S3.
5. Created the SageMaker model successfully.

### Model Artifact

```text
s3://mlops-cia1-shubham-2026/sagemaker-model/model.tar.gz
```

### Inference Script

The inference implementation supports:

```text
model_fn()
input_fn()
predict_fn()
output_fn()
```

The model accepts JSON input containing the online-shopping features and returns the predicted purchase outcome.

### Deployment Limitation

The final real-time SageMaker endpoint could not be created because the provided VocLabs AWS environment explicitly denied:

```text
sagemaker:CreateEndpointConfig
```

The denial originated from the lab IAM policy:

```text
PvocLabs2
```

Therefore:

```text
SageMaker Model Creation     ✅
S3 Model Artifact            ✅
Endpoint Configuration       ❌ IAM restricted
Real-time Endpoint           ❌ Not completed
```

This was an environment-level IAM restriction rather than a model or implementation error.

---

# 📁 Project Structure

```text
MLOps-CIA1/
│
├── data/
│   └── online_shoppers_intention.csv
│
├── notebooks/
│   ├── MLOps_CIA1.ipynb
│   └── SageMaker_Deployment.ipynb
│
├── feast_repo/
│   ├── feature_store.yaml
│   ├── feature_definitions.py
│   └── data/
│       └── online_shoppers_features.parquet
│
├── online_shoppers_pipeline.yaml
│
├── models/
│   └── random_forest_model.joblib
│
├── mlruns/
│   └── MLflow experiment artifacts
│
├── .dvc/
│   └── DVC metadata/cache configuration
│
├── data.dvc
│
└── README.md
```

> File locations may vary slightly depending on the execution environment and notebook workflow.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Scikit-learn | Preprocessing and ML models |
| XGBoost | Gradient boosting model |
| MLflow | Experiment tracking |
| DVC | Dataset versioning |
| Git & GitHub | Source/version control |
| Kubeflow Pipelines | ML workflow orchestration |
| Feast | Feature store |
| Parquet | Feature data storage |
| AWS S3 | Model artifact storage |
| AWS SageMaker | Model deployment preparation |
| Google Colab | Development environment |

---

# 🚀 How to Run

## 1. Clone the Repository

```bash
git clone https://github.com/shubham8patil/MLOps-CIA1.git
cd MLOps-CIA1
```

## 2. Install Required Libraries

```bash
pip install pandas numpy scikit-learn xgboost mlflow dvc feast kfp joblib
```

Additional packages may be required depending on the specific notebook or component being executed.

---

## 3. Run the Main Notebook

Open:

```text
MLOps_CIA1.ipynb
```

The notebook contains the primary ML implementation, preprocessing, model training, evaluation, MLflow tracking, and related MLOps work.

---

## 4. Run the Kubeflow Pipeline

The compiled pipeline definition is available as:

```text
online_shoppers_pipeline.yaml
```

It can be uploaded to a compatible Kubeflow Pipelines environment.

---

## 5. Run Feast

Navigate to the Feast repository:

```bash
cd feast_repo
```

Apply the feature definitions:

```bash
feast apply
```

Materialize the features:

```bash
feast materialize 2026-01-01 2026-01-02
```

The feature store can then be queried for online features.

---

# 🔁 MLOps Lifecycle Implemented

The project demonstrates the following lifecycle:

```text
        ┌─────────────────────┐
        │       Dataset       │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │        DVC          │
        │  Version Dataset    │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │   Preprocessing     │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │   Model Training    │
        └──────┬──────┬───────┘
               │      │
       ┌───────┘      └────────┐
       ▼                       ▼
┌─────────────┐         ┌─────────────┐
│   MLflow    │         │   Kubeflow  │
│ Experiments │         │   Pipeline   │
└─────────────┘         └─────────────┘
               │
               ▼
        ┌─────────────────────┐
        │       Feast         │
        │   Feature Store     │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │  Model Evaluation   │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │ Deployment Prepare  │
        │   AWS SageMaker     │
        └─────────────────────┘
```

---

# 📌 Key Findings

- Removing duplicate records reduced the dataset from **12,330 to 12,205 records**.
- The target variable is imbalanced, making metrics beyond accuracy important.
- Ensemble models performed better than the Logistic Regression baseline.
- Random Forest achieved the highest accuracy.
- XGBoost achieved the highest recall and F1-score.
- MLflow successfully tracked the experiments and evaluation metrics.
- DVC successfully maintained two dataset versions.
- The Kubeflow pipeline was successfully created and compiled.
- Feast successfully registered, materialized, and served online features.
- The SageMaker model was successfully created, but endpoint creation was restricted by the provided AWS IAM policy.

---

# 🎓 Conclusion

This project demonstrates an end-to-end MLOps workflow for an online shopping purchase prediction problem.

The implementation integrates **data versioning, experiment tracking, pipeline orchestration, feature management, model evaluation, and deployment preparation** into a single workflow.

The final results show that ensemble-based models provided strong predictive performance, with Random Forest achieving **90.37% accuracy** and XGBoost achieving the highest **66.10% F1-score**.

Although the final SageMaker real-time endpoint could not be created due to an IAM restriction in the provided VocLabs environment, the model artifact was successfully packaged, uploaded to S3, and registered as a SageMaker model.

---

# 👨‍💻 Author

**Shubham Patil**

MSc Artificial Intelligence & Machine Learning  
Christ University, Bangalore

GitHub: [@shubham8patil](https://github.com/shubham8patil)

---

# 📜 License

This project was developed for academic and educational purposes as part of an MLOps coursework assignment.

