#setup.py

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sagittarius-brugalada", # Replace with your own username
    version="0.0.1",
    author="Pau Ramos",
    author_email="p.ramos@unistra.fr",
    description="Empiric interpolators for the properties (distance and proper motions) of the Sagittarius stream.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brugalada/Sagittarius",
    packages=setuptools.find_packages(),
    install_requires=[ 'numpy', 'scipy' ],
    package_data={'': ['LICENSE', 'MANIFEST.in','tutorials/*.ipynb'],
            'interpolators': ['pickles/*.pkl']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)