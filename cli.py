from colorama import init
import requests
import os

init(autoreset=True)

def card_transport(card):
    global status
    r = requests.post(f'https://madridd.com.es/v1/card-transport/{card}')
    data = r.json()
    status = r.status_code

    return data

def dateChange(date):
    date = date.split("T")[0]
    date = date.split("-")
    date = f"{date[2]}/{date[1]}/{date[0]}"
    return date


banner = """
        \033[39m _______
          \   /
            |                       
         ___|___               
       _|_______|_            
    / |[  \033[94mSaldo\033[39m  ]| \         
    | |     |     | |           
    | |     |     | |           
    | |_____|_____| |           by: @j3qn
    |\|====(M)====|/|           
    |\[][]_____[][]/|            
    |/  |0 [ ]  |  \|         
     ==((       ))==              
   ===//=========\\===       
  ===//===========\\===  """



def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    card = input("\nIntroduce el número de la tarjeta: \033[94m")
    data = card_transport(card)
    main = data["tickets"][0]["charge"]

    if status == 404:
        print("\033[91m - \033[39mLa tarjeta no existe")
        return
    
    if status == 200:
        print("\033[39m Status \033[92m200 \u2713") 
        print("\n\033[94m [\U0001F4B2] \033[39mUltima Recarga:\033[94m "+dateChange(main["purchaseDate"]))
        print("\033[94m [\U0001F4B2] \033[39mPrimera vez usado:\033[94m "+dateChange(main["firstUseDate"]))
        print("\033[94m [\u2717] \033[39mFecha de expiracion:\033[94m "+dateChange(main["lastUseDate"]))





    



if __name__ == "__main__":
    main()