#!/bin/bash
# requirements installation

chmod +x enum4loser.py
pip install -r requirements.txt
git clone https://github.com/aboul3la/Sublist3r.git
cd Sublist3r/ ;pip install -r requirements.txt;cp -r subbrute /usr/local/bin/ ; cp sublist3r.py /usr/local/bin/ ; cd ../ ; rm -rf Sublist3r/

apt-get install -y golang-go
apt-get install -y gccgo-go
go get github.com/tomnomnom/waybackurls
cp $HOME/go/bin/waybackurls /usr/local/bin/
