# Part05: License and .gitignore files
## In the first lesson we mentioned .gitignore files and LICENSE files, lets have a detailed look on it.
## **gitignore files**
## A .gitignore file is a file that tells git to "ignore" certain files when we use <code>git add . <code> For example, you have some hidden windows system files like "desktop.ini" in your repository, and you don't want them in you git repository, since it will be very messy. So you can put a line in the .gitignore file: 
## <code> *.ini </code>
## And git will always ignore the files that ends with a .ini suffix!
## **Creating .gitignore files**
## Since windows does not allow files with only suffixes, so how can we bypass the restriction? Use the git bash.
## Use the code in bash <code> touch .gitignore </code>
## And you are done, you can see the .gitignore file!
## **LICENSE files**
## License files are just simply legal restrictions of copying code on the repository, if you are doing an open-source, this is important, you can edit it via notepad and such.
## And you are all done!
## *Next class we are learning deleting and renaming files in git.*
### **[Comment here](https://qqiumax.github.io/comment/)**
[back](https://qqiumax.github.io/blog/)