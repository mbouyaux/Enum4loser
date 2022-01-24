#!/usr/bin/python3
# By SpawnZii Version 0.5

from pathlib import Path
import sys
import click
import pyfiglet
from functions.creatfolder import *
from functions.subenum import *
from functions.urlwayback import *

HOME_PATH = str(Path.home())
HUNT_FOLDER = "bugbounty"
TARGET_FOLDER = "target"

@click.command()
@click.option('--domain','-d',help='target domain name')
@click.option('--filename','-f',help='name of the output folder store at ~/Desktop/bugbouty/target/here')
@click.option('--nosub',default="false",help='This options enumerate juste the main domain and not the subdomain, false by default')

def main(domain,filename,nosub):
    banner_one = pyfiglet.figlet_format("Enum4loser")
    print("\033[91m"+banner_one[0:232]+"\033[0m"+"\033[92m"+banner_one[232:300]+"\033[0m")
    print('Version 0.5')
    print('By SpawnZii made with \033[91m<3\033[0m \n')
    name_folder = filename
    attacker_srv = "https://attacker.com/"
    nosub = str(nosub.lower())

    if domain is None:
        print('\033[91mIndicate a valid domain\033[0m \n')
        sys.exit(0)
    if filename is None:
        print('\033[91mIndicate a valid filename\033[0m \n')
        sys.exit(0) 
    else:
        if nosub == "true":
            create_folder(HOME_PATH,name_folder,HUNT_FOLDER,TARGET_FOLDER)
            single_domain_url(domain,HOME_PATH,HUNT_FOLDER,TARGET_FOLDER,name_folder)
            single_domain_filter(domain,HOME_PATH,HUNT_FOLDER,TARGET_FOLDER,name_folder)
            openredirect(HOME_PATH,HUNT_FOLDER,TARGET_FOLDER,name_folder,attacker_srv)
        else:
            create_folder(HOME_PATH,name_folder,HUNT_FOLDER,TARGET_FOLDER)
            subdomain_enum(domain,HOME_PATH,HUNT_FOLDER,TARGET_FOLDER,name_folder)
            scrap_url(HOME_PATH,HUNT_FOLDER,TARGET_FOLDER,name_folder,attacker_srv)

if __name__ == "__main__":
    main()
