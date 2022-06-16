# Installing and Generating GPG keys
## **installing gpg tool for your system**
## 1. use <code>git clone git@github.com:qqiumax/qqiumax.github.io.git</code> to clone my repository for installing, or you can install on gnupg's official site, but might be slower
## 2. If you cloned my repository, delete the .git file and then unzip the zip file. You should be able to find the installing program suitable for your operating system.
## 3. Follow the program's directions and you are done!
## 1. Open Git Bash or terminal or cmd or any command line for your system.
## 2. use <code>gpg --full-generate-key</code> You **MUST** use RSA for first prompt(first option)
## 3. Enter 4096
## 4.Enter the length of time the key should be valid. Press Enter to specify the default selection, indicating that the key doesn't expire.
## 5. Verify that your selections are correct.
## 6. Enter your user ID information.
## Note: When asked to enter your email address, ensure that you enter the verified email address for your GitHub account. 
## 7. Type a secure passphrase.
## 8. Use the gpg --list-secret-keys --keyid-format=long command to list the long form of the GPG keys for which you have both a public and private key. A private key is required for signing commits or tags.<code>gpg --list-secret-keys --keyid-format=long</code>
## If error: use <code>git config --global gpg.program gpg2 </code>
## From the list of GPG keys, copy the long form of the GPG key ID you'd like to use. In this example, the GPG key ID is 3AA5C34371567BD2:

    $ gpg --list-secret-keys --keyid-format=long
    /Users/Administrator/.gnupg/secring.gpg
    ------------------------------------
    sec   4096R/3AA5C34371567BD2 2022/6/6
    uid                          Hubot 
    ssb   4096R/42B317FD4BA89E7A 2022/6/6

## 9. use <code>gpg --armor --export "GPG-Key-ID-you-just-copied" > key.txt</code>
## 10. Open the key.txt and go to Github=> settings => SSH and GPG keys => add new gpg key, and paste the whole thing in your key.txt to the box!
## 11. You are done!
## **tell git your signing key**
## Use <code>git config --global user.signingkey "your-Key-ID"</code>
## **Generating revocation certificates in case of leaking**
## Use <code>gpg --output revoke.asc --gen-revoke key-ID-here</code>
## Type 0 and type ctrl-Z for windows
## Safely store the revoke.asc in a safe place.
## You are done!
## Next class we are going to learn sending your keys to a keyserver! Get ready!
### **[Comment here](https://qqiumax.github.io/comment/)**
[back](https://qqiumax.github.io/blog/)



###### You may copy anything on the website, but you have to cite the author and give a link to this website. See [LICENSE](https://qqiumax.github.io/LICENSE) for more information. You HAVE to keep this message when copying or duplicating.

###### Copyright Max Qiu 2022. All Rights Reserved.