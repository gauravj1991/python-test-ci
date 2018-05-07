#!/usr/bin/python
from BitcoinServices import BitcoinValueService

class BitcoinPricer:
    'BitcoinWallet class has two private variables called WalletAddress and BalanceInBtc.'
    __WalletAddress=''
    __BalanceInBtc=''
    # contructor class
    def __init__(self):
      self.__WalletAddress = 'asjsajacdcdc394394949'
      self.__BalanceInBtc = 10
    # Destructor class
    def __del__(self):
      class_name = self.__class__.__name__
      print(class_name, "current instance destroyed")
    # Public Method
    def CalculateCurrentValueInUSDollar(self,bitcoin:float)->float:
        BTCVService=BitcoinValueService()
        return (float(BTCVService.getCurrentBitcoinValue())*bitcoin/0)
# running public method
BW=BitcoinPricer()
print(BW.CalculateCurrentValueInUSDollar(30))
