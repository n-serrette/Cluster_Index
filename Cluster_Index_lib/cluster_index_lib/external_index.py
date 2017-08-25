#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""External cluster index seen in literature."""
from __future__ import division
import math

__all__ = (
    'ari',
    'ri',
    'precision',
    'recall',
    'f_measure',
    'folkes_mallows',
    'jaccard',
    'kulczynski',
    'mc_nemar',
    'phi',
    'rogers_tanimoto',
    'russel_rao',
    'solkal_sneath',
    'solkal_sneath_2',
    'hubert',
    'mirkin',
    'purity',
    'entropy',
    'mi',
    'sg_nmi',
    'fj_nmi',
    'variation_information')


def compute_pairs_count(labels, res):
    """Compute confusion matrix.

    yy the two points belong to the same cluster, according to both P1 and P2
    nn the two points belong to the same cluster according to P1 but not to P2
    yn the two points belong to the same cluster acording to P2 but not to P1
    ny the two points do not belong to the same cluster, according to both P1
       and P2
    """
    yy = 0
    nn = 0
    yn = 0
    ny = 0
    for i in range(len(labels)):
        for j in range(i+1, len(labels)):
            if labels[i] == labels[j] and res[i] == res[j]:
                yy += 1
            if labels[i] != labels[j] and res[i] != res[j]:
                nn += 1
            if labels[i] == labels[j] and res[i] != res[j]:
                yn += 1
            if labels[i] != labels[j] and res[i] == res[j]:
                ny += 1
    return (yy, nn, yn, ny)


def compute_confusion_matrix(labels, res):
    """Compute confusion matrix M with m_i,j=|C_i inter C'_j|."""
    k = set(labels)
    h = set(res)
    n = len(labels)
    if n != len(res):
        raise ValueError("The two partitions have different size.")
    M = []
    for i in k:
        m_i = []
        C_i = set([index for index, value in enumerate(labels) if value == i])
        for j in h:
            C_j = set([index for index, value in enumerate(res) if value == j])
            m_i.append(len(C_i.intersection(C_j)))
        M.append(m_i)
    return M


def cluster_entropy(labels):
    """Compute the entropy of a clustering."""
    n = len(labels)
    sum = 0
    for i in set(labels):
        C_i = [x for x in labels if x == i]
        p_i = len(C_i)/n
        sum += p_i*math.log(p_i, 2)
    return -1*sum


def ari(labels, res):
    """Compute Hubert and Arabi's Adjusted Rand Index."""
    yy, nn, yn, ny = compute_pairs_count(labels, res)
    return 2*(yy*nn-yn*ny)/((yy+ny)*(ny+nn)+(yy + yn)*(yn + nn))


def ri(labels, res):
    """Compute Rand Index."""
    yy, nn, yn, ny = compute_pairs_count(labels, res)
    return (yy+nn)/(yy+nn+yn+ny)


def precision(labels, res):
    """Precision coefficient, portion of points rightly grouped together."""
    yy, nn, yn, ny = compute_pairs_count(labels, res)
    return yy/(yy+ny)


def recall(labels, res):
    """Recall coefficient.

    this is  the proportion of points which are supposed to be grouped together
    according to the reference partition P1 and which are effectively marked
    as such by partition P2.
    """
    yy, nn, yn, ny = compute_pairs_count(labels, res)
    return yy/(yy+yn)


def f_measure(labels, res):
    """F measeure or Czekanowski-Dice index aka Ochiai index."""
    yy, nn, yn, ny = compute_pairs_count(labels, res)
    return (2*yy)/(2*yy+yn+ny)


def folkes_mallows(labels, res):  # noqa:D401
    """Folkes-Mallows index.

    The geometric mean of the Recall and the Precision.
    """
    yy, nn, yn, ny = compute_pairs_count(labels, res)
    return yy/math.sqrt((yy+yn)*(yy+ny))


def jaccard(labels, res):
    """Jaccard index."""
    yy, nn, yn, ny = compute_pairs_count(labels, res)
    return yy/(yy+yn+ny)


def kulczynski(labels, res):
    """Kulczynski index.

    This is the arithmetic mean of the precision and recall coefficients.
    """
    yy, nn, yn, ny = compute_pairs_count(labels, res)
    return 1/2*(yy/(yy+ny)+yy/(yy+yn))


def mc_nemar(labels, res):
    """Mc Nemar index."""
    yy, nn, yn, ny = compute_pairs_count(labels, res)
    return (nn-ny)/math.sqrt(nn+ny)


def phi(labels, res):
    """Phi index."""
    yy, nn, yn, ny = compute_pairs_count(labels, res)
    return (yy*nn-yn*ny)/((yy+yn)*(yy+ny)*(yn+nn)*(ny+nn))


def rogers_tanimoto(labels, res):
    """Rogers-Tanimoto index."""
    yy, nn, yn, ny = compute_pairs_count(labels, res)
    return (yy+nn)/(yy+nn+2*(yn + ny))


def russel_rao(labels, res):
    """Russel-Rao index."""
    yy, nn, yn, ny = compute_pairs_count(labels, res)
    return yy/(yy+nn+yn+ny)


def solkal_sneath(labels, res):
    """Solkal_Sneath index, first version."""
    yy, nn, yn, ny = compute_pairs_count(labels, res)
    return yy/(yy+2*(yn+ny))


def solkal_sneath_2(labels, res):
    """Solkal_Sneath index, second version."""
    yy, nn, yn, ny = compute_pairs_count(labels, res)
    return (yy + nn)/(yy + nn + (yn + ny)/2)


def hubert(labels, res):
    """Hubert index."""
    yy, nn, yn, ny = compute_pairs_count(labels, res)
    Nt = yy + nn + yn + ny
    return (Nt*yy-((yy+yn)*(yy+ny)))/math.sqrt((yy+yn)*(yy+ny)*(nn+yn)*(nn+ny))


def mirkin(labels, res):
    """Mirkin metric or Equivalence Mismatch Distance."""
    yy, nn, yn, ny = compute_pairs_count(labels, res)
    return 2 * (ny + yn)


def van_dongen_measure(labels, res):
    """Compute Van Dongen Measure."""
    m = compute_confusion_matrix(labels, res)
    n = len(labels)
    k = len(set(labels))
    h = len(set(res))
    sum_k = 0
    sum_l = 0
    for i in m:
        sum_k += max(i)
    for j in range(h):
        max_i = 0
        for i in range(k):
            if m[i][j] > max_i:
                max_i = m[i][j]
        sum_l += max_i
    print(2*n-sum_k-sum_l)


def purity(labels, res):
    """Purity of a clustering."""
    confusion_matrix = compute_confusion_matrix(labels, res)
    n = len(labels)
    sum = 0
    for c in confusion_matrix:
        sum += max(c)
    return sum / n


def entropy(labels, res):
    """Entropy of two clustering."""
    confusion_matrix = compute_confusion_matrix(labels, res)
    n = len(labels)
    sum_E = 0
    for c in confusion_matrix:
        n_j = sum(c)
        sum_j = 0
        for j in c:
            p_ij = j / sum(c)
            if p_ij != 0:
                sum_j += p_ij * math.log(p_ij, 2)
        sum_E -= n_j/n * sum_j
    return sum_E


def mi(labels, res):
    """Compute mutual information."""
    k = set(labels)
    h = set(labels)
    n = len(labels)
    if n != len(res):
        raise ValueError("The two partitions have different size.")
    sum_k = 0
    for i in k:
        C_i = set([index for index, value in enumerate(labels) if value == i])
        p_i = len(C_i)/n
        sum_h = 0
        for j in h:
            C_j = set([index for index, value in enumerate(res) if value == j])
            p_j = len(C_j)/n
            p_ij = len(C_i.intersection(C_j))/n
            if p_ij != 0:
                sum_h += p_ij * math.log((p_ij/(p_i*p_j)), 2)
        sum_k += sum_h
    return sum_k


def sg_nmi(labels, res):
    """Strehl and Glosh Normalized Mutual Information."""
    mutualI = mi(labels, res)
    return mutualI / math.sqrt(cluster_entropy(labels) * cluster_entropy(res))


def fj_nmi(labels, res):
    """Fred and Jain Normalized Mutual Information."""
    mutualI = mi(labels, res)
    return 2 * mutualI / (cluster_entropy(labels) + cluster_entropy(res))


def variation_information(labels, res):
    """Meila Variation of Information."""
    return cluster_entropy(labels) + cluster_entropy(res) - 2 * mi(labels, res)
