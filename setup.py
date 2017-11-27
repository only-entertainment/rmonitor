from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the requirements from the requirements file
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    install_requires = [line.strip() for line in f.readlines()]
    print('Requirements.txt: %s\r\n' % install_requires)


setup(
    name="rmonitor",
    version="0.0.1",
    description="",
    url="",
    long_description="",
    author="krisneuharth",
    author_email="kris.neuharth@gmail.com",
    maintainer="kris.neuharth@gmail.com",
    maintainer_email="kris.neuharth@gmail.com",
    license="Other/Proprietary",
    packages=find_packages(exclude=("tests",)),
    install_requires=install_requires,
    test_suite="nose.collector",
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Utility",
        "License :: Other/Proprietary License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5"
        "Topic :: Software Development",
    ],
)
