from colorama import Fore
import os
import platform
import re

oS = platform.system()
def clean():
    if oS == 'Linux':
        os.system("clear")
    else:
        os.system("cls")
def clear_screen(func):
    def clearScreen(*args, **kwargs):
        clean()
        func(*args,**kwargs)
        clean()
    return clearScreen

def execute_command(command : str) -> None:
    print(Fore.GREEN + "----------- ON EXECUTION ----------------")
    print(Fore.YELLOW + f"!!!! Executing -> {command}")
    input("===> Press Any Key to Continue")
    #os.system(command)

@clear_screen
def print_message(message : str) -> None:
    print(Fore.GREEN +"----------- MENSAJE ----------------")
    print(Fore.GREEN + "===>" + message)
    input(Fore.GREEN + "==> Press Any Key to Continue")

def print_submessage(message : str) -> None:
    print(Fore.WHITE + message)
    input(Fore.WHITE + "==> Press Any Key to Continue")

def print_alert(alert : str) -> None:
    print(Fore.RED + "-------------WARNING-----------------")
    print(Fore.RED + "==>" + alert)
    input(Fore.RED + "==> Press Any Key to Continue")

if __name__ == '__main__':
    with open("archivo.txt","r") as arch:
        for line in arch.readlines():
            if re.match("^message\s+",line):
                print_message(re.sub("^message\s+","",line,1))
            elif re.match("^submessage\s+",line):
                print_submessage(re.sub("^submessage\s+","",line,1))
            elif re.match("^alert\s+",line):
                print_alert(re.sub("^âlert\s+","",line,1))
            else:
                execute_command(line)
