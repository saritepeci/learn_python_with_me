*** Settings ***
Documentation    Acceptance tests for the Python learning guide.
...              Run from the project root:
...                  python -m robot tests/robot/guide.robot
Library          PyGuideLibrary.py    WITH NAME    Guide
Library          BuiltIn


*** Test Cases ***

Deposit Increases Account Balance
    [Documentation]    Basic deposit flow — the most fundamental bank operation.
    ${account}=    Guide.Create Bank Account    Alice    100.0
    ${balance}=    Guide.Deposit To Account    ${account}    50.0
    Should Be Equal As Numbers    ${balance}    150.0

Withdrawal Decreases Account Balance
    ${account}=    Guide.Create Bank Account    Bob    200.0
    ${balance}=    Guide.Withdraw From Account    ${account}    75.0
    Should Be Equal As Numbers    ${balance}    125.0

Overdraft Raises An Error
    [Documentation]    Withdrawing more than the balance should raise ValueError.
    ${account}=    Guide.Create Bank Account    Carol    50.0
    Run Keyword And Expect Error    *Insufficient funds*
    ...    Guide.Withdraw From Account    ${account}    999.0

Sequential Deposits Accumulate Correctly
    ${account}=    Guide.Create Bank Account    Dave    0.0
    Guide.Deposit To Account    ${account}    100.0
    Guide.Deposit To Account    ${account}    200.0
    ${balance}=    Guide.Get Balance    ${account}
    Should Be Equal As Numbers    ${balance}    300.0

Circle Area Is Mathematically Correct
    [Documentation]    pi * r^2 for r=5 should be approximately 78.54.
    ${area}=      Guide.Circle Area    5.0
    ${close}=     Guide.Values Are Close    ${area}    78.5398    0.001
    Should Be True    ${close}

Rectangle Area Is Width Times Height
    ${area}=    Guide.Rectangle Area    4.0    6.0
    Should Be Equal As Numbers    ${area}    24.0


*** Keywords ***

Account Balance Should Be
    [Documentation]    Reusable keyword: asserts exact numeric balance.
    [Arguments]    ${account}    ${expected}
    ${actual}=    Guide.Get Balance    ${account}
    Should Be Equal As Numbers    ${actual}    ${expected}
