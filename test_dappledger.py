# test_dappledger.py
"""
Tests for DappLedger module.
"""

import unittest
from dappledger import DappLedger

class TestDappLedger(unittest.TestCase):
    """Test cases for DappLedger class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DappLedger()
        self.assertIsInstance(instance, DappLedger)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DappLedger()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
