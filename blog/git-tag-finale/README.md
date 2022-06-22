# Finale: Tagging in Git
## Have you every wondered, how to set a reset point, so that you can retrieve your files, even if you have updated many times, this is what git tagging is about, there are 3 types of tags, lightweight, annotated, and signed. Lets see how each works.
## **Lightweight tags**
## These are like commit messages, are only messages, and does not contain files.
##  use the code <code>git tag tag_name</code> and you are done!
## **Annotated tags**
## These are the most important type of tag. It contains both the message and EVERY SINGLE FILE at the tagging moment!
## Use the code <code>git tag -a tag_name -m "tag message"</code> to create this type of tag.
## **Signed tags**
## Those are just gpg-signed annotated tags.
## Use the code <code> git tag -s tag_name -m "tag message" </code>  and then <code>git tag -v tag_name</code>to create the tags.
## **Pushing the tag to remote repository**
## Update the tag to a remote repository using this code:
## <code>git push origin main --tags</code>
## **Restoring files from tags**
## To restore from the tag, use <code>git checkout tag_name</code> you can have experimental changes, but no commits are allowed. To be able to have changes, use:

    git checkout tag_name -b branch_name
    git checkout main
    git reset --hard branch_name

## And you are all done!
## *This is the finale and you should have learned all the basic of git. I will have another new advanced series later!*
### **[Comment here](https://qqiumax.github.io/comment/)**
[back](https://qqiumax.github.io/blog/)