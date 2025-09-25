Customer Segmentation & Targeted Marketing for India Bank
This project implements an end-to-end pipeline for segmenting banking customers using RFM (Recency, Frequency, Monetary) analysis and K-Means clustering. The goal is to identify distinct customer personas to enable targeted and effective marketing campaigns.

Project Goal
The primary objective is to move from raw transaction data to actionable business insights. We achieve this by:

Segmenting customers based on their transactional behavior (RFM).

Using K-Means clustering to group customers into meaningful segments.

Translating these data-driven clusters into understandable business personas (e.g., "High-Value Champions", "At-Risk Customers").

Providing a foundation for creating targeted marketing strategies for each persona.

Codebase Structure

```text
customer_segmentation/
├─ data/
│  │─ transactions.csv       
├─ src/
│  ├─ __init__.py
│  ├─ data_preprocessing.py
│  ├─ feature_engineering.py
│  ├─ clustering.py
│  ├─ visualization.py
│  ├─ personas.py
|
├─ tests/
│  ├─ test_data_preprocessing.py
│  ├─ test_feature_engineering.py
│ 
├─ main.py
├─ requirements.txt
└─ README.md

```

Technical Stack
Python 3.10+

Pandas & NumPy for data manipulation

scikit-learn for K-Means clustering and evaluation metrics

Matplotlib & Seaborn for static visualizations

Plotly for interactive 3D visualizations

Jupyter for initial exploration (optional)

Setup and Installation
Clone the repository:

git clone <repository-url>
cd customer_segmentation

Create a virtual environment

Install the required dependencies:

pip install -r requirements.txt

How to Run the Project
The entire pipeline can be executed by running the main.py script from the root directory of the project.

python main.py


