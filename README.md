# Cluster_Index
[![Build Status](https://travis-ci.org/n-serrette/Cluster_Index.svg?branch=master)](https://travis-ci.org/n-serrette/Cluster_Index) [![Coverage Status](https://coveralls.io/repos/github/n-serrette/Cluster_Index/badge.svg?branch=master)](https://coveralls.io/github/n-serrette/Cluster_Index?branch=master)

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
![precision](images/precision.png)
#### Recall
![recall](images/recall.png)
#### Rand Index [[3]](#references)
![ri](images/RI.png)
#### Adjusted Rand Index
![ari](images/ARI.png)
#### Folkes-Mallows Index [[4]](#references)
![folkesMallows](images/FolkesMallows.png)
#### Jaccard Index
![jaccard](images/jaccard.png)
#### Kulczynski Index
![kulczynski](images/Kulczynski.png)
#### McNemar Index
![McNemar](images/McNemar.png)
#### Phi Index
![phi](images/phi.png)
#### Rogers and Tanimoto Index
![rogerstanimoto](images/RT.png)
#### Russel and Rao Index
![russelRao](images/RR.png)
#### Solkal and Sneath Index (version 1 and 2)

#### Hubert Index

#### Mirkin Metric




### Measures based on set overlaps

#### F-measure
Also call Czebanowski-Dice index or Ochiai index

![fmeasure](images/Fmeasure.png)


### Measures based on Mutual Information

#### Mutual Information

#### Strehl and Ghosh Normalized Mutual Information

#### Fred and Jain Normalized Mutual Information

#### Variation of Infomation

### Other

#### Purity

#### Entropy



## References

1. Silke Wagner and Dorothea Wagner, Comparing Clustering - An Overview, 2007
3. Bernard Desgraupes, Clustering Indices, 2016, [https://CRAN.R-project.org/package=clusterCrit]
4. Rand, William M.: Objective Criteria for the Evaluation of Clustering Methods. Journal of the American Statistical Association, 66(336):846-850, 1971.
5. Fowlkes, E. B., Mallows, C. L.: A Method for Comparing Two Hierarchical Clusterings. Journal of the American Statistical Association, 78(383):553–569, 1983.


## TODO

* add internal cluster indexes
* complete References section
* add definition and formula for each indexes
