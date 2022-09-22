import os
import sys
import requests
from ast import Delete
from time import sleep
from colorama import Fore
from dhooks import Webhook

os.system('cls') #Clearing console

#Creating functions

def duck():

    os.system("cls")

    webhook = Webhook(input("Webhook : ")) #Getting webhook from user

    messeage = "[@everyone]\n\n" + ("𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫\n" * 200) + "\n\n [@here]"#This is the message 

    amount = int(input("Amount : ")) #amount of messages to send

    for i in range(amount): #Making the loop
        webhook.send(messeage+'\n' * 100) #Sending messages
        print(Fore.GREEN + "Sent !")
    requests.delete(webhook) #Deleting webhook

def sendmessage():
    
    os.system("cls") #Clearing console

    webhook = Webhook(input("Webhook : "))  #Getting webhook from user

    messeage = input("Enter the message : ") #Getting message from user

    amount = int(input("Enter the amount of messages : "))#Getting the amount of messages from user 

    for i in range(amount): #Making loop
        webhook.send(messeage) #Sending messages
        print(Fore.GREEN + "Sent !")

while(True): #Creating a loop
    
    #Making Header
    print(f"""

    {Fore.MAGENTA}█░░░█ █▀▀ █▀▀▄ █░░█ █▀▀█ █▀▀█ █░█    ▀▀█▀▀ █▀▀█ █▀▀█ █░░ █▀▀
    {Fore.BLUE}█▄█▄█ █▀▀ █▀▀▄ █▀▀█ █░░█ █░░█ █▀▄    ░░█░░ █░░█ █░░█ █░░ ▀▀█ 
    {Fore.LIGHTMAGENTA_EX}░▀░▀░ ▀▀▀ ▀▀▀░ ▀░░▀ ▀▀▀▀ ▀▀▀▀ ▀░▀    ░░▀░░ ▀▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀

{Fore.MAGENTA}[1] Send message
{Fore.BLUE}[2] Delete webhook
{Fore.LIGHTMAGENTA_EX}[3] Nuke webhook
{Fore.LIGHTBLUE_EX}[4] Exit
    """)

    choose = input("> ") #Getting the choosed number

    if(choose == "1"):
        sendmessage()
        sleep(1.5)
    elif(choose == "2"):
        webhook = Webhook(input("Webhook : "))
        requests.delete(webhook)
        sleep(1.5)
    elif(choose == "3"):
        duck()
        sleep(1.5)
    elif(choose == "4"):
        sys.exit()
    else:
        print(Fore.RED + "Wrong input !")
        sleep(1.5)