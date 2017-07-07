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

  <img src="http://www.sciweavers.org/tex2img.php?eq=P%20%3D%20%5Cfrac%7Byy%7D%7Byy%2Bny%7D%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="P = \frac{yy}{yy+ny}" width="100" height="43" />

### Recall

<img src="http://www.sciweavers.org/tex2img.php?eq=R%20%3D%20%5Cfrac%7Byy%7D%7Byy%2Byn%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="R = \frac{yy}{yy+yn}" width="101" height="43" />

### F-measure
Also call Czebanowski-Dice index or Ochiai index

  <img src="http://www.sciweavers.org/tex2img.php?eq=F%20%3D%20%5Cfrac%7B2yy%7D%7B2yy%2Byn%2Bny%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="F = \frac{2yy}{2yy+yn+ny}" width="153" height="46" />

### Rand Index

<img src="http://www.sciweavers.org/tex2img.php?eq=RI%20%3D%20%5Cfrac%7Byy%2Bnn%7D%7Byy%2Byn%2Bny%2Bnn%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="RI = \frac{yy+nn}{yy+yn+ny+nn}" width="192" height="44" />

### Adjusted Rand Index

<img src="http://www.sciweavers.org/tex2img.php?eq=F%20%3D%20%5Cfrac%7B2%28yy%20%5Ctimes%20nn%20-%20yn%20%5Ctimes%20ny%29%7D%7B%28yy%2Bny%29%5Ctimes%28ny%2Bnn%29%2B%28yy%2Byn%29%20%5Ctimes%20%28yn%2Bnn%29%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="F = \frac{2(yy \times nn - yn \times ny)}{(yy+ny)\times(ny+nn)+(yy+yn) \times (yn+nn)}" width="404" height="47" />

### Folkes-Mallows Index

<img src="http://www.sciweavers.org/tex2img.php?eq=Folkes%20%3D%20%5Cfrac%7Byy%7D%7B%5Csqrt%7B%28yy%2Byn%29%28yy%2Bny%29%7D%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="Folkes = \frac{yy}{\sqrt{(yy+yn)(yy+ny)}} " width="251" height="49" />

### Jaccard Index

<img src="http://www.sciweavers.org/tex2img.php?eq=J%20%3D%20%5Cfrac%7Byy%7D%7Byy%2Byn%2Bny%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="J = \frac{yy}{yy+yn+ny} " width="136" height="43" />
