Customer Segmentation & Targeted Marketing for India Bank
This project implements an end-to-end pipeline for segmenting banking customers using RFM (Recency, Frequency, Monetary) analysis and K-Means clustering. The goal is to identify distinct customer personas to enable targeted and effective marketing campaigns.

Project Goal
The primary objective is to move from raw transaction data to actionable business insights. We achieve this by:

Segmenting customers based on their transactional behavior (RFM).

Using K-Means clustering to group customers into meaningful segments.

Translating these data-driven clusters into understandable business personas (e.g., "High-Value Champions", "At-Risk Customers").

Providing a foundation for creating targeted marketing strategies for each persona.

Codebase Structure
The project is organized into a modular structure for clarity, maintainability, and scalability.

/customer_segmentation_bfsi
|-- /data
|   |-- transactions.csv      # Raw and processed data
|   |-- customer_segments.csv # Output file with final segments and personas
|-- /notebooks
|   `-- (Exploratory notebooks, if any)
|-- /src
|   |-- data_preprocessing.py   # Load, clean, and preprocess data
|   |-- feature_engineering.py  # Compute RFM features
|   |-- clustering.py           # K-Means clustering and optimal k analysis
|   |-- visualization.py        # Generate plots for clusters and personas
|   |-- personas.py             # Map clusters to business personas
|-- /tests
|   |-- test_data_preprocessing.py
|   |-- test_feature_engineering.py
|-- /visuals
|   |-- (Generated plots and charts)
|-- main.py                     # Main script to run the entire pipeline
|-- requirements.txt            # Project dependencies
`-- README.md                   # This file

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
cd customer_segmentation_bfsi

Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required dependencies:

pip install -r requirements.txt

How to Run the Project
The entire pipeline can be executed by running the main.py script from the root directory of the project (customer_segmentation_bfsi).

python main.py

What the script does:
Loads the transaction data from data/transactions.csv.

Cleans and preprocesses the data.

Calculates RFM features for each customer.

Scales the RFM features.

Determines the optimal number of clusters (k) using the Elbow and Silhouette methods and saves the plots to the visuals folder.

Performs K-Means clustering with the chosen k (hardcoded as 4 in main.py for demonstration).

Assigns business personas to each cluster.

Generates and saves visualizations (cluster distribution, boxplots, 3D scatter plot) to the visuals folder.

Saves the final segmented data with customer IDs, RFM values, cluster labels, and personas to data/customer_segments.csv.

Expected Outputs
data/customer_segments.csv: A CSV file containing the final segmentation results for each customer.
| CustomerID | Recency | Frequency | MonetaryValue | Cluster | Persona               |
|------------|---------|-----------|---------------|---------|-----------------------|
| 1001       | ...     | ...       | ...           | 0       | Champions             |
| 1002       | ...     | ...       | ...           | 1       | At-Risk Customers     |

Visualizations in the /visuals folder:

optimal_k_plots.png: Elbow and Silhouette plots to help determine the best k.

cluster_distribution.png: Bar chart showing the number of customers in each cluster.

rfm_boxplots.png: Boxplots comparing the RFM distributions across clusters.

3d_scatter_plot.html: An interactive 3D plot to visualize the clusters.

Running Tests
To ensure the core logic is working correctly, you can run the unit tests.

python -m unittest discover tests
