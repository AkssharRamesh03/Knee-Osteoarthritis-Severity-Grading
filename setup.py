import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Knee-Osteoarthritis-Severity-Grading"
AUTHOR_USER_NAME = "AkssharRamesh03"
SRC_REPO = "deepLearningModel"
AUTHOR_EMAIL = "rmshakshar@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=" deep learning model that identifies and grade severity of knee osteoarthritis.",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)