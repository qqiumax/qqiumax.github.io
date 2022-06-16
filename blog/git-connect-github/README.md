# Part02: Connecting Git with Github
## **What is github**
## You have many times heard me talking about Github, but what IS github actually? Github is actually a bunch of free remote repositories and you can push your local repository there.
## **Connecting to Github by SSH(reccommanded)**
## Github uses SSH access, thus you need to generate a SSH key.
## 1. open git bash, and type or paste <code>ssh-keygen -t rsa -b 4096 -C "your_email@example.com"</code>
## 2. press enter to accept the  default path
## 3. type your wanted passphrase twice, but you can simply enter to avoid passwords
## 4. type <code>eval "$(ssh-agent -s)"</code> and then <code>ssh-add ~/.ssh/id_rsa</code> to add to ssh-agent
## type <code>cd ~/.ssh/</code> and then <code>cat id_rsa</code>, copy the output message, starts with ----start OPENSSh... and end with ----end OPENSSH ...
## open github => account settings=> GPG and SSH keys => new SSH key
## Name the key "main" and paste the key in the textbox below. Click save.
## Use <code>ssh -T git@github.com</code> and type *yes* if you see a warning. If you see Hi! .... shell access. You are ok!
## **Connecting with https(not reccommanded)**
## 1. Go to github => account settings => developer tools => personal access token => and generate new token, copy the code and store it in a SECURE place. When you connect later as we learn, you have to use this code EVERY TIME. Which, is not reccommanded over SSH as you just need a passphrase.
## And you are done! Get ready to put your hands on git next class!
[back](https://qqiumax.github.io/blog/)

###### You may copy anything on the website, but you have to cite the author and give a link to this website. See [LICENSE](https://qqiumax.github.io/LICENSE) for more information. You HAVE to keep this message when copying or duplicating.

###### Copyright Max Qiu 2022. All Rights Reserved.