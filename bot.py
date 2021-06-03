import time 
import hmac
import requests
import json
def getData(x):
    if x==1:
        response=requests.get("https://ftx.com/api/futures/BTC-1231")
        spotResponse=requests.get("https://ftx.com/api/futures/BTC-PERP")
    elif x==2:   
        response=requests.get("https://ftx.com/api/futures/ETH-1231")
        spotResponse=requests.get("https://ftx.com/api/futures/ETH-PERP")
    elif x==3:
        response=requests.get("https://ftx.com/api/futures/SOL-0625")
        spotResponse=requests.get("https://ftx.com/api/futures/SOL-PERP")
    elif x==4:
        response=requests.get("https://ftx.com/api/futures/BNB-0625")
        spotResponse=requests.get("https://ftx.com/api/futures/BNB-PERP")
    elif x==5:
        response=requests.get("https://ftx.com/api/futures/XRP-0625")
        spotResponse=requests.get("https://ftx.com/api/futures/XRP-PERP")
    elif x==6:
        response=requests.get("https://ftx.com/api/futures/DOGE-0625")
        spotResponse=requests.get("https://ftx.com/api/futures/DOGE-PERP")
    else:
        print("Invalid number selected")
        exit()
    futuresName=response.json()['result']['description']
    futuresPrice=response.json()['result']['last']
    spotPrice=spotResponse.json()['result']['last']
    currentAPY=(futuresPrice-spotPrice)/spotPrice
    print("Current Farthest Out Futures Expiry:",futuresName)
    print("Current Price of Future: $",futuresPrice)
    print("Current Price of Spot: $",spotPrice)
    print("Current Yield From Capturing Futures Premium: "+"{:.2%}".format(currentAPY))

print("Welcome to Futures Premium Calculator")
print("This tool can be used to quickly calculate yield on capturing premium profits")
print("Market data extracted from FTX")
print("By Dawid Chudzik")
print("-------------------------------------------")
print("1.Bitcoin")
print("2.Ethereum")
print("3.Solana")
print("4.BNB")
print("5.Ripple")
print("6.Dogecoin")
print("-------------------------------------------")
selection=input("Please enter the number of which coin you'd like to check yield on:")
getData(int(selection))
