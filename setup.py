from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Movies Recommender System"
AUTHOR_USER_NAME = "Junaid Ali"
SRC_REPO = "Movie-Recommender-System"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="JunaidARahat",
    description="A small local packages for ML based movies recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JunaidARahat/Movie-Recommender-System",
    author_email="mjunaidrahat1990@gmail.com",
    packages=find_packages(),
    license="MIT", 
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
     )

 