from gettext import install
from importlib.metadata import entry_points
from setuptools import setup, find_packages

install_requires = [
    'arrow==0.16.0',
    'python-decouple==3.3',
    'furl==2.1.0',
    'python-dotenv==0.14.0',
    'requests==2.24.0',
    'marshmallow==3.7.1',    
    'azure-keyvault==4.1.0',
    'azure-keyvault-secrets==4.2.0',
    'azure-identity==1.4.0',
    'azure-mgmt-authorization==0.60.0',
    'azure-mgmt-resource==10.2.0',
    'azure-mgmt-compute==13.0.0',
    'azure-storage-queue==12.1.2',
    'azure-cosmosdb-table==1.0.6',
]

with open('README.md') as fp:
    long_description = fp.read()

setup(
    name='lms-it-lib',
    version="0.0.1",
    description="Librairies pour la consommation des services Azure",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
    author='Eugene Rodolphe MAZAMDA TANGUEU',
    author_email="rodolphemazamda@gmail.com",
    python_requires='>=3.7',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
        'console_scripts': [
            'az-update-providers = lms_shared_lib.update_azure_providers:main'
        ]
    }
)