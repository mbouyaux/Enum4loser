# Enum4Loser
## About
- Enum4loser is a tool I developed to simplify the enumeration of your scope in bugbounty. He will get all target subdomains and find all urls thanks to webarchive.
![](/images/df.png)
- He will test if some specific urls are vulnerable to open-redirect and print the PoC, all tested urls are saved in redirect file.
![](/images/op.png)
- New's featurs will comming soon.
- It is completely modular, you can integrate other tools and modify the functions already present.
---
## Install
- `sudo ./setup.sh`
---
## Docker install
- `sudo docker build -t enum4loser .`
- `sudo docker run -it enum4loser bash`
- `root@4ad60d36ad15:/tool# ./setup.sh`
## How to use Enum4loser
- `python3 enum4loser.py -d www.target.com -f name_of_folder`
- exemple : `python3 enum4loser.py -d www.yeswehack.com -f ywh --nosub true` for single domain.
- `python3 enum4loser.py -d target.com -f ywhack `
- exemple : `python3 enum4loser.py -d name_of_folder -f ywhalldomains`
- The result is store at /home/user/Desktop/bugbounty/target/name_of_folder .
