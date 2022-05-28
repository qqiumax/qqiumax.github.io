# Part 03: Controlling blogs using Git
## At the end of [last class](https://qqiumax.github.io/blog/write-blog-using-markdown/) you should have installed git, let us learn about git to controll your website locally!

## **Downloading git**
## First install git [here](https://git-scm.com/downloads)and keep clicking next, but remember to change the default branch to "main" not master, read the directions on each page carefully until the finish installing page. Left click anywhere and it look like this:
![git](https://qqiumax.github.io/blog/write-blog-using-markdown/git.png)
## And you are done!

## **Initializing Git Config**
## 1. Open a folder, and left click, choose *Git Bash Here* until it opens a command bash.
## 2. tyoe or paste <code>git config --global user.name "your_github_username_here"</code> to set up your name
## 3. type or paste <code>git config --global user.email "your_github_email_here"</code> to set up your email for Git

## **Open SSH keygen**
## 1. type or paste <code>ssh-keygen -t rsa -b 4096 -C "your_github_email_here" to generate key
## 2. Follow the instructions in Git, or just press enter continuously
## 3. Navigate to c:\\users\ur-name\.ssh\id_rsa.pub, open file with notepad, and copy the whole thing in it
![image1](https://qqiumax.github.io/blog/controlling-using-git/gitkey01.png)
## 4. Open [Github](https://github.com) in yout browser, navigate to settings => SSH and GPG keys => new SSH key, and paste what you just copied. Should end with your email.
![image2](https://qqiumax.github.io/blog/controlling-using-git/gitkey02.png)
![image3](https://qqiumax.github.io/blog/controlling-using-git/gitkey03.png)
![image4](https://qqiumax.github.io/blog/controlling-using-git/gitkey04.png)
## And you are done with your keys!

## **Initialize your local repository**
## 1. Open browser and go to github, find your repository that holds your blog, navigate to "code" tab and copy according to image.
![image5](https://qqiumax.github.io/blog/controlling-using-git/init01.png)
## 2. Open git bash in a folder, type <code>git clone</code> and then paste the thing you just copied.

## **Upgrading blogs**
## **Wait for a few second, close the bash, and you are done!**

## If you added or modified, open git bash, type
    git add *
    git commit -m "a_small_note_you_want_to_leave"
    git push origin main


## And you are done, you can also use git status to check too.
## If you want to remove a file:
    git rm "file_path_you_removed"
    git commit -m "a_small_note_you_want_to_leave"
    git push origin main

## **Errors While Pushing**
## Use <code>git pull --rebase origin main</code> and then push.

## **(Optional) GPG Signature key**
## 1. Install the newest gpg signer for your system [here](https://www.gnupg.org/download/)
## 2.use <code>gpg --full-generate-key</code> in git bash.
## 3.press enter
## 4.press 4096
## 5.follow the directions
## 6.Make sure to write your sign-up email and username for github.
## 7.enter a secure password twice, following the directions.
## 8.enter <code>gpg --list-secret-keys --keyid-format=long</code>
## 9.copy the code in sec section after the / slash.
## 10.enter <code>gpg --armor --export "your_copied_code"</code>
## 11.copy the ----Begin ... part until the ---End.. part, inclusive.
## 12.Go to github => settings => ssh and gpg keys, add new GPG key, and paste it.
![image7](https://qqiumax.github.io/blog/controlling-using-git/gpg.png)
## 13. remember the code we copied before? enter <code>git config --global user.signingkey "your-code-here"</code>
## Whenever you want to sign a commit do <code>git commit -S -m "your message here"</code>
## And you are done!

## **Other Functions**
## [go here to see](https://git-scm.com/doc/)

## Use Git to controll your blog freely!
## Next class we are going to learn creating sub-directories!

[back](https://qqiumax.github.io/blog/)