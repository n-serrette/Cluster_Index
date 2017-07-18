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

### F-measure
Also call Czebanowski-Dice index or Ochiai index

### Rand Index

### Adjusted Rand Index

### Folkes-Mallows Index

### Jaccard Index
