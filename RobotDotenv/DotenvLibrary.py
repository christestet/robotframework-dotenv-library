import dotenv
from robot.libraries import OperatingSystem as robot_os
from robot.api.deco import library


@library(scope="GLOBAL", auto_keywords=True)
class DotenvLibrary:
    """
    == Description ==
    loads the .env file to use these environment variables in robotframework at runtime
    """

    __version__ = "0.1.0"
    ROBOT_LIBRARY_VERSION = __version__

    def load_dotenv(self, dotenv_path=None):
        r"""Sets the Environment variables form .env file to use them in robotframework tests
            For using `%{env}` in tests out of a `.env` file

        == Args ==
            dotenv_path (str): path to dotenv file (default: .env)

        == Keyword ==
            `Load Dotenv`

        == Examples ==

            - Load Dotenv
            - Load Dotenv  .env.testing
            - Load Dotenv  dotenv_path=.env.production

        """
        for key, value in dotenv.dotenv_values(dotenv_path).items():
            robot_os.set_env_var(key, value)
