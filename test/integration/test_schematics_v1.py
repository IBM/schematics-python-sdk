# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Integration Tests for SchematicsV1
"""

import os
import pytest
import time
from ibm_cloud_sdk_core import *
from ibm_schematics.schematics_v1 import *
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Config file name
config_file = 'schematics_v1.env'


class TestSchematicsV1:
    """
    Integration Test Class for SchematicsV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.schematics_service = SchematicsV1.new_instance()
            assert cls.schematics_service is not None

            cls.config = read_external_sources(SchematicsV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            auth = IAMAuthenticator(
                apikey=cls.config.get('APIKEY'),
                url=cls.config.get('AUTH_URL'),
                client_id=cls.config.get('CLIENT_ID'),
                client_secret=cls.config.get('CLIENT_SECRET'),
                disable_ssl_verification=False,
            )

            cls.refresh_token = auth.token_manager.request_token()['refresh_token']

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    def createWorkspace(self):

        # Construct a dict representation of a TemplateSourceDataRequest model
        template_source_data_request_model = {
            'env_values': [{'KEY1': 'VALUE1'}, {'KEY2': 'VALUE2'}],
            'folder': '.',
            'type': 'terraform_v0.12.20',
            'variablestore': [
                {'name': 'variable_name1', 'value': 'variable_valuename1'},
                {'name': 'variable_name2', 'value': 'variable_valuename2'},
            ],
        }

        # Construct a dict representation of a TemplateRepoRequest model
        template_repo_request_model = {'url': 'https://github.ibm.com/gshamann/tf_cloudless_sleepy'}

        response = self.schematics_service.create_workspace(
            description='description',
            name='workspace_name',
            tags=['testString'],
            template_data=[template_source_data_request_model],
            template_repo=template_repo_request_model,
            type=['terraform_v0.12.20'],
        )

        workspace_response = response.get_result()
        print(json.dumps(workspace_response, indent=2))
        return workspace_response

    def createWorkspaceWithEmptyRepoURL(self):
        # Construct a dict representation of a TemplateSourceDataRequest model
        template_source_data_request_model = {
            'env_values': [{'KEY1': 'VALUE1'}, {'KEY2': 'VALUE2'}],
            'folder': '.',
            'type': 'terraform_v0.11.14',
            'variablestore': [
                {'name': 'variable_name1', 'value': 'variable_valuename1'},
                {'name': 'variable_name2', 'value': 'variable_valuename2'},
            ],
        }

        response = self.schematics_service.create_workspace(
            description='description',
            name='workspace_name',
            tags=['testString'],
            template_data=[template_source_data_request_model],
            type=['terraform_v0.11.14'],
        )

        workspace_response = response.get_result()
        print(json.dumps(workspace_response, indent=2))
        return workspace_response

    def getWorkspaceById(self, wid):
        response = self.schematics_service.get_workspace(w_id=wid)
        workspace_response = response.get_result()
        print(json.dumps(workspace_response, indent=2))
        return workspace_response

    def getWorkspaceActivityById(self, wid, activityid):
        response = self.schematics_service.get_workspace_activity(
            w_id=wid,
            activity_id=activityid,
        )
        workspace_response = response.get_result()
        print(json.dumps(workspace_response, indent=2))
        return workspace_response

    def waitForWorkspaceStatus(self, wid, status):
        workspaceStatus = ""

        while workspaceStatus != status:
            workspaceStatus = self.getWorkspaceById(wid)['status']
            print(workspaceStatus)
            time.sleep(2)

    def waitForWorkspaceActivityStatus(self, wid, activityid, status):
        workspaceActivityStatus = ""

        while workspaceActivityStatus != status:
            workspaceActivityStatus = self.getWorkspaceActivityById(wid, activityid)['status']
            print(workspaceActivityStatus)
            time.sleep(2)

    def deleteWorkspaceById(self, wid):

        success = False

        while not success:

            try:

                response = self.schematics_service.delete_workspace(w_id=wid, refresh_token=self.refresh_token)

                workspace_response = response.get_result()
                print(json.dumps(workspace_response, indent=2))

                success = True

            except:  # pylint: disable=bare-except
                time.sleep(2)

        return workspace_response

    def uploadTarFile(self):
        ws = self.createWorkspaceWithEmptyRepoURL()
        self.waitForWorkspaceStatus(ws['id'], "DRAFT")

        fileDir = os.getcwd()
        fileName = "tf_cloudless_sleepy_git_archive.tar"
        filePath = os.path.join(fileDir, "tarfiles", fileName)
        fileReader = open(filePath, "rb")

        response = self.schematics_service.template_repo_upload(
            w_id=ws['id'], t_id=ws['template_data'][0]['id'], file_content_type="multipart/form-data", file=fileReader
        )

        workspace_response = response.get_result()
        print(json.dumps(workspace_response, indent=2))
        return ws

    def planWorkspaceAction(self):

        ws = self.uploadTarFile()
        self.waitForWorkspaceStatus(ws['id'], "INACTIVE")

        response = self.schematics_service.plan_workspace_command(w_id=ws['id'], refresh_token=self.refresh_token)

        activity = response.get_result()

        self.waitForWorkspaceActivityStatus(ws['id'], activity['activityid'], "COMPLETED")

        return ws['id'], activity['activityid']

    def applyWorkspaceAction(self):

        ws = self.uploadTarFile()
        self.waitForWorkspaceStatus(ws['id'], "INACTIVE")

        response = self.schematics_service.apply_workspace_command(w_id=ws['id'], refresh_token=self.refresh_token)

        activity = response.get_result()

        self.waitForWorkspaceActivityStatus(ws['id'], activity['activityid'], "COMPLETED")

        return ws, activity['activityid']

    def applyWorkspaceActionByIdWithoutWait(self, id):

        response = self.schematics_service.apply_workspace_command(w_id=id, refresh_token=self.refresh_token)

        activity = response.get_result()

        return id, activity['activityid']

    def destroyWorkspaceAction(self):

        ws = self.uploadTarFile()
        self.waitForWorkspaceStatus(ws['id'], "INACTIVE")

        response = self.schematics_service.destroy_workspace_command(w_id=ws['id'], refresh_token=self.refresh_token)

        activity = response.get_result()

        self.waitForWorkspaceActivityStatus(ws['id'], activity['activityid'], "COMPLETED")

        return ws['id'], activity['activityid']

    def destroyWorkspaceActionById(self, id):

        response = self.schematics_service.destroy_workspace_command(w_id=id, refresh_token=self.refresh_token)

        activity = response.get_result()

        self.waitForWorkspaceActivityStatus(id, activity['activityid'], "COMPLETED")

        return id, activity['activityid']

    def refreshWorkspaceAction(self):

        ws = self.uploadTarFile()
        self.waitForWorkspaceStatus(ws['id'], "INACTIVE")

        response = self.schematics_service.refresh_workspace_command(w_id=ws['id'], refresh_token=self.refresh_token)

        activity = response.get_result()

        self.waitForWorkspaceActivityStatus(ws['id'], activity['activityid'], "COMPLETED")

        return ws['id'], activity['activityid']

    def refreshWorkspaceActionById(self, id):

        response = self.schematics_service.refresh_workspace_command(w_id=id, refresh_token=self.refresh_token)

        activity = response.get_result()

        self.waitForWorkspaceActivityStatus(id, activity['activityid'], "COMPLETED")

        return id, activity['activityid']

    @needscredentials
    def test_list_schematics_location(self):

        list_schematics_location_response = self.schematics_service.list_schematics_location()

        assert list_schematics_location_response.get_status_code() == 200
        list_schematics_locations = list_schematics_location_response.get_result()
        assert list_schematics_locations is not None

    @needscredentials
    def test_list_resource_group(self):

        list_resource_group_response = self.schematics_service.list_resource_group()

        assert list_resource_group_response.get_status_code() == 200
        list_resource_group_response = list_resource_group_response.get_result()
        assert list_resource_group_response is not None

    @needscredentials
    def test_get_schematics_version(self):

        get_schematics_version_response = self.schematics_service.get_schematics_version()

        assert get_schematics_version_response.get_status_code() == 200
        version_response = get_schematics_version_response.get_result()
        assert version_response is not None

    @needscredentials
    def test_list_workspaces(self):

        list_workspaces_response = self.schematics_service.list_workspaces()

        assert list_workspaces_response.get_status_code() == 200
        workspace_response_list = list_workspaces_response.get_result()
        assert workspace_response_list is not None

    @needscredentials
    def test_create_workspace(self):

        # Construct a dict representation of a TemplateSourceDataRequest model
        template_source_data_request_model = {
            'env_values': [{'KEY1': 'VALUE1'}, {'KEY2': 'VALUE2'}],
            'folder': '.',
            'type': 'terraform_v0.12.20',
            'variablestore': [
                {'name': 'variable_name1', 'value': 'variable_valuename1'},
                {'name': 'variable_name2', 'value': 'variable_valuename2'},
            ],
        }

        # Construct a dict representation of a TemplateRepoRequest model
        template_repo_request_model = {'url': 'https://github.ibm.com/gshamann/tf_cloudless_sleepy'}

        create_workspace_response = self.schematics_service.create_workspace(
            description='description',
            name='workspace_name',
            tags=['testString'],
            template_data=[template_source_data_request_model],
            template_repo=template_repo_request_model,
            type=['terraform_v0.12.20'],
        )

        assert create_workspace_response.get_status_code() == 201
        workspace_response = create_workspace_response.get_result()
        assert workspace_response is not None

        self.deleteWorkspaceById(workspace_response['id'])

    @needscredentials
    def test_get_workspace(self):

        ws = self.createWorkspace()

        get_workspace_response = self.schematics_service.get_workspace(
            w_id=ws['id'],
        )

        assert get_workspace_response.get_status_code() == 200
        workspace_response = get_workspace_response.get_result()
        assert workspace_response is not None

        self.deleteWorkspaceById(workspace_response['id'])

    @needscredentials
    def test_replace_workspace(self):

        ws = self.createWorkspace()
        self.waitForWorkspaceStatus(ws['id'], "INACTIVE")

        replace_workspace_response = self.schematics_service.replace_workspace(
            w_id=ws['id'],
            description="",
            name="myworkspace",
            type=["terraform_v0.12.20"],
        )

        assert replace_workspace_response.get_status_code() == 200
        workspace_response = replace_workspace_response.get_result()
        assert workspace_response is not None

        self.deleteWorkspaceById(workspace_response['id'])

    @needscredentials
    def test_update_workspace(self):

        ws = self.createWorkspace()
        self.waitForWorkspaceStatus(ws['id'], "INACTIVE")

        update_workspace_response = self.schematics_service.update_workspace(
            w_id=ws['id'],
            description="",
            name="myworkspace",
            type=["terraform_v0.12.20"],
        )

        assert update_workspace_response.get_status_code() == 200
        workspace_response = update_workspace_response.get_result()
        assert workspace_response is not None

        self.deleteWorkspaceById(workspace_response['id'])

    @needscredentials
    def test_upload_template_tar(self):

        ws = self.createWorkspaceWithEmptyRepoURL()
        self.waitForWorkspaceStatus(ws['id'], "DRAFT")

        fileDir = os.getcwd()
        fileName = "tf_cloudless_sleepy_git_archive.tar"
        filePath = os.path.join(fileDir, "tarfiles", fileName)
        fileReader = open(filePath, "rb")

        upload_template_tar_response = self.schematics_service.template_repo_upload(
            w_id=ws['id'], t_id=ws['template_data'][0]['id'], file_content_type="multipart/form-data", file=fileReader
        )

        assert upload_template_tar_response.get_status_code() == 200
        template_repo_tar_upload_response = upload_template_tar_response.get_result()
        assert template_repo_tar_upload_response is not None

        self.deleteWorkspaceById(ws['id'])

    @needscredentials
    def test_get_workspace_readme(self):

        (ws, activityid) = self.applyWorkspaceAction()

        get_workspace_readme_response = self.schematics_service.get_workspace_readme(w_id=ws['id'])

        assert get_workspace_readme_response.get_status_code() == 200
        template_readme = get_workspace_readme_response.get_result()
        assert template_readme is not None

        self.deleteWorkspaceById(ws['id'])

    @needscredentials
    def test_list_workspace_activities(self):

        ws = self.uploadTarFile()
        self.waitForWorkspaceStatus(ws['id'], "INACTIVE")

        self.refreshWorkspaceActionById(ws['id'])
        self.destroyWorkspaceActionById(ws['id'])

        list_workspace_activities_response = self.schematics_service.list_workspace_activities(w_id=ws['id'])

        assert list_workspace_activities_response.get_status_code() == 200
        workspace_activities = list_workspace_activities_response.get_result()
        assert workspace_activities is not None

        self.deleteWorkspaceById(ws['id'])

    @needscredentials
    def test_get_workspace_activity(self):

        ws = self.uploadTarFile()
        self.waitForWorkspaceStatus(ws['id'], "INACTIVE")

        activity = self.refreshWorkspaceActionById(ws['id'])

        get_workspace_activity_response = self.schematics_service.get_workspace_activity(
            w_id=ws['id'], activity_id=activity[1]
        )

        assert get_workspace_activity_response.get_status_code() == 200
        workspace_activity = get_workspace_activity_response.get_result()
        assert workspace_activity is not None

        self.deleteWorkspaceById(ws['id'])

    @needscredentials
    def test_run_workspace_commands(self):

        (ws, activityid) = self.applyWorkspaceAction()

        # Construct a dict representation of a TerraformCommand model
        terraform_command_model = {
            'command': 'state show',
            'command_params': 'data.template_file.test',
            'command_name': 'Test Command',
            'command_desc': 'Check command execution',
            'command_onError': 'continue',
            'command_dependsOn': '',
        }

        run_workspace_commands_response = self.schematics_service.run_workspace_commands(
            w_id=ws['id'],
            refresh_token=self.refresh_token,
            commands=[terraform_command_model],
            operation_name='testString',
            description='testString',
        )

        self.waitForWorkspaceActivityStatus(ws['id'], activityid, "COMPLETED")

        assert run_workspace_commands_response.get_status_code() == 202
        workspace_activity_command_result = run_workspace_commands_response.get_result()
        assert workspace_activity_command_result is not None

        self.deleteWorkspaceById(ws['id'])

    @needscredentials
    def test_apply_workspace_command(self):

        ws = self.uploadTarFile()
        self.waitForWorkspaceStatus(ws['id'], "INACTIVE")

        apply_workspace_command_response = self.schematics_service.apply_workspace_command(
            w_id=ws['id'], refresh_token=self.refresh_token
        )

        assert apply_workspace_command_response.get_status_code() == 202
        workspace_activity_apply_result = apply_workspace_command_response.get_result()
        assert workspace_activity_apply_result is not None

        self.waitForWorkspaceActivityStatus(ws['id'], workspace_activity_apply_result['activityid'], "COMPLETED")

        self.deleteWorkspaceById(ws['id'])

    @needscredentials
    def test_destroy_workspace_command(self):

        ws = self.uploadTarFile()
        self.waitForWorkspaceStatus(ws['id'], "INACTIVE")

        destroy_workspace_command_response = self.schematics_service.destroy_workspace_command(
            w_id=ws['id'],
            refresh_token=self.refresh_token,
        )

        assert destroy_workspace_command_response.get_status_code() == 202
        workspace_activity_destroy_result = destroy_workspace_command_response.get_result()
        assert workspace_activity_destroy_result is not None

        self.waitForWorkspaceActivityStatus(ws['id'], workspace_activity_destroy_result['activityid'], "COMPLETED")

        self.deleteWorkspaceById(ws['id'])

    @needscredentials
    def test_plan_workspace_command(self):

        ws = self.uploadTarFile()
        self.waitForWorkspaceStatus(ws['id'], "INACTIVE")

        plan_workspace_command_response = self.schematics_service.plan_workspace_command(
            w_id=ws['id'], refresh_token=self.refresh_token
        )

        assert plan_workspace_command_response.get_status_code() == 202
        workspace_activity_plan_result = plan_workspace_command_response.get_result()
        assert workspace_activity_plan_result is not None

        self.waitForWorkspaceActivityStatus(ws['id'], workspace_activity_plan_result['activityid'], "COMPLETED")

        self.deleteWorkspaceById(ws['id'])

    @needscredentials
    def test_refresh_workspace_command(self):

        ws = self.uploadTarFile()
        self.waitForWorkspaceStatus(ws['id'], "INACTIVE")

        refresh_workspace_command_response = self.schematics_service.refresh_workspace_command(
            w_id=ws['id'], refresh_token=self.refresh_token
        )

        assert refresh_workspace_command_response.get_status_code() == 202
        workspace_activity_refresh_result = refresh_workspace_command_response.get_result()
        assert workspace_activity_refresh_result is not None

        self.waitForWorkspaceActivityStatus(ws['id'], workspace_activity_refresh_result['activityid'], "COMPLETED")

        self.deleteWorkspaceById(ws['id'])

    @needscredentials
    def test_get_workspace_inputs(self):

        (ws, activityid) = self.applyWorkspaceAction()

        get_workspace_inputs_response = self.schematics_service.get_workspace_inputs(
            w_id=ws['id'], t_id=ws['template_data'][0]['id']
        )

        assert get_workspace_inputs_response.get_status_code() == 200
        template_values = get_workspace_inputs_response.get_result()
        assert template_values is not None

    @needscredentials
    def test_replace_workspace_inputs(self):

        (ws, activityid) = self.applyWorkspaceAction()

        replace_workspace_inputs_response = self.schematics_service.replace_workspace_inputs(
            w_id=ws['id'], t_id=ws['template_data'][0]['id'], variablestore=[{'name': 'updated_var', 'value': 'test'}]
        )

        assert replace_workspace_inputs_response.get_status_code() == 200
        user_values = replace_workspace_inputs_response.get_result()
        assert user_values is not None

    @needscredentials
    def test_get_all_workspace_inputs(self):

        (ws, activityid) = self.applyWorkspaceAction()

        get_all_workspace_inputs_response = self.schematics_service.get_all_workspace_inputs(w_id=ws['id'])

        assert get_all_workspace_inputs_response.get_status_code() == 200
        workspace_template_values_response = get_all_workspace_inputs_response.get_result()
        assert workspace_template_values_response is not None

    @needscredentials
    def test_get_workspace_input_metadata(self):

        (ws, activityid) = self.applyWorkspaceAction()

        get_workspace_input_metadata_response = self.schematics_service.get_workspace_input_metadata(
            w_id=ws['id'], t_id=ws['template_data'][0]['id']
        )

        assert get_workspace_input_metadata_response.get_status_code() == 200
        result = get_workspace_input_metadata_response.get_result()
        assert result is not None

    @needscredentials
    def test_get_workspace_outputs(self):

        (ws, activityid) = self.applyWorkspaceAction()

        get_workspace_outputs_response = self.schematics_service.get_workspace_outputs(w_id=ws['id'])

        assert get_workspace_outputs_response.get_status_code() == 200
        list_output_values_item = get_workspace_outputs_response.get_result()
        assert list_output_values_item is not None

    @needscredentials
    def test_get_workspace_resources(self):

        (ws, activityid) = self.applyWorkspaceAction()

        get_workspace_resources_response = self.schematics_service.get_workspace_resources(w_id=ws['id'])

        assert get_workspace_resources_response.get_status_code() == 200
        list_template_resources = get_workspace_resources_response.get_result()
        assert list_template_resources is not None

    @needscredentials
    def test_get_workspace_state(self):

        (ws, activityid) = self.applyWorkspaceAction()

        get_workspace_state_response = self.schematics_service.get_workspace_state(
            w_id=ws['id'],
        )

        assert get_workspace_state_response.get_status_code() == 200
        state_store_response_list = get_workspace_state_response.get_result()
        assert state_store_response_list is not None

    @needscredentials
    def test_get_workspace_template_state(self):

        (ws, activityid) = self.applyWorkspaceAction()

        get_workspace_template_state_response = self.schematics_service.get_workspace_template_state(
            w_id=ws['id'], t_id=ws['template_data'][0]['id']
        )

        assert get_workspace_template_state_response.get_status_code() == 200
        template_state_store = get_workspace_template_state_response.get_result()
        assert template_state_store is not None

    @needscredentials
    def test_get_workspace_activity_logs(self):

        (ws, activityid) = self.applyWorkspaceAction()

        get_workspace_activity_logs_response = self.schematics_service.get_workspace_activity_logs(
            w_id=ws['id'], activity_id=activityid
        )

        assert get_workspace_activity_logs_response.get_status_code() == 200
        workspace_activity_logs = get_workspace_activity_logs_response.get_result()
        assert workspace_activity_logs is not None

    @needscredentials
    def test_get_workspace_log_urls(self):

        (ws, activityid) = self.applyWorkspaceAction()

        get_workspace_log_urls_response = self.schematics_service.get_workspace_log_urls(
            w_id=ws['id'],
        )

        assert get_workspace_log_urls_response.get_status_code() == 200
        log_store_response_list = get_workspace_log_urls_response.get_result()
        assert log_store_response_list is not None

    @needscredentials
    def test_get_template_logs(self):

        (ws, activityid) = self.applyWorkspaceAction()

        get_template_logs_response = self.schematics_service.get_template_logs(
            w_id=ws['id'],
            t_id=ws['template_data'][0]['id'],
            log_tf_cmd=True,
            log_tf_prefix=True,
            log_tf_null_resource=True,
            log_tf_ansible=True,
        )

        assert get_template_logs_response.get_status_code() == 200
        result = get_template_logs_response.get_result()
        assert result is not None

    @needscredentials
    def test_get_template_activity_log(self):

        (ws, activityid) = self.applyWorkspaceAction()

        get_template_activity_log_response = self.schematics_service.get_template_activity_log(
            w_id=ws['id'],
            t_id=ws['template_data'][0]['id'],
            activity_id=activityid,
            log_tf_cmd=True,
            log_tf_prefix=True,
            log_tf_null_resource=True,
            log_tf_ansible=True,
        )

        assert get_template_activity_log_response.get_status_code() == 200
        result = get_template_activity_log_response.get_result()
        assert result is not None
