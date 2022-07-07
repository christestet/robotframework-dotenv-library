*** Settings ***
Library     ../libs/DotenvLibrary.py
Library     OperatingSystem


*** Variables ***
@{env_list}=    KEY_1 KEY_2


*** Test Cases ***
Test Set Env
    DotenvLibrary.Set Env Var    @{env_list}
    ${env_value_1}=    Get Environment Variable    KEY_1
    Should Not Be Empty    ${env_value_1}
    Should Be Equal As Strings    ${env_value_1}    Hello
    Should Be Equal As Strings    ${env_value_1}    %{KEY_1}
    ${env_value_2}=    Get Environment Variable    KEY_2
    Should Not Be Empty    ${env_value_2}
    Should Be Equal As Strings    ${env_value_2}    World
    Should Be Equal As Strings    ${env_value_2}    %{KEY_2}