# Part01: What is Git, Install, and Config
## So, here is Git, but what actually IS git?
## **Git definition**
## Git is an amzing code-management system. It is much better than other managements systems because of:
## 1. It CAN be decentralized, with proper workflow system.
## 2. It records ALL history of whole repository, but size is almost as same as others who do not save histories. AND you can reset code to ANY other time in history.
## 3. EVERYONE has an backup of the main repository, making the code strong.
## 4. It has lightweight branches and tags. 
## **Git concepts**
## So here is the basic concepts of git. There are 4 places: The workplace, the index, local repository, and remote repository.
## The workplace is what you see locally.
## The index is a staging (cached) area for your works, you can stage things here to wait for commiting.
## The repository is a database of your history and now commits.
## The remote repository is a published version of the local repository.
![image01](https://qqiumax.github.io/blog/what-is-git/git01.jpg)
![image02](https://qqiumax.github.io/blog/what-is-git/git02.jpg)
## **Explore: The local repository**
## There could many branches of a local repository, but how just changing the branch changes the whole working directory?
## The answer is: HEAD. An repository stores snapshots of your codes, and name each branch with a HEAD.
## When you are changing the branch, the HEAD changes, displaying a different snapshot, which changes the repository!
![image03](https://qqiumax.github.io/blog/what-is-git/git03.png)
## **Installing Git** 
## Now you have learnt the basics of git! Now lets install the program!
## 1. Go to <https://git-scm.com/> and download the package for your operating system.
## 2. execute the downloaded installer
## 3. Just keep clicking next, use the default options.
## 4. Wait for it to finish
## 5. And you are ok!
## **Configuring Git**
## prerequisites: a username on github & a validated email on github.
## Optional : a github validated gpg key
## 1. use <code>git config --global init.defaultBranch main</code> to set branch
## 2. use <code>git config --global user.name "your-github-username-here"</code> to set username
## 3. use <code>git config --global user.email "your-github-email-here"</code> to set email.
## 4.(optional) use <code>git config --user.signingkey "key-id-here"</code> to set gpg key.
## And you are done
## Next class we are going to learn connecting git(local repository) with github (remote repository)!
[back](https://qqiumax.github.io/blog/)


###### You may copy anything on the website, but you have to cite the author and give a link to this website. See [LICENSE](https://qqiumax.github.io/LICENSE) for more information. You HAVE to keep this message when copying or duplicating.

###### Copyright 2022 Max Qiu All Rights Reserved.