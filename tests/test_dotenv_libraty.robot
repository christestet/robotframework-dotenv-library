*** Settings ***
Library     RobotDotenv.DotenvLibrary
Library     OperatingSystem


*** Test Cases ***
Test Set Env
    Load Dotenv  tests/.env
    Should Not Be Empty    %{FIRST=None}
    Should Be Equal As Strings    %{FIRST=None}    1
    Load Dotenv  tests/.env.1
    Should Not Be Empty    %{SECOND=None}
    Should Not Be Empty    %{THIRD=None}
    Should Be Equal As Strings    %{SECOND=None}    2
    Should Be Equal As Strings    %{THIRD=None}    3
