# Netflix ETL Pipeline

A simple end-to-end ETL (Extract, Transform, Load) pipeline project using open-source tools and Python.
This project takes Netflix data, cleans and transforms it, and loads it into a database for analysis.

## 🚀 Project Overview

The goal of this project is to demonstrate an end-to-end data engineering workflow:

Extract: Pull raw Netflix data (CSV).

Transform: Clean, process, and prepare the data for analytics (handling nulls, formatting, feature engineering).

Load: Store the transformed data into a relational database (PostgreSQL/SQLite).

Orchestration: Use Apache Airflow to schedule and automate the pipeline.

Visualization: Analyze the processed data using SQL or Jupyter Notebooks.

## 🏗️ Architecture

[Netflix Dataset] → [Extract] → [Transform] → [Load to DB] → [Airflow Orchestration] → [Analysis/Visualization]

Dataset: Netflix titles dataset (movies and shows).

ETL Scripts: Python scripts for each step.

Database: PostgreSQL (or SQLite for simplicity).

Orchestration: Apache Airflow DAGs.

Analysis: SQL queries, Pandas, or visualization tools.

## 🛠️ Tech Stack

Python (pandas, sqlalchemy)

PostgreSQL / SQLite

Apache Airflow

Jupyter Notebook

Docker (optional) for containerization

## 📂 Repository Structure

netflix-etl-pipeline/
│── README.md              # Project overview, setup steps
│── requirements.txt       # Python dependencies
│── data/                  # Raw and processed datasets
│   ├── raw/               # Original Netflix dataset
│   └── processed/         # Cleaned & transformed data
│── src/                   # Source code
│   ├── extract/           # Extraction scripts
│   ├── transform/         # Transformation scripts
│   └── load/              # Loading scripts
│── airflow_dags/          # Airflow DAGs
│── notebooks/             # Jupyter notebooks
│── docs/                  # Documentation and diagrams
│── tests/                 # Unit tests

## ⚡ Setup Instructions

1. Clone the repo:
   git clone https://github.com/your-username/netflix-etl-pipeline.git
   cd netflix-etl-pipeline
2. Create a virtual environment & install dependencies:
   python3 -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   pip install -r requirements.txt
3. Add Netflix dataset in data/raw/.
4. Run ETL pipeline manually:
   python src/extract/extract_netflix.py
   python src/transform/transform_netflix.py
   python src/load/load_netflix.py
5. Start Airflow for orchestration.

## 📊 Example Analysis

After loading data into PostgreSQL:

Count number of movies vs TV shows.

Find top 10 directors with most Netflix titles.

Check content added by year.

## 🔮 Future Improvements

Add Docker for easier deployment.

Automate dataset updates.

Add dbt for transformations.

Build dashboard with Tableau/Power BI/Metabase.



