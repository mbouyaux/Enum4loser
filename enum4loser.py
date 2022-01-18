#!/usr/bin/python3
# By SpawnZii Version 0.4

import sys,getopt
import pyfiglet
from pathlib import Path
from functions.creatfolder import *
from functions.subenum import *
from functions.urlwayback import *

home_path = str(Path.home())
hunt_folder = "bugbounty" # path for outpout folder /home/user/Desktop/bugbounty/target/
target_folder = "target"  # you can change the value of this two variables


def main(argv):
    banner_one = pyfiglet.figlet_format("Enum4loser")
    print("\033[91m"+banner_one[0:232]+"\033[0m"+"\033[92m"+banner_one[232:300]+"\033[0m")
    print('Version 0.4')
    print('By SpawnZii made with \033[91m<3\033[0m \n')
    target = ''
    name_folder = ''
    attacker_srv = ''
    try:
        opts, args = getopt.getopt(argv,"hd:f:s:",["domain="])
    except getopt.GetoptError:
      print("""Usage: python3 enum4loser.py -d target.com -f name_of_folder

        -d    Domain name.
        -f    Name of the folder 
        -s    Server of attaker.
Quick start: python3 enum4loser.py -d yeswehack.com -f ywhack -s https://attacker.com""")
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("""Usage: python3 enum4loser.py -d target.com -f name_of_folder

        -d    Domain name.
        -f    Name of the folder 
Quick start: python3 enum4loser.py -d yeswehack.com -f ywhack""")
            sys.exit()
        elif opt in ("-d", "--domain"):
            target = arg
        elif opt in ("-f", "--folder"):
            name_folder = arg
            creat_folder(home_path,name_folder,hunt_folder,target_folder)
            subdomain_enum(target,home_path,hunt_folder,target_folder,name_folder)
        if opt in ("-s","--server"):
            attacker_srv = arg
            scrap_url(home_path,hunt_folder,target_folder,name_folder,attacker_srv)

if __name__ == "__main__":
   main(sys.argv[1:])
