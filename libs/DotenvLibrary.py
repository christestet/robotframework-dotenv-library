import os
from dotenv import load_dotenv
from robot.libraries import OperatingSystem as robot_os
from robot.api.deco import library
#########
# Maintainer: Christoph Kempe - https://github.com/christestet
# Creation Date: 07.07.2022 
########
@library(scope='GLOBAL', auto_keywords=True)
class DotenvLibrary:
    """
        == Description ==
        loads the .env file to use these environment variables in robotframework at runtime
    """
    __version__ = "0.0.1"
    ROBOT_LIBRARY_VERSION = __version__

    def set_env_var(self, env_list):
        r"""Sets the Environment variables form .env file to use them in robotframework tests
            For using `%{env}` in tests out of a `.env` file

        == Args ==
            env_list (list): list of keys from .env file

        == Keyword ==
            `Set Env Var`  @{env_var_list}

        == Examples ==
            Given is a `.env` file with: KEY1="VALUE1"

            "Variables" Section: 

            - @{env_var_list}=  KEY1

            "Test Cases" Section:

            - Set Env Var  @{env_var_list}

            Now the environment variable `%{KEY1}` can be used in tests

        """
        load_dotenv()
        for env in env_list:
            robot_os.set_env_var(env, os.getenv(env))