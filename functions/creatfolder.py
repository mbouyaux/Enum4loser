import os
from pathlib import Path

def create_folder(home_path,name_folder,hunt_folder,target_folder):

    check_dir_bb = os.path.isdir(f'{home_path}/Desktop/{hunt_folder}')
    if check_dir_bb == False:
        os.mkdir(f'{home_path}/Desktop/{hunt_folder}')

    check_dir_target = os.path.isdir(f'{home_path}/Desktop/{hunt_folder}/{target_folder}')
    if check_dir_target == False:
        os.mkdir(f'{home_path}/Desktop/{hunt_folder}/{target_folder}')

    check_dir_main = os.path.isdir(f'{home_path}/Desktop/{hunt_folder}/{target_folder}/{name_folder}/')
    if check_dir_main == False:
        os.mkdir(f'{home_path}/Desktop/{hunt_folder}/{target_folder}/{name_folder}/')
        print('\033[92m[+] Creating folders...\033[0m')
    else:
        print(f'\033[93m[-] Folder already created at {home_path}/Desktop/{hunt_folder}/{target_folder}/{name_folder}/ \033[0m')

    check_dir_url = os.path.isdir(f'{home_path}/Desktop/{hunt_folder}/{target_folder}/{name_folder}/url')
    if check_dir_url == False:
        os.mkdir(f'{home_path}/Desktop/{hunt_folder}/{target_folder}/{name_folder}/url')