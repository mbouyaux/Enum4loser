#!/usr/bin/python3
# By SpawnZii Version 0.3

from posix import NGROUPS_MAX
import sys,getopt
import subprocess
import os
import pyfiglet
import threading
import getpass
import requests
import aiohttp
import asyncio

open_redirect_parameter = ['=http','=https','=www','=/','=//']
current_user = getpass.getuser()
hunt_folder = "bugbounty"
target_folder = "target"

def creat_folder(name_folder):
    check_dir_bb = os.path.isdir('/home/{}/Desktop/{}'.format(current_user,hunt_folder))
    if check_dir_bb == False:
        os.mkdir('/home/{}/Desktop/{}'.format(current_user,hunt_folder))

    check_dir_t = os.path.isdir('/home/{}/Desktop/{}/{}'.format(current_user,hunt_folder,target_folder))
    if check_dir_t == False:
        os.mkdir('/home/{}/Desktop/{}/{}'.format(current_user,hunt_folder,target_folder))

    check_dir_main = os.path.isdir('/home/{}/Desktop/{}/{}/{}/'.format(current_user,hunt_folder,target_folder,name_folder))
    if check_dir_main == False:
        os.mkdir('/home/{}/Desktop/{}/{}/{}/'.format(current_user,hunt_folder,target_folder,name_folder))
        print('\033[92m[+] Creating folders...\033[0m')
    else:
        print('\033[93m[-] Folder already created at /home/{}/Desktop/{}/{}/{}/ \033[0m'.format(current_user,hunt_folder,target_folder,name_folder))

    check_dir_url = os.path.isdir('/home/{}/Desktop/{}/{}/{}/url'.format(current_user,hunt_folder,target_folder,name_folder))
    if check_dir_url == False:
        os.mkdir('/home/{}/Desktop/{}/{}/{}/url'.format(current_user,hunt_folder,target_folder,name_folder))
    

def subdomain_enum(target,name_folder):
    check_dir_sub = os.path.isfile('/home/{}/Desktop/{}/{}/{}/subdomain.txt'.format(current_user,hunt_folder,target_folder,name_folder))
    if check_dir_sub == False:
        print("\033[92m[+] Get all subdomains ...\033[0m")
        sublister = subprocess.run(["/usr/bin/python3","/usr/local/bin/sublist3r.py","-d",""+target+"","-o","/home/"+current_user+"/Desktop/"+hunt_folder+"/"+target_folder+"/"+name_folder+"/subdomain.txt"],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    else:
        print("\033[93m[-] Already have subdomains ...\033[0m")

def scrap_url(name_folder,attacker_srv):
        print('\033[92m[+] Get urls of subdomains ...\033[0m')
        sub_file = open("/home/{}/Desktop/{}/{}/{}/subdomain.txt".format(current_user,hunt_folder,target_folder,name_folder),"r")
        sub_number = 0
        sub_list = []
        for sub in sub_file:
            sub_number = sub_number+1
            sub_list.append(str(sub.strip('\n')))
        for i in range(sub_number):
                t_one = threading.Thread(target=url_file,args=(name_folder,sub_list,i))
                t_one.start()
                t_one.join()
        print('\033[92m[+] Try to find potential open redirect ...\033[0m')
        trigger_open_redirect(name_folder,open_redirect_parameter,attacker_srv)

def url_file(name_folder,sub_list,i):
    cmd = '/usr/bin/echo "{}" | /usr/local/bin/waybackurls >> /home/{}/Desktop/{}/{}/{}/url/{}.txt '.format(sub_list[i].rstrip("\n"),current_user,hunt_folder,target_folder,name_folder,sub_list[i].rstrip("\n"))
    subprocess.Popen(cmd,shell=True,stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT).wait()
    open_redirect(name_folder)


def open_redirect(name_folder):
    known_url = []
    path = "/home/{}/Desktop/{}/{}/{}/url/".format(current_user,hunt_folder,target_folder,name_folder)
    url_list = os.listdir(path)
    for file in url_list:
        size = os.path.getsize(path+file)
        if size >1 :
            f = open(path+file,'r')
            f = f.readlines()
            for url in f:
                for p in open_redirect_parameter:
                    if p in url :
                        file_open_path = '/home/{}/Desktop/{}/{}/{}/redirect'.format(current_user,hunt_folder,target_folder,name_folder)
                        if url.split('=')[0] not in known_url:
                            f = open(file_open_path, "a")
                            f.write(url)
                            f.close()
                            known_url.append(url.split('=')[0])
async def fetch(URL):
    async with aiohttp.ClientSession(trust_env=True) as session:
        try:
            async with session.get(URL,allow_redirects=True) as response:
                rep = response.url 
                repcheck = response.real_url
                in_url = str(URL)
                if in_url not in str(rep) and in_url not in str(repcheck):
                    print("\033[91m[$$$] Open redirect found at : {}\033[0m".format(URL))
        except aiohttp.ClientConnectionError as e:
            pass

async def start(url):
    await fetch(url)

def trigger_open_redirect(name_folder,open_redirect_parameter,attacker_srv):
    path = "/home/{}/Desktop/{}/{}/{}/".format(current_user,hunt_folder,target_folder,name_folder)
    file_of_vuln_urls = open(path+"redirect")

    for url in file_of_vuln_urls:
        for i in open_redirect_parameter:
            if url.count(i) > 0:
                url = url.split("=")
                url_done = url[0] + "="+attacker_srv+"/?vuln_url="+url[0]
                loop = asyncio.new_event_loop()
                loop.run_until_complete(start(url_done))


def main(argv):
    banner_one = pyfiglet.figlet_format("Enum4loser")
    print("\033[91m"+banner_one[0:232]+"\033[0m"+"\033[92m"+banner_one[232:300]+"\033[0m")
    print('Version 0.3')
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
            creat_folder(name_folder)
            subdomain_enum(target,name_folder)
            #scrap_url(name_folder)
        if opt in ("-s","--server"):
            attacker_srv = arg
            scrap_url(name_folder,attacker_srv)

if __name__ == "__main__":
   main(sys.argv[1:])
