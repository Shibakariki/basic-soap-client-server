# --- Import client library ---

from zeep import Client as ZeepClient
from models import Todos

# --- Defining the client ---

test_client = ZeepClient('http://localhost:7789/?wsdl')

print("Zeep client is used")    

# --- Launching the client ---

while(True):
    print("\n1. Test service")
    print("2. Test service2")
    print("3. Random from")
    print("4. Exit\n")
    choice = int(input("Enter your choice: "))
    # --- Test service "test_request" ---
    if choice == 1:
        datas = test_client.service.test_request()[0]["Todos"]            
        text_to_print = "ID | USER ID | TITLE | DUE ON | STATUS \n"
        for data in datas:
            text_to_print += str(data.id) + " | " + str(data.user_id) + " | "+ str(data.title) +" | " + str(data.due_on) + " | " + str(data.status) + "\n"
        print(text_to_print)
    # --- Test service "test_request2" ---
    elif choice == 2:
        datas = test_client.service.test_request2()
        print(datas)
    # --- Test service "random_from" ---
    elif choice == 3:
        rand = int(input("Enter a max number for the random: "))
        name = input("Enter your name: ")
        datas = test_client.service.random_from(rand+1,name)[0]
        print(datas)
    # --- Exit ---
    elif choice == 4:
        break
    else:
        print("Invalid choice")


