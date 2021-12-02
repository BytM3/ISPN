from rich.console import Console
console=Console()
import os
parent=os.getcwd()

import ip
import phone

def menu(): ##--Main.Menu
    console.print('[b][[green1]1[/]] [cyan]ISP location[/][/]')
    console.print('[b][[green1]2[/]] [cyan]Phone location[/][/]')
    console.print('[b][[green1]0[/]] [red]EXIT[/][/]')
def menu1(): ##--ip.Menu
    console.print('\n[b][[green1]1[/]] [cyan]Info\Locate[/][/]')
    console.print('[bold][[green1]-[/]] [red]Return to Menu[/][/]')
def menu2(): ##--PHN.Menu
    console.print('\n[b][[green1]1[/]] [cyan]Info\Locate[/][/]')
    console.print('[bold][[green1]2[/]] [red]Help Region[/][/]')
    console.print('[bold][[green1]-[/]] [red]Return to Menu[/][/]')    
def header(): ##--INTRO
        console.print("_____________________[b][red]I.S.P.N[/][/]_____________________")
        console.print("\n[[b][green1]>[/][/]] [b][purple3]Crated by[/][/]: ",end="")
        console.print("Jawher Ben Smida",style="bold blue")
        console.print("\n[[b][green1]>[/][/]] [b][purple3]Version[/][/]: ",end="")
        console.print("1.0")
        console.print("\n[[b][green1]>[/][/]] [b][purple3]GitHub[/][/]: ",end="")
        console.print("https://github.com/j4wher",style="blue3")
        print("__________________________________________________")
def info(): ##--INFO
    console.print("\nFYI: All locations will be saved.",style="bold red")
    console.print("     Folder = HTML > contain all maps .",style="bold red")                  
    console.print("     Folder = his  > contain all data .",style="bold red") 
    print("__________________________________________________")

header()
info()
print()
menu()
opt=int(input("\nEnter your option: "))
while opt!=0:
    if opt == 1:
        menu1()
        ans=int(input("\nEnter your option: "))
        if ans == 1:
            ip.Loc(parent)
            break
        else:
            print()
            menu()
            opt=int(input("\nEnter your option: "))
    elif opt ==2:
        menu2()
        ans1=int(input("\nEnter your option: "))
        if ans1 == 1:
                n=phone.get_number()
                while True:
                    if phone.valid(n) == True:
                        phone.get_info(n)
                        phone.location(n,parent)
                        opt=3
                        break
                    else:
                        n=phone.get_number()
                break
        elif ans1 == 2:
                phone.help_reg()
                ans1=1
        else:
                print()
                menu()
                opt=int(input("\nEnter your option: "))
    else:
        print()
        menu()
        opt=int(input("\nEnter your option: "))
console.print("\nThanks for using our program.",style="italic bright_red")