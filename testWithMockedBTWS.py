import unittest, mock
from BitcoinWallet import BitcoinPricer
from BitcoinServices import BitcoinValueService

@mock.patch('BitcoinServices.BitcoinValueService.getCurrentBitcoinValue')
class BitcoinPricerTests(unittest.TestCase):
    __arg=2345
    def setUp(self):
        self.btc_pricer = BitcoinPricer()

    def test_checkInputFormat(self, mock_getCurrentBitcoinValue):
        mock_getCurrentBitcoinValue.return_value = 435
        self.assertRaises(TypeError, self.btc_pricer.CalculateCurrentValueInUSDollar,'abcd')

    def test_checkOutputFormat(self, mock_getCurrentBitcoinValue):
        mock_getCurrentBitcoinValue.return_value =435
        self.assertIsInstance(self.btc_pricer.CalculateCurrentValueInUSDollar(self.__arg), float)

    def test_outputMinRange(self, mock_getCurrentBitcoinValue):
        mock_getCurrentBitcoinValue.return_value = 435
        self.assertGreater(self.btc_pricer.CalculateCurrentValueInUSDollar(self.__arg),0)

    def test_outputMaxRange(self, mock_getCurrentBitcoinValue):
        mock_getCurrentBitcoinValue.return_value = 435
        self.assertLess(self.btc_pricer.CalculateCurrentValueInUSDollar(self.__arg),20999999*self.__arg)

if __name__ == '__main__':
    unittest.main(verbosity=3)
