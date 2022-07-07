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

- Install the pip packages with `pip install -r requirements.txt` or use the [run_tests](run_tests.sh) script
- Create a .env file in the *libs* folder. You can use the [env.template file](libs/.env.template) 
- Add the DotenvLibrary to your `*** Settings ***` section
- Use the Keyword `Set Env Var` with a list of keys you want to store in `%{ENVIRONMENT_VARIABLES}`


## Contibuting ##
- Contribution is allways welcome :) feel free to use and get in contact 
