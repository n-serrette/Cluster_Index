#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Internal cluster index seen in literature."""
from __future__ import division
import math
import numpy as np


__all__ = (
    'c_index',
    'wcss',
    'bcss',
    'calinski_harabasz',
    'log_ss_ratio',
    'ball_hall',
    'sd',
    'xie_beni',
    'ray_turi',
    'gamma',
    'silhouette'
    )


# TODO: small delta between c_index, gamma index, tau index
# and their value in clusterCrit
# TODO: issues with S_Dbw index
def compute_distance_matrix(data):
    """Compute the euclidian distance matrix of the data."""
    n = len(data)
    matrix = np.zeros([n, n])
    for i in range(n):
        for j in range(i):
            matrix[i][j] = matrix[j][i] = np.linalg.norm(data[i]-data[j])
    return matrix


def single_linkage_distance(cluster_data_1, cluster_data_2):
    """Single linkage distance."""
    dist_min = np.inf
    for p1 in cluster_data_1:
        for p2 in cluster_data_2:
            dist = np.linalg.norm(p1-p2)
            if dist < dist_min:
                dist_min = dist
    return dist_min


def compute_pairs_count(labels):
    """Pair count

        Nt total number of pair

        Nb the number of pairs constituted of points which do not
         belong to the same cluster

        Nw the number of pairs constituted of points which belong
        to the same cluster
    """
    Nt = 0
    Nb = 0
    Nw = 0
    for i in range(len(labels)):
        for j in range(i):
            Nt += 1
            if labels[i] == labels[j]:
                Nw += 1
            else:
                Nb += 1
    return (Nt, Nw, Nb)


def concordante_discordante_pair_count(labels, data):
    """Count concordante and discordante pair in the classification."""
    within_dist = []
    between_dist = []
    N = len(labels)
    for i in range(N):
        for j in range(i):
            if labels[i] == labels[j]:
                within_dist.append(np.linalg.norm(data[i]-data[j]))
            else:
                between_dist.append(np.linalg.norm(data[i]-data[j]))
    concordante_count = 0
    discordante_count = 0
    for w in within_dist:
        for b in between_dist:
            if w < b:
                concordante_count += 1
            elif b < w:
                discordante_count += 1
    return (concordante_count, discordante_count)


def average_scattering(labels, data):
    """Average scattering for clusters."""
    norm_v = np.linalg.norm(np.var(data, axis=0))
    clusters = set(labels)
    K = len(clusters)
    sum_variance_k = 0
    for c in clusters:
        clust_point = data[labels == c]
        sum_variance_k += np.linalg.norm(np.var(clust_point, axis=0))
    return (sum_variance_k/K)/norm_v


def total_separation(labels, data):
    """Total separation between clusters"""
    clusters = set(labels)
    centroids = []

    for c in clusters:
        clust_point = data[labels == c]
        centroids.append(np.mean(clust_point, axis=0))

    centroids_dist = []
    d_sum = 0
    for i in centroids:
        centroids_dist_tmp = []
        for j in [x for x in centroids if np.all(x != i)]:
            centroids_dist_tmp.append(np.linalg.norm(i-j))
        centroids_dist += centroids_dist_tmp
        d_sum += 1 / np.sum(centroids_dist_tmp)

    d_max = np.max(centroids_dist)
    d_min = np.min(centroids_dist)

    return d_max/d_min * d_sum


def _s_dbw_sigma(labels, data):
    """Limit value for S_Dbw's density."""
    clusters = set(labels)
    sum_variance_k = 0
    for c in clusters:
        clust_point = data[labels == c]
        sum_variance_k += np.linalg.norm(np.var(clust_point, axis=0))
    return 1/len(clusters) * np.sqrt(sum_variance_k)


