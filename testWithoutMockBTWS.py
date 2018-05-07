import unittest
from BitcoinWallet import BitcoinPricer
from BitcoinServices import BitcoinValueService

class BitcoinPricerTests(unittest.TestCase):
    __NumberOfBitcoin=2345
    def setUp(self):
        self.btc_pricer = BitcoinPricer()

    def test_checkInputFormat(self):
        self.assertRaises(TypeError, self.btc_pricer.CalculateCurrentValueInUSDollar,'abcd')

    def test_checkOutputFormat(self):
        self.assertIsInstance(self.btc_pricer.CalculateCurrentValueInUSDollar(self.__NumberOfBitcoin), float)

    def test_outputMinRange(self):
        self.assertGreater(self.btc_pricer.CalculateCurrentValueInUSDollar(self.__NumberOfBitcoin),0)

    def test_outputMaxRange(self):
        self.assertLess(self.btc_pricer.CalculateCurrentValueInUSDollar(self.__NumberOfBitcoin),20999999*self.__NumberOfBitcoin)

if __name__ == '__main__':
    unittest.main(verbosity=3)
