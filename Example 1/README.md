## Installing and Running

1. Make sure that you have `Anaconda` and `pyzmq` installed on your computer.
2. Fork and clone this repo on your computer.
3. `cd` into the root directory and run ` python server.py (yourPORT) (your directory path)`.
4. Run `python client.py (yourIP) (yourPORT) (your operation)`.


<h2>Time testing </h2>

<p>To test the speed we used the time library for Python 3.6 and we got the following outputs in differents size transfers: </p>

<h3>The size of the test file to transfer is 6,6 mb </h3>
	<ul>1 mb =  0.04123806953430176 seconds! </ul>
	<ul>2 mb = 0.04090428352355957 seconds! </ul>
	<ul>4 mb = 0.039481401443481445 seconds! </ul>
	<ul>8 mb = 0.039623260498046875 seconds! </ul>
	<ul>16 mb = 0.039234161376953125 seconds! </ul>
	<ul>32 mb = 0.03752446174621582 seconds! </ul>
	<ul>64 mb = 0.04180192947387695 seconds! </ul>
