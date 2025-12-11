from datasets import load_dataset
import pandas as pd

def load_and_filter_webnlg():
    print("Loading WebNLG 2020...")
    # Load the release v3.0 (corresponds to 2020 challenge)
    dataset = load_dataset("GEM/web_nlg", "en", split='train')

    one_hop_data = []
    conjunction_data = []

    for entry in dataset:
        triples = entry['input']
        text = entry['target']

        # One hop data includes entries with one triple.
        if len(triples) == 1:
            one_hop_data.append({
                'text': text,
                'triples': triples,
                'type': 'one_hop'
            })
        # Conjuction data includes entries with multiple triples.
        elif len(triples) > 1:
            conjunction_data.append({
                'text': text,
                'triples': triples,
                'type': 'conjunction'
            })

    '''
    for entry in dataset:
        # WebNLG entries have a list of triples and list of lexicalizations (sentences)
        triples = entry['modified_triple_sets']['mtriple_set'][0]
        lexicalizations = entry['lex']['text']
        
        # We only care about the first valid sentence for generation
        if not lexicalizations:
            continue
            
        text = lexicalizations[0]
        
        # Sw subset: Single Triple
        if len(triples) == 1:
            one_hop_data.append({
                "text": text,
                "triples": triples,
                "type": "one_hop"
            })
        # Multi Triple (for Conjunctions)
        elif len(triples) > 1:
            conjunction_data.append({
                "text": text,
                "triples": triples,
                "type": "conjunction"
            })
    '''

    print(f"Loaded {len(one_hop_data)} One-hop samples.")
    print(f"Loaded {len(conjunction_data)} Conjunction samples.")

    
    return one_hop_data, conjunction_data

if __name__ == "__main__":
    load_and_filter_webnlg()