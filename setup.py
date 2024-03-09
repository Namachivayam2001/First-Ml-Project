from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    requirements = []
    HIPAN_E_DOT = '-e .'

    with open(file_path) as fp:
        requirements = fp.readlines()
        requirements = [rqmnt.replace('\n', '') for rqmnt in requirements]

        if(HIPAN_E_DOT in requirements):
            requirements.remove(HIPAN_E_DOT)

    return requirements
        

setup(
    name = 'first-ml-project',
    version = '1.0.0',
    author = 'newton',
    author_email = 'newtonremo143@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)