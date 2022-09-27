import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt


def Q1_generate_samples():
    samples = np.random.randint(low=0, high=2, size=(40, 2))
    samples[samples == 0] = 5
    samples[samples == 1] = 20
    noise = np.random.randn(40, 2)
    samples = samples.astype(float) + noise

    with open('samples.npy', 'wb') as f:
        np.save(f, samples)
    return None


def Q2_plot_samples(samples):
    # plot
    fig, ax = plt.subplots()
    ax.scatter(samples[:, 0], samples[:, 1])
    ax.set(xlim=(0, 25), xticks=np.arange(1, 25, 5),
           ylim=(0, 25), yticks=np.arange(1, 25, 5))
    plt.show()


def Q3_cluster_samples(samples):
    db = DBSCAN(eps=5, min_samples=3).fit(samples)

    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_

    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise_ = list(labels).count(-1)
    print("Estimated number of clusters: %d" % n_clusters_)
    print("Estimated number of noise points: %d" % n_noise_)

    plot_dbscan(samples, labels, core_samples_mask, n_clusters_)


def Q4_clust_test_samples(samples):
    Q3_cluster_samples(samples)


def plot_dbscan(samples, labels, core_samples_mask, n_clusters_):
    # Black removed and is used for noise instead.
    unique_labels = set(labels)
    colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]
    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = [0, 0, 0, 1]

        class_member_mask = labels == k

        xy = samples[class_member_mask & core_samples_mask]
        plt.plot(
            xy[:, 0],
            xy[:, 1],
            "o",
            markerfacecolor=tuple(col),
            markeredgecolor="k",
            markersize=14,
        )

        xy = samples[class_member_mask & ~core_samples_mask]
        plt.plot(
            xy[:, 0],
            xy[:, 1],
            "o",
            markerfacecolor=tuple(col),
            markeredgecolor="k",
            markersize=6,
        )

    plt.title("Estimated number of clusters: %d" % n_clusters_)
    plt.show()
