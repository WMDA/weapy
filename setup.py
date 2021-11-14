from setuptools import setup, find_packages

def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()

VERSION = '0.0.1' 
DESCRIPTION = 'WeaPy'
LONG_DESCRIPTION = 'Enumerate and scrap websites for CTFs/ethical Hacking'
REQUIREMENTS = read_requirements("requirements.txt")

# Setting up
setup(  
    name="WeaPY", 
    version=VERSION,
    author="WMDA (aka DAniel Halls)",
    author_email="p3dh0001@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=REQUIREMENTS, 
    classifiers= [
            "Development Status :: Alpha",
            "Intended Audience :: Education/CTFs/Ethical Hacking",
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ]
)