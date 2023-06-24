# test = 'crd'
# def test_func():
#     global test
#     #test += 'crd'
#     print(test)
# test_func()

*** Settings ***

Test Teardown     Run Keyword If Test Failed    update automationcenter failure    ${TEST MESSAGE}

Library           AutomationCenter

Library           lib/FormatOrder.py

Library           lib/RemoteExecution.py

Library           lib/GetEntityid.py

Library           Collections

 

*** Variables ***

#input

${aeuser}         ${EMPTY}

${aeparameters}    ${EMPTY}

${aeci}           ${EMPTY}

${aepassword}     ${EMPTY}

${aeprivatekey}    ${EMPTY}

${aedatastore}    ${EMPTY}

${timeout}        NONE

#result

${output}         "Updated Successfully"

${error}          ""

${rc}             0

 

*** Test Cases ***

run

    [Timeout]    ${timeout}

    &{aeci}    AutomationCenter.Json Parse    ${aeci}

    &{aedatastore}    AutomationCenter.Json Parse    ${aedatastore}

    Set Suite Variable    ${aedatastore}

    &{aeparameters}    AutomationCenter.Json Parse    ${aeparameters}

    ${jump_server1}    AutomationCenter.Get Value    ${aeparameters}    jump_server1

    ${jump_server1_details}    AutomationCenter.Resolve Entity    ${aedatastore}    ${jump_server1}

    ${jump_server2}    AutomationCenter.Get Value    ${aeparameters}    jump_server2

    ${jump_server2_details}    AutomationCenter.Resolve Entity    ${aedatastore}    ${jump_server2}

    ${jump_server3}    AutomationCenter.Get Value    ${aeparameters}    jump_server3

    ${jump_server3_details}    AutomationCenter.Resolve Entity    ${aedatastore}    ${jump_server3}

    ${ae_server}    AutomationCenter.Get Value    ${aeparameters}    ae_server

    ${ae_server_details}    AutomationCenter.Resolve Entity    ${aedatastore}    ${ae_server}

    ${db_server}    AutomationCenter.Get Value    ${aeparameters}    db_server

    ${db_server_details}    AutomationCenter.Resolve Entity    ${aedatastore}    ${db_server}

    ${inc_num}    AutomationCenter.Get Value    ${aeparameters}    inc_num

    ${activity_num}    AutomationCenter.Get Value    ${aeparameters}    ActivityId

    ${dbname}    AutomationCenter.Get Value    ${aeparameters}    dbname

    ${host_details}    AutomationCenter.Get Value    ${aeparameters}    sql_output

    #Log    ${jump_server3_details}

    ${host_details_list}    FormatOrder.start_order    ${host_details}

    #Log    ${host_details_list}

    @{cs_status_list}    Create List

    FOR    ${host}    IN    @{host_details_list}

        ${windows_details}    ${windcredential_id}    Run Keyword If    "${host['OS_Type'].lower()}"=="windows"    Get Windows server details    ${host['HostName']}

        ${cs_svr}    Run Keyword If    "${host['CS_Server'].lower()}" == "yes" and ${host['Start_Order']} == 1    Run Start Command    ${host}    ${jump_server1_details}    ${jump_server2_details}    ${jump_server3_details}    ${windows_details}    ${ae_server_details}    ${db_server_details}    ${dbname}    ${inc_num}    ${activity_num}    ${windcredential_id}

        Append To List    ${cs_status_list}    ${cs_svr}

        ${non

_cs_svr}    Run Keyword If    "${host['CS_Server'].lower()}" == "no" and ${host['Start_Order']} != 1 and "${cs_status_list}[0]" == "success"    Run Start SAP noncs Command    ${host}    ${jump_server1_details}    ${jump_server2_details}    ${jump_server3_details}    ${windows_details}    ${ae_server_details}    ${db_server_details}    ${dbname}    ${inc_num}    ${activity_num}    ${windcredential_id}

        ${non_cs_svr}    Run Keyword If    "${host['CS_Server'].lower()}" == "no" and "${cs_status_list}[0]" == "None"    Run Start SAP noncs Command    ${host}    ${jump_server1_details}    ${jump_server2_details}    ${jump_server3_details}    ${windows_details}    ${ae_server_details}    ${db_server_details}    ${dbname}    ${inc_num}    ${activity_num}    ${windcredential_id}

        ${non_cs_svr_fail}    Run Keyword If    "${host['CS_Server'].lower()}" == "no" and ${host['Start_Order']} != 1 and "${cs_status_list}[0]" == "failure"    Run Start Failure Command    ${db_server_details}    ${host}    ${dbname}    ${inc_num}    ${activity_num}

    END

    #sleep    300s

    FOR    ${host}    IN    @{host_details_list}

        ${windows_details}    ${windcredential_id}    Run Keyword If    "${host['OS_Type'].lower()}"=="windows"    Get Windows server details    ${host['HostName']}

        ${non_cs_svr}    Run Keyword If    "${host['CS_Server'].lower()}" == "no" and ${host['Start_Order']} != 1 and "${cs_status_list}[0]" == "success"    Run Start SAP noncs update Command    ${host}    ${jump_server1_details}    ${jump_server2_details}    ${jump_server3_details}    ${windows_details}    ${ae_server_details}    ${db_server_details}    ${dbname}    ${inc_num}    ${activity_num}

        ${non_cs_svr}    Run Keyword If    "${host['CS_Server'].lower()}" == "no" and "${cs_status_list}[0]" == "None"    Run Start SAP noncs update Command    ${host}    ${jump_server1_details}    ${jump_server2_details}    ${jump_server3_details}    ${windows_details}    ${ae_server_details}    ${db_server_details}    ${dbname}    ${inc_num}    ${activity_num}

    END

    ${result}=    update automationcenter    ${output}    ${error}    ${rc}

 

*** Keywords ***

Get Windows server details

    [Arguments]    ${host}

    ${svr_id}=    GetEntityid.get_entityid    ${aedatastore}    ${host}

    ${windows_details}    AutomationCenter.Resolve Entity    ${aedatastore}    ${svr_id}

    ${cred}    RemoteExecution.get_password    ${windows_details}

    [Return]    ${windows_details}    ${cred}

 

Run Start Command

    [Arguments]    ${host}    ${jump_server1_details}    ${jump_server2_details}    ${jump_server3_details}    ${windows_details}    ${ae_server_details}    ${db_server_details}    ${dbname}    ${inc_num}    ${activity_num}    ${windcredential_id}

    ${start_status}    ${start_output}    RemoteExecution.start_order    ${host}    ${jump_server1_details}    ${jump_server2_details}    ${jump_server3_details}    ${windows_details}    ${windcredential_id}

    #sleep    300s

    ${server_status}=    set variable    ${NONE}

    FOR    ${in_cnt}    IN RANGE    15

        ${validation_status}    ${svr_output}    RemoteExecution.validate_server    ${host}    ${jump_server1_details}    ${jump_server2_details}    ${jump_server3_details}    ${windows_details}

        ${validated_status}    ${validated_output}    RemoteExecution.validate_start_output    ${ae_server_details}    ${svr_output}    ${host}    ${inc_num}    ${activity_num}

        ${server_status}    automationcenter.get_value    ${validated_output}    colr

        Run Keyword If    "${server_status}"=="Green"    Exit for loop

        sleep    30s

    END

    ${update_status}    ${output}    RemoteExecution.update_excel    ${db_server_details}    ${validated_output["status"]}    ${dbname}

    ${cs_status}    ${cssvr_status}    RemoteExecution.set_csstatus    ${validated_output["status"]}

    [Return]    ${cssvr_status}

 

Run Start SAP noncs Command

    [Arguments]    ${host}    ${jump_server1_details}    ${jump_server2_details}    ${jump_server3_details}    ${windows_details}    ${ae_server_details}    ${db_server_details}    ${dbname}    ${inc_num}    ${activity_num}    ${windcredential_id}

    ${start_status}    ${start_output}    RemoteExecution.start_order    ${host}    ${jump_server1_details}    ${jump_server2_details}    ${jump_server3_details}    ${windows_details}    ${windcredential_id}

 

Run Start SAP noncs update Command

    [Arguments]    ${host}    ${jump_server1_details}    ${jump_server2_details}    ${jump_server3_details}    ${windows_details}    ${ae_server_details}    ${db_server_details}    ${dbname}    ${inc_num}    ${activity_num}

    ${server_status}=    set variable    ${NONE}

    FOR    ${in_cnt}    IN RANGE    15

        ${validation_status}    ${svr_output}    RemoteExecution.validate_server    ${host}    ${jump_server1_details}    ${jump_server2_details}    ${jump_server3_details}    ${windows_details}

        ${validated_status}    ${validated_output}    RemoteExecution.validate_start_output    ${ae_server_details}    ${svr_output}    ${host}    ${inc_num}    ${activity_num}

        ${server_status}    automationcenter.get_value    ${validated_output}    colr

        Run Keyword If    "${server_status}"=="Green"    Exit for loop

        sleep    30s

    END

    ${update_status}    ${output}    RemoteExecution.update_excel    ${db_server_details}    ${validated_output["status"]}    ${dbname}

    [Return]    ${output}

 

Run Start Failure Command

    [Arguments]    ${db_server_details}    ${host}    ${dbname}    ${inc_num}    ${activity_num}

    ${update_status}    ${output}    RemoteExecution.update_excel_failure    ${db_server_details}    ${host}    ${dbname}    ${inc_num}    ${activity_num}

    [Return]    ${output}