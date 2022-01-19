import os

open_redirect_parameter = ['=http','=https','=www','=/','=//']

def single_domain_filter(domain,home_path,hunt_folder,target_folder,name_folder):
    known_url = []
    path = f'{home_path}/Desktop/{hunt_folder}/{target_folder}/{name_folder}/url/{domain}.txt'
    new_file = f'{home_path}/Desktop/{hunt_folder}/{target_folder}/{name_folder}/url/filtered.{domain}.txt'
    redirect_file = f'{home_path}/Desktop/{hunt_folder}/{target_folder}/{name_folder}/redirect.txt'
    with open(path) as file:
        for i in file:
            if domain in i:
                url = i
                f = open(new_file, "a")
                f.write(url)
                f.close()
    with open(new_file) as file:
        for url in file:
            for param in open_redirect_parameter:
                if param in url:
                    if url.split('=')[0] not in known_url:
                        f = open(redirect_file, "a")
                        f.write(url)
                        f.close()
                        known_url.append(url.split('=')[0])
                    

def search_pattern(home_path,hunt_folder,target_folder,name_folder):
    known_url = []
    path = f'{home_path}/Desktop/{hunt_folder}/{target_folder}/{name_folder}/url/'
    url_list = os.listdir(path)
    for file in url_list:
        size = os.path.getsize(path+file)
        if size >1 :
            f = open(path+file,'r')
            f = f.readlines()
            for url in f:
                for p in open_redirect_parameter:
                    if p in url :
                        file_open_path = f'{home_path}/Desktop/{hunt_folder}/{target_folder}/{name_folder}/redirect.txt'
                        if url.split('=')[0] not in known_url:
                            f = open(file_open_path, "a")
                            f.write(url)
                            f.close()
                            known_url.append(url.split('=')[0])
