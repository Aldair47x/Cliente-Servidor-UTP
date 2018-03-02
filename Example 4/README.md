<h1>Matrix times performance</h1>

<p>Here we going to compare the time between the times of a matrix by itself with threads and without it.</p>

## Installing and Running

1. Make sure that you have `Anaconda`, `pyzmq` and `pyaudio` installed on your computer.
2. Fork and clone this repo on your computer.
3. `cd` into the root directory and run `python server.py (yourPORT)`.
4. Run `python client.py (ServerIP) (ServerPORT)`.

<h2>Times</h2>

<h3>Matrix without threads</h3>

  <ul>10x10 : 0.0009765625</ul>
  <ul>50x50 : 0.09705638885498047</ul>
  <ul>100x100 : 0.7100338935852051</ul>
  <ul>500x500 : 88.25754237174988</ul>
  <ul>1000x1000 : 699.0429532527924</ul>
 
 <h3>Matrix with threads</h3>
 
  <ul>10x10 : 0.015333890914916992</ul>
  <ul>50x50 : 0.5847659111022949</ul>
  <ul>100x100 : 3.0362913608551025</ul>
  <ul>500x500 : 253.14607620239258</ul>
  <ul>1000x1000 : 1555.7971708774567</ul>
  
  
