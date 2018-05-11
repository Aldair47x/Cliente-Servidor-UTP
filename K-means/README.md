<h3>Example that contains data point name (Netlix movies's name): </h3>



558634 [(4, 1), (3, 28), (4, 48), (4, 57), (4, 58), (4, 73), (5, 76), (4, 138), (4, 143), (4, 152), (5, 165), (4, 166), (5, 171), (4, 175), (3, 187), (4, 191), (4, 209), (5, 215), (4, 223), (4, 252), (4, 257), (4, 269), (5, 270), (4, 283), (3, 285), (4, 299), (4, 311), (5, 312), (4, 313), (4, 329), (3, 330), (3, 331), (4, 357), (5, 359), (2, 362), (4, 414), (4, 417), (4, 433), (4, 442), (4, 448), (4, 457), (4, 459), (5, 466), (4, 468), (5, 482), (5, 518), (4, 524), (2, 528), (3, 533), (3, 550), (4, 571), (3, 596), (4, 599), (3, 607), (3, 629), (4, 636), (4, 641), (4, 642), (4, 658), (4, 668), (4, 689), (3, 692), (5, 694), (3, 705), (3, 711), (4, 720), (3, 723), (5, 752), (4, 758), (5, 760), (3, 788), (4, 798), (2, 811), (5, 825), (3, 831), (5, 837), (5, 851), (4, 862), (4, 886), (4, 896), (4, 907), (3, 909), (3, 937), (4, 940), (3, 963), (3, 985), (3, 994)]<br />
2165002 [(4, 1), (3, 28), (4, 46)]<br />
427928 [(4, 1), (3, 23), (2, 28), (2, 35), (3, 84), (2, 252), (3, 255), (4, 257), (3, 262), (3, 264), (4, 265), (4, 299), (2, 334), (3, 425), (5, 455), (5, 482), (3, 486), (3, 563), (4, 571), (4, 609), (3, 651), (3, 675), (4, 694), (2, 788), (3, 912), (2, 940), (4, 980)]<br />
(...)<br />

"558634" is an anonymous user encrypted <br />
"(4,1)" '4' is the integral rating of the  (1 to 5) and '1' is the number of the movie <br />



<h2>Quick analysis of the data </h2>

<h3>Sequential</h3>

After compiling the `Kmeans sequential` with the `combined_1.txt` we obtain that putting manual K clusters for the clustering of the data is obtained: <br />

<h3>K = 5 && 100 iterations</h3>

Square error mean: 2333097<br />

Cluster 1 <br />
Numbers of points in the cluster: 6079 <br />
Cluster values: 1191793 3 6 <br />

Cluster 2 <br />
Numbers of points in the cluster: 4124 <br />
Cluster values: 1168937 3 6 <br />

Cluster 3 <br />
Numbers of points in the cluster: 3841
Cluster values: 1708601 3 7 <br />

Cluster 4 <br />
Numbers of points in the cluster: 723 <br />
Cluster values: 1099236 2 4 <br />

Cluster 5 <br />
Numbers of points in the cluster: 233 <br />
Cluster values: 1748914 2 4 <br />

<h3>Parallel</h3>

Compiling the `Kmeans parallel` with the `combined_1.txt` we obtain that putting manual K clusters for the clustering of the data is obtained: 
<br />

<h3>K = 5 && 100 iterations</h3>

Square error mean: 2337811 <br />

Cluster 1 <br />
Numbers of points in the cluster: 5838 <br />
Cluster values: 587162 3 6 <br />

Cluster 2 <br />
Numbers of points in the cluster: 2667 <br />
Cluster values: 1750646 3 5 <br />

Cluster 3 <br />
Numbers of points in the cluster: 2910 <br />
Cluster values: 1448558 3 6 <br />

Cluster 4 <br />
Numbers of points in the cluster: 1346 <br />
Cluster values: 1981024 2 5 <br />

Cluster 5 <br />
Numbers of points in the cluster: 2239 <br />
Cluster values: 2167038 3 7 <br />

Parallel Kmeans 538 s <br />



<h4>#####</h4>


The euclidean distance was used for to calculate the distance of each data point for the centroid of cluster.

The algorithm stops by maximum number of iterations or if no data point exchange cluster.

</p>

## Installing and Running

1. Make sure that you have `g++` installed on your computer.
2. Fork and clone this repo on your computer.
3. `cd` into the root directory and run `g++ -std=c++11 -o skmeans sKmeans.cc`.



This algotihm is based on the next repository and all rights are reserved to him
https://github.com/marcoscastro/kmeans




