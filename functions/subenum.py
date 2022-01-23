import subprocess
import os
from posix import NGROUPS_MAX

def subdomain_enum(target,home_path,hunt_folder,target_folder,name_folder):
    check_dir_sub = os.path.isfile(f'{home_path}/Desktop/{hunt_folder}/{target_folder}/{name_folder}/subdomain.txt')
    if check_dir_sub == False:
        print("\033[92m[+] Get all subdomains ...\033[0m")
        cmd = f"/usr/bin/python3 /usr/local/bin/sublist3r.py -d '{target}' -o {home_path}/Desktop/{hunt_folder}/{target_folder}/{name_folder}/subdomain.txt"
        subprocess.Popen(cmd,shell=True,stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT).wait()
    else:
        print("\033[93m[-] Already have subdomains ...\033[0m") 