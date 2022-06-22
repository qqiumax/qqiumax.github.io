# Part 06: Update your remote repository.
## You have learned most of the Git now, and you can literally do almost everything locally, but have you ever thought, how to update your things on Github?
## The best way is to use the "Push" method.
## **Using the Push method**
## Follow us through the code here:
## <code>git push origin main</code>
## It will ask you the passphrase, if you had one, and a few seconds later, github will quickly update!
## **Use Pull or Fetch method to avoid differences**
## Sometimes it will say: Failed to push some refs to origin/main
## What shall we do now?
## You can use the code:

    git fetch origin main
    git merge origin/main

## You can also use
## <code>git pull origin main</code>

## If nothing is wrong, then you are done! You can now <code>git push origin main</code> again!
## **Use diff method to solve differences if failed to pull or merge**
## Use the code:

    git fetch origin main
    git diff main origin/main

## After you see the differences, you can solve the problem by changing the files manually
## And finally use <code>git merge origin/main</code> again!
## If nothing is wrong, then you are done! You can now <code>git push origin main</code> again!
## **Using --force option to force update**
## THIS IS VERY DANGEROUS AND IS NOT RECOMMANDED
## If you want to force an update and not care about everything, use the code:
## <code>git push --force origin main</code>
## And you are done, this REWRITES EVERYTHING on the remote repository.
## *Next class is the finale and is about tagging!*
## **[Comment Here](https://qqiumax.github.io/comment)**
[back](https://qqiumax.github.io/blog/) 