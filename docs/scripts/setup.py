from setuptools import setup

setup(
    name='mypackage-name',
    version="0.1.0",
    description="Hello world de formation",
    scripts=[
        "hello-world.py"
    ],
    install_requires=[
        "flask",
        "requests==2.24.0"
    ],
    author='Eugene Rodolphe',
    author_email="rodolphemazamda@gmail.com",
    python_requires='>=3.7',
)

