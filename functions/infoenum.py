import subprocess
import os

def wafdetector(domain,home_path,hunt_folder,target_folder,name_folder):
    print(f'\033[92m[+] WAF detection ...\033[0m')
    cmd = f"/usr/bin/wafw00f '{domain}' > {home_path}/Desktop/{hunt_folder}/{target_folder}/{name_folder}/waf.txt"
    subprocess.Popen(cmd,shell=True,stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT).wait()
    path = f"{home_path}/Desktop/{hunt_folder}/{target_folder}/{name_folder}/waf.txt"
