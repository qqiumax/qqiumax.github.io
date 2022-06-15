# Signing commits and tags
## So in the last series we learnt git in [lesson 3](https://qqiumax.github.io/blog/controlling-using-git/) about commiting, today I will introduce tagging and how to sign commits and tags
## So, **What is a tag**
## A normal tag is an clarification of different branches, versions, etc, while a annotated tag or a signed tag can store every single file in a repository, like a retore point, or a timestamp.
## Now, let's move on to commits
## **How to sign a commit**
## 1. open git bash
## 2. type or paste: <code>git commit -a -S -m "your commit message"</code>
## 3. enter the password and push it to Github
## 4. and you are done!
## 5. Now there is a verified in your commits section!
![verified](https://qqiumax.github.io/blog/signing-commits-and-tags/verified.png)

## **Creating a signed tag!**
## 1. Open git bash
## 2. type <code>git tag -s your_tag_name_here</code> to create tag
## 3. type <code>git tag -v your_tag_name_here</code> to verify your signed tag and store it
## 4. use <code>git tag</code> to see your new tag!
## Note: If you want to go back to the tag restore point, use 

    git checkout substitute_tag_name_here
    git commit -a -S -m "commit_message_here"
    git push origin main

## And you are done
## Next class we are going to learn how to sign and verify files.
## Get ready!
[back](https://qqiumax.github.io/blog/)


###### You may copy anything on the website, but you have to cite the author and give a link to this website. See [LICENSE](https://qqiumax.github.io/LICENSE) for more information. You HAVE to keep this message when copying or duplicating.

###### Copyright 2022 Max Qiu All Rights Reserved.