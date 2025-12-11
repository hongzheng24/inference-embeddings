import unittest
from typing import Optional, Callable

from dataloader import load_and_filter_webnlg


class IOTest(unittest.TestCase):

    def test_dataloader(self):
        '''
        Test one hop data and conjuction data have entries with the
        correct number of triples.
        '''
        one_hop_data, conjunction_data = load_and_filter_webnlg()
        for entry in one_hop_data:
            assert(len(entry['triples']) == 1)
        for entry in conjunction_data:
            assert(len(entry['triples']) > 1)

if __name__ == "__main__":
    unittest.main()