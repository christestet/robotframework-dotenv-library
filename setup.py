import setuptools

setuptools.setup(
    name="RobotDotenv",
    packages=setuptools.find_packages(),
    version="0.1.0",
    description="Robot Wrapper Library for python-dotenv",
    author="Christoph Kempe",
    url="https://github.com/christestet/robotframework-dotenv-library",
    python_requires=">=3.6",
    install_requires=["robotframework", "python-dotenv"],
)
