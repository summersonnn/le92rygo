from distutils.core import setup
from setuptools import find_packages
setup(name='le92rygo',
version='0.1',
author='Kubilay Yazoglu',
author_email='kubilay.ky.yazoglu@fau.de',
packages=find_packages(),
install_requires=['numpy', 'Pillow', 'ipywidgets'])