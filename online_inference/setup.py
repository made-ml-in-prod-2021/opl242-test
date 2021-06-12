from setuptools import find_packages, setup


with open("requirements.txt", "r", encoding="utf-8") as req_file:
    reqs = list(map(str.strip, req_file.readlines()))


setup(
    name='online_inference',
    description='Service for online star class prediction',
    version='0.2.0',
    url="https://github.com/made-ml-in-prod-2021/opl242-test",
    author='Alexey Opolchenov',
    author_email="None",
    license='MIT',
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=reqs
)