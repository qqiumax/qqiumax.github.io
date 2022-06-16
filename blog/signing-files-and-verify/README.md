# Signing your files and verifying.
## How do you make sure a file is sent from the correct person, and is not corrupted on its way to you? A digital signature needed, as I have talked in the [first blog](https://qqiumax.github.io/blog/what-is-gpg/) It can prove the sender and the message.
## **Showing everyone your keys -- send it to a keyserver**
## use <code>gpg --keyserver a-key-server-here --send-keys KEY-ID-HERE</code> to send to keyserver.
## subsitute a-key-server-here with one of the following, just copy the text, not the link: 
## 1. keys.openpgp.org <https://keys.openpgp.org/>
## 2. pgp.mit.edu <http://pgp.mit.edu/>
## 3. keyserver.ubuntu.com <https://keyserver.ubuntu.com/>
## Substitute KEY_ID_HERE with your key id
## **Troubleshoot: It you met any problem in sending the key, you can try their interface, just click on the links and follow the site's directions.**
## Then use <code>gpg --keysever keysever-you-just-wrote --recv-keys KEY_ID_HERE</code> To check status
## If it shows something like "successfully found key ..." you are done!

## **Signing files -detached signature**
## Use <code>gpg --detach-sign FILE_NAME_HERE</code> for a detached sign of the file, the .sig file is the detached signature file, send the original file **AND** the .sig file to the reciever.
## If you want human-readable signature, try <code>gpg --detach-sign -a FILE_NAME_HERE</code> The .asc file is a human-readable acsii encoded file. Same, send the .asc file **AND** the original file to 
## **Signing files -entached signature**
## Use <code>gpg --sign FILE_HERE</code> the .gpg file contains the message AND the signature.
## **Verifying a detached signature**
## Use <code>gpg --import File_Name_Contains_Public-Key</code> to import public key
## Use <code>gpg --verify "signature-file-here" "original-file-here"</code>
## If produces "Good signature from xxxxx, then message is not corrupted"
## Or else "bad signature from xxxx", then the message is CORRUPTED!
## **Verifying an entached signature**
## Use <code>gpg --import File_Name_Contains_Public-Key</code> to import public key
## For example, I recieved a code.txt.gpg, first create a file without the .gpg, in this example, code.txt.
## Use <code>gpg --output "without-gpg-filename" ".gpg-signed-file"</code>
## If it is a "good signature from xxx" the message is not corrupted
## Else, the message IS CORRUPTED
## If it is a good signature, open the file with name without .gpg, in this case, code.txt, then you can see the original message!
## You are done!
## *Next class we are going to learn encrypting and decrypting files! Get ready!*
[back](https://qqiumax.github.io/blog/) 


###### You may copy anything on the website, but you have to cite the author and give a link to this website. See [LICENSE](https://qqiumax.github.io/LICENSE) for more information. You HAVE to keep this message when copying or duplicating.

###### Copyright Max Qiu 2022. All Rights Reserved.