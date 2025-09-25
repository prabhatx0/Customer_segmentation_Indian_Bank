import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Tuple

def scale_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Scales the RFM features using StandardScaler.

    Args:
        df (pd.DataFrame): DataFrame with RFM features.

    Returns:
        pd.DataFrame: DataFrame with scaled features.
    """
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df)
    scaled_df = pd.DataFrame(scaled_features, index=df.index, columns=df.columns)
    print("RFM features scaled successfully.")
    return scaled_df

def find_optimal_k(df: pd.DataFrame, max_k: int = 10):
    """
    Finds the optimal number of clusters (k) using the Elbow and Silhouette methods.

    Args:
        df (pd.DataFrame): DataFrame with scaled features.
        max_k (int): Maximum number of clusters to test.
    """
    wcss = []
    silhouette_scores = []
    k_values = range(2, max_k + 1)

    for k in k_values:
        kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10)
        kmeans.fit(df)
        wcss.append(kmeans.inertia_)
        silhouette_scores.append(silhouette_score(df, kmeans.labels_))

    # Plot Elbow Method
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.lineplot(x=k_values, y=wcss, marker='o')
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('WCSS')
    plt.grid(True)

    # Plot Silhouette Scores
    plt.subplot(1, 2, 2)
    sns.lineplot(x=k_values, y=silhouette_scores, marker='o')
    plt.title('Silhouette Scores for Each k')
    plt.xlabel('Number of clusters (k)')
    plt.ylabel('Silhouette Score')
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('../visuals/optimal_k_plots.png')
    print(f"Optimal k plots saved to ../visuals/optimal_k_plots.png")
    plt.show()


def perform_kmeans(df: pd.DataFrame, k: int) -> Tuple[pd.DataFrame, KMeans]:
    """
    Performs K-Means clustering on the given data.

    Args:
        df (pd.DataFrame): DataFrame with scaled RFM features.
        k (int): The number of clusters.

    Returns:
        Tuple[pd.DataFrame, KMeans]: A tuple containing the DataFrame with cluster labels
                                     and the trained KMeans model.
    """
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(df)
    print(f"K-Means clustering performed with k={k}.")
    return df, kmeans

if __name__ == '__main__':
    # Example Usage from a dummy RFM dataframe
    data = {'Recency': [10, 300, 50, 200, 20],
            'Frequency': [50, 2, 20, 5, 30],
            'MonetaryValue': [5000, 200, 1500, 800, 3000]}
    rfm_df_sample = pd.DataFrame(data, index=[1001, 1002, 1003, 1004, 1005])
    
    scaled_rfm = scale_features(rfm_df_sample)
    
    print("\nFinding optimal k...")
    find_optimal_k(scaled_rfm) # This will show plots
    
    optimal_k = 4 # Assume we chose 4 from the plots
    print(f"\nPerforming K-Means with k={optimal_k}...")
    clustered_df, kmeans_model = perform_kmeans(scaled_rfm.copy(), optimal_k)
    
    print("\nClustered Data:")
    print(clustered_df)