def _s_dbw_density(labels, data, cluster_1, cluster_2, point):
    """Compute the density for the given point, use in S_Dbw index."""
    clusters_union = data[labels == cluster_1] + data[labels == cluster_2]
    sigma = _s_dbw_sigma(labels, data)
    density = 0
    for p in clusters_union:
        if np.linalg.norm(p-point) <= sigma:
            density += 1
    return density


def _s_dbw_cluster_pair_density(labels, data, cluster_1, cluster_2):
    """"Compute density ratio for the two given clusters."""
    clust_point = data[labels == cluster_1]
    centroid_1 = np.mean(clust_point, axis=0)
    clust_point = data[labels == cluster_2]
    centroid_2 = np.mean(clust_point, axis=0)
    midpoint = np.divide(np.sum([centroid_1, centroid_2], axis=0), 2.0)
    cluster_1_density = _s_dbw_density(
        labels, data, cluster_1, cluster_2, centroid_1)
    cluster_2_density = _s_dbw_density(
        labels, data, cluster_1, cluster_2, centroid_2)
    midpoint_density = _s_dbw_density(
        labels, data, cluster_1, cluster_2, midpoint)
    return midpoint_density / np.max(cluster_1_density, cluster_2_density)


def _silhouette_within_cluster_mean_dist(cluster_points, point):
    """Compute the within cluster mean distance used in silhouette index."""
    n_k = len(cluster_points)
    sum_dist = 0
    for p in cluster_points:
        sum_dist += np.linalg.norm(point - p)
    return 1 / (n_k - 1) * sum_dist


def _silhouette_sigma(cluster_points, point):
    """Compute sigma used in silhouette index."""
    n_k = len(cluster_points)
    sum_dist = 0
    for p in cluster_points:
        sum_dist += np.linalg.norm(point - p)
    return 1 / n_k * sum_dist


def _silhouette_between_cluster_min_dist(labels, data, cluster, point):
    """Compute the between cluster min distance used in silhouette index."""
    clusters = set(labels)
    min_sigma = np.inf
    for c in [x for x in clusters if x != cluster]:
        cluster_points = data[labels == c]
        sigma = _silhouette_sigma(cluster_points, point)
        if sigma < min_sigma:
            min_sigma = sigma
    return min_sigma


def _cluster_silhouette_mean(labels, data, cluster):
    """Compute cluster silhouette mean, used in silhouette index."""
    clust_point = data[labels == cluster]
    sum_point_silhouette = 0
    for p in clust_point:
        mean_dist_within = _silhouette_within_cluster_mean_dist(clust_point, p)
        min_dist_between = _silhouette_between_cluster_min_dist(
            labels,
            data,
            cluster,
            p)
        delta = min_dist_between - mean_dist_within
        point_silhouette = delta / max(min_dist_between, mean_dist_within)
        sum_point_silhouette += point_silhouette
    return 1 / len(clust_point) * sum_point_silhouette


def between_clusters_density(labels, data):
    """Compute between cluster density G for S_Dbw index."""
    clusters = list(set(labels))
    K = len(clusters)
    sum = 0
    for i in range(K):
        for j in range(i):
            cluster_1 = clusters[i]
            cluster_2 = clusters[j]
            sum += _s_dbw_cluster_pair_density(
                labels, data, cluster_1, cluster_2)
    ratio = 2 / (K * (K - 1))
    return ratio * sum


def s_dbw(labels, data):
    """Compute S_Dbw index."""
    scatt = average_scattering(labels, data)
    density = between_clusters_density(labels, data)
    return scatt + density


def c_index(labels, data):
    """C index, take the list of data labels and a distance matrix"""
    """ of the data, data point should have the same index in both """
    """labels list and distance matrix."""
    Nt, Nw, Nb = compute_pairs_count(labels)
    dist_matrix = compute_distance_matrix(data)
    flat_matrix = dist_matrix[np.tril(dist_matrix, -1) != 0]

    id_nw = np.argpartition(flat_matrix, Nw)
    Sum_min = np.sum(flat_matrix[id_nw[:Nw]])
    id_nw = np.argpartition(flat_matrix, -Nw)
    Sum_max = np.sum(flat_matrix[id_nw[-Nw:]])

    Sum_w = 0
    for i in range(len(labels)):
        for j in range(i):
            if labels[i] == labels[j]:
                Sum_w += dist_matrix[i][j]

    return (Sum_w - Sum_min)/(Sum_max - Sum_min)


def wcss(labels, data):
    """Within cluster sum of square."""
    clusters = set(labels)
    wcss = 0
    for c in clusters:
        clust_point = data[labels == c]
        centroid = np.mean(clust_point, axis=0)
        for p in clust_point:
            wcss += np.linalg.norm(centroid-p) ** 2
    return wcss


def bcss(labels, data):
    """Between cluster sum of square."""
    clusters = set(labels)
    data_center = np.mean(data, axis=0)
    bcss = 0
    for c in clusters:
        clust_point = data[labels == c]
        centroid = np.mean(clust_point, axis=0)
        bcss += len(clust_point)*np.linalg.norm(centroid-data_center) ** 2
    return bcss


def calinski_harabasz(labels, data):
    """Calinski-Harabasz index."""
    N = len(data)
    K = len(set(labels))
    return (N-K)/(K-1) * bcss(labels, data)/wcss(labels, data)


def log_ss_ratio(labels, data):
    """Log SS Ratio index."""
    return math.log(bcss(labels, data)/wcss(labels, data))


def sd(labels, data, alpha):
    """SD index."""
    scatt = average_scattering(labels, data)
    dis = total_separation(labels, data)
    return alpha * scatt + dis


def ball_hall(labels, data):
    """"Ball-Hall index."""
    clusters = set(labels)

    total_sum = 0
    for c in clusters:
        clust_point = data[labels == c]
        centroid = np.mean(clust_point, axis=0)
        n_k = len(clust_point)
        internal_sum = 0
        for p in clust_point:
            internal_sum += np.linalg.norm(p-centroid) ** 2
        total_sum += 1/n_k * internal_sum
    return 1/len(clusters) * total_sum


def xie_beni(labels, data):
    """Xie-Beni index."""
    clusters = list(set(labels))
    K = len(clusters)
    clust_dist = []
    for i in range(K):
        for j in range(i):
            cluster_1 = clusters[i]
            cluster_2 = clusters[j]
            clust_data_1 = data[labels == cluster_1]
            clust_data_2 = data[labels == cluster_2]
            clust_dist.append(
                single_linkage_distance(clust_data_1, clust_data_2))
    return 1/len(data) * wcss(labels, data) / (np.min(clust_dist) ** 2)


def ray_turi(labels, data):
    """Ray-Turi index."""
    clusters = set(labels)
    centroids = []

    for c in clusters:
        clust_point = data[labels == c]
        centroids.append(np.mean(clust_point, axis=0))
    centroids_dist = []
    for i in range(len(clusters)):
        for j in range(i):
            centroids_dist.append(
                np.linalg.norm(centroids[i]-centroids[j]) ** 2)
    return 1 / len(data) * wcss(labels, data) / np.min(centroids_dist)


def gamma(labels, data):
    """Baker-Hubert Gamma index."""
    s_p, s_m = concordante_discordante_pair_count(labels, data)
    return (s_p - s_m) / (s_p + s_m)


def tau(labels, data):
    """Tau index."""
    s_p, s_m = concordante_discordante_pair_count(labels, data)
    Nt, Nw, Nb = compute_pairs_count(labels)
    det = np.sqrt(Nb * Nw * (Nt * (Nt - 1) / 2))
    return (s_p - s_m) / det


def silhouette(labels, data):
    """Silhouette index"""
    clusters = set(labels)
    sum_silhouette_mean = 0
    for c in clusters:
        sum_silhouette_mean += _cluster_silhouette_mean(labels, data, c)
    return 1 / len(clusters) * sum_silhouette_mean
