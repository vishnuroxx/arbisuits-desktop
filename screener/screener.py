'''Version 2.0 Testing phase'''
import yfinance as yf
from yfinance import EquityQuery 
import time



major_exchanges = [ # risk of rate limiting
    "DFM", "BUE", "VIE", "ASX", "BRU", "SAO", "TOR", "EBS", 
    "SGO", "SHH", "BVC", "PRA", "FRA", "CPH", "TAL", "CAI", 
    "MAD", "HEL", "PAR", "LSE", "ATH", "HKG", "BUD", "JKT", 
    "ISE", "TLV", "NSI", "ICE", "MIL", "JPX", "KSC", "KUW", 
    "CSE", "LIT", "RIS", "MEX", "KLS", "AMS", "OSL", "NZE", 
    "PHS", "KAR", "WSE", "LIS", "DOH", "BVB", "MCX", "SAU", 
    "STO", "SES", "SET", "IST", "TAI", "NYQ", "VSE", "JNB"
]


valid_exchanges = ["NYQ"]

def screen_stocks() -> list:
    result  = []
    marketCapQuery = EquityQuery('gt', ["lastclosemarketcap.lasttwelvemonths", 1e9]) # 1 biLLION 
    roeQuery = EquityQuery('gt', ['returnonequity.lasttwelvemonths', 0.12])
    peRatioQuery = EquityQuery('lte',['peratio.lasttwelvemonths', 30])
    grossPorfitQuery = EquityQuery('gt', ["grossprofitmargin.lasttwelvemonths", 0.30])
    dividendsQuery = EquityQuery('gt', ["forward_dividend_yield", 0.02])

    for exchange in valid_exchanges:    
        exchangeQuery = EquityQuery('is-in', ['exchange', exchange])
        query = EquityQuery('and',
                            [marketCapQuery,exchangeQuery, roeQuery, peRatioQuery, grossPorfitQuery,dividendsQuery])
        response = yf.screen(query, size=250, sortField="grossprofitmargin.lasttwelvemonths")
            
        result += [data['symbol'] for data in response['quotes']]
        time.sleep(1)

    return result

