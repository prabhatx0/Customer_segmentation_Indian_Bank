import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def plot_cluster_distribution(df: pd.DataFrame):
    """
    Plots the distribution of customers across clusters.

    Args:
        df (pd.DataFrame): DataFrame with a 'Cluster' column.
    """
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Cluster', data=df, palette='viridis')
    plt.title('Customer Distribution Across Clusters')
    plt.xlabel('Cluster')
    plt.ylabel('Number of Customers')
    plt.grid(axis='y')
    plt.savefig('../visuals/cluster_distribution.png')
    print("Cluster distribution plot saved to ../visuals/cluster_distribution.png")
    plt.show()

def plot_rfm_boxplots(df: pd.DataFrame):
    """
    Creates boxplots for RFM features for each cluster.

    Args:
        df (pd.DataFrame): DataFrame with RFM features and a 'Cluster' column.
    """
    features = ['Recency', 'Frequency', 'MonetaryValue']
    plt.figure(figsize=(15, 10))
    
    for i, feature in enumerate(features, 1):
        plt.subplot(2, 2, i)
        sns.boxplot(x='Cluster', y=feature, data=df, palette='viridis')
        plt.title(f'{feature} by Cluster')

    plt.tight_layout()
    plt.savefig('../visuals/rfm_boxplots.png')
    print("RFM boxplots saved to ../visuals/rfm_boxplots.png")
    plt.show()

def plot_3d_scatter(df: pd.DataFrame):
    """
    Creates an interactive 3D scatter plot of the clusters.

    Args:
        df (pd.DataFrame): DataFrame with RFM features and a 'Cluster' column.
    """
    fig = px.scatter_3d(df,
                        x='Recency',
                        y='Frequency',
                        z='MonetaryValue',
                        color='Cluster',
                        symbol='Cluster',
                        size_max=18,
                        opacity=0.7)

    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0),
                      title='3D Scatter Plot of RFM Clusters')
    fig.write_html("../visuals/3d_scatter_plot.html")
    print("3D scatter plot saved to ../visuals/3d_scatter_plot.html")
    fig.show()

if __name__ == '__main__':
    # Create a sample clustered dataframe for testing
    data = {
        'Recency': [10, 300, 50, 200, 20, 15, 250, 60],
        'Frequency': [50, 2, 20, 5, 30, 45, 3, 22],
        'MonetaryValue': [5000, 200, 1500, 800, 3000, 4800, 250, 1600],
        'Cluster': [0, 1, 2, 1, 0, 0, 1, 2]
    }
    clustered_df_sample = pd.DataFrame(data)
    
    plot_cluster_distribution(clustered_df_sample)
    plot_rfm_boxplots(clustered_df_sample)
    plot_3d_scatter(clustered_df_sample)
