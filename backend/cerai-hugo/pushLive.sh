#!/bin/bash

: '
Script to pull changes, build HTML and update RBCDSAI Website

Command usage:
	./pushLive.sh -p "<commit message>"
	Arguments:
		-p (optional): Provide this flag and commit message if you want to push the changes to our GitHub repo
'

git remote set-url origin https://github.com/RBC-DSAI-IITM/crai-hugo.git

echo "Pulling latest main branch from GitHub"
git pull origin main

echo "------------------------------"
~/Hugo/hugo -F

echo "------------------------------"
echo "Do you want to view site on localhost? [Y/n]"
read input

if [[ $input == "Y" || $input == "y" ]]; then
	hugo server -DF
fi
echo "------------------------------"

# if push argument is given, commit and push to GitHub
while [[ $# -gt 0 ]];
do
	case $1 in
		-p|--push) # push to git
			
			git add -v .
			git commit -m "$2"
			git push origin main
			break;
	esac
done

echo "------------------------------"
echo "Pushing website to server.."
scp -r public/* administrator@10.24.8.94:/var/www/html/

if [ $? -eq 0 ]; then
	echo "******************************"
	echo "Push complete. Latest changes live on https://cerai.iitm.ac.in/"
	echo "******************************"
	exit 1
else
	echo "Server connection failed."
	echo "Please check if system is connected to IITM server."
fi
