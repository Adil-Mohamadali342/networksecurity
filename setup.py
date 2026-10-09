from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines()]

    requirements = [
        req for req in requirements
        if req and not req.startswith('#') and req != HYPEN_E_DOT
    ]
    return requirements

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Adil',
    author_email='master.adil06@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)