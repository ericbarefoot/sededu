from setuptools import setup
from sededu

setup(
    name='SedEdu',
    version='1.0.2',
    author='Andrew J. Moodie other contributors',
    author_email='amoodie@rice.edu',
    packages=['sededu'],
    url='https://github.com/amoodie/sededu',
    license='LICENSE.txt',
    description='sediment-related educational activity suite',
    long_description=open('README.md').read(),
	install_requires=[
		'scipy',
        'numpy',
		'matplotlib',
        'shapely',
        'pygame']
)
