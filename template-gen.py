import json
import math
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('number', metavar='N', type=int, help='number of nodes')

def gen_wallet(idx, stake):
    name = "Wallet_{}".format(idx+1)
    wallet = {    
        "Name": name,
        "Stake": stake,
        "Online": True
    }
    return wallet

def gen_node(idx):
    if idx == 0:
        node = {
            "Name": "Primary",
            "IsRelay": True,
            "Wallets": [
                { "Name": "Wallet_1",
                  "ParticipationOnly": False }
            ]
        }
    else:
        node = {
            "Name": "Node_{}".format(idx),
            "Wallets": [
                { "Name": "Wallet_{}".format(idx+1),
                  "ParticipationOnly": False 
                  }
            ]
        }
    return node

if __name__ == "__main__":
    args = parser.parse_args()
    node_count = args.number
    node_stake = math.floor(100/node_count)
    primary_stake = 100 - (node_count -1)*node_stake
    stakes = [primary_stake if i==0 else node_stake for i in range(node_count)]
    template = {
        "Genesis": {
            "NetworkName": "lbvrf",
            "ConsensusProtocol": "future",
            "Wallets": [gen_wallet(i, stakes[i]) for i in range(node_count)]
        },
        "Nodes": [gen_node(i) for i in range(node_count)]
    }
    print(json.dumps(template, indent=4, sort_keys=True))
