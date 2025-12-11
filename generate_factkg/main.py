from dataloader import *
from generator import *

def main():
    one_hop_data, conjuction_data = load_and_filter_webnlg()

    dataset = []
    one_hop_claims = generate_one_hop(one_hop_data)
    conjunction_claims = generate_conjuction(conjuction_data)
    dataset.extend(one_hop_claims)
    dataset.extend(conjunction_claims)

    print('===Printing data in main====')
    for claim in one_hop_claims[:5]:
        print(claim)
    for claim in conjunction_claims[:5]:
        print(claim)

if __name__ == '__main__':
    main()
