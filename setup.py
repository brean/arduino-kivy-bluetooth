from setuptools import setup, find_packages

setup(
    name="blinking",
    version="0.0.1",
    author="wemakesoftware.com",
    author_email="a.bresser@greyrook.com",
    description="arduino control software using kivy and firmata",
    install_requires=['pyfirmata', 'pybluez', 'kivy'],
    zip_save=False,
    packages=find_packages(),
    dependency_links=[
        "https://bitbucket.org/tino/pyfirmata/get/0.9.4.tar.gz#egg=pyfirmata"
    ]
)
