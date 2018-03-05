# Ethereum blockchain straw poll app

Resources
* [Full Stack Hello World Voting Ethereum Dapp Tutorial — Part 1](https://medium.com/@mvmurthy/full-stack-hello-world-voting-ethereum-dapp-tutorial-part-1-40d2d0d807c2)
* [Installing the Solidity Compiler](https://solidity.readthedocs.io/en/develop/installing-solidity.html#binary-packages)
* [Web3 Python docs](https://web3py.readthedocs.io/en/stable/web3.eth.html)


Setup

Install ganache-cli
```bash
npm install ganache-cli
node_modules/.bin/ganache-cli
```


In a new terminal window or tab (these ones take forever) install solidity binary
```bash
brew update
brew upgrade
brew tap ethereum/ethereum
brew install solidity
brew linkapps solidity
```


Create a virtualenv 
```bash
virtualenv env -p python3
source ./env/bin/activate
pip install -r requirements.txt
```


Run the app
```bash
python app.py
```