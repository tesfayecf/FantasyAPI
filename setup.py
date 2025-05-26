from setuptools import setup, find_packages

setup(
    name="FantasyAPI",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy==1.26.0",
        "scipy==1.11.3",
        "requests==2.32.3",
    ],  # Add dependencies here if needed
)
