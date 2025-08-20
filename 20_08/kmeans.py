import os
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

DATASET_PATH = os.path.join(
    os.path.dirname(__file__), "dataset", "Online_Retail_with_clv2.csv"
)


def find_best_k(X) -> dict[int, float]:
    """
    Find the best number of clusters for KMeans using the elbow method.
    """
    sse: dict[int, float] = {}

    for k in range(1, 10):
        kmeans = KMeans(n_clusters=k, max_iter=1000).fit(X)
        sse[k] = (
            kmeans.inertia_
        )  # Inertia: Sum of distances of samples to their closest cluster center

    return sse


def plot_elbow(sse: dict[int, float]):
    """
    Plot the elbow curve to visualize the best number of clusters.
    """
    plt.figure()
    plt.plot(list(sse.keys()), list(sse.values()))
    plt.xlabel("Number of clusters")
    plt.ylabel("SSE (Sum of Squared Errors)")
    plt.title("Elbow Method for Optimal k")
    plt.show()


def train_kmeans(X, k):
    """
    Train KMeans with the specified number of clusters.
    """
    kmeans = KMeans(n_clusters=k, max_iter=1000).fit(X)
    return kmeans


def predict_kmeans(kmeans, X):
    """
    Predict the cluster labels for the given data using the trained KMeans model.
    """
    return kmeans.predict(X)


def plot_clusters(X, kmeans):
    """
    Plot the clusters formed by KMeans.
    """
    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap="viridis", marker="o")
    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c="red", marker="x", s=200)
    plt.xlabel("CustomerID")
    plt.ylabel("CLV")
    plt.title("KMeans Clustering")
    plt.show()


def main():
    df = pd.read_csv(DATASET_PATH)

    X = df[["CustomerID", "purchase_frequency"]].values

    sse = find_best_k(X)
    plot_elbow(sse)

    # trained_kmeans = train_kmeans(X, 3)

    # plot_clusters(X, trained_kmeans)


if __name__ == "__main__":
    main()
