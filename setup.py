import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='ipysettings',
    version='0.0.1',
    author='Enno Luebbers',
    author_email='ennol@xilinx.com',
    description='Settings container class with ipywidget support',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitenterprise.xilinx.com/ennol/ipysettings',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD3 License',
        'Operating System :: OS Independent',
    ],
)
