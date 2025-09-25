import os
from src.data_preprocessing import load_data, clean_data, preprocess_transactions
from src.feature_engineering import calculate_rfm
from src.clustering import scale_features, find_optimal_k, perform_kmeans
from src.visualization import plot_cluster_distribution, plot_rfm_boxplots, plot_3d_scatter
from src.personas import assign_personas

def main():
    """
    Main function to run the entire customer segmentation pipeline.
    """
    # Define file paths
    data_path = 'data/transactions.csv'
    output_path = 'data/customer_segments.csv'
    
    # Create directories if they don't exist
    os.makedirs('data', exist_ok=True)
    os.makedirs('visuals', exist_ok=True)
    
    print("--- Starting Customer Segmentation Pipeline ---")

    # 1. Data Preprocessing
    print("\nStep 1: Data Preprocessing...")
    transactions_df = load_data(data_path)
    if transactions_df is None:
        print("Halting pipeline due to data loading failure.")
        return
        
    cleaned_df = clean_data(transactions_df)
    preprocessed_df = preprocess_transactions(cleaned_df)

    # 2. Feature Engineering (RFM)
    print("\nStep 2: Feature Engineering (RFM)...")
    rfm_df = calculate_rfm(preprocessed_df)

    # 3. Clustering
    print("\nStep 3: K-Means Clustering...")
    # Scale features before clustering
    scaled_rfm_df = scale_features(rfm_df)
    
    # Find optimal k (for exploratory analysis)
    # In a production pipeline, you might set a fixed k.
    print("Finding optimal number of clusters (k)...")
    find_optimal_k(scaled_rfm_df)
    
    # Let's assume k=4 is chosen based on the elbow/silhouette plots
    OPTIMAL_K = 4
    print(f"Performing clustering with k={OPTIMAL_K}...")
    clustered_df, _ = perform_kmeans(scaled_rfm_df.copy(), k=OPTIMAL_K)
    
    # Add cluster labels back to the original RFM dataframe
    rfm_df['Cluster'] = clustered_df['Cluster']

    # 4. Persona Assignment
    print("\nStep 4: Assigning Personas...")
    final_df = assign_personas(rfm_df)

    # 5. Visualization
    print("\nStep 5: Generating Visualizations...")
    plot_cluster_distribution(final_df)
    plot_rfm_boxplots(final_df)
    plot_3d_scatter(final_df)

    # 6. Save Results
    print(f"\nStep 6: Saving final segmented data to {output_path}...")
    final_df.to_csv(output_path)
    print("Results saved successfully.")

    print("\n--- Customer Segmentation Pipeline Finished ---")
    print("\nFinal Data Head:")
    print(final_df.head())

if __name__ == '__main__':
    main()
