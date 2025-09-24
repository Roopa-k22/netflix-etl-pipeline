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

[Netflix Dataset] → [Extract] → [Transform] → [Load to DB] → [Analysis/Visualization]

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



