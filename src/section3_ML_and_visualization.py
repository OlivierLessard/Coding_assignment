from src.section3_implementation import Q1_generate_samples, Q2_plot_samples, Q3_cluster_samples, Q4_clust_test_samples
import numpy as np


if __name__ == '__main__':
    Q1_generate_samples()
    samples = np.load("samples.npy")

    Q2_plot_samples(samples)

    Q3_cluster_samples(samples)

    test_samples = np.load("sample_data.npy")
    Q4_clust_test_samples(test_samples)

    # Q5
    """
    A) Points can be labeled as noise if they are not 'close enough' to clusters. Furthermore, points can be clustered 
    in the wrong cluster if the parameters are not chosen correctly. Borders points can be hard to cluster correctly. Their
    clustering may depend on the order the data is processed.
    
    B) Yes, the clusters are already well separated. The density of points in the cluster is high versus the density between clusters. 
    K-Means could have been a good choice too.
    
    C) I would change the dbscan parameters (eps=5, min_samples=3)
    
    D) Unsupervised learning. The data has not labels and the algorithm tries to extract information from the data itself.
    """