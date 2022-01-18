#!/usr/bin/python3
# By SpawnZii Version 0.5

import click
import sys,getopt
import pyfiglet
from pathlib import Path
from functions.creatfolder import *
from functions.subenum import *
from functions.urlwayback import *

home_path = str(Path.home())
urlsorting_parameter = ['=http','=https','=www','=/','=//']
hunt_folder = "bugbounty"
target_folder = "target"
@click.command()

@click.option('--domain','-d',help='target domain name')
@click.option('--filename','-f',help='name of the output folder store at ~/Desktop/bugbouty/target/here')
@click.option('--server','-s',default='https://www.google.com',help='You can add your web server to see the logs in live')
@click.option('--nosub',default="False",help='This options enumerate juste the main domain and not the subdomain')

def main(domain,filename,server,nosub):
    banner_one = pyfiglet.figlet_format("Enum4loser")
    print("\033[91m"+banner_one[0:232]+"\033[0m"+"\033[92m"+banner_one[232:300]+"\033[0m")
    print('Version 0.5')
    print('By SpawnZii made with \033[91m<3\033[0m \n')
    name_folder = domain
    target = filename
    attacker_srv = server
    nosub = str(nosub.lower())
    if nosub == "true":
        print("Under dev")

    else:
        if domain == None:
            print('\033[91mIndicate a valid domain\033[0m \n')
        if filename == None:
            print('\033[91mIndicate a valid filename\033[0m \n')
        else:
            creat_folder(home_path,name_folder,hunt_folder,target_folder)
            subdomain_enum(target,home_path,hunt_folder,target_folder,name_folder)
            scrap_url(home_path,hunt_folder,target_folder,name_folder,attacker_srv)

if __name__ == "__main__":
   main()
