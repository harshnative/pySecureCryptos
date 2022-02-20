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







# Installation - 

```bash
pip install pySecureCryptos
```

or from tar.gz

```bash
pip install *tar.gz
```

1. [version 0.40](https://www.letscodeofficial.com/media/fileSharer/pySecureCryptos-0.4.tar.gz) 
2. [version 0.43](https://www.letscodeofficial.com/media/fileSharer/pySecureCryptos-0.43.tar.gz)
3. [version 0.44](https://pypi.org/project/pySecureCryptos/0.44/#files)
4. [version 0.46](https://pypi.org/project/pySecureCryptos/0.46/#files)
5. [version 0.47](https://pypi.org/project/pySecureCryptos/0.47/#files)


check out the change log [here](https://www.letscodeofficial.com/documentations/pySecureCryptos%20change%20logs#/)

<br>
<br>


### Warnings - 

1. This module does not provide any garantee for perfect unbreakable security. Nothing is secure in the world of computer. But this modules makes its best to provide encryption system and is circulated as good will.
2. Do not use OTP generator for version 0.43 , use 0.44 or above. 0.43 had empty otp bug but it has been fixed in version 0.44.
3. RandomWrapper EpollSelector bug as been fixed in version 0.46.
4. Numpy installation required for version 0.43 and 0.44.



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


14. [Random Wrapper](https://www.letscodeofficial.com/documentations/pySecureCryptos%20Random%20Wrapper#/)

Wrapper containing many methods to generate random things from integers to strings. It even has its own True Random Generator from mouse movements.



<br>
<br>


15. [AES Wrapper](https://www.letscodeofficial.com/documentations/pySecureCryptos%20AES%20Wrapper#/)

Wrapper Encryptions methods using AES encryption algo.

#### Recommended symmetric algo for most use cases.


<br>
<br>


16. [Fernet + AES Wrapper](https://www.letscodeofficial.com/documentations/pySecureCryptos%20Fernet%20+%20AES%20Wrapper#/)

Wrapper Encryptions methods using fernet + AES encryption algo.

<br>
<br>
<br>
<br>
<br>
<br>
<br>





# Issues - 

Raise Issues at github - https://github.com/harshnative/pySecureCryptos





<br>
<br>
<br>
<br>
<br>
<br>
<br>









# Version Specfic Readme - 

At github - https://github.com/harshnative/pySecureCryptos/tree/master/documentations/version_specific





<br>
<br>
<br>
<br>
<br>
<br>
<br>






# Sponsors
<a href="https://www.letscodeofficial.com/"><img src="https://www.letscodeofficial.com/static/images/favicon.ico" width="150" height="150" /><h3>Lets Code Official</h3></a>


</br>
</br>
</br>


# Contributors

<a href="https://github.com/harshnative/"><img src="https://www.letscodeofficial.com/static/images/jarvis/HarshNativeProfile.JPG" width="150" height="150" /><h3>Harsh Native</h3></a>


</br>
</br>
</br>
</br>
</br>