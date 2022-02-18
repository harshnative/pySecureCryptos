import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


from pySecureCryptos import version


setuptools.setup(
    name="pySecureCryptos", # Replace with your own username
    version=version.current_verison,
    author="Harsh Native",
    author_email="Harshnative@gmail.com",
    description="All the tools for cryptography / encryption for everything including databases , files , string , containers and another security methods like hashing and true random number generators in one place.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/harshnative/pySecureCryptos",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    install_requires=[
   'cryptography==35.0.0',
   'onetimepad==1.4',
   'pycryptodomex==3.11.0',
   'numpy==1.22.2'
    ],

    python_requires='>=3.8',
)