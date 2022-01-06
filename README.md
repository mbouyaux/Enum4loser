# Enum4Loser
## About
Enum4loser is a tool I developed to simplify enumeration in bugbounty.
It is completely modular, you can integrate other tools and modify the functions already present.
---
## Install
`sudo ./setup.sh`
- After installation you have to change the shebang of the sublist3r script locate at : /usr/local/bin/sublist3r.py, replace by /usr/bin/python3.
---
## How to use Enum4loser
`python3 enum4loser.py -d target.com -f name_of_folder -s endpoint_for_open-redirect`
`python3 enum4loser.py -d yeswehack.com -f ywhack -s https://www.google.com`
