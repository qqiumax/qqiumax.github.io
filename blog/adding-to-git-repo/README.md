# Part04: Adding things to github
## In the last few lessons, we have successfully learned about connecting to github and initializing a repository.
## Today we will be studying about adding things to your empty git repository.
## **branching to prepare for adding**
## The prerequisites of everything is opening git bash
## Use code in git bash 

    git branch "branch_name"
    git checkout "branch_name_you_just_entered_above"

## Therefore, you are ready to give changes to your repository

## **Creating a file or folder**
## To create a folder, use the code in git bash: <code>mkdir "folder_name"</code> be sure the "folder_name" does NOT contain spaces.
## To create a file, use the code in git bash: <code>touch "file_name"</code> make sure that the file_name does NOT contain spaces.

## **Adding the file to your repository**
## Use the following code, please ignore the things after the hashtag <code>#</code>

    git add "file_name you just creates" #Adds the file to git index
    git commit -m "a_message_or_note_you_have_for_the_change" #commits the file to storage
    git push origin main #Updates the remote repository

## If you have many files or complicated files to add, you can substitude the first line for <code>git add *</code>
## If you have a gpg key, substitude the second line for the code <code>git commit -S -m "a_message_or_note_you_have_for_the_change" #commits the file to storage, but signed</code> 

## **Checking the status of files**
## Use the code in git bash <code>git status</code> to see, if it says

    git status
    On branch main
    Your branch is up to date with 'origin/main'.
    nothing to commit, working tree clean

## You have successfully added a file to your repositroy, horray!

## Next lesson we are going to be talking about .gitignore files, which can help git to "ignore" some files you don't want to add.


[back](https://qqiumax.github.io/home/)



###### You may copy anything on the website, but you have to cite the author and give a link to this website. See [LICENSE](https://qqiumax.github.io/LICENSE) for more information. You HAVE to keep this message when copying or duplicating.

###### Copyright Max Qiu 2022. All Rights Reserved.