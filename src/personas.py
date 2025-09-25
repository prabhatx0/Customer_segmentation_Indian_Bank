import pandas as pd

def assign_personas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Assigns business personas to customers based on their cluster's RFM characteristics.

    This function uses a rule-based approach on the median RFM values of each cluster.
    You may need to adjust the logic based on your specific cluster profiles.

    Args:
        df (pd.DataFrame): DataFrame with original RFM values and a 'Cluster' column.

    Returns:
        pd.DataFrame: The input DataFrame with an added 'Persona' column.
    """
    # Calculate median RFM values for each cluster
    cluster_profiles = df.groupby('Cluster').agg({
        'Recency': 'median',
        'Frequency': 'median',
        'MonetaryValue': 'median'
    }).reset_index()

    print("Cluster Profiles (Median RFM):")
    print(cluster_profiles)

    # Define personas based on typical RFM patterns
    # These rules are examples and should be tailored to the actual cluster characteristics
    
    # Sort clusters by MonetaryValue to identify high to low value
    sorted_clusters = cluster_profiles.sort_values(by='MonetaryValue', ascending=False)
    
    persona_map = {}
    
    # Top spender cluster is likely 'Champions' if R and F are good
    top_cluster = sorted_clusters.iloc[0]
    if top_cluster['Recency'] < df['Recency'].median() and top_cluster['Frequency'] > df['Frequency'].median():
        persona_map[top_cluster['Cluster']] = 'Champions'
    else:
        persona_map[top_cluster['Cluster']] = 'High-Value Sleepers'

    # Identify 'At-Risk' customers: high value but high recency (haven't transacted recently)
    at_risk_candidates = sorted_clusters[~sorted_clusters['Cluster'].isin(persona_map.keys())]
    at_risk_cluster = at_risk_candidates.sort_values('Recency', ascending=False).iloc[0]
    if at_risk_cluster['MonetaryValue'] > df['MonetaryValue'].median():
         persona_map[at_risk_cluster['Cluster']] = 'At-Risk Customers'
    else:
         persona_map[at_risk_cluster['Cluster']] = 'Lost Low-Value Customers'


    # 'New Customers' or 'Promising': low recency, low frequency
    new_cust_candidates = sorted_clusters[~sorted_clusters['Cluster'].isin(persona_map.keys())]
    new_cust_cluster = new_cust_candidates.sort_values('Recency').iloc[0]
    if new_cust_cluster['Frequency'] < df['Frequency'].median():
        persona_map[new_cust_cluster['Cluster']] = 'New & Promising'
    else:
        persona_map[new_cust_cluster['Cluster']] = 'Loyal Customers'
        
    # Any remaining cluster can be 'Needs Attention' or a default category
    for c in cluster_profiles['Cluster']:
        if c not in persona_map:
            persona_map[c] = 'Needs Attention'
            
    df['Persona'] = df['Cluster'].map(persona_map)
    
    print("\nPersona Mapping:")
    print(persona_map)
    print("\nPersonas assigned successfully.")
    
    return df

if __name__ == '__main__':
    # Create a sample clustered dataframe for testing
    data = {
        'CustomerID': [1, 2, 3, 4, 5, 6, 7, 8],
        'Recency': [10, 300, 50, 200, 20, 15, 250, 60],
        'Frequency': [50, 2, 20, 5, 30, 45, 3, 22],
        'MonetaryValue': [5000, 200, 1500, 800, 3000, 4800, 250, 1600],
        'Cluster': [0, 1, 2, 1, 0, 0, 1, 2]
    }
    clustered_df_sample = pd.DataFrame(data).set_index('CustomerID')
    
    persona_df = assign_personas(clustered_df_sample)
    
    print("\nData with Personas:")
    print(persona_df)
    print("\nPersona Counts:")
    print(persona_df['Persona'].value_counts())
