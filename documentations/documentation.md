# py Secure Cryptos

All the tools for cryptography / encryption for everything including databases , files , string , containers and another security methods like hashing and true random number generators in one place.

<br>
<br>
<br>
<br>
<br>


# Goal

Although the python as many inbuilt modules like onetimpad , crytography , pycryptodom etc which are all great crytography modules but you need to still write a lot of boiler plate code to get the best out of them. This module combines the power of all to encrypt all types of data like strings, bytes , files etc with just few lines of code with further improving the security by adding additional salting.


<br>
<br>
<br>
<br>
<br>

# Features

1. [Shuffler - shuffle and unshuffle things based on a seed](https://www.letscodeofficial.com/documentations/pySecureCryptos%20shuffler#/)

used to jumble things up so that they are hard to read in correct order , used in most encryption algo's in this module.

<br>
<br>

2. [Encoder Decoder - encode and decode strings and bytes](https://www.letscodeofficial.com/documentations/pySecureCryptos%20encoderDecoders#/)

used to convert byte into strings and vice versa and string into byte and vice versa

<br>
<br>


3. [Fernet Wrapper - encrypt and decrypt strings and bytes using fernet](https://www.letscodeofficial.com/documentations/pySecureCryptos%20fernetWrapper#/)

you can encrypt and decrypt any string or byte with just a password. there are also generator function for tracking progress on large encryption and decryptions. Better for large byte datatypes than onetimepad.

<br>
<br>


4. [Onetimepad Wrapper - encrypt and decrypt strings and bytes using onetimepad](https://www.letscodeofficial.com/documentations/pySecureCryptos%20onetimepadWrapper#/)

you can encrypt and decrypt any string or byte with just a password. there are also generator function for tracking progress on large encryption and decryptions.

<br>
<br>


5. [Verifier Fernet Wrapper - encrypt and decrypt strings and bytes using fernet](https://www.letscodeofficial.com/documentations/pySecureCryptos%20Verifier%20fernetWrapper#/)

Same has fernet wrapper , but also adds a encrypted checksum to verify the data integrity 

<br>
<br>

6. [Verifier Onetimepad Wrapper - encrypt and decrypt strings and bytes using onetimepad](https://www.letscodeofficial.com/documentations/pySecureCryptos%20Verifier%20onetimepadWrapper#/)

Same has onetimepad wrapper , but also adds a encrypted checksum to verify the data integrity

<br>
<br>



7. [Password Checker - check if you password is secure enough](https://www.letscodeofficial.com/documentations/pySecureCryptos%20passwordChecker#/)

Has different qualifications for password , low , medium , high and max level security.

For sensitive applications , make sure your password qualifies for at least high level security.

<br>
<br>

8. [Hashers - Securely verify documents and passwords](https://www.letscodeofficial.com/documentations/pySecureCryptos%20hashers)

contains modified SHA256 , SHA384 , SHA512 algo's

<br>
<br>



9. [rsa Wrapper - encrypt and decrypt strings and bytes](https://www.letscodeofficial.com/documentations/pySecureCryptos%20rsaWrapper#/)

#### Recommended asymmetric algo for most use cases.

<br>
<br>




10. [Verifier Fernet Wrapper version 2 - encrypt and decrypt strings and bytes using fernet](https://www.letscodeofficial.com/documentations/pySecureCryptos%20Verifier%20fernetWrapper%20v2#/)

faster version of Verifier Fernet Wrapper.

#### Recommended symmetric algo for most use cases.

<br>
<br>



11. [Verifier Fernet Wrapper version 2.2 - encrypt and decrypt strings and bytes using fernet](https://www.letscodeofficial.com/documentations/pySecureCryptos%20Verifier%20fernetWrapper%20v2.2#/)

faster version of Verifier Fernet Wrapper but with less compatability across.

<br>
<br>



12. [Hashers 2.2 - Securely verify documents and passwords](https://www.letscodeofficial.com/documentations/pySecureCryptos%20hashers%20v2)

contains modified SHA256 , SHA384 , SHA512 algo's. Much faster than hashers version 1 but is comparitively less secure.

<br>
<br>


13. [Verifier Fernet Wrapper version 3 - encrypt and decrypt strings and bytes using fernet](https://www.letscodeofficial.com/documentations/pySecureCryptos%20Verifier%20fernetWrapper%20v3#/)

Fastest version of Verifier Fernet Wrapper making use of multiple cores of CPU.

<br>
<br>
<br>
<br>
<br>
<br>
<br>

