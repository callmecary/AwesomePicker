import marketData
import datetime
import math
import pandas as pd
from yahoo_finance import Share
from pandas.tseries.offsets import BDay


def get_pead_quotes(date):
    '''date = datetime.date(2016,12,6)'''
    previous_businessDt = (date-BDay(1)).date()
    days90backDt = previous_businessDt - datetime.timedelta(days=90)

    asofDate = date.strftime("%Y%m%d")
    previousDt = previous_businessDt.strftime("%Y%m%d")

    interestingQuotes = marketData.getInterestingQuotes(asofDate, previousDt)
    pead_results = []
    for interestingQuote in interestingQuotes:
        yahoo = Share(interestingQuote['symbol'])
        if yahoo.get_open() is None: continue
        quotes = yahoo.get_historical(str(days90backDt),str(previous_businessDt))
        size = len(quotes)
        total = 0
        for i in range(0,size-1):
            total += abs(float(quotes[i]['Close'])-float(quotes[i+1]['Open']))

        avg = total/(size-1)

        squared_deviations_total = 0 
        for i in range(0,size-1):
            squared_deviations_total += math.pow(abs(float(quotes[i]["Close"])-float(quotes[i+1]["Open"]))-avg,2)

        variance = squared_deviations_total/(size-1)
        std_dv90days = math.sqrt(variance)
        
        previous_close = yahoo.get_prev_close()
        today_open = yahoo.get_open()
        
        todaysmoving = float(today_open)-float(previous_close)

        if(abs(todaysmoving)>std_dv90days):
            if(todaysmoving>0):
                pead_results.append({'symbol':interestingQuote['symbol'],'action':'Long'})
                #print(interestingQuote['symbol']+' Long '+str(todaysmoving)+' '+str(std_dv90days))
            else:
                pead_results.append({'symbol':interestingQuote['symbol'],'action':'Short'})
                #print(interestingQuote['symbol']+' Short '+str(todaysmoving)+' '+str(std_dv90days))
        
    return pead_results



def main():
    date = datetime.date(2016,12,6)
    pead_results = get_pead_quotes(date)
    print(pead_results)

if __name__ == '__main__':
    main()