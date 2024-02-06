import getch

def encoded_input(message): 
    print (message, end="") 
    pw = ""
    while True:
        symbol = getch.getch()
        if symbol == "\n" or symbol == "\r":
            break
        print("*", end="", flush=True)
        pw += symbol
    print()
    return pw