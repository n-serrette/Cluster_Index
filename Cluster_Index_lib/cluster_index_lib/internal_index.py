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
    'log_ss_ratio'
    )


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
        for j in range(i+1, len(labels)):
            Nt += 1
            if labels[i] == labels[j]:
                Nw += 1
            else:
                Nb += 1
    return (Nt, Nw, Nb)


def c_index(labels, dist_matrix):
    """C index, take the list of data labels and a distance matrix"""
    """ of the data, data point should have the same index in both """
    """labels list and distance matrix."""
    Nt, Nw, Nb = compute_pairs_count(labels)
    flat_matrix = dist_matrix[np.tril(dist_matrix, -1) != 0]

    Sum_min = np.sum(flat_matrix[:np.argpartition(flat_matrix, Nw)])
    Sum_max = np.sum(flat_matrix[np.argpartition(flat_matrix, -Nw):])

    Sum_w = 0
    for i in range(len(labels)):
        for j in range(i+1, len(labels)):
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
            wcss += np.linalg.norm(centroid-p, 2, 0)
    return wcss


def bcss(labels, data):
    """Between cluster sum of square."""
    clusters = set(labels)
    data_center = np.mean(data, axis=0)
    bcss = 0
    for c in clusters:
        clust_point = data[labels == c]
        centroid = np.mean(clust_point, axis=0)
        bcss += len(data)*np.linalg.norm(centroid-data_center, 2, 0)
    return bcss


def calinski_harabasz(labels, data):
    """Calinski-Harabasz index."""
    N = len(data)
    K = len(set(labels))
    return (N-K)/(K-1) * bcss(labels, data)/wcss(labels, data)


def log_ss_ratio(labels, data):
    """Log SS Ratio index."""
    return math.log(bcss(labels, data)/wcss(labels, data))
