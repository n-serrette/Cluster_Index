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
![Precision](http://www.sciweavers.org/tex2img.php?eq=P%28C%2CC%27%29%20%3D%20%5Cfrac%7Byy%7D%7Byy%2Bny%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)
#### Recall
![Recall](http://www.sciweavers.org/tex2img.php?eq=R%28C%2CC%27%29%20%3D%20%5Cfrac%7Byy%7D%7Byy%2Byn%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)
#### Rand Index [[3]](#references)
![RI](http://www.sciweavers.org/tex2img.php?eq=RI%28C%2C%20C%27%29%3D%5Cfrac%7B%28yy%20%2B%20nn%29%7D%7Byy%2Bnn%2Byn%2Bny%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)
#### Adjusted Rand Index
![ARI](http://www.sciweavers.org/tex2img.php?eq=ARI%28C%2CC%27%29%20%3D%20%5Cfrac%7Byy%5Ctimes%20nn%20-%20yn%20%5Ctimes%20ny%7D%7B%28yy%2Bny%29%5Ctimes%20%28ny%2Bnn%29%2B%28yy%20%2B%20yn%29%5Ctimes%20%28yn%20%2B%20nn%29%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)
#### Folkes-Mallows Index [[4]](#references)
![FolkesMallows](http://www.sciweavers.org/tex2img.php?eq=FolkesMallows%28C%2CC%27%29%20%3D%20%5Cfrac%7Byy%7D%7B%28yy%2Byn%29%5Ctimes%20%28yy%2Bny%29%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)
#### Jaccard Index
![Jaccard](http://www.sciweavers.org/tex2img.php?eq=Jaccard%28C%2CC%27%29%20%3D%20%5Cfrac%7Byy%7D%7Byy%2Byn%2Bny%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)
#### Kulczynski Index
![Kulczynski](http://www.sciweavers.org/tex2img.php?eq=Kulczynski%28C%2CC%27%29%20%3D%20%5Cfrac%7B1%7D%7B2%7D%28%5Cfrac%7Byy%7D%7Byy%2Bny%7D%2B%5Cfrac%7Byy%7D%7Byy%2Byn%7D%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)
#### McNemar Index
![McNemar](http://www.sciweavers.org/tex2img.php?eq=McNemar%28C%2CC%27%29%20%3D%20%5Cfrac%7Bnn-ny%7D%7B%20%5Csqrt%7Bnn%2Bny%7D%20%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)
#### Phi Index

#### Rogers and Tanimoto Index

#### Russel and Rao Index

#### Solkal and Sneath Index (version 1 and 2)

#### Hubert Index

#### Mirkin Metric




### Measures based on set overlaps

#### F-measure
Also call Czebanowski-Dice index or Ochiai index



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

