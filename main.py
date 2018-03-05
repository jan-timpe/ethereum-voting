import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract



if __name__ == '__main__':

    # compile the contract source
    sol = None
    with open('Voting.sol', 'r') as f:
        sol = f.read().replace('\n', '')

    compiled_sol = compile_source(sol)
    contract_interface = compiled_sol['<stdin>:Voting']


    # instantiate and deploy a contract
    w3 = Web3(HTTPProvider('http://localhost:8545'))
    contract = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']
    )

    # getting transaction hash from deployed contract
    transaction_hash = contract.deploy(transaction={
        'from': w3.eth.accounts[0],
        'gas': 410000
    }, args=[['Bernie', 'Hillbot', 'Cheeto']])

    transaction_receipt = w3.eth.getTransactionReceipt(transaction_hash)
    contract_address = transaction_receipt['contractAddress']
    contract_instance = w3.eth.contract(
        contract_interface['abi'],
        contract_address,
        ContractFactoryClass=ConciseContract
    )

    print('Contract value: {}'.format(contract_instance.totalVotesFor('Bernie')))
    contract_instance.voteForCandidate('Bernie', transact={'from': w3.eth.accounts[0]})
    print('Setting value...')
    print('Contract value: {}'.format(contract_instance.totalVotesFor('Bernie')))