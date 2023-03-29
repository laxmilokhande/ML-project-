from setuptools import setup,find_packages
HYPEN_E_DOT = '-e.'

def get_requirement(file_path):
    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("\n", "") for req in requirement]

        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)

setup(
    name= "ML project",
    version= "0.0.1",
    author= "laxmi",
    author_email= "laxmilokhande806@gmail.com",
    packages=find_packages(),
    install_requires = get_requirement('requirement.txt')
)