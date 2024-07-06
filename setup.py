from setuptools import setup,find_packages
from typing import List
PROJECT_NAME="Housing-predictor"
VERSION="0.0.1"
AUTHOR="SURAJ"
DESCRIPTION="THis a my first END to ENd project"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if "-e ." in requirement_list:
            requirement_list.remove("-e .")
        return requirement_list
    
setup(name=PROJECT_NAME,
      version=VERSION,
      author=AUTHOR,
      description=DESCRIPTION,
      packages=find_packages(),
      install_requires=get_requirements_list())

