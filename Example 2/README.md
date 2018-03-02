## Installing and Running

1. Make sure that you have `Anaconda`, `pyzmq` and `pyaudio` installed on your computer.
2. Fork and clone this repo on your computer.
3. `cd` into the root directory and run `python server.py (yourPORT)`.
4. Run `python client.py (ServerIP) (ServerPORT)` (This client has no threads, so the information arrives late).
4. Run `python hclient.py (ServerIP) (ServerPORT)`(This cliente has threads).

<h2>Brief of the practice</h2>

<p>In client.py we can note that the efficiency is not the best for the implementation of two people, but when is adding threads to enhance the efficiency is considering better than without it</p>
