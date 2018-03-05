from flask import Flask, render_template, request


import web3
from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract

sol = None
with open('Voting.sol', 'r') as f:
    sol = f.read().replace('\n', '')

compiled_sol = compile_source(sol)
contract_interface = compiled_sol['<stdin>:Voting']
w3 = Web3(HTTPProvider('http://localhost:8545'))
contract = w3.eth.contract(
    abi=contract_interface['abi'],
    bytecode=contract_interface['bin']
)


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')




@app.route("/results/<contract_addr>")
def results(contract_addr):
    instance = w3.eth.contract(
        contract_interface['abi'],
        contract_addr,
        ContractFactoryClass=ConciseContract
    )
    choices = instance.getAllCandidates()

    results = {}
    for c in choices:
        results[c] = instance.totalVotesFor(c)

    return render_template('results.html', results=results, contract_addr=contract_addr)






@app.route("/vote", methods=['POST'])
def vote():
    choice = request.form['choice'].strip()
    contract_addr = request.form['contract_addr'].strip()

    instance = w3.eth.contract(
        contract_interface['abi'],
        contract_addr,
        ContractFactoryClass=ConciseContract
    )
    instance.voteForCandidate(choice, transact={
        'from': w3.eth.accounts[0]
    })

    return render_template('vote.html', choice=choice, contract_addr=contract_addr)





@app.route("/create", methods=['POST'])
def create():

    choices = request.form['choices'].replace(', ', ',').split(',')

    transaction_hash = contract.deploy(
        transaction={
            'from': w3.eth.accounts[0],
            'gas': 410000
        },
        args=[
            choices
        ]
    )
    transaction_receipt = w3.eth.getTransactionReceipt(transaction_hash)
    contract_address = transaction_receipt['contractAddress']

    return render_template('create.html', choices=choices, contract_addr=contract_address)





if __name__ == '__main__':
    app.run(debug=True)