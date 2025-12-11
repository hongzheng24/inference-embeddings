


def generate_one_hop(dataset):

    results = []
    for sample in dataset:
        text = sample['text']
        # triple = sample['triples'][0]
        # subject, relation, object = [x.strip() for x in triple.split('|')]
        triples = [[x.strip() for x in triple.split('|')] for triple in sample['triples']]

        # Supported claims
        results.append({
            'claim': text,
            'label': 'SUPPORTED',
            'reasoning': 'One-hop',
            'evidence': triples
        })

        # Refuted claims
        # TODO
    
    return results

def generate_conjuction(dataset):
    results = []
    for sample in dataset:
        text = sample['text']
        triples = [[x.strip() for x in triple.split('|')] for triple in sample['triples']]

        # Supported claims
        results.append({
            'claim': text,
            'label': 'SUPPORTED',
            'reasoning': 'Conjunction',
            'evidence': triples
        })

        # Refuted claims
        # TODO

    return results
        
