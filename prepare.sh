#!/bin/sh
sudo apt update
sudo apt install wget unzip python3 python3-pip -y
pip3 install -U selenium pytest click
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb -y
wget https://chromedriver.storage.googleapis.com/85.0.4183.87/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
rm chromedriver_linux64.zip
sudo cp chromedriver /usr/local/bin/
