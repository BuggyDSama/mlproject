from setuptools import find_packages,setup
from typing import List

Hypen_E_dot = '-e .'

def get_requirement(file_path:str) -> List[str]:
    '''
    this fucntion will return the list of requirements
    '''
    reruirement=[]
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("\n","") for req in requirement] 

        if Hypen_E_dot in requirement:
            requirement.remove(Hypen_E_dot)
    
    return requirement


setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Vaibhavy',
    author_email = 'vaibhavysai@gmail.com',
    packages = find_packages(),
    install_requires = get_requirement('requirement.txt')

)