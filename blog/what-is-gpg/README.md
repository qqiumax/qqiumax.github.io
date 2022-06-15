# Part01: What is GPG?
## So, Here, let us begin our journey on GPG. You may have heard it in the firest series [here](https://qqiumax.github.io/blog/controlling-using-git/), but since the thing is optional, not many people chose this, but as I recently exprored this GPG in depth, I found it was amazing.
## Lets begin with the question What is GPG?
## GPG itself is actually a software, GnuPG, which we will download later. But actuallly refers more to the OpenPGP protocle, a re-written, open source, not license form of PGP(Pretty Good Privacy). The protacol can be used for both  signing and encrypting, which we will explore them together one by one. Itself is an asymetrical encryption, which is like this: 
## An asymmetrical signature has not only one key, for they use the same key for both encrypting and decrypting, they have one **pair** of keys. One key is private, you **DO NOT** want to share with anyone. Another one is a public key, which in GPG case, you want to share with EVERYONE. Both keys are bound by complicated mathmatical relationships, and private keys can give birth to public keys, while **NOT** vice versa.The Private key can **ONLY** be used for signing and decrypting, while the public key can **ONLY** encrypt and verify signatures.
## Now, lets dive into gpg
## GPG has even more keys, so there is a pair of "Primary key" and one or more"subkeys" Generally, a key could have CSAE 4 characteristic. Each for Certification, Signing, Authenticaiton, and Encryption. Certification can only put on a primary key, and encryption only on a subkey. Generally, we do not use GPG for authentication, we rather use SSH keys. And usually a keyring(one whole gpg key) primary key has both C and S, while there is another subkey having character E. 
## Lets continue about its signature and encryption, lets start with encryption.
## So here is a message Bob want to send to you friend, Alice, he first retrieves the public key of Alice, and use it to encrypt the message. Since the public key cannot decrypt the message, thus, nobody is able to see the encrypted message, except for Alice, who has the private key, uses her subkey having the E characteristic, for decryption.
## Let us continue about signing, which is a bit more complicated, the sender uses a hash(mathematical function that converts an input of arbitrary length into an encrypted output of a fixed length, theoretically, cannot be decrypted) function to hash a message. With his or her *Private* key, he or she encrypts the message, and attaches it to the original message. This process is called signing. The reciever decrypts the encrypted message and hashes the original message, if the result of decryption is same to the hashed original message, the sender is verified and message is not corrupted.
![image1](https://qqiumax.github.io/blog/what-is-gpg/sign.png)

## Web of Trust 
## Whenever you recieve a public key from another person, you wish to trust it either:
## 1. Ultimately(total trust, as same as I did it on my own)(usually we only use it on our own keys)
## 2. Fully(full trust, but not ultimate)(usually on friends and families)
## 3. marginal(somewhat trust)(a familiar person)
## 4. Never(do not trust it)(for unknown person)
## When you import a key from even me, you should name the key as never trust since we shouldn't be familiar, so build your ring of trust on the keys and manage it well! I will moreover elaborate on it more in the latter of the series!

## Now you have learned the basic concept of GPG, wait for my next blog about how to really use it!
[back](https://qqiumax.github.io/blog/)


###### You may copy anything on the website, but you have to cite the author and give a link to this website. See [LICENSE](https://qqiumax.github.io/LICENSE) for more information. You HAVE to keep this message when copying or duplicating.

###### Copyright 2022 Max Qiu All Rights Reserved.