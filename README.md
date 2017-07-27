# Cluster_Index
Several clustering indexes implementation

## External Indices

This indexes are designed to measure the similarity of two partitions.

### Indexes based on pair counting
All this indices are based on counting pair depending on wether they belong to the same cluster or not according to the partition C or C'. There are four possibilities:
  * yy : the two points belong to the same cluster according to both C and C'
  * yn : the two points belong to the same cluster according to C but not to C'
  * ny : the two points belong to the same cluster according to C' but not to C
  * nn : the two points does not belong to the same cluster according to C and C'

#### Precision

#### Recall

#### F-measure
Also call Czebanowski-Dice index or Ochiai index

#### Rand Index [[2]](##references)

#### Adjusted Rand Index

#### Folkes-Mallows Index

#### Jaccard Index

#### Kulczynski Index

#### McNemar Index

#### Phi Index

#### Rogers and Tanimoto Index

#### Russel and Rao Index

#### Solkal and Sneath Index (version 1 and 2)

#### Hubert Index

#### Mirkin Metric

#### Purity

#### Entropy

#### Mutual Information

#### Strehl and Ghosh Normalized Mutual Information

#### Fred and Jain Normalized Mutual Information

#### Variation of Infomation

## References

1. Silke Wagner and Dorothea Wagner, Comparing Clustering - An Overview, 2007
2.  Rand, William M.: Objective Criteria for the Evaluation of Clustering Methods. Journal of the American Statistical Association, 66(336):846-850, 1971.
