import requests
import json

class BitcoinValueService:
    def getCurrentBitcoinValue(self):
        try:
            response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
            json_data = response.json()
            return (json_data['bpi']['USD']['rate_float'])
        except:
            print('Some error in getCurrentBitcoinValue service occured')
