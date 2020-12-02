# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
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
from ibm_cloud_sdk_core import *
from ibm_schematics.schematics_v1 import *

# Config file name
config_file = 'schematics_v1.env'

class TestSchematicsV1():
    """
    Integration Test Class for SchematicsV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.schematics_service = SchematicsV1.new_instance(
                )
            assert cls.schematics_service is not None

            cls.config = read_external_sources(
                SchematicsV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

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

        list_workspaces_response = self.schematics_service.list_workspaces(
            offset=0,
            limit=1
        )

        assert list_workspaces_response.get_status_code() == 200
        workspace_response_list = list_workspaces_response.get_result()
        assert workspace_response_list is not None

    @needscredentials
    def test_create_workspace(self):

        # Construct a dict representation of a CatalogRef model
        catalog_ref_model = {
            'dry_run': True,
            'item_icon_url': 'testString',
            'item_id': 'testString',
            'item_name': 'testString',
            'item_readme_url': 'testString',
            'item_url': 'testString',
            'launch_url': 'testString',
            'offering_version': 'testString'
        }

        # Construct a dict representation of a SharedTargetData model
        shared_target_data_model = {
            'cluster_created_on': 'testString',
            'cluster_id': 'testString',
            'cluster_name': 'testString',
            'cluster_type': 'testString',
            'entitlement_keys': [{ 'foo': 'bar' }],
            'namespace': 'testString',
            'region': 'testString',
            'resource_group_id': 'testString',
            'worker_count': 26,
            'worker_machine_type': 'testString'
        }

        # Construct a dict representation of a WorkspaceVariableRequest model
        workspace_variable_request_model = {
            'description': 'testString',
            'name': 'testString',
            'secure': True,
            'type': 'testString',
            'use_default': True,
            'value': 'testString'
        }

        # Construct a dict representation of a TemplateSourceDataRequest model
        template_source_data_request_model = {
            'env_values': [{ 'foo': 'bar' }],
            'folder': 'testString',
            'init_state_file': 'testString',
            'type': 'testString',
            'uninstall_script_name': 'testString',
            'values': 'testString',
            'values_metadata': [{ 'foo': 'bar' }],
            'variablestore': [workspace_variable_request_model]
        }

        # Construct a dict representation of a TemplateRepoRequest model
        template_repo_request_model = {
            'branch': 'testString',
            'release': 'testString',
            'repo_sha_value': 'testString',
            'repo_url': 'testString',
            'url': 'testString'
        }

        # Construct a dict representation of a WorkspaceStatusRequest model
        workspace_status_request_model = {
            'frozen': True,
            'frozen_at': '2020-01-28T18:40:40.123456Z',
            'frozen_by': 'testString',
            'locked': True,
            'locked_by': 'testString',
            'locked_time': '2020-01-28T18:40:40.123456Z'
        }

        create_workspace_response = self.schematics_service.create_workspace(
            applied_shareddata_ids=['testString'],
            catalog_ref=catalog_ref_model,
            description='testString',
            location='testString',
            name='testString',
            resource_group='testString',
            shared_data=shared_target_data_model,
            tags=['testString'],
            template_data=[template_source_data_request_model],
            template_ref='testString',
            template_repo=template_repo_request_model,
            type=['testString'],
            workspace_status=workspace_status_request_model,
            x_github_token='testString'
        )

        assert create_workspace_response.get_status_code() == 201
        workspace_response = create_workspace_response.get_result()
        assert workspace_response is not None

    @needscredentials
    def test_get_workspace(self):

        get_workspace_response = self.schematics_service.get_workspace(
            w_id='testString'
        )

        assert get_workspace_response.get_status_code() == 200
        workspace_response = get_workspace_response.get_result()
        assert workspace_response is not None

    @needscredentials
    def test_replace_workspace(self):

        # Construct a dict representation of a CatalogRef model
        catalog_ref_model = {
            'dry_run': True,
            'item_icon_url': 'testString',
            'item_id': 'testString',
            'item_name': 'testString',
            'item_readme_url': 'testString',
            'item_url': 'testString',
            'launch_url': 'testString',
            'offering_version': 'testString'
        }

        # Construct a dict representation of a SharedTargetData model
        shared_target_data_model = {
            'cluster_created_on': 'testString',
            'cluster_id': 'testString',
            'cluster_name': 'testString',
            'cluster_type': 'testString',
            'entitlement_keys': [{ 'foo': 'bar' }],
            'namespace': 'testString',
            'region': 'testString',
            'resource_group_id': 'testString',
            'worker_count': 26,
            'worker_machine_type': 'testString'
        }

        # Construct a dict representation of a WorkspaceVariableRequest model
        workspace_variable_request_model = {
            'description': 'testString',
            'name': 'testString',
            'secure': True,
            'type': 'testString',
            'use_default': True,
            'value': 'testString'
        }

        # Construct a dict representation of a TemplateSourceDataRequest model
        template_source_data_request_model = {
            'env_values': [{ 'foo': 'bar' }],
            'folder': 'testString',
            'init_state_file': 'testString',
            'type': 'testString',
            'uninstall_script_name': 'testString',
            'values': 'testString',
            'values_metadata': [{ 'foo': 'bar' }],
            'variablestore': [workspace_variable_request_model]
        }

        # Construct a dict representation of a TemplateRepoUpdateRequest model
        template_repo_update_request_model = {
            'branch': 'testString',
            'release': 'testString',
            'repo_sha_value': 'testString',
            'repo_url': 'testString',
            'url': 'testString'
        }

        # Construct a dict representation of a WorkspaceStatusUpdateRequest model
        workspace_status_update_request_model = {
            'frozen': True,
            'frozen_at': '2020-01-28T18:40:40.123456Z',
            'frozen_by': 'testString',
            'locked': True,
            'locked_by': 'testString',
            'locked_time': '2020-01-28T18:40:40.123456Z'
        }

        # Construct a dict representation of a WorkspaceStatusMessage model
        workspace_status_message_model = {
            'status_code': 'testString',
            'status_msg': 'testString'
        }

        replace_workspace_response = self.schematics_service.replace_workspace(
            w_id='testString',
            catalog_ref=catalog_ref_model,
            description='testString',
            name='testString',
            shared_data=shared_target_data_model,
            tags=['testString'],
            template_data=[template_source_data_request_model],
            template_repo=template_repo_update_request_model,
            type=['testString'],
            workspace_status=workspace_status_update_request_model,
            workspace_status_msg=workspace_status_message_model
        )

        assert replace_workspace_response.get_status_code() == 200
        workspace_response = replace_workspace_response.get_result()
        assert workspace_response is not None

    @needscredentials
    def test_update_workspace(self):

        # Construct a dict representation of a CatalogRef model
        catalog_ref_model = {
            'dry_run': True,
            'item_icon_url': 'testString',
            'item_id': 'testString',
            'item_name': 'testString',
            'item_readme_url': 'testString',
            'item_url': 'testString',
            'launch_url': 'testString',
            'offering_version': 'testString'
        }

        # Construct a dict representation of a SharedTargetData model
        shared_target_data_model = {
            'cluster_created_on': 'testString',
            'cluster_id': 'testString',
            'cluster_name': 'testString',
            'cluster_type': 'testString',
            'entitlement_keys': [{ 'foo': 'bar' }],
            'namespace': 'testString',
            'region': 'testString',
            'resource_group_id': 'testString',
            'worker_count': 26,
            'worker_machine_type': 'testString'
        }

        # Construct a dict representation of a WorkspaceVariableRequest model
        workspace_variable_request_model = {
            'description': 'testString',
            'name': 'testString',
            'secure': True,
            'type': 'testString',
            'use_default': True,
            'value': 'testString'
        }

        # Construct a dict representation of a TemplateSourceDataRequest model
        template_source_data_request_model = {
            'env_values': [{ 'foo': 'bar' }],
            'folder': 'testString',
            'init_state_file': 'testString',
            'type': 'testString',
            'uninstall_script_name': 'testString',
            'values': 'testString',
            'values_metadata': [{ 'foo': 'bar' }],
            'variablestore': [workspace_variable_request_model]
        }

        # Construct a dict representation of a TemplateRepoUpdateRequest model
        template_repo_update_request_model = {
            'branch': 'testString',
            'release': 'testString',
            'repo_sha_value': 'testString',
            'repo_url': 'testString',
            'url': 'testString'
        }

        # Construct a dict representation of a WorkspaceStatusUpdateRequest model
        workspace_status_update_request_model = {
            'frozen': True,
            'frozen_at': '2020-01-28T18:40:40.123456Z',
            'frozen_by': 'testString',
            'locked': True,
            'locked_by': 'testString',
            'locked_time': '2020-01-28T18:40:40.123456Z'
        }

        # Construct a dict representation of a WorkspaceStatusMessage model
        workspace_status_message_model = {
            'status_code': 'testString',
            'status_msg': 'testString'
        }

        update_workspace_response = self.schematics_service.update_workspace(
            w_id='testString',
            catalog_ref=catalog_ref_model,
            description='testString',
            name='testString',
            shared_data=shared_target_data_model,
            tags=['testString'],
            template_data=[template_source_data_request_model],
            template_repo=template_repo_update_request_model,
            type=['testString'],
            workspace_status=workspace_status_update_request_model,
            workspace_status_msg=workspace_status_message_model
        )

        assert update_workspace_response.get_status_code() == 200
        workspace_response = update_workspace_response.get_result()
        assert workspace_response is not None

    @needscredentials
    def test_upload_template_tar(self):

        upload_template_tar_response = self.schematics_service.upload_template_tar(
            w_id='testString',
            t_id='testString',
            file=io.BytesIO(b'This is a mock file.').getvalue(),
            file_content_type='testString'
        )

        assert upload_template_tar_response.get_status_code() == 200
        template_repo_tar_upload_response = upload_template_tar_response.get_result()
        assert template_repo_tar_upload_response is not None

    @needscredentials
    def test_get_workspace_readme(self):

        get_workspace_readme_response = self.schematics_service.get_workspace_readme(
            w_id='testString',
            ref='testString',
            formatted='markdown'
        )

        assert get_workspace_readme_response.get_status_code() == 200
        template_readme = get_workspace_readme_response.get_result()
        assert template_readme is not None

    @needscredentials
    def test_list_workspace_activities(self):

        list_workspace_activities_response = self.schematics_service.list_workspace_activities(
            w_id='testString',
            offset=0,
            limit=1
        )

        assert list_workspace_activities_response.get_status_code() == 200
        workspace_activities = list_workspace_activities_response.get_result()
        assert workspace_activities is not None

    @needscredentials
    def test_get_workspace_activity(self):

        get_workspace_activity_response = self.schematics_service.get_workspace_activity(
            w_id='testString',
            activity_id='testString'
        )

        assert get_workspace_activity_response.get_status_code() == 200
        workspace_activity = get_workspace_activity_response.get_result()
        assert workspace_activity is not None

    @needscredentials
    def test_apply_workspace_command(self):

        # Construct a dict representation of a WorkspaceActivityOptionsTemplate model
        workspace_activity_options_template_model = {
            'target': ['testString'],
            'tf_vars': ['testString']
        }

        apply_workspace_command_response = self.schematics_service.apply_workspace_command(
            w_id='testString',
            refresh_token='testString',
            action_options=workspace_activity_options_template_model
        )

        assert apply_workspace_command_response.get_status_code() == 202
        workspace_activity_apply_result = apply_workspace_command_response.get_result()
        assert workspace_activity_apply_result is not None

    @needscredentials
    def test_destroy_workspace_command(self):

        # Construct a dict representation of a WorkspaceActivityOptionsTemplate model
        workspace_activity_options_template_model = {
            'target': ['testString'],
            'tf_vars': ['testString']
        }

        destroy_workspace_command_response = self.schematics_service.destroy_workspace_command(
            w_id='testString',
            refresh_token='testString',
            action_options=workspace_activity_options_template_model
        )

        assert destroy_workspace_command_response.get_status_code() == 202
        workspace_activity_destroy_result = destroy_workspace_command_response.get_result()
        assert workspace_activity_destroy_result is not None

    @needscredentials
    def test_plan_workspace_command(self):

        plan_workspace_command_response = self.schematics_service.plan_workspace_command(
            w_id='testString',
            refresh_token='testString'
        )

        assert plan_workspace_command_response.get_status_code() == 202
        workspace_activity_plan_result = plan_workspace_command_response.get_result()
        assert workspace_activity_plan_result is not None

    @needscredentials
    def test_refresh_workspace_command(self):

        refresh_workspace_command_response = self.schematics_service.refresh_workspace_command(
            w_id='testString',
            refresh_token='testString'
        )

        assert refresh_workspace_command_response.get_status_code() == 202
        workspace_activity_refresh_result = refresh_workspace_command_response.get_result()
        assert workspace_activity_refresh_result is not None

    @needscredentials
    def test_get_workspace_inputs(self):

        get_workspace_inputs_response = self.schematics_service.get_workspace_inputs(
            w_id='testString',
            t_id='testString'
        )

        assert get_workspace_inputs_response.get_status_code() == 200
        template_values = get_workspace_inputs_response.get_result()
        assert template_values is not None

    @needscredentials
    def test_replace_workspace_inputs(self):

        # Construct a dict representation of a WorkspaceVariableRequest model
        workspace_variable_request_model = {
            'description': 'testString',
            'name': 'testString',
            'secure': True,
            'type': 'testString',
            'use_default': True,
            'value': 'testString'
        }

        replace_workspace_inputs_response = self.schematics_service.replace_workspace_inputs(
            w_id='testString',
            t_id='testString',
            env_values=[{ 'foo': 'bar' }],
            values='testString',
            variablestore=[workspace_variable_request_model]
        )

        assert replace_workspace_inputs_response.get_status_code() == 200
        user_values = replace_workspace_inputs_response.get_result()
        assert user_values is not None

    @needscredentials
    def test_get_all_workspace_inputs(self):

        get_all_workspace_inputs_response = self.schematics_service.get_all_workspace_inputs(
            w_id='testString'
        )

        assert get_all_workspace_inputs_response.get_status_code() == 200
        workspace_template_values_response = get_all_workspace_inputs_response.get_result()
        assert workspace_template_values_response is not None

    @needscredentials
    def test_get_workspace_input_metadata(self):

        get_workspace_input_metadata_response = self.schematics_service.get_workspace_input_metadata(
            w_id='testString',
            t_id='testString'
        )

        assert get_workspace_input_metadata_response.get_status_code() == 200
        result = get_workspace_input_metadata_response.get_result()
        assert result is not None

    @needscredentials
    def test_get_workspace_outputs(self):

        get_workspace_outputs_response = self.schematics_service.get_workspace_outputs(
            w_id='testString'
        )

        assert get_workspace_outputs_response.get_status_code() == 200
        list_output_values_item = get_workspace_outputs_response.get_result()
        assert list_output_values_item is not None

    @needscredentials
    def test_get_workspace_resources(self):

        get_workspace_resources_response = self.schematics_service.get_workspace_resources(
            w_id='testString'
        )

        assert get_workspace_resources_response.get_status_code() == 200
        list_template_resources = get_workspace_resources_response.get_result()
        assert list_template_resources is not None

    @needscredentials
    def test_get_workspace_state(self):

        get_workspace_state_response = self.schematics_service.get_workspace_state(
            w_id='testString'
        )

        assert get_workspace_state_response.get_status_code() == 200
        state_store_response_list = get_workspace_state_response.get_result()
        assert state_store_response_list is not None

    @needscredentials
    def test_get_workspace_template_state(self):

        get_workspace_template_state_response = self.schematics_service.get_workspace_template_state(
            w_id='testString',
            t_id='testString'
        )

        assert get_workspace_template_state_response.get_status_code() == 200
        template_state_store = get_workspace_template_state_response.get_result()
        assert template_state_store is not None

    @needscredentials
    def test_get_workspace_activity_logs(self):

        get_workspace_activity_logs_response = self.schematics_service.get_workspace_activity_logs(
            w_id='testString',
            activity_id='testString'
        )

        assert get_workspace_activity_logs_response.get_status_code() == 200
        workspace_activity_logs = get_workspace_activity_logs_response.get_result()
        assert workspace_activity_logs is not None

    @needscredentials
    def test_get_workspace_log_urls(self):

        get_workspace_log_urls_response = self.schematics_service.get_workspace_log_urls(
            w_id='testString'
        )

        assert get_workspace_log_urls_response.get_status_code() == 200
        log_store_response_list = get_workspace_log_urls_response.get_result()
        assert log_store_response_list is not None

    @needscredentials
    def test_get_template_logs(self):

        get_template_logs_response = self.schematics_service.get_template_logs(
            w_id='testString',
            t_id='testString',
            log_tf_cmd=True,
            log_tf_prefix=True,
            log_tf_null_resource=True,
            log_tf_ansible=True
        )

        assert get_template_logs_response.get_status_code() == 200
        result = get_template_logs_response.get_result()
        assert result is not None

    @needscredentials
    def test_get_template_activity_log(self):

        get_template_activity_log_response = self.schematics_service.get_template_activity_log(
            w_id='testString',
            t_id='testString',
            activity_id='testString',
            log_tf_cmd=True,
            log_tf_prefix=True,
            log_tf_null_resource=True,
            log_tf_ansible=True
        )

        assert get_template_activity_log_response.get_status_code() == 200
        result = get_template_activity_log_response.get_result()
        assert result is not None

    @needscredentials
    def test_create_workspace_deletion_job(self):

        create_workspace_deletion_job_response = self.schematics_service.create_workspace_deletion_job(
            refresh_token='testString',
            new_delete_workspaces=True,
            new_destroy_resources=True,
            new_job='testString',
            new_version='testString',
            new_workspaces=['testString'],
            destroy_resources='testString'
        )

        assert create_workspace_deletion_job_response.get_status_code() == 200
        workspace_bulk_delete_response = create_workspace_deletion_job_response.get_result()
        assert workspace_bulk_delete_response is not None

    @needscredentials
    def test_get_workspace_deletion_job_status(self):

        get_workspace_deletion_job_status_response = self.schematics_service.get_workspace_deletion_job_status(
            wj_id='testString'
        )

        assert get_workspace_deletion_job_status_response.get_status_code() == 200
        workspace_job_response = get_workspace_deletion_job_status_response.get_result()
        assert workspace_job_response is not None

    @needscredentials
    def test_create_action(self):

        # Construct a dict representation of a UserState model
        user_state_model = {
            'state': 'draft',
            'set_by': 'testString',
            'set_at': '2020-01-28T18:40:40.123456Z'
        }

        # Construct a dict representation of a ExternalSourceGit model
        external_source_git_model = {
            'git_repo_url': 'testString',
            'git_token': 'testString',
            'git_repo_folder': 'testString',
            'git_release': 'testString',
            'git_branch': 'testString'
        }

        # Construct a dict representation of a ExternalSource model
        external_source_model = {
            'source_type': 'local',
            'git': external_source_git_model
        }

        # Construct a dict representation of a SystemLock model
        system_lock_model = {
            'sys_locked': True,
            'sys_locked_by': 'testString',
            'sys_locked_at': '2020-01-28T18:40:40.123456Z'
        }

        # Construct a dict representation of a TargetResourceset model
        target_resourceset_model = {
            'name': 'testString',
            'type': 'testString',
            'description': 'testString',
            'resource_query': 'testString',
            'credential': 'testString',
            'sys_lock': system_lock_model
        }

        # Construct a dict representation of a VariableMetadata model
        variable_metadata_model = {
            'type': 'boolean',
            'aliases': ['testString'],
            'description': 'testString',
            'default_value': 'testString',
            'secure': True,
            'immutable': True,
            'hidden': True,
            'options': ['testString'],
            'min_value': 38,
            'max_value': 38,
            'min_length': 38,
            'max_length': 38,
            'matches': 'testString',
            'position': 38,
            'group_by': 'testString',
            'source': 'testString'
        }

        # Construct a dict representation of a VariableData model
        variable_data_model = {
            'name': 'testString',
            'value': 'testString',
            'metadata': variable_metadata_model
        }

        # Construct a dict representation of a ActionState model
        action_state_model = {
            'status_code': 'normal',
            'status_message': 'testString'
        }

        create_action_response = self.schematics_service.create_action(
            name='Stop Action',
            description='This Action can be used to Stop the targets',
            location='us_south',
            resource_group='testString',
            tags=['testString'],
            user_state=user_state_model,
            source_readme_url='testString',
            source=external_source_model,
            source_type='local',
            command_parameter='testString',
            bastion=target_resourceset_model,
            targets=[target_resourceset_model],
            inputs=[variable_data_model],
            outputs=[variable_data_model],
            settings=[variable_data_model],
            trigger_record_id='testString',
            state=action_state_model,
            sys_lock=system_lock_model,
            x_github_token='testString'
        )

        assert create_action_response.get_status_code() == 201
        action = create_action_response.get_result()
        assert action is not None

    @needscredentials
    def test_list_actions(self):

        list_actions_response = self.schematics_service.list_actions(
            offset=0,
            limit=1,
            sort='testString',
            profile='ids'
        )

        assert list_actions_response.get_status_code() == 200
        action_list = list_actions_response.get_result()
        assert action_list is not None

    @needscredentials
    def test_get_action(self):

        get_action_response = self.schematics_service.get_action(
            action_id='testString',
            profile='summary'
        )

        assert get_action_response.get_status_code() == 200
        action = get_action_response.get_result()
        assert action is not None

    @needscredentials
    def test_update_action(self):

        # Construct a dict representation of a UserState model
        user_state_model = {
            'state': 'draft',
            'set_by': 'testString',
            'set_at': '2020-01-28T18:40:40.123456Z'
        }

        # Construct a dict representation of a ExternalSourceGit model
        external_source_git_model = {
            'git_repo_url': 'testString',
            'git_token': 'testString',
            'git_repo_folder': 'testString',
            'git_release': 'testString',
            'git_branch': 'testString'
        }

        # Construct a dict representation of a ExternalSource model
        external_source_model = {
            'source_type': 'local',
            'git': external_source_git_model
        }

        # Construct a dict representation of a SystemLock model
        system_lock_model = {
            'sys_locked': True,
            'sys_locked_by': 'testString',
            'sys_locked_at': '2020-01-28T18:40:40.123456Z'
        }

        # Construct a dict representation of a TargetResourceset model
        target_resourceset_model = {
            'name': 'testString',
            'type': 'testString',
            'description': 'testString',
            'resource_query': 'testString',
            'credential': 'testString',
            'sys_lock': system_lock_model
        }

        # Construct a dict representation of a VariableMetadata model
        variable_metadata_model = {
            'type': 'boolean',
            'aliases': ['testString'],
            'description': 'testString',
            'default_value': 'testString',
            'secure': True,
            'immutable': True,
            'hidden': True,
            'options': ['testString'],
            'min_value': 38,
            'max_value': 38,
            'min_length': 38,
            'max_length': 38,
            'matches': 'testString',
            'position': 38,
            'group_by': 'testString',
            'source': 'testString'
        }

        # Construct a dict representation of a VariableData model
        variable_data_model = {
            'name': 'testString',
            'value': 'testString',
            'metadata': variable_metadata_model
        }

        # Construct a dict representation of a ActionState model
        action_state_model = {
            'status_code': 'normal',
            'status_message': 'testString'
        }

        update_action_response = self.schematics_service.update_action(
            action_id='testString',
            name='Stop Action',
            description='This Action can be used to Stop the targets',
            location='us_south',
            resource_group='testString',
            tags=['testString'],
            user_state=user_state_model,
            source_readme_url='testString',
            source=external_source_model,
            source_type='local',
            command_parameter='testString',
            bastion=target_resourceset_model,
            targets=[target_resourceset_model],
            inputs=[variable_data_model],
            outputs=[variable_data_model],
            settings=[variable_data_model],
            trigger_record_id='testString',
            state=action_state_model,
            sys_lock=system_lock_model,
            x_github_token='testString'
        )

        assert update_action_response.get_status_code() == 200
        action = update_action_response.get_result()
        assert action is not None

    @needscredentials
    def test_create_job(self):

        # Construct a dict representation of a VariableMetadata model
        variable_metadata_model = {
            'type': 'boolean',
            'aliases': ['testString'],
            'description': 'testString',
            'default_value': 'testString',
            'secure': True,
            'immutable': True,
            'hidden': True,
            'options': ['testString'],
            'min_value': 38,
            'max_value': 38,
            'min_length': 38,
            'max_length': 38,
            'matches': 'testString',
            'position': 38,
            'group_by': 'testString',
            'source': 'testString'
        }

        # Construct a dict representation of a VariableData model
        variable_data_model = {
            'name': 'testString',
            'value': 'testString',
            'metadata': variable_metadata_model
        }

        # Construct a dict representation of a JobStatusAction model
        job_status_action_model = {
            'action_name': 'testString',
            'status_code': 'job_pending',
            'status_message': 'testString',
            'bastion_status_code': 'none',
            'bastion_status_message': 'testString',
            'targets_status_code': 'none',
            'targets_status_message': 'testString',
            'updated_at': '2020-01-28T18:40:40.123456Z'
        }

        # Construct a dict representation of a JobStatus model
        job_status_model = {
            'action_job_status': job_status_action_model
        }

        # Construct a dict representation of a JobDataAction model
        job_data_action_model = {
            'action_name': 'testString',
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'updated_at': '2020-01-28T18:40:40.123456Z'
        }

        # Construct a dict representation of a JobData model
        job_data_model = {
            'job_type': 'repo_download_job',
            'action_job_data': job_data_action_model
        }

        # Construct a dict representation of a SystemLock model
        system_lock_model = {
            'sys_locked': True,
            'sys_locked_by': 'testString',
            'sys_locked_at': '2020-01-28T18:40:40.123456Z'
        }

        # Construct a dict representation of a TargetResourceset model
        target_resourceset_model = {
            'name': 'testString',
            'type': 'testString',
            'description': 'testString',
            'resource_query': 'testString',
            'credential': 'testString',
            'sys_lock': system_lock_model
        }

        # Construct a dict representation of a JobLogSummaryRepoDownloadJob model
        job_log_summary_repo_download_job_model = {
        }

        # Construct a dict representation of a JobLogSummaryActionJobRecap model
        job_log_summary_action_job_recap_model = {
            'target': ['testString'],
            'ok': 72.5,
            'changed': 72.5,
            'failed': 72.5,
            'skipped': 72.5,
            'unreachable': 72.5
        }

        # Construct a dict representation of a JobLogSummaryActionJob model
        job_log_summary_action_job_model = {
            'recap': job_log_summary_action_job_recap_model
        }

        # Construct a dict representation of a JobLogSummary model
        job_log_summary_model = {
            'job_type': 'repo_download_job',
            'repo_download_job': job_log_summary_repo_download_job_model,
            'action_job': job_log_summary_action_job_model
        }

        create_job_response = self.schematics_service.create_job(
            refresh_token='testString',
            command_object='workspace',
            command_object_id='testString',
            command_name='workspace_init_flow',
            command_parameter='testString',
            command_options=['testString'],
            inputs=[variable_data_model],
            settings=[variable_data_model],
            tags=['testString'],
            location='us_south',
            status=job_status_model,
            data=job_data_model,
            bastion=target_resourceset_model,
            log_summary=job_log_summary_model
        )

        assert create_job_response.get_status_code() == 202
        job = create_job_response.get_result()
        assert job is not None

    @needscredentials
    def test_list_jobs(self):

        list_jobs_response = self.schematics_service.list_jobs(
            offset=0,
            limit=1,
            sort='testString',
            profile='ids',
            resource='workspaces',
            action_id='testString',
            list='all'
        )

        assert list_jobs_response.get_status_code() == 200
        job_list = list_jobs_response.get_result()
        assert job_list is not None

    @needscredentials
    def test_replace_job(self):

        # Construct a dict representation of a VariableMetadata model
        variable_metadata_model = {
            'type': 'boolean',
            'aliases': ['testString'],
            'description': 'testString',
            'default_value': 'testString',
            'secure': True,
            'immutable': True,
            'hidden': True,
            'options': ['testString'],
            'min_value': 38,
            'max_value': 38,
            'min_length': 38,
            'max_length': 38,
            'matches': 'testString',
            'position': 38,
            'group_by': 'testString',
            'source': 'testString'
        }

        # Construct a dict representation of a VariableData model
        variable_data_model = {
            'name': 'testString',
            'value': 'testString',
            'metadata': variable_metadata_model
        }

        # Construct a dict representation of a JobStatusAction model
        job_status_action_model = {
            'action_name': 'testString',
            'status_code': 'job_pending',
            'status_message': 'testString',
            'bastion_status_code': 'none',
            'bastion_status_message': 'testString',
            'targets_status_code': 'none',
            'targets_status_message': 'testString',
            'updated_at': '2020-01-28T18:40:40.123456Z'
        }

        # Construct a dict representation of a JobStatus model
        job_status_model = {
            'action_job_status': job_status_action_model
        }

        # Construct a dict representation of a JobDataAction model
        job_data_action_model = {
            'action_name': 'testString',
            'inputs': [variable_data_model],
            'outputs': [variable_data_model],
            'settings': [variable_data_model],
            'updated_at': '2020-01-28T18:40:40.123456Z'
        }

        # Construct a dict representation of a JobData model
        job_data_model = {
            'job_type': 'repo_download_job',
            'action_job_data': job_data_action_model
        }

        # Construct a dict representation of a SystemLock model
        system_lock_model = {
            'sys_locked': True,
            'sys_locked_by': 'testString',
            'sys_locked_at': '2020-01-28T18:40:40.123456Z'
        }

        # Construct a dict representation of a TargetResourceset model
        target_resourceset_model = {
            'name': 'testString',
            'type': 'testString',
            'description': 'testString',
            'resource_query': 'testString',
            'credential': 'testString',
            'sys_lock': system_lock_model
        }

        # Construct a dict representation of a JobLogSummaryRepoDownloadJob model
        job_log_summary_repo_download_job_model = {
        }

        # Construct a dict representation of a JobLogSummaryActionJobRecap model
        job_log_summary_action_job_recap_model = {
            'target': ['testString'],
            'ok': 72.5,
            'changed': 72.5,
            'failed': 72.5,
            'skipped': 72.5,
            'unreachable': 72.5
        }

        # Construct a dict representation of a JobLogSummaryActionJob model
        job_log_summary_action_job_model = {
            'recap': job_log_summary_action_job_recap_model
        }

        # Construct a dict representation of a JobLogSummary model
        job_log_summary_model = {
            'job_type': 'repo_download_job',
            'repo_download_job': job_log_summary_repo_download_job_model,
            'action_job': job_log_summary_action_job_model
        }

        replace_job_response = self.schematics_service.replace_job(
            job_id='testString',
            refresh_token='testString',
            command_object='workspace',
            command_object_id='testString',
            command_name='workspace_init_flow',
            command_parameter='testString',
            command_options=['testString'],
            inputs=[variable_data_model],
            settings=[variable_data_model],
            tags=['testString'],
            location='us_south',
            status=job_status_model,
            data=job_data_model,
            bastion=target_resourceset_model,
            log_summary=job_log_summary_model
        )

        assert replace_job_response.get_status_code() == 202
        job = replace_job_response.get_result()
        assert job is not None

    @needscredentials
    def test_get_job(self):

        get_job_response = self.schematics_service.get_job(
            job_id='testString',
            profile='summary'
        )

        assert get_job_response.get_status_code() == 200
        job = get_job_response.get_result()
        assert job is not None

    @needscredentials
    def test_list_job_logs(self):

        list_job_logs_response = self.schematics_service.list_job_logs(
            job_id='testString'
        )

        assert list_job_logs_response.get_status_code() == 202
        job_log = list_job_logs_response.get_result()
        assert job_log is not None

    @needscredentials
    def test_list_job_states(self):

        list_job_states_response = self.schematics_service.list_job_states(
            job_id='testString'
        )

        assert list_job_states_response.get_status_code() == 202
        job_state_data = list_job_states_response.get_result()
        assert job_state_data is not None

    @needscredentials
    def test_list_shared_datasets(self):

        list_shared_datasets_response = self.schematics_service.list_shared_datasets()

        assert list_shared_datasets_response.get_status_code() == 200
        shared_dataset_response_list = list_shared_datasets_response.get_result()
        assert shared_dataset_response_list is not None

    @needscredentials
    def test_create_shared_dataset(self):

        # Construct a dict representation of a SharedDatasetData model
        shared_dataset_data_model = {
            'default_value': 'testString',
            'description': 'testString',
            'hidden': True,
            'immutable': True,
            'matches': 'testString',
            'max_value': 'testString',
            'max_value_len': 'testString',
            'min_value': 'testString',
            'min_value_len': 'testString',
            'options': ['testString'],
            'override_value': 'testString',
            'secure': True,
            'var_aliases': ['testString'],
            'var_name': 'testString',
            'var_ref': 'testString',
            'var_type': 'testString'
        }

        create_shared_dataset_response = self.schematics_service.create_shared_dataset(
            auto_propagate_change=True,
            description='testString',
            effected_workspace_ids=['testString'],
            resource_group='testString',
            shared_dataset_data=[shared_dataset_data_model],
            shared_dataset_name='testString',
            shared_dataset_source_name='testString',
            shared_dataset_type=['testString'],
            tags=['testString'],
            version='testString'
        )

        assert create_shared_dataset_response.get_status_code() == 201
        shared_dataset_response = create_shared_dataset_response.get_result()
        assert shared_dataset_response is not None

    @needscredentials
    def test_get_shared_dataset(self):

        get_shared_dataset_response = self.schematics_service.get_shared_dataset(
            sd_id='testString'
        )

        assert get_shared_dataset_response.get_status_code() == 200
        shared_dataset_response = get_shared_dataset_response.get_result()
        assert shared_dataset_response is not None

    @needscredentials
    def test_replace_shared_dataset(self):

        # Construct a dict representation of a SharedDatasetData model
        shared_dataset_data_model = {
            'default_value': 'testString',
            'description': 'testString',
            'hidden': True,
            'immutable': True,
            'matches': 'testString',
            'max_value': 'testString',
            'max_value_len': 'testString',
            'min_value': 'testString',
            'min_value_len': 'testString',
            'options': ['testString'],
            'override_value': 'testString',
            'secure': True,
            'var_aliases': ['testString'],
            'var_name': 'testString',
            'var_ref': 'testString',
            'var_type': 'testString'
        }

        replace_shared_dataset_response = self.schematics_service.replace_shared_dataset(
            sd_id='testString',
            auto_propagate_change=True,
            description='testString',
            effected_workspace_ids=['testString'],
            resource_group='testString',
            shared_dataset_data=[shared_dataset_data_model],
            shared_dataset_name='testString',
            shared_dataset_source_name='testString',
            shared_dataset_type=['testString'],
            tags=['testString'],
            version='testString'
        )

        assert replace_shared_dataset_response.get_status_code() == 200
        shared_dataset_response = replace_shared_dataset_response.get_result()
        assert shared_dataset_response is not None

    @needscredentials
    def test_get_kms_settings(self):

        get_kms_settings_response = self.schematics_service.get_kms_settings(
            location='testString'
        )

        assert get_kms_settings_response.get_status_code() == 200
        kms_settings = get_kms_settings_response.get_result()
        assert kms_settings is not None

    @needscredentials
    def test_replace_kms_settings(self):

        # Construct a dict representation of a KMSSettingsPrimaryCrk model
        kms_settings_primary_crk_model = {
            'kms_name': 'testString',
            'kms_private_endpoint': 'testString',
            'key_crn': 'testString'
        }

        # Construct a dict representation of a KMSSettingsSecondaryCrk model
        kms_settings_secondary_crk_model = {
            'kms_name': 'testString',
            'kms_private_endpoint': 'testString',
            'key_crn': 'testString'
        }

        replace_kms_settings_response = self.schematics_service.replace_kms_settings(
            location='testString',
            encryption_scheme='testString',
            resource_group='testString',
            primary_crk=kms_settings_primary_crk_model,
            secondary_crk=kms_settings_secondary_crk_model
        )

        assert replace_kms_settings_response.get_status_code() == 200
        kms_settings = replace_kms_settings_response.get_result()
        assert kms_settings is not None

    @needscredentials
    def test_get_discovered_kms_instances(self):

        get_discovered_kms_instances_response = self.schematics_service.get_discovered_kms_instances(
            encryption_scheme='testString',
            location='testString',
            resource_group='testString',
            limit=1,
            sort='testString'
        )

        assert get_discovered_kms_instances_response.get_status_code() == 200
        kms_discovery = get_discovered_kms_instances_response.get_result()
        assert kms_discovery is not None

    @needscredentials
    def test_delete_workspace_activity(self):

        delete_workspace_activity_response = self.schematics_service.delete_workspace_activity(
            w_id='testString',
            activity_id='testString'
        )

        assert delete_workspace_activity_response.get_status_code() == 202
        workspace_activity_apply_result = delete_workspace_activity_response.get_result()
        assert workspace_activity_apply_result is not None

    @needscredentials
    def test_delete_workspace(self):

        delete_workspace_response = self.schematics_service.delete_workspace(
            w_id='testString',
            refresh_token='testString',
            destroy_resources='testString'
        )

        assert delete_workspace_response.get_status_code() == 200
        result = delete_workspace_response.get_result()
        assert result is not None

    @needscredentials
    def test_delete_shared_dataset(self):

        delete_shared_dataset_response = self.schematics_service.delete_shared_dataset(
            sd_id='testString'
        )

        assert delete_shared_dataset_response.get_status_code() == 200
        shared_dataset_response = delete_shared_dataset_response.get_result()
        assert shared_dataset_response is not None

    @needscredentials
    def test_delete_job(self):

        delete_job_response = self.schematics_service.delete_job(
            job_id='testString',
            refresh_token='testString',
            force=True,
            propagate=True
        )

        assert delete_job_response.get_status_code() == 204

    @needscredentials
    def test_delete_action(self):

        delete_action_response = self.schematics_service.delete_action(
            action_id='testString',
            force=True,
            propagate=True
        )

        assert delete_action_response.get_status_code() == 204

