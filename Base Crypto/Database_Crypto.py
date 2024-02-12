import webbrowser

def cryptoesp():

    print ("1. Bitcoin")
    print ("2. Ethereum")
    print ("3. Dogecoin")
    print ("4. Tether")
    print ("5. Binance Coin")
    print ("6. Desconectar")

def cryptoeng():

    print ("1. Bitcoin")
    print ("2. Ethereum")
    print ("3. Dogecoin")
    print ("4. Tether")
    print ("5. Binance Coin")
    print ("6. Disconnect")

def cryptoselectesp():
    crypto = input("    Criptomoneda?")
    match crypto:
        case "1":
            webbrowser.open('https://crypto.com/price/bitcoin')
        case "2":
            webbrowser.open('https://crypto.com/price/ethereum')
        case "3":
            webbrowser.open('https://crypto.com/price/dogecoin')
        case "4":
            webbrowser.open('https://crypto.com/price/tether')
        case "5":
            webbrowser.open('https://crypto.com/price/bnb')
        case "6":
            print ("Gotcha")

def cryptoselecteng():
    crypto = input("    Crypto Currency?")
    match crypto:
        case "1":
            webbrowser.open('https://crypto.com/price/bitcoin')
        case "2":
            webbrowser.open('https://crypto.com/price/ethereum')
        case "3":
            webbrowser.open('https://crypto.com/price/dogecoin')
        case "4":
            webbrowser.open('https://crypto.com/price/tether')
        case "5":
            webbrowser.open('https://crypto.com/price/bnb')
        case "6":
            print ("Gotcha")

cryptoesp()
cryptoselectesp()