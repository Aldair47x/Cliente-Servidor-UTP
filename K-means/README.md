<h1>K-Means Clustering Algorithm</h1>

<p>Implementation in C++ of the K-Means clustering algorithm.

Examples of datasets are in datasets folder.

References are in references folder.

This link was very useful for me: http://mnemstudio.org/clustering-k-means-example-1.htm

The implementation is in the file kmeans.cpp.

Each dataset is in format expected by the program.

Explanation of the format:

First line: A B C D E

"A" is the amount of data points.<br />
"B" is the amount of attributes.<br />
"C" is the amount of clusters.<br />
"D" is the maximum iterations.<br />
"E" indicates if contains a name for each data point. The value for "E" is 0 (not contains) or 1 (contains).<br />
The next "A" lines contains "B" attributes and the data point name (if "E" variable is 1).<br />

<h3>Example that contains data point name (Netlix movies's name): </h3>


105 2 7 100 1 <br />
1488844 3 Movie1 <br />
822109 5 Movie1 <br />
885013 4 Movie1 <br />
30878 4 Movie1 <br />
823519 3 Movie1 <br />
893988 3 Movie1 <br />
124105 4 Movie1 <br />
(...)<br />

"1488844" is an anonymous user encrypted <br />
"3" The integral rating of the movie (1 to 5) <br />
"Movie1" The number of the movie <br />


<h2>Quick analisis of the data </h2>

After compiling the algoritm with the `NetflixDataSet.txt` we obtain that putting manual K clusters for the classification of the data is obtained: <br />

<h3>K = 7</h3>
<p>Cluster 1 values: 2.49372e+06 - 2.92857 </p>
<p>Cluster 2 values: 602683 - 3.0625 </p>
<p>Cluster 3 values: 149175 - 3.25 </p>
<p>Cluster 4 values: 1.40995e+06 - 2.8 </p>
<p>Cluster 5 values: 1.76299e+06 - 3.53333 </p>
<p>Cluster 6 values: 2.07667e+06 - 3.78571 </p>
<p>Cluster 7 values: 955751 - 3.36842 </p>


<h3>Example of dataset: </h3>

7 2 2 100 0<br />
1.0 1.0<br />
1.5 2.0<br />
3.0 4.0<br />
5.0 7.0<br />
3.5 5.0<br />
4.5 5.0<br />
3.5 4.5<br />

7 is the amount of data points.<br />
2 is the amount of attributes.<br />
2 is the amount of clusters.<br />
100 is the maximum iterations.<br />
0 indicates that not contains data point name.<br />
The next 7 lines contains 2 attributes each.<br />



The euclidean distance was used for to calculate the distance of each data point for the centroid of cluster.

The algorithm stops by maximum number of iterations or if no data point exchange cluster.
</p>

## Installing and Running

1. Make sure that you have `g++` installed on your computer.
2. Fork and clone this repo on your computer.
3. `cd` into the root directory and run `g++ sKmeans.cc -o kmeans `.



This algotihm is based on the next repository and all rights are reserved to him
https://github.com/marcoscastro/kmeans



