# robotframework-dotenv-library #
Use .env files in your [Robotframework](https://robotframework.org) tests
This is a wrapper Library to python-dotenv for dynamic environment setting in Robotframework

## Why using dotenv? ##
- You don´t need to set environment Variables before test Execution
- You don´t need additional cli robot options like `--variable`

## Roadmap ##
- Create pip package installation to use  `pip install robotframework-dotenvlibrary`
- Add functionality to store secrets safe

## Requirements ##
This Library uses the following dependencies:

- [python-doten](https://pypi.org/project/python-dotenv/) at Version 0.20.0

## Getting started ##

- Install package with `pip install -e .`
- Create a .env file
- Add the DotenvLibrary to your `*** Settings ***` section
- Use the Keyword `Load Dotenv`
- Read the [Library Documentation](https://christestet.github.io/robotframework-dotenv-library/) for futher details


## Contibuting ##
- Contribution is allways welcome :) feel free to use and get in contact
