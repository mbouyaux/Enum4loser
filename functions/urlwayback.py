import threading
import subprocess
import os
from functions.searchvuln import*
from functions.urlsorting import *


def single_domain_url(domain,home_path,hunt_folder,target_folder,name_folder):
    print(f'\033[92m[+] Get urls of subdomain {domain}\033[0m') 
    cmd = f"/usr/bin/echo '{domain}' | /usr/local/bin/waybackurls >> {home_path}/Desktop/{hunt_folder}/{target_folder}/{name_folder}/url/{domain}.txt"
    subprocess.Popen(cmd,shell=True,stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT).wait()
    size = os.path.getsize(f'{home_path}/Desktop/{hunt_folder}/{target_folder}/{name_folder}/url/{domain}.txt')
    if size <= 1 :
        print(f"\033[91mNo url found for {domain}\033[0m \n")
    

def subdomain_url_file(home_path,hunt_folder,target_folder,name_folder,sub_list,i):
    fname = sub_list[i].rstrip("\n")
    cmd = f'/usr/bin/echo "{fname}" | /usr/local/bin/waybackurls >> {home_path}/Desktop/{hunt_folder}/{target_folder}/{name_folder}/url/{fname}.txt'
    subprocess.Popen(cmd,shell=True,stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT).wait()
    size = os.path.getsize(f'{home_path}/Desktop/{hunt_folder}/{target_folder}/{name_folder}/url/{fname}.txt')
    if size <= 1 :
        os.remove(f'{home_path}/Desktop/{hunt_folder}/{target_folder}/{name_folder}/url/{fname}.txt')

    search_pattern(home_path,hunt_folder,target_folder,name_folder)

def scrap_url(home_path,hunt_folder,target_folder,name_folder,attacker_srv):
        print('\033[92m[+] Get urls of subdomains ...\033[0m')
        sub_file = open(f'{home_path}/Desktop/{hunt_folder}/{target_folder}/{name_folder}/subdomain.txt','r')
        sub_number = 0
        sub_list = []
        for sub in sub_file:
            sub_number = sub_number+1
            sub_list.append(str(sub.strip('\n')))
        for i in range(sub_number):
                t_one = threading.Thread(target=subdomain_url_file,args=(home_path,hunt_folder,target_folder,name_folder,sub_list,i))
                t_one.start()
                t_one.join()
        openredirect(home_path,hunt_folder,target_folder,name_folder,attacker_srv)