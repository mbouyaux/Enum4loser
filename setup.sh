#!/bin/bash
# requirements installation

pip install -r requirements.txt
git clone https://github.com/aboul3la/Sublist3r.git
cd Sublist3r/ ;pip install -r requirements.txt;cp -r subbrute /usr/local/bin/ ; cp sublist3r.py /usr/local/bin/ ; cd ../ ; rm -rf Sublist3r/

sudo apt install golang-go
sudo apt install gccgo-go
go get github.com/tomnomnom/waybackurls
cp $HOME/go/bin/waybackurls /usr/local/bin/
