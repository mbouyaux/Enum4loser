#!/usr/bin/python3
# By SpawnZii Version 0.1

from posix import NGROUPS_MAX
import sys,getopt
import subprocess
import os
import pyfiglet
import threading
import getpass

open_redirect_parameter = ['=http','=https','=www']
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

    check_dir_main = os.path.isdir('/home/{}/Desktop/{}/{}/{}'.format(current_user,hunt_folder,target_folder,name_folder))
    if check_dir_main == False:
        os.mkdir('/home/{}/Desktop/{}/{}/{}'.format(current_user,hunt_folder,target_folder,name_folder))
        print('\033[92m[+] Creating folders...\033[0m')
    else:
        print('\033[93m[-] Folder already created at /home/{}/Desktop/{}/{}/{}\033[0m'.format(current_user,hunt_folder,target_folder,name_folder))

    check_dir_url = os.path.isdir('/home/{}/Desktop/{}/{}/{}/url'.format(current_user,hunt_folder,target_folder,name_folder))
    if check_dir_url == False:
        os.mkdir('/home/{}/Desktop/{}/{}/{}/url'.format(current_user,hunt_folder,target_folder,name_folder))
    

def subdomain_enum(target,name_folder):
    check_dir_sub = os.path.isfile('/home/{}/Desktop/{}/{}/{}/subdomain.txt'.format(current_user,hunt_folder,target_folder,name_folder))
    if check_dir_sub == False:
        print("\033[92m[+] Get all subdomains ...\033[0m")
        sublister = subprocess.run([sys.executable,"/usr/local/bin/sublist3r.py","-d",""+target+"","-o","/home/"+current_user+"/Desktop/"+hunt_folder+"/"+target_folder+"/"+name_folder+"/subdomain.txt"],stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)
    else:
        print("\033[93m[-] Already have subdomains ...\033[0m")

def scrap_url(name_folder):
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
        print('\033[92m[+] Try to find potential open redirect ...\033[0m')

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
                        if url not in known_url:
                            f = open(file_open_path, "a")
                            f.write(url)
                            f.close()
                            known_url.append(url)

def main(argv):
    banner_one = pyfiglet.figlet_format("Enum4loser")
    print("\033[91m"+banner_one[0:232]+"\033[0m"+"\033[92m"+banner_one[232:300]+"\033[0m")
    print('Version 0.1')
    print('By SpawnZii made with \033[91m<3\033[0m \n')
    target = ''
    name_folder = ''
    try:
        opts, args = getopt.getopt(argv,"hd:n:g",["domain="])
    except getopt.GetoptError:
      print ('Usage: python3 Enum4loser.py -d target.com -n name_of_folder')
      sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
         print ("\033[2;31;43m Usage: python3 Enum4loser.py -d target.com -n name_of_folder -g \n -g Get url for all subdomains \n -n Creat folder with 'n' name \033[0;0m")
         sys.exit()
        elif opt in ("-d", "--domain"):
            target = arg
        elif opt in ("-n", "--name"):
            name_folder = arg
            creat_folder(name_folder)
            subdomain_enum(target,name_folder)

        elif opt in ("-g","--geturl"):
            scrap_url(name_folder)

if __name__ == "__main__":
   main(sys.argv[1:])
