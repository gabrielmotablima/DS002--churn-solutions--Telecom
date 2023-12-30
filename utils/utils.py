import pandas as pd

from sklearn.metrics import (
    silhouette_score,
    davies_bouldin_score,
    calinski_harabasz_score,
    adjusted_rand_score,
    adjusted_mutual_info_score,
    homogeneity_completeness_v_measure,
    fowlkes_mallows_score
)

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

def df_columns(df: pd.DataFrame):
    numerical_columns = ["tenure", "MonthlyCharges", "TotalCharges"]
    categorical_columns = list(set(df.columns.tolist()) - set(numerical_columns) - set(["customerID"]))
    return numerical_columns, categorical_columns


def cluster_metrics(model, data, labels_true, labels_pred):
    silhouette = silhouette_score(data, labels_pred)
    davies_bouldin = davies_bouldin_score(data, labels_pred)
    calinski_harabasz = calinski_harabasz_score(data, labels_pred)
    mutual_info = adjusted_mutual_info_score(labels_true, labels_pred)
    homogeneity, completeness, v_measure = homogeneity_completeness_v_measure(labels_true, labels_pred)
    fowlkes_mallows = fowlkes_mallows_score(labels_true, labels_pred)

    print(f"Results for {model}:")
    print(f"Silhouette Score: {silhouette}")
    print(f"Davies-Bouldin Score: {davies_bouldin}")
    print(f"Calinski-Harabasz Score: {calinski_harabasz}")
    print(f"Adjusted Mutual Information: {mutual_info}")
    print(f"Homogeneity: {homogeneity}")
    print(f"Completeness: {completeness}")
    print(f"V-Measure: {v_measure}")
    print(f"Fowlkes-Mallows Score: {fowlkes_mallows}\n")
