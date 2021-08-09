# Chess-bot


I would suggest doing this process on a system that has a public IP address so that you can use the SSH functionality in Integromat without needing to use a tunneler like Ngrok.

First step is to git clone this project and then cd in it's directory

then:
```
pip install argparse
```
```
pip install stockfish
```
in your terminal on a linux machine write
```
wget https://stockfishchess.org/files/stockfish-10-linux.zip
```
```
unzip stockfish-10-linux.zip
```
```
chmod +x stockfish-10-linux/Linux/stockfish_10_x64
```
this will download and unzip stockfish to this directory and will change the privileges


Then move all these files out of this folder and into the home directory


