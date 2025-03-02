from setuptools import setup, find_packages

setup(
    name='learning_circuit',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        "scipy==1.12.0",
        "matplotlib==3.8.3",
        "tqdm==4.66.2",
        "networkx==3.2.1",
        "numba==0.59.0",
        "jax==0.4.25",
        "jaxlib==0.4.25",
        "cmocean==3.1.3",
        "poisson_disc==0.2.1",
        "vapory==0.1.2",
        "jupyter==1.0.0",
        "pandas==2.2.3",
        "sklearn==1.6.1",
    ],
    author='Marcelo Guzman',
    author_email='mguzmanj@sas.upenn.edu',
    description='Learning using linear circuits',
    url='https://github.com/adamgkline/learning_circuit'
)


# # To generate install_requires field
# f = open("requirements.txt")
# o = open("requirements_delimited.txt", "w")
# for l in f:
#     o.write('"' + l.strip() + '",\n')
