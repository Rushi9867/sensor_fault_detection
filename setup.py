from setuptools import find_packages,setup
from typing import List

REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]

    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    """
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list


setup(
    name="sensor",
    version="0.0.1",
    author="Rushikesh",
    author_email="rushikhandare2203@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements() #["pymongo==4.2.0"],
)

