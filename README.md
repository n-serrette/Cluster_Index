# Cluster_Index
Several clustering indexes implementation

## External Indices

This indexes are designed to measure the similarity of two partitions.

## Indexes based on pair counting
All this indices are based on counting pair depending on wether they belong to the same cluster or not according to the partition C or C'. There are four possibilities:
  * yy : the two points belong to the same cluster according to both C and C'
  * yn : the two points belong to the same cluster according to C but not to C'
  * ny : the two points belong to the same cluster according to C' but not to C
  * nn : the two points does not belong to the same cluster according to C and C'

### Precision



### Recall

<img src="http://www.sciweavers.org/tex2img.php?eq=R%20%3D%20%5Cfrac%7Byy%7D%7Byy%2Byn%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="R = \frac{yy}{yy+yn}" width="101" height="43" />

### F-measure
Also call Czebanowski-Dice index or Ochiai index



### Rand Index



### Adjusted Rand Index



### Folkes-Mallows Index

<img src="http://www.sciweavers.org/tex2img.php?eq=Folkes%20%3D%20%5Cfrac%7Byy%7D%7B%5Csqrt%7B%28yy%2Byn%29%28yy%2Bny%29%7D%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="Folkes = \frac{yy}{\sqrt{(yy+yn)(yy+ny)}} " width="251" height="49" />

### Jaccard Index

<img src="http://www.sciweavers.org/tex2img.php?eq=J%20%3D%20%5Cfrac%7Byy%7D%7Byy%2Byn%2Bny%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="J = \frac{yy}{yy+yn+ny} " width="136" height="43" />
