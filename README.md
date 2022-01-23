# Enum4Loser
## About
- Enum4loser is a tool I developed to simplify enumeration in bugbounty.
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
- `python3 enum4loser.py -d target.com -f name_of_folder`
- exemple : `python3 enum4loser.py -d www.yeswehack.com -f ywh --nosub true`
- `python3 enum4loser.py -d yeswehack.com -f ywhack --nosub true` for single domain.
- exemple : `python3 enum4loser.py -d www.yeswehack.com -f ywhalldomains`
