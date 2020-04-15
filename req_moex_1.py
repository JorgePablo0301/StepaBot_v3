import requests

import apimoex
import pandas as pd

class req_moex():
    NAME = 'SNGSP'
    PRICE_NOW = 0
    #def req_moex_ex:


with requests.Session() as session:
    data = apimoex.get_board_history(session, 'SNGSP')
    #data = apimoex.(session, 'SNGSP')
    print(data)
    #df = pd.DataFrame(data)
    #df.set_index('TRADEDATE', inplace=True)
    #print(df.head(), '\n')
    #print(df.tail(), '\n')
    #df.info()