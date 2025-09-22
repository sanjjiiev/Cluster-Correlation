Step 1: Problem Understanding

    1D dataset: Production data (single variable)

    2D dataset: Geological data (two variables: Depth and Pressure)

Our goal is to find the correlation between these two clustered datasets.

Step 2: Data Synthesis

We generate synthetic data that mimics an oil field scenario. We create three groups of wells:

    Low producers: low production, shallow depth, low pressure

    Medium producers: medium production, medium depth, medium pressure

    High producers: high production, deep, high pressure
We use normal distributions to generate these groups and then shuffle the data to mix the rows (but the inherent relationship remains).
Step 3: Clustering

We perform clustering on both datasets:

    For the 1D production data, we use KMeans with 3 clusters and then order the clusters from low to high production.

    For the 2D geological data (Depth and Pressure), we first standardize the data (because the variables are on different scales) and then apply KMeans with 3 clusters.

Step 4: Cluster Comparison Metrics

We use two standard metrics to compare the two clusterings:

    Adjusted Rand Index (ARI): Measures the similarity between two clusterings by considering pairs of samples and counting those assigned to the same or different clusters in both clusterings. Adjusted for chance (0 means random, 1 means perfect match).

    Normalized Mutual Information (NMI): Measures the mutual information between the clusterings, normalized by the entropy of each clustering.
We also create a contingency table (cross-tabulation) to see the mapping between production clusters and geological clusters.
Step 5: Statistical Significance Test

We perform a chi-squared test of independence on the contingency table (without the margins) to check if the relationship between the two clusterings is statistically significant.
Step 6: Inter-Regional Correlation Estimation

We go beyond the cluster labels and look at the characteristics of each cluster. We calculate the centroids (mean values) of the geological features (Depth, Pressure) and production feature for each cluster. Then, we compute the Pearson correlation between the average geological features and the average production of the corresponding clusters.

Step 7: Visualization

We create a comprehensive set of visualizations:

    Original data colored by production value.

    Histogram of production clusters.

    Scatter plot of geological clusters.

    Heatmap of the contingency table.

    Scatter plot of average depth vs average production for the clusters (inter-regional).

    Scatter plot of average pressure vs average production for the clusters (inter-regional).
