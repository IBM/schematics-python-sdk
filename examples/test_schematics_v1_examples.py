# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2024.
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
Examples for SchematicsV1
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import io
import os
import pytest
from ibm_cloud.schematics_v1 import *

#
# This file provides an example of how to use the schematics service.
#
# The following configuration properties are assumed to be defined:
# SCHEMATICS_URL=<service base url>
# SCHEMATICS_AUTH_TYPE=iam
# SCHEMATICS_APIKEY=<IAM apikey>
# SCHEMATICS_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'schematics_v1.env'

schematics_service = None

config = None


##############################################################################
# Start of Examples for Service: SchematicsV1
##############################################################################
# region
class TestSchematicsV1Examples:
    """
    Example Test Class for SchematicsV1
    """

    @classmethod
    def setup_class(cls):
        global schematics_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            schematics_service = SchematicsV1.new_instance()

            # end-common
            assert schematics_service is not None

            # Load the configuration
            global config
            config = read_external_sources(SchematicsV1.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_list_schematics_location_example(self):
        """
        list_schematics_location request example
        """
        try:
            print('\nlist_schematics_location() result:')

            # begin-list_schematics_location

            response = schematics_service.list_schematics_location()
            list_schematics_locations = response.get_result()

            print(json.dumps(list_schematics_locations, indent=2))

            # end-list_schematics_location

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_locations_example(self):
        """
        list_locations request example
        """
        try:
            print('\nlist_locations() result:')

            # begin-list_locations

            response = schematics_service.list_locations()
            schematics_locations_list = response.get_result()

            print(json.dumps(schematics_locations_list, indent=2))

            # end-list_locations

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_resource_group_example(self):
        """
        list_resource_group request example
        """
        try:
            print('\nlist_resource_group() result:')

            # begin-list_resource_group

            response = schematics_service.list_resource_group()
            list_resource_group_response = response.get_result()

            print(json.dumps(list_resource_group_response, indent=2))

            # end-list_resource_group

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_schematics_version_example(self):
        """
        get_schematics_version request example
        """
        try:
            print('\nget_schematics_version() result:')

            # begin-get_schematics_version

            response = schematics_service.get_schematics_version()
            version_response = response.get_result()

            print(json.dumps(version_response, indent=2))

            # end-get_schematics_version

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_process_template_meta_data_example(self):
        """
        process_template_meta_data request example
        """
        try:
            print('\nprocess_template_meta_data() result:')

            # begin-ProcessTemplateMetaData

            external_source_model = {
                'source_type': 'local',
            }

            response = schematics_service.process_template_meta_data(
                template_type='testString',
                source=external_source_model,
            )
            template_meta_data_response = response.get_result()

            print(json.dumps(template_meta_data_response, indent=2))

            # end-ProcessTemplateMetaData

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_workspaces_example(self):
        """
        list_workspaces request example
        """
        try:
            print('\nlist_workspaces() result:')

            # begin-list_workspaces

            response = schematics_service.list_workspaces()
            workspace_response_list = response.get_result()

            print(json.dumps(workspace_response_list, indent=2))

            # end-list_workspaces

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_workspace_example(self):
        """
        create_workspace request example
        """
        try:
            print('\ncreate_workspace() result:')

            # begin-create_workspace

            response = schematics_service.create_workspace()
            workspace_response = response.get_result()

            print(json.dumps(workspace_response, indent=2))

            # end-create_workspace

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_example(self):
        """
        get_workspace request example
        """
        try:
            print('\nget_workspace() result:')

            # begin-get_workspace

            response = schematics_service.get_workspace(
                w_id='testString',
            )
            workspace_response = response.get_result()

            print(json.dumps(workspace_response, indent=2))

            # end-get_workspace

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_workspace_example(self):
        """
        replace_workspace request example
        """
        try:
            print('\nreplace_workspace() result:')

            # begin-replace_workspace

            response = schematics_service.replace_workspace(
                w_id='testString',
            )
            workspace_response = response.get_result()

            print(json.dumps(workspace_response, indent=2))

            # end-replace_workspace

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_workspace_example(self):
        """
        update_workspace request example
        """
        try:
            print('\nupdate_workspace() result:')

            # begin-update_workspace

            response = schematics_service.update_workspace(
                w_id='testString',
            )
            workspace_response = response.get_result()

            print(json.dumps(workspace_response, indent=2))

            # end-update_workspace

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_readme_example(self):
        """
        get_workspace_readme request example
        """
        try:
            print('\nget_workspace_readme() result:')

            # begin-get_workspace_readme

            response = schematics_service.get_workspace_readme(
                w_id='testString',
            )
            template_readme = response.get_result()

            print(json.dumps(template_readme, indent=2))

            # end-get_workspace_readme

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_template_repo_upload_example(self):
        """
        template_repo_upload request example
        """
        try:
            print('\ntemplate_repo_upload() result:')

            # begin-template_repo_upload

            response = schematics_service.template_repo_upload(
                w_id='testString',
                t_id='testString',
            )
            template_repo_tar_upload_response = response.get_result()

            print(json.dumps(template_repo_tar_upload_response, indent=2))

            # end-template_repo_upload

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_inputs_example(self):
        """
        get_workspace_inputs request example
        """
        try:
            print('\nget_workspace_inputs() result:')

            # begin-get_workspace_inputs

            response = schematics_service.get_workspace_inputs(
                w_id='testString',
                t_id='testString',
            )
            template_values = response.get_result()

            print(json.dumps(template_values, indent=2))

            # end-get_workspace_inputs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_workspace_inputs_example(self):
        """
        replace_workspace_inputs request example
        """
        try:
            print('\nreplace_workspace_inputs() result:')

            # begin-replace_workspace_inputs

            response = schematics_service.replace_workspace_inputs(
                w_id='testString',
                t_id='testString',
            )
            user_values = response.get_result()

            print(json.dumps(user_values, indent=2))

            # end-replace_workspace_inputs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_all_workspace_inputs_example(self):
        """
        get_all_workspace_inputs request example
        """
        try:
            print('\nget_all_workspace_inputs() result:')

            # begin-get_all_workspace_inputs

            response = schematics_service.get_all_workspace_inputs(
                w_id='testString',
            )
            workspace_template_values_response = response.get_result()

            print(json.dumps(workspace_template_values_response, indent=2))

            # end-get_all_workspace_inputs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_input_metadata_example(self):
        """
        get_workspace_input_metadata request example
        """
        try:
            print('\nget_workspace_input_metadata() result:')

            # begin-get_workspace_input_metadata

            response = schematics_service.get_workspace_input_metadata(
                w_id='testString',
                t_id='testString',
            )
            template_metadata = response.get_result()

            print(json.dumps(template_metadata, indent=2))

            # end-get_workspace_input_metadata

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_outputs_example(self):
        """
        get_workspace_outputs request example
        """
        try:
            print('\nget_workspace_outputs() result:')

            # begin-get_workspace_outputs

            response = schematics_service.get_workspace_outputs(
                w_id='testString',
            )
            list_output_values_inner = response.get_result()

            print(json.dumps(list_output_values_inner, indent=2))

            # end-get_workspace_outputs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_resources_example(self):
        """
        get_workspace_resources request example
        """
        try:
            print('\nget_workspace_resources() result:')

            # begin-get_workspace_resources

            response = schematics_service.get_workspace_resources(
                w_id='testString',
            )
            list_template_resources = response.get_result()

            print(json.dumps(list_template_resources, indent=2))

            # end-get_workspace_resources

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_state_example(self):
        """
        get_workspace_state request example
        """
        try:
            print('\nget_workspace_state() result:')

            # begin-get_workspace_state

            response = schematics_service.get_workspace_state(
                w_id='testString',
            )
            state_store_response_list = response.get_result()

            print(json.dumps(state_store_response_list, indent=2))

            # end-get_workspace_state

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_template_state_example(self):
        """
        get_workspace_template_state request example
        """
        try:
            print('\nget_workspace_template_state() result:')

            # begin-get_workspace_template_state

            response = schematics_service.get_workspace_template_state(
                w_id='testString',
                t_id='testString',
            )
            template_state_store = response.get_result()

            print(json.dumps(template_state_store, indent=2))

            # end-get_workspace_template_state

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_activity_logs_example(self):
        """
        get_workspace_activity_logs request example
        """
        try:
            print('\nget_workspace_activity_logs() result:')

            # begin-get_workspace_activity_logs

            response = schematics_service.get_workspace_activity_logs(
                w_id='testString',
                activity_id='testString',
            )
            workspace_activity_logs = response.get_result()

            print(json.dumps(workspace_activity_logs, indent=2))

            # end-get_workspace_activity_logs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_log_urls_example(self):
        """
        get_workspace_log_urls request example
        """
        try:
            print('\nget_workspace_log_urls() result:')

            # begin-get_workspace_log_urls

            response = schematics_service.get_workspace_log_urls(
                w_id='testString',
            )
            log_store_response_list = response.get_result()

            print(json.dumps(log_store_response_list, indent=2))

            # end-get_workspace_log_urls

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_template_logs_example(self):
        """
        get_template_logs request example
        """
        try:
            print('\nget_template_logs() result:')

            # begin-get_template_logs

            response = schematics_service.get_template_logs(
                w_id='testString',
                t_id='testString',
            )
            template_log_store_string = response.get_result()

            print(json.dumps(template_log_store_string, indent=2))

            # end-get_template_logs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_template_activity_log_example(self):
        """
        get_template_activity_log request example
        """
        try:
            print('\nget_template_activity_log() result:')

            # begin-get_template_activity_log

            response = schematics_service.get_template_activity_log(
                w_id='testString',
                t_id='testString',
                activity_id='testString',
            )
            workspace_activity_template_log_string = response.get_result()

            print(json.dumps(workspace_activity_template_log_string, indent=2))

            # end-get_template_activity_log

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_actions_example(self):
        """
        list_actions request example
        """
        try:
            print('\nlist_actions() result:')

            # begin-list_actions

            response = schematics_service.list_actions()
            action_list = response.get_result()

            print(json.dumps(action_list, indent=2))

            # end-list_actions

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_action_example(self):
        """
        create_action request example
        """
        try:
            print('\ncreate_action() result:')

            # begin-create_action

            response = schematics_service.create_action()
            action = response.get_result()

            print(json.dumps(action, indent=2))

            # end-create_action

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_action_example(self):
        """
        get_action request example
        """
        try:
            print('\nget_action() result:')

            # begin-get_action

            response = schematics_service.get_action(
                action_id='testString',
            )
            action = response.get_result()

            print(json.dumps(action, indent=2))

            # end-get_action

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_action_example(self):
        """
        update_action request example
        """
        try:
            print('\nupdate_action() result:')

            # begin-update_action

            response = schematics_service.update_action(
                action_id='testString',
            )
            action = response.get_result()

            print(json.dumps(action, indent=2))

            # end-update_action

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_upload_template_tar_action_example(self):
        """
        upload_template_tar_action request example
        """
        try:
            print('\nupload_template_tar_action() result:')

            # begin-upload_template_tar_action

            response = schematics_service.upload_template_tar_action(
                action_id='testString',
            )
            template_repo_tar_upload_response = response.get_result()

            print(json.dumps(template_repo_tar_upload_response, indent=2))

            # end-upload_template_tar_action

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_workspace_activities_example(self):
        """
        list_workspace_activities request example
        """
        try:
            print('\nlist_workspace_activities() result:')

            # begin-list_workspace_activities

            response = schematics_service.list_workspace_activities(
                w_id='testString',
            )
            workspace_activities = response.get_result()

            print(json.dumps(workspace_activities, indent=2))

            # end-list_workspace_activities

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_activity_example(self):
        """
        get_workspace_activity request example
        """
        try:
            print('\nget_workspace_activity() result:')

            # begin-get_workspace_activity

            response = schematics_service.get_workspace_activity(
                w_id='testString',
                activity_id='testString',
            )
            workspace_activity = response.get_result()

            print(json.dumps(workspace_activity, indent=2))

            # end-get_workspace_activity

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_run_workspace_commands_example(self):
        """
        run_workspace_commands request example
        """
        try:
            print('\nrun_workspace_commands() result:')

            # begin-run_workspace_commands

            response = schematics_service.run_workspace_commands(
                w_id='testString',
                refresh_token='testString',
            )
            workspace_activity_command_result = response.get_result()

            print(json.dumps(workspace_activity_command_result, indent=2))

            # end-run_workspace_commands

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_apply_workspace_command_example(self):
        """
        apply_workspace_command request example
        """
        try:
            print('\napply_workspace_command() result:')

            # begin-apply_workspace_command

            response = schematics_service.apply_workspace_command(
                w_id='testString',
                refresh_token='testString',
            )
            workspace_activity_apply_result = response.get_result()

            print(json.dumps(workspace_activity_apply_result, indent=2))

            # end-apply_workspace_command

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_destroy_workspace_command_example(self):
        """
        destroy_workspace_command request example
        """
        try:
            print('\ndestroy_workspace_command() result:')

            # begin-destroy_workspace_command

            response = schematics_service.destroy_workspace_command(
                w_id='testString',
                refresh_token='testString',
            )
            workspace_activity_destroy_result = response.get_result()

            print(json.dumps(workspace_activity_destroy_result, indent=2))

            # end-destroy_workspace_command

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_plan_workspace_command_example(self):
        """
        plan_workspace_command request example
        """
        try:
            print('\nplan_workspace_command() result:')

            # begin-plan_workspace_command

            response = schematics_service.plan_workspace_command(
                w_id='testString',
                refresh_token='testString',
            )
            workspace_activity_plan_result = response.get_result()

            print(json.dumps(workspace_activity_plan_result, indent=2))

            # end-plan_workspace_command

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_refresh_workspace_command_example(self):
        """
        refresh_workspace_command request example
        """
        try:
            print('\nrefresh_workspace_command() result:')

            # begin-refresh_workspace_command

            response = schematics_service.refresh_workspace_command(
                w_id='testString',
                refresh_token='testString',
            )
            workspace_activity_refresh_result = response.get_result()

            print(json.dumps(workspace_activity_refresh_result, indent=2))

            # end-refresh_workspace_command

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_jobs_example(self):
        """
        list_jobs request example
        """
        try:
            print('\nlist_jobs() result:')

            # begin-list_jobs

            response = schematics_service.list_jobs()
            job_list = response.get_result()

            print(json.dumps(job_list, indent=2))

            # end-list_jobs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_job_example(self):
        """
        create_job request example
        """
        try:
            print('\ncreate_job() result:')

            # begin-create_job

            response = schematics_service.create_job(
                refresh_token='testString',
            )
            job = response.get_result()

            print(json.dumps(job, indent=2))

            # end-create_job

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_job_example(self):
        """
        get_job request example
        """
        try:
            print('\nget_job() result:')

            # begin-get_job

            response = schematics_service.get_job(
                job_id='testString',
            )
            job = response.get_result()

            print(json.dumps(job, indent=2))

            # end-get_job

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_job_example(self):
        """
        update_job request example
        """
        try:
            print('\nupdate_job() result:')

            # begin-update_job

            response = schematics_service.update_job(
                job_id='testString',
                refresh_token='testString',
            )
            job = response.get_result()

            print(json.dumps(job, indent=2))

            # end-update_job

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_job_logs_example(self):
        """
        list_job_logs request example
        """
        try:
            print('\nlist_job_logs() result:')

            # begin-list_job_logs

            response = schematics_service.list_job_logs(
                job_id='testString',
            )
            job_log = response.get_result()

            print(json.dumps(job_log, indent=2))

            # end-list_job_logs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_job_files_example(self):
        """
        get_job_files request example
        """
        try:
            print('\nget_job_files() result:')

            # begin-get_job_files

            response = schematics_service.get_job_files(
                job_id='testString',
                file_type='template_repo',
            )
            job_file_data = response.get_result()

            print(json.dumps(job_file_data, indent=2))

            # end-get_job_files

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_workspace_deletion_job_example(self):
        """
        create_workspace_deletion_job request example
        """
        try:
            print('\ncreate_workspace_deletion_job() result:')

            # begin-create_workspace_deletion_job

            response = schematics_service.create_workspace_deletion_job(
                refresh_token='testString',
            )
            workspace_bulk_delete_response = response.get_result()

            print(json.dumps(workspace_bulk_delete_response, indent=2))

            # end-create_workspace_deletion_job

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_workspace_deletion_job_status_example(self):
        """
        get_workspace_deletion_job_status request example
        """
        try:
            print('\nget_workspace_deletion_job_status() result:')

            # begin-get_workspace_deletion_job_status

            response = schematics_service.get_workspace_deletion_job_status(
                wj_id='testString',
            )
            workspace_job_response = response.get_result()

            print(json.dumps(workspace_job_response, indent=2))

            # end-get_workspace_deletion_job_status

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_inventories_example(self):
        """
        list_inventories request example
        """
        try:
            print('\nlist_inventories() result:')

            # begin-list_inventories

            response = schematics_service.list_inventories()
            inventory_resource_record_list = response.get_result()

            print(json.dumps(inventory_resource_record_list, indent=2))

            # end-list_inventories

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_inventory_example(self):
        """
        create_inventory request example
        """
        try:
            print('\ncreate_inventory() result:')

            # begin-create_inventory

            response = schematics_service.create_inventory()
            inventory_resource_record = response.get_result()

            print(json.dumps(inventory_resource_record, indent=2))

            # end-create_inventory

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_inventory_example(self):
        """
        get_inventory request example
        """
        try:
            print('\nget_inventory() result:')

            # begin-get_inventory

            response = schematics_service.get_inventory(
                inventory_id='testString',
            )
            inventory_resource_record = response.get_result()

            print(json.dumps(inventory_resource_record, indent=2))

            # end-get_inventory

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_inventory_example(self):
        """
        replace_inventory request example
        """
        try:
            print('\nreplace_inventory() result:')

            # begin-replace_inventory

            response = schematics_service.replace_inventory(
                inventory_id='testString',
            )
            inventory_resource_record = response.get_result()

            print(json.dumps(inventory_resource_record, indent=2))

            # end-replace_inventory

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_resource_query_example(self):
        """
        list_resource_query request example
        """
        try:
            print('\nlist_resource_query() result:')

            # begin-list_resource_query

            response = schematics_service.list_resource_query()
            resource_query_record_list = response.get_result()

            print(json.dumps(resource_query_record_list, indent=2))

            # end-list_resource_query

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_resource_query_example(self):
        """
        create_resource_query request example
        """
        try:
            print('\ncreate_resource_query() result:')

            # begin-create_resource_query

            response = schematics_service.create_resource_query()
            resource_query_record = response.get_result()

            print(json.dumps(resource_query_record, indent=2))

            # end-create_resource_query

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_resources_query_example(self):
        """
        get_resources_query request example
        """
        try:
            print('\nget_resources_query() result:')

            # begin-get_resources_query

            response = schematics_service.get_resources_query(
                query_id='testString',
            )
            resource_query_record = response.get_result()

            print(json.dumps(resource_query_record, indent=2))

            # end-get_resources_query

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_resources_query_example(self):
        """
        replace_resources_query request example
        """
        try:
            print('\nreplace_resources_query() result:')

            # begin-replace_resources_query

            response = schematics_service.replace_resources_query(
                query_id='testString',
            )
            resource_query_record = response.get_result()

            print(json.dumps(resource_query_record, indent=2))

            # end-replace_resources_query

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_execute_resource_query_example(self):
        """
        execute_resource_query request example
        """
        try:
            print('\nexecute_resource_query() result:')

            # begin-execute_resource_query

            response = schematics_service.execute_resource_query(
                query_id='testString',
            )
            resource_query_response_record = response.get_result()

            print(json.dumps(resource_query_response_record, indent=2))

            # end-execute_resource_query

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_agent_example(self):
        """
        list_agent request example
        """
        try:
            print('\nlist_agent() result:')

            # begin-list_agent

            response = schematics_service.list_agent()
            agent_list = response.get_result()

            print(json.dumps(agent_list, indent=2))

            # end-list_agent

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_register_agent_example(self):
        """
        register_agent request example
        """
        try:
            print('\nregister_agent() result:')

            # begin-register_agent

            response = schematics_service.register_agent(
                name='MyDevAgent',
                agent_location='us-south',
                location='us-south',
                profile_id='testString',
            )
            agent = response.get_result()

            print(json.dumps(agent, indent=2))

            # end-register_agent

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_agent_example(self):
        """
        get_agent request example
        """
        try:
            print('\nget_agent() result:')

            # begin-get_agent

            response = schematics_service.get_agent(
                agent_id='testString',
            )
            agent = response.get_result()

            print(json.dumps(agent, indent=2))

            # end-get_agent

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_agent_registration_example(self):
        """
        update_agent_registration request example
        """
        try:
            print('\nupdate_agent_registration() result:')

            # begin-update_agent_registration

            response = schematics_service.update_agent_registration(
                agent_id='testString',
                name='MyDevAgent',
                agent_location='us-south',
                location='us-south',
                profile_id='testString',
            )
            agent = response.get_result()

            print(json.dumps(agent, indent=2))

            # end-update_agent_registration

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_agent_data_example(self):
        """
        list_agent_data request example
        """
        try:
            print('\nlist_agent_data() result:')

            # begin-list_agent_data

            response = schematics_service.list_agent_data()
            agent_data_list = response.get_result()

            print(json.dumps(agent_data_list, indent=2))

            # end-list_agent_data

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_agent_data_example(self):
        """
        create_agent_data request example
        """
        try:
            print('\ncreate_agent_data() result:')

            # begin-create_agent_data

            agent_infrastructure_model = {}

            response = schematics_service.create_agent_data(
                name='MyDevAgent',
                resource_group='Default',
                version='v1.0.0',
                schematics_location='us-south',
                agent_location='us-south',
                agent_infrastructure=agent_infrastructure_model,
            )
            agent_data = response.get_result()

            print(json.dumps(agent_data, indent=2))

            # end-create_agent_data

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_agent_data_example(self):
        """
        get_agent_data request example
        """
        try:
            print('\nget_agent_data() result:')

            # begin-get_agent_data

            response = schematics_service.get_agent_data(
                agent_id='testString',
            )
            agent_data = response.get_result()

            print(json.dumps(agent_data, indent=2))

            # end-get_agent_data

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_agent_data_example(self):
        """
        update_agent_data request example
        """
        try:
            print('\nupdate_agent_data() result:')

            # begin-update_agent_data

            agent_infrastructure_model = {}

            response = schematics_service.update_agent_data(
                agent_id='testString',
                name='MyDevAgent',
                resource_group='Default',
                version='v1.0.0',
                schematics_location='us-south',
                agent_location='us-south',
                agent_infrastructure=agent_infrastructure_model,
            )
            agent_data = response.get_result()

            print(json.dumps(agent_data, indent=2))

            # end-update_agent_data

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_agent_versions_example(self):
        """
        get_agent_versions request example
        """
        try:
            print('\nget_agent_versions() result:')

            # begin-get_agent_versions

            response = schematics_service.get_agent_versions()
            agent_versions = response.get_result()

            print(json.dumps(agent_versions, indent=2))

            # end-get_agent_versions

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_prs_agent_job_example(self):
        """
        get_prs_agent_job request example
        """
        try:
            print('\nget_prs_agent_job() result:')

            # begin-get_prs_agent_job

            response = schematics_service.get_prs_agent_job(
                agent_id='testString',
            )
            agent_prs_job = response.get_result()

            print(json.dumps(agent_prs_job, indent=2))

            # end-get_prs_agent_job

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_prs_agent_job_example(self):
        """
        prs_agent_job request example
        """
        try:
            print('\nprs_agent_job() result:')

            # begin-prs_agent_job

            response = schematics_service.prs_agent_job(
                agent_id='testString',
            )
            agent_prs_job = response.get_result()

            print(json.dumps(agent_prs_job, indent=2))

            # end-prs_agent_job

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_health_check_agent_job_example(self):
        """
        get_health_check_agent_job request example
        """
        try:
            print('\nget_health_check_agent_job() result:')

            # begin-get_health_check_agent_job

            response = schematics_service.get_health_check_agent_job(
                agent_id='testString',
            )
            agent_health_job = response.get_result()

            print(json.dumps(agent_health_job, indent=2))

            # end-get_health_check_agent_job

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_health_check_agent_job_example(self):
        """
        health_check_agent_job request example
        """
        try:
            print('\nhealth_check_agent_job() result:')

            # begin-health_check_agent_job

            response = schematics_service.health_check_agent_job(
                agent_id='testString',
            )
            agent_health_job = response.get_result()

            print(json.dumps(agent_health_job, indent=2))

            # end-health_check_agent_job

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_deploy_agent_job_example(self):
        """
        get_deploy_agent_job request example
        """
        try:
            print('\nget_deploy_agent_job() result:')

            # begin-get_deploy_agent_job

            response = schematics_service.get_deploy_agent_job(
                agent_id='testString',
            )
            agent_deploy_job = response.get_result()

            print(json.dumps(agent_deploy_job, indent=2))

            # end-get_deploy_agent_job

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_deploy_agent_job_example(self):
        """
        deploy_agent_job request example
        """
        try:
            print('\ndeploy_agent_job() result:')

            # begin-deploy_agent_job

            response = schematics_service.deploy_agent_job(
                agent_id='testString',
            )
            agent_deploy_job = response.get_result()

            print(json.dumps(agent_deploy_job, indent=2))

            # end-deploy_agent_job

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_kms_settings_example(self):
        """
        get_kms_settings request example
        """
        try:
            print('\nget_kms_settings() result:')

            # begin-get_kms_settings

            response = schematics_service.get_kms_settings(
                location='testString',
            )
            kms_settings = response.get_result()

            print(json.dumps(kms_settings, indent=2))

            # end-get_kms_settings

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_kms_settings_example(self):
        """
        update_kms_settings request example
        """
        try:
            print('\nupdate_kms_settings() result:')

            # begin-update_kms_settings

            response = schematics_service.update_kms_settings()
            kms_settings = response.get_result()

            print(json.dumps(kms_settings, indent=2))

            # end-update_kms_settings

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_kms_example(self):
        """
        list_kms request example
        """
        try:
            print('\nlist_kms() result:')

            # begin-list_kms

            response = schematics_service.list_kms(
                encryption_scheme='testString',
                location='testString',
            )
            kms_discovery = response.get_result()

            print(json.dumps(kms_discovery, indent=2))

            # end-list_kms

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_policy_example(self):
        """
        list_policy request example
        """
        try:
            print('\nlist_policy() result:')

            # begin-list_policy

            response = schematics_service.list_policy()
            policy_list = response.get_result()

            print(json.dumps(policy_list, indent=2))

            # end-list_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_policy_example(self):
        """
        create_policy request example
        """
        try:
            print('\ncreate_policy() result:')

            # begin-create_policy

            response = schematics_service.create_policy()
            policy = response.get_result()

            print(json.dumps(policy, indent=2))

            # end-create_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_policy_example(self):
        """
        get_policy request example
        """
        try:
            print('\nget_policy() result:')

            # begin-get_policy

            response = schematics_service.get_policy(
                policy_id='testString',
            )
            policy = response.get_result()

            print(json.dumps(policy, indent=2))

            # end-get_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_policy_example(self):
        """
        update_policy request example
        """
        try:
            print('\nupdate_policy() result:')

            # begin-update_policy

            response = schematics_service.update_policy(
                policy_id='testString',
            )
            policy = response.get_result()

            print(json.dumps(policy, indent=2))

            # end-update_policy

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_workspace_example(self):
        """
        delete_workspace request example
        """
        try:
            print('\ndelete_workspace() result:')

            # begin-delete_workspace

            response = schematics_service.delete_workspace(
                refresh_token='testString',
                w_id='testString',
            )
            workspace_delete_response = response.get_result()

            print(json.dumps(workspace_delete_response, indent=2))

            # end-delete_workspace

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_action_example(self):
        """
        delete_action request example
        """
        try:
            # begin-delete_action

            response = schematics_service.delete_action(
                action_id='testString',
            )

            # end-delete_action
            print('\ndelete_action() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_workspace_activity_example(self):
        """
        delete_workspace_activity request example
        """
        try:
            print('\ndelete_workspace_activity() result:')

            # begin-delete_workspace_activity

            response = schematics_service.delete_workspace_activity(
                w_id='testString',
                activity_id='testString',
            )
            workspace_activity_apply_result = response.get_result()

            print(json.dumps(workspace_activity_apply_result, indent=2))

            # end-delete_workspace_activity

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_job_example(self):
        """
        delete_job request example
        """
        try:
            # begin-delete_job

            response = schematics_service.delete_job(
                job_id='testString',
                refresh_token='testString',
            )

            # end-delete_job
            print('\ndelete_job() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_inventory_example(self):
        """
        delete_inventory request example
        """
        try:
            # begin-delete_inventory

            response = schematics_service.delete_inventory(
                inventory_id='testString',
            )

            # end-delete_inventory
            print('\ndelete_inventory() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_resources_query_example(self):
        """
        delete_resources_query request example
        """
        try:
            # begin-delete_resources_query

            response = schematics_service.delete_resources_query(
                query_id='testString',
            )

            # end-delete_resources_query
            print('\ndelete_resources_query() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_agent_example(self):
        """
        delete_agent request example
        """
        try:
            # begin-delete_agent

            response = schematics_service.delete_agent(
                agent_id='testString',
            )

            # end-delete_agent
            print('\ndelete_agent() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_agent_data_example(self):
        """
        delete_agent_data request example
        """
        try:
            # begin-delete_agent_data

            response = schematics_service.delete_agent_data(
                agent_id='testString',
            )

            # end-delete_agent_data
            print('\ndelete_agent_data() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_agent_resources_example(self):
        """
        delete_agent_resources request example
        """
        try:
            # begin-delete_agent_resources

            response = schematics_service.delete_agent_resources(
                agent_id='testString',
                refresh_token='testString',
            )

            # end-delete_agent_resources
            print('\ndelete_agent_resources() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_policy_example(self):
        """
        delete_policy request example
        """
        try:
            # begin-delete_policy

            response = schematics_service.delete_policy(
                policy_id='testString',
            )

            # end-delete_policy
            print('\ndelete_policy() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: SchematicsV1
##############################################################################
