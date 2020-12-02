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
Unit Tests for SchematicsV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import base64
import inspect
import io
import json
import pytest
import re
import requests
import responses
import tempfile
import urllib
from ibm_schematics.schematics_v1 import *


service = SchematicsV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://schematics-dev.containers.appdomain.cloud'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Schematics
##############################################################################
# region

class TestListSchematicsLocation():
    """
    Test Class for list_schematics_location
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_schematics_location_all_params(self):
        """
        list_schematics_location()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/locations')
        mock_response = '[{"country": "country", "geography": "geography", "id": "id", "kind": "kind", "metro": "metro", "multizone_metro": "multizone_metro", "name": "name"}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_schematics_location()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestListResourceGroup():
    """
    Test Class for list_resource_group
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_resource_group_all_params(self):
        """
        list_resource_group()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/resource_groups')
        mock_response = '[{"account_id": "account_id", "crn": "crn", "default": false, "name": "name", "resource_group_id": "resource_group_id", "state": "state"}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_resource_group()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestGetSchematicsVersion():
    """
    Test Class for get_schematics_version
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_schematics_version_all_params(self):
        """
        get_schematics_version()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/version')
        mock_response = '{"builddate": "builddate", "buildno": "buildno", "commitsha": "commitsha", "helm_provider_version": "helm_provider_version", "helm_version": "helm_version", "supported_template_types": [{"anyKey": "anyValue"}], "terraform_provider_version": "terraform_provider_version", "terraform_version": "terraform_version"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_schematics_version()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: Schematics
##############################################################################

##############################################################################
# Start of Service: Workspaces
##############################################################################
# region

class TestListWorkspaces():
    """
    Test Class for list_workspaces
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_workspaces_all_params(self):
        """
        list_workspaces()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces')
        mock_response = '{"count": 5, "limit": 5, "offset": 6, "workspaces": [{"applied_shareddata_ids": ["applied_shareddata_ids"], "catalog_ref": {"dry_run": false, "item_icon_url": "item_icon_url", "item_id": "item_id", "item_name": "item_name", "item_readme_url": "item_readme_url", "item_url": "item_url", "launch_url": "launch_url", "offering_version": "offering_version"}, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "crn": "crn", "description": "description", "id": "id", "last_health_check_at": "2019-01-01T12:00:00", "location": "location", "name": "name", "resource_group": "resource_group", "runtime_data": [{"engine_cmd": "engine_cmd", "engine_name": "engine_name", "engine_version": "engine_version", "id": "id", "log_store_url": "log_store_url", "output_values": [{"anyKey": "anyValue"}], "resources": [[{"anyKey": "anyValue"}]], "state_store_url": "state_store_url"}], "shared_data": {"cluster_id": "cluster_id", "cluster_name": "cluster_name", "entitlement_keys": [{"anyKey": "anyValue"}], "namespace": "namespace", "region": "region", "resource_group_id": "resource_group_id"}, "status": "status", "tags": ["tags"], "template_data": [{"env_values": [{"hidden": true, "name": "name", "secure": true, "value": "value"}], "folder": "folder", "has_githubtoken": false, "id": "id", "template_type": "template_type", "uninstall_script_name": "uninstall_script_name", "values": "values", "values_metadata": [{"anyKey": "anyValue"}], "values_url": "values_url", "variablestore": [{"description": "description", "name": "name", "secure": true, "type": "type", "value": "value"}]}], "template_ref": "template_ref", "template_repo": {"branch": "branch", "full_url": "full_url", "has_uploadedgitrepotar": true, "release": "release", "repo_sha_value": "repo_sha_value", "repo_url": "repo_url", "url": "url"}, "type": ["type"], "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "workspace_status": {"frozen": true, "frozen_at": "2019-01-01T12:00:00", "frozen_by": "frozen_by", "locked": true, "locked_by": "locked_by", "locked_time": "2019-01-01T12:00:00"}, "workspace_status_msg": {"status_code": "status_code", "status_msg": "status_msg"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        offset = 0
        limit = 1

        # Invoke method
        response = service.list_workspaces(
            offset=offset,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'offset={}'.format(offset) in query_string
        assert 'limit={}'.format(limit) in query_string


    @responses.activate
    def test_list_workspaces_required_params(self):
        """
        test_list_workspaces_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces')
        mock_response = '{"count": 5, "limit": 5, "offset": 6, "workspaces": [{"applied_shareddata_ids": ["applied_shareddata_ids"], "catalog_ref": {"dry_run": false, "item_icon_url": "item_icon_url", "item_id": "item_id", "item_name": "item_name", "item_readme_url": "item_readme_url", "item_url": "item_url", "launch_url": "launch_url", "offering_version": "offering_version"}, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "crn": "crn", "description": "description", "id": "id", "last_health_check_at": "2019-01-01T12:00:00", "location": "location", "name": "name", "resource_group": "resource_group", "runtime_data": [{"engine_cmd": "engine_cmd", "engine_name": "engine_name", "engine_version": "engine_version", "id": "id", "log_store_url": "log_store_url", "output_values": [{"anyKey": "anyValue"}], "resources": [[{"anyKey": "anyValue"}]], "state_store_url": "state_store_url"}], "shared_data": {"cluster_id": "cluster_id", "cluster_name": "cluster_name", "entitlement_keys": [{"anyKey": "anyValue"}], "namespace": "namespace", "region": "region", "resource_group_id": "resource_group_id"}, "status": "status", "tags": ["tags"], "template_data": [{"env_values": [{"hidden": true, "name": "name", "secure": true, "value": "value"}], "folder": "folder", "has_githubtoken": false, "id": "id", "template_type": "template_type", "uninstall_script_name": "uninstall_script_name", "values": "values", "values_metadata": [{"anyKey": "anyValue"}], "values_url": "values_url", "variablestore": [{"description": "description", "name": "name", "secure": true, "type": "type", "value": "value"}]}], "template_ref": "template_ref", "template_repo": {"branch": "branch", "full_url": "full_url", "has_uploadedgitrepotar": true, "release": "release", "repo_sha_value": "repo_sha_value", "repo_url": "repo_url", "url": "url"}, "type": ["type"], "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "workspace_status": {"frozen": true, "frozen_at": "2019-01-01T12:00:00", "frozen_by": "frozen_by", "locked": true, "locked_by": "locked_by", "locked_time": "2019-01-01T12:00:00"}, "workspace_status_msg": {"status_code": "status_code", "status_msg": "status_msg"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_workspaces()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestCreateWorkspace():
    """
    Test Class for create_workspace
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_workspace_all_params(self):
        """
        create_workspace()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces')
        mock_response = '{"applied_shareddata_ids": ["applied_shareddata_ids"], "catalog_ref": {"dry_run": false, "item_icon_url": "item_icon_url", "item_id": "item_id", "item_name": "item_name", "item_readme_url": "item_readme_url", "item_url": "item_url", "launch_url": "launch_url", "offering_version": "offering_version"}, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "crn": "crn", "description": "description", "id": "id", "last_health_check_at": "2019-01-01T12:00:00", "location": "location", "name": "name", "resource_group": "resource_group", "runtime_data": [{"engine_cmd": "engine_cmd", "engine_name": "engine_name", "engine_version": "engine_version", "id": "id", "log_store_url": "log_store_url", "output_values": [{"anyKey": "anyValue"}], "resources": [[{"anyKey": "anyValue"}]], "state_store_url": "state_store_url"}], "shared_data": {"cluster_id": "cluster_id", "cluster_name": "cluster_name", "entitlement_keys": [{"anyKey": "anyValue"}], "namespace": "namespace", "region": "region", "resource_group_id": "resource_group_id"}, "status": "status", "tags": ["tags"], "template_data": [{"env_values": [{"hidden": true, "name": "name", "secure": true, "value": "value"}], "folder": "folder", "has_githubtoken": false, "id": "id", "template_type": "template_type", "uninstall_script_name": "uninstall_script_name", "values": "values", "values_metadata": [{"anyKey": "anyValue"}], "values_url": "values_url", "variablestore": [{"description": "description", "name": "name", "secure": true, "type": "type", "value": "value"}]}], "template_ref": "template_ref", "template_repo": {"branch": "branch", "full_url": "full_url", "has_uploadedgitrepotar": true, "release": "release", "repo_sha_value": "repo_sha_value", "repo_url": "repo_url", "url": "url"}, "type": ["type"], "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "workspace_status": {"frozen": true, "frozen_at": "2019-01-01T12:00:00", "frozen_by": "frozen_by", "locked": true, "locked_by": "locked_by", "locked_time": "2019-01-01T12:00:00"}, "workspace_status_msg": {"status_code": "status_code", "status_msg": "status_msg"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a CatalogRef model
        catalog_ref_model = {}
        catalog_ref_model['dry_run'] = True
        catalog_ref_model['item_icon_url'] = 'testString'
        catalog_ref_model['item_id'] = 'testString'
        catalog_ref_model['item_name'] = 'testString'
        catalog_ref_model['item_readme_url'] = 'testString'
        catalog_ref_model['item_url'] = 'testString'
        catalog_ref_model['launch_url'] = 'testString'
        catalog_ref_model['offering_version'] = 'testString'

        # Construct a dict representation of a SharedTargetData model
        shared_target_data_model = {}
        shared_target_data_model['cluster_created_on'] = 'testString'
        shared_target_data_model['cluster_id'] = 'testString'
        shared_target_data_model['cluster_name'] = 'testString'
        shared_target_data_model['cluster_type'] = 'testString'
        shared_target_data_model['entitlement_keys'] = [{ 'foo': 'bar' }]
        shared_target_data_model['namespace'] = 'testString'
        shared_target_data_model['region'] = 'testString'
        shared_target_data_model['resource_group_id'] = 'testString'
        shared_target_data_model['worker_count'] = 26
        shared_target_data_model['worker_machine_type'] = 'testString'

        # Construct a dict representation of a WorkspaceVariableRequest model
        workspace_variable_request_model = {}
        workspace_variable_request_model['description'] = 'testString'
        workspace_variable_request_model['name'] = 'testString'
        workspace_variable_request_model['secure'] = True
        workspace_variable_request_model['type'] = 'testString'
        workspace_variable_request_model['use_default'] = True
        workspace_variable_request_model['value'] = 'testString'

        # Construct a dict representation of a TemplateSourceDataRequest model
        template_source_data_request_model = {}
        template_source_data_request_model['env_values'] = [{ 'foo': 'bar' }]
        template_source_data_request_model['folder'] = 'testString'
        template_source_data_request_model['init_state_file'] = 'testString'
        template_source_data_request_model['type'] = 'testString'
        template_source_data_request_model['uninstall_script_name'] = 'testString'
        template_source_data_request_model['values'] = 'testString'
        template_source_data_request_model['values_metadata'] = [{ 'foo': 'bar' }]
        template_source_data_request_model['variablestore'] = [workspace_variable_request_model]

        # Construct a dict representation of a TemplateRepoRequest model
        template_repo_request_model = {}
        template_repo_request_model['branch'] = 'testString'
        template_repo_request_model['release'] = 'testString'
        template_repo_request_model['repo_sha_value'] = 'testString'
        template_repo_request_model['repo_url'] = 'testString'
        template_repo_request_model['url'] = 'testString'

        # Construct a dict representation of a WorkspaceStatusRequest model
        workspace_status_request_model = {}
        workspace_status_request_model['frozen'] = True
        workspace_status_request_model['frozen_at'] = '2020-01-28T18:40:40.123456Z'
        workspace_status_request_model['frozen_by'] = 'testString'
        workspace_status_request_model['locked'] = True
        workspace_status_request_model['locked_by'] = 'testString'
        workspace_status_request_model['locked_time'] = '2020-01-28T18:40:40.123456Z'

        # Set up parameter values
        applied_shareddata_ids = ['testString']
        catalog_ref = catalog_ref_model
        description = 'testString'
        location = 'testString'
        name = 'testString'
        resource_group = 'testString'
        shared_data = shared_target_data_model
        tags = ['testString']
        template_data = [template_source_data_request_model]
        template_ref = 'testString'
        template_repo = template_repo_request_model
        type = ['testString']
        workspace_status = workspace_status_request_model
        x_github_token = 'testString'

        # Invoke method
        response = service.create_workspace(
            applied_shareddata_ids=applied_shareddata_ids,
            catalog_ref=catalog_ref,
            description=description,
            location=location,
            name=name,
            resource_group=resource_group,
            shared_data=shared_data,
            tags=tags,
            template_data=template_data,
            template_ref=template_ref,
            template_repo=template_repo,
            type=type,
            workspace_status=workspace_status,
            x_github_token=x_github_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['applied_shareddata_ids'] == ['testString']
        assert req_body['catalog_ref'] == catalog_ref_model
        assert req_body['description'] == 'testString'
        assert req_body['location'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['resource_group'] == 'testString'
        assert req_body['shared_data'] == shared_target_data_model
        assert req_body['tags'] == ['testString']
        assert req_body['template_data'] == [template_source_data_request_model]
        assert req_body['template_ref'] == 'testString'
        assert req_body['template_repo'] == template_repo_request_model
        assert req_body['type'] == ['testString']
        assert req_body['workspace_status'] == workspace_status_request_model


    @responses.activate
    def test_create_workspace_required_params(self):
        """
        test_create_workspace_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces')
        mock_response = '{"applied_shareddata_ids": ["applied_shareddata_ids"], "catalog_ref": {"dry_run": false, "item_icon_url": "item_icon_url", "item_id": "item_id", "item_name": "item_name", "item_readme_url": "item_readme_url", "item_url": "item_url", "launch_url": "launch_url", "offering_version": "offering_version"}, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "crn": "crn", "description": "description", "id": "id", "last_health_check_at": "2019-01-01T12:00:00", "location": "location", "name": "name", "resource_group": "resource_group", "runtime_data": [{"engine_cmd": "engine_cmd", "engine_name": "engine_name", "engine_version": "engine_version", "id": "id", "log_store_url": "log_store_url", "output_values": [{"anyKey": "anyValue"}], "resources": [[{"anyKey": "anyValue"}]], "state_store_url": "state_store_url"}], "shared_data": {"cluster_id": "cluster_id", "cluster_name": "cluster_name", "entitlement_keys": [{"anyKey": "anyValue"}], "namespace": "namespace", "region": "region", "resource_group_id": "resource_group_id"}, "status": "status", "tags": ["tags"], "template_data": [{"env_values": [{"hidden": true, "name": "name", "secure": true, "value": "value"}], "folder": "folder", "has_githubtoken": false, "id": "id", "template_type": "template_type", "uninstall_script_name": "uninstall_script_name", "values": "values", "values_metadata": [{"anyKey": "anyValue"}], "values_url": "values_url", "variablestore": [{"description": "description", "name": "name", "secure": true, "type": "type", "value": "value"}]}], "template_ref": "template_ref", "template_repo": {"branch": "branch", "full_url": "full_url", "has_uploadedgitrepotar": true, "release": "release", "repo_sha_value": "repo_sha_value", "repo_url": "repo_url", "url": "url"}, "type": ["type"], "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "workspace_status": {"frozen": true, "frozen_at": "2019-01-01T12:00:00", "frozen_by": "frozen_by", "locked": true, "locked_by": "locked_by", "locked_time": "2019-01-01T12:00:00"}, "workspace_status_msg": {"status_code": "status_code", "status_msg": "status_msg"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a CatalogRef model
        catalog_ref_model = {}
        catalog_ref_model['dry_run'] = True
        catalog_ref_model['item_icon_url'] = 'testString'
        catalog_ref_model['item_id'] = 'testString'
        catalog_ref_model['item_name'] = 'testString'
        catalog_ref_model['item_readme_url'] = 'testString'
        catalog_ref_model['item_url'] = 'testString'
        catalog_ref_model['launch_url'] = 'testString'
        catalog_ref_model['offering_version'] = 'testString'

        # Construct a dict representation of a SharedTargetData model
        shared_target_data_model = {}
        shared_target_data_model['cluster_created_on'] = 'testString'
        shared_target_data_model['cluster_id'] = 'testString'
        shared_target_data_model['cluster_name'] = 'testString'
        shared_target_data_model['cluster_type'] = 'testString'
        shared_target_data_model['entitlement_keys'] = [{ 'foo': 'bar' }]
        shared_target_data_model['namespace'] = 'testString'
        shared_target_data_model['region'] = 'testString'
        shared_target_data_model['resource_group_id'] = 'testString'
        shared_target_data_model['worker_count'] = 26
        shared_target_data_model['worker_machine_type'] = 'testString'

        # Construct a dict representation of a WorkspaceVariableRequest model
        workspace_variable_request_model = {}
        workspace_variable_request_model['description'] = 'testString'
        workspace_variable_request_model['name'] = 'testString'
        workspace_variable_request_model['secure'] = True
        workspace_variable_request_model['type'] = 'testString'
        workspace_variable_request_model['use_default'] = True
        workspace_variable_request_model['value'] = 'testString'

        # Construct a dict representation of a TemplateSourceDataRequest model
        template_source_data_request_model = {}
        template_source_data_request_model['env_values'] = [{ 'foo': 'bar' }]
        template_source_data_request_model['folder'] = 'testString'
        template_source_data_request_model['init_state_file'] = 'testString'
        template_source_data_request_model['type'] = 'testString'
        template_source_data_request_model['uninstall_script_name'] = 'testString'
        template_source_data_request_model['values'] = 'testString'
        template_source_data_request_model['values_metadata'] = [{ 'foo': 'bar' }]
        template_source_data_request_model['variablestore'] = [workspace_variable_request_model]

        # Construct a dict representation of a TemplateRepoRequest model
        template_repo_request_model = {}
        template_repo_request_model['branch'] = 'testString'
        template_repo_request_model['release'] = 'testString'
        template_repo_request_model['repo_sha_value'] = 'testString'
        template_repo_request_model['repo_url'] = 'testString'
        template_repo_request_model['url'] = 'testString'

        # Construct a dict representation of a WorkspaceStatusRequest model
        workspace_status_request_model = {}
        workspace_status_request_model['frozen'] = True
        workspace_status_request_model['frozen_at'] = '2020-01-28T18:40:40.123456Z'
        workspace_status_request_model['frozen_by'] = 'testString'
        workspace_status_request_model['locked'] = True
        workspace_status_request_model['locked_by'] = 'testString'
        workspace_status_request_model['locked_time'] = '2020-01-28T18:40:40.123456Z'

        # Set up parameter values
        applied_shareddata_ids = ['testString']
        catalog_ref = catalog_ref_model
        description = 'testString'
        location = 'testString'
        name = 'testString'
        resource_group = 'testString'
        shared_data = shared_target_data_model
        tags = ['testString']
        template_data = [template_source_data_request_model]
        template_ref = 'testString'
        template_repo = template_repo_request_model
        type = ['testString']
        workspace_status = workspace_status_request_model

        # Invoke method
        response = service.create_workspace(
            applied_shareddata_ids=applied_shareddata_ids,
            catalog_ref=catalog_ref,
            description=description,
            location=location,
            name=name,
            resource_group=resource_group,
            shared_data=shared_data,
            tags=tags,
            template_data=template_data,
            template_ref=template_ref,
            template_repo=template_repo,
            type=type,
            workspace_status=workspace_status,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['applied_shareddata_ids'] == ['testString']
        assert req_body['catalog_ref'] == catalog_ref_model
        assert req_body['description'] == 'testString'
        assert req_body['location'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['resource_group'] == 'testString'
        assert req_body['shared_data'] == shared_target_data_model
        assert req_body['tags'] == ['testString']
        assert req_body['template_data'] == [template_source_data_request_model]
        assert req_body['template_ref'] == 'testString'
        assert req_body['template_repo'] == template_repo_request_model
        assert req_body['type'] == ['testString']
        assert req_body['workspace_status'] == workspace_status_request_model


class TestGetWorkspace():
    """
    Test Class for get_workspace
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_workspace_all_params(self):
        """
        get_workspace()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString')
        mock_response = '{"applied_shareddata_ids": ["applied_shareddata_ids"], "catalog_ref": {"dry_run": false, "item_icon_url": "item_icon_url", "item_id": "item_id", "item_name": "item_name", "item_readme_url": "item_readme_url", "item_url": "item_url", "launch_url": "launch_url", "offering_version": "offering_version"}, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "crn": "crn", "description": "description", "id": "id", "last_health_check_at": "2019-01-01T12:00:00", "location": "location", "name": "name", "resource_group": "resource_group", "runtime_data": [{"engine_cmd": "engine_cmd", "engine_name": "engine_name", "engine_version": "engine_version", "id": "id", "log_store_url": "log_store_url", "output_values": [{"anyKey": "anyValue"}], "resources": [[{"anyKey": "anyValue"}]], "state_store_url": "state_store_url"}], "shared_data": {"cluster_id": "cluster_id", "cluster_name": "cluster_name", "entitlement_keys": [{"anyKey": "anyValue"}], "namespace": "namespace", "region": "region", "resource_group_id": "resource_group_id"}, "status": "status", "tags": ["tags"], "template_data": [{"env_values": [{"hidden": true, "name": "name", "secure": true, "value": "value"}], "folder": "folder", "has_githubtoken": false, "id": "id", "template_type": "template_type", "uninstall_script_name": "uninstall_script_name", "values": "values", "values_metadata": [{"anyKey": "anyValue"}], "values_url": "values_url", "variablestore": [{"description": "description", "name": "name", "secure": true, "type": "type", "value": "value"}]}], "template_ref": "template_ref", "template_repo": {"branch": "branch", "full_url": "full_url", "has_uploadedgitrepotar": true, "release": "release", "repo_sha_value": "repo_sha_value", "repo_url": "repo_url", "url": "url"}, "type": ["type"], "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "workspace_status": {"frozen": true, "frozen_at": "2019-01-01T12:00:00", "frozen_by": "frozen_by", "locked": true, "locked_by": "locked_by", "locked_time": "2019-01-01T12:00:00"}, "workspace_status_msg": {"status_code": "status_code", "status_msg": "status_msg"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'

        # Invoke method
        response = service.get_workspace(
            w_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_workspace_value_error(self):
        """
        test_get_workspace_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString')
        mock_response = '{"applied_shareddata_ids": ["applied_shareddata_ids"], "catalog_ref": {"dry_run": false, "item_icon_url": "item_icon_url", "item_id": "item_id", "item_name": "item_name", "item_readme_url": "item_readme_url", "item_url": "item_url", "launch_url": "launch_url", "offering_version": "offering_version"}, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "crn": "crn", "description": "description", "id": "id", "last_health_check_at": "2019-01-01T12:00:00", "location": "location", "name": "name", "resource_group": "resource_group", "runtime_data": [{"engine_cmd": "engine_cmd", "engine_name": "engine_name", "engine_version": "engine_version", "id": "id", "log_store_url": "log_store_url", "output_values": [{"anyKey": "anyValue"}], "resources": [[{"anyKey": "anyValue"}]], "state_store_url": "state_store_url"}], "shared_data": {"cluster_id": "cluster_id", "cluster_name": "cluster_name", "entitlement_keys": [{"anyKey": "anyValue"}], "namespace": "namespace", "region": "region", "resource_group_id": "resource_group_id"}, "status": "status", "tags": ["tags"], "template_data": [{"env_values": [{"hidden": true, "name": "name", "secure": true, "value": "value"}], "folder": "folder", "has_githubtoken": false, "id": "id", "template_type": "template_type", "uninstall_script_name": "uninstall_script_name", "values": "values", "values_metadata": [{"anyKey": "anyValue"}], "values_url": "values_url", "variablestore": [{"description": "description", "name": "name", "secure": true, "type": "type", "value": "value"}]}], "template_ref": "template_ref", "template_repo": {"branch": "branch", "full_url": "full_url", "has_uploadedgitrepotar": true, "release": "release", "repo_sha_value": "repo_sha_value", "repo_url": "repo_url", "url": "url"}, "type": ["type"], "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "workspace_status": {"frozen": true, "frozen_at": "2019-01-01T12:00:00", "frozen_by": "frozen_by", "locked": true, "locked_by": "locked_by", "locked_time": "2019-01-01T12:00:00"}, "workspace_status_msg": {"status_code": "status_code", "status_msg": "status_msg"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_workspace(**req_copy)



class TestReplaceWorkspace():
    """
    Test Class for replace_workspace
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_replace_workspace_all_params(self):
        """
        replace_workspace()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString')
        mock_response = '{"applied_shareddata_ids": ["applied_shareddata_ids"], "catalog_ref": {"dry_run": false, "item_icon_url": "item_icon_url", "item_id": "item_id", "item_name": "item_name", "item_readme_url": "item_readme_url", "item_url": "item_url", "launch_url": "launch_url", "offering_version": "offering_version"}, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "crn": "crn", "description": "description", "id": "id", "last_health_check_at": "2019-01-01T12:00:00", "location": "location", "name": "name", "resource_group": "resource_group", "runtime_data": [{"engine_cmd": "engine_cmd", "engine_name": "engine_name", "engine_version": "engine_version", "id": "id", "log_store_url": "log_store_url", "output_values": [{"anyKey": "anyValue"}], "resources": [[{"anyKey": "anyValue"}]], "state_store_url": "state_store_url"}], "shared_data": {"cluster_id": "cluster_id", "cluster_name": "cluster_name", "entitlement_keys": [{"anyKey": "anyValue"}], "namespace": "namespace", "region": "region", "resource_group_id": "resource_group_id"}, "status": "status", "tags": ["tags"], "template_data": [{"env_values": [{"hidden": true, "name": "name", "secure": true, "value": "value"}], "folder": "folder", "has_githubtoken": false, "id": "id", "template_type": "template_type", "uninstall_script_name": "uninstall_script_name", "values": "values", "values_metadata": [{"anyKey": "anyValue"}], "values_url": "values_url", "variablestore": [{"description": "description", "name": "name", "secure": true, "type": "type", "value": "value"}]}], "template_ref": "template_ref", "template_repo": {"branch": "branch", "full_url": "full_url", "has_uploadedgitrepotar": true, "release": "release", "repo_sha_value": "repo_sha_value", "repo_url": "repo_url", "url": "url"}, "type": ["type"], "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "workspace_status": {"frozen": true, "frozen_at": "2019-01-01T12:00:00", "frozen_by": "frozen_by", "locked": true, "locked_by": "locked_by", "locked_time": "2019-01-01T12:00:00"}, "workspace_status_msg": {"status_code": "status_code", "status_msg": "status_msg"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CatalogRef model
        catalog_ref_model = {}
        catalog_ref_model['dry_run'] = True
        catalog_ref_model['item_icon_url'] = 'testString'
        catalog_ref_model['item_id'] = 'testString'
        catalog_ref_model['item_name'] = 'testString'
        catalog_ref_model['item_readme_url'] = 'testString'
        catalog_ref_model['item_url'] = 'testString'
        catalog_ref_model['launch_url'] = 'testString'
        catalog_ref_model['offering_version'] = 'testString'

        # Construct a dict representation of a SharedTargetData model
        shared_target_data_model = {}
        shared_target_data_model['cluster_created_on'] = 'testString'
        shared_target_data_model['cluster_id'] = 'testString'
        shared_target_data_model['cluster_name'] = 'testString'
        shared_target_data_model['cluster_type'] = 'testString'
        shared_target_data_model['entitlement_keys'] = [{ 'foo': 'bar' }]
        shared_target_data_model['namespace'] = 'testString'
        shared_target_data_model['region'] = 'testString'
        shared_target_data_model['resource_group_id'] = 'testString'
        shared_target_data_model['worker_count'] = 26
        shared_target_data_model['worker_machine_type'] = 'testString'

        # Construct a dict representation of a WorkspaceVariableRequest model
        workspace_variable_request_model = {}
        workspace_variable_request_model['description'] = 'testString'
        workspace_variable_request_model['name'] = 'testString'
        workspace_variable_request_model['secure'] = True
        workspace_variable_request_model['type'] = 'testString'
        workspace_variable_request_model['use_default'] = True
        workspace_variable_request_model['value'] = 'testString'

        # Construct a dict representation of a TemplateSourceDataRequest model
        template_source_data_request_model = {}
        template_source_data_request_model['env_values'] = [{ 'foo': 'bar' }]
        template_source_data_request_model['folder'] = 'testString'
        template_source_data_request_model['init_state_file'] = 'testString'
        template_source_data_request_model['type'] = 'testString'
        template_source_data_request_model['uninstall_script_name'] = 'testString'
        template_source_data_request_model['values'] = 'testString'
        template_source_data_request_model['values_metadata'] = [{ 'foo': 'bar' }]
        template_source_data_request_model['variablestore'] = [workspace_variable_request_model]

        # Construct a dict representation of a TemplateRepoUpdateRequest model
        template_repo_update_request_model = {}
        template_repo_update_request_model['branch'] = 'testString'
        template_repo_update_request_model['release'] = 'testString'
        template_repo_update_request_model['repo_sha_value'] = 'testString'
        template_repo_update_request_model['repo_url'] = 'testString'
        template_repo_update_request_model['url'] = 'testString'

        # Construct a dict representation of a WorkspaceStatusUpdateRequest model
        workspace_status_update_request_model = {}
        workspace_status_update_request_model['frozen'] = True
        workspace_status_update_request_model['frozen_at'] = '2020-01-28T18:40:40.123456Z'
        workspace_status_update_request_model['frozen_by'] = 'testString'
        workspace_status_update_request_model['locked'] = True
        workspace_status_update_request_model['locked_by'] = 'testString'
        workspace_status_update_request_model['locked_time'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a WorkspaceStatusMessage model
        workspace_status_message_model = {}
        workspace_status_message_model['status_code'] = 'testString'
        workspace_status_message_model['status_msg'] = 'testString'

        # Set up parameter values
        w_id = 'testString'
        catalog_ref = catalog_ref_model
        description = 'testString'
        name = 'testString'
        shared_data = shared_target_data_model
        tags = ['testString']
        template_data = [template_source_data_request_model]
        template_repo = template_repo_update_request_model
        type = ['testString']
        workspace_status = workspace_status_update_request_model
        workspace_status_msg = workspace_status_message_model

        # Invoke method
        response = service.replace_workspace(
            w_id,
            catalog_ref=catalog_ref,
            description=description,
            name=name,
            shared_data=shared_data,
            tags=tags,
            template_data=template_data,
            template_repo=template_repo,
            type=type,
            workspace_status=workspace_status,
            workspace_status_msg=workspace_status_msg,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['catalog_ref'] == catalog_ref_model
        assert req_body['description'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['shared_data'] == shared_target_data_model
        assert req_body['tags'] == ['testString']
        assert req_body['template_data'] == [template_source_data_request_model]
        assert req_body['template_repo'] == template_repo_update_request_model
        assert req_body['type'] == ['testString']
        assert req_body['workspace_status'] == workspace_status_update_request_model
        assert req_body['workspace_status_msg'] == workspace_status_message_model


    @responses.activate
    def test_replace_workspace_value_error(self):
        """
        test_replace_workspace_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString')
        mock_response = '{"applied_shareddata_ids": ["applied_shareddata_ids"], "catalog_ref": {"dry_run": false, "item_icon_url": "item_icon_url", "item_id": "item_id", "item_name": "item_name", "item_readme_url": "item_readme_url", "item_url": "item_url", "launch_url": "launch_url", "offering_version": "offering_version"}, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "crn": "crn", "description": "description", "id": "id", "last_health_check_at": "2019-01-01T12:00:00", "location": "location", "name": "name", "resource_group": "resource_group", "runtime_data": [{"engine_cmd": "engine_cmd", "engine_name": "engine_name", "engine_version": "engine_version", "id": "id", "log_store_url": "log_store_url", "output_values": [{"anyKey": "anyValue"}], "resources": [[{"anyKey": "anyValue"}]], "state_store_url": "state_store_url"}], "shared_data": {"cluster_id": "cluster_id", "cluster_name": "cluster_name", "entitlement_keys": [{"anyKey": "anyValue"}], "namespace": "namespace", "region": "region", "resource_group_id": "resource_group_id"}, "status": "status", "tags": ["tags"], "template_data": [{"env_values": [{"hidden": true, "name": "name", "secure": true, "value": "value"}], "folder": "folder", "has_githubtoken": false, "id": "id", "template_type": "template_type", "uninstall_script_name": "uninstall_script_name", "values": "values", "values_metadata": [{"anyKey": "anyValue"}], "values_url": "values_url", "variablestore": [{"description": "description", "name": "name", "secure": true, "type": "type", "value": "value"}]}], "template_ref": "template_ref", "template_repo": {"branch": "branch", "full_url": "full_url", "has_uploadedgitrepotar": true, "release": "release", "repo_sha_value": "repo_sha_value", "repo_url": "repo_url", "url": "url"}, "type": ["type"], "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "workspace_status": {"frozen": true, "frozen_at": "2019-01-01T12:00:00", "frozen_by": "frozen_by", "locked": true, "locked_by": "locked_by", "locked_time": "2019-01-01T12:00:00"}, "workspace_status_msg": {"status_code": "status_code", "status_msg": "status_msg"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CatalogRef model
        catalog_ref_model = {}
        catalog_ref_model['dry_run'] = True
        catalog_ref_model['item_icon_url'] = 'testString'
        catalog_ref_model['item_id'] = 'testString'
        catalog_ref_model['item_name'] = 'testString'
        catalog_ref_model['item_readme_url'] = 'testString'
        catalog_ref_model['item_url'] = 'testString'
        catalog_ref_model['launch_url'] = 'testString'
        catalog_ref_model['offering_version'] = 'testString'

        # Construct a dict representation of a SharedTargetData model
        shared_target_data_model = {}
        shared_target_data_model['cluster_created_on'] = 'testString'
        shared_target_data_model['cluster_id'] = 'testString'
        shared_target_data_model['cluster_name'] = 'testString'
        shared_target_data_model['cluster_type'] = 'testString'
        shared_target_data_model['entitlement_keys'] = [{ 'foo': 'bar' }]
        shared_target_data_model['namespace'] = 'testString'
        shared_target_data_model['region'] = 'testString'
        shared_target_data_model['resource_group_id'] = 'testString'
        shared_target_data_model['worker_count'] = 26
        shared_target_data_model['worker_machine_type'] = 'testString'

        # Construct a dict representation of a WorkspaceVariableRequest model
        workspace_variable_request_model = {}
        workspace_variable_request_model['description'] = 'testString'
        workspace_variable_request_model['name'] = 'testString'
        workspace_variable_request_model['secure'] = True
        workspace_variable_request_model['type'] = 'testString'
        workspace_variable_request_model['use_default'] = True
        workspace_variable_request_model['value'] = 'testString'

        # Construct a dict representation of a TemplateSourceDataRequest model
        template_source_data_request_model = {}
        template_source_data_request_model['env_values'] = [{ 'foo': 'bar' }]
        template_source_data_request_model['folder'] = 'testString'
        template_source_data_request_model['init_state_file'] = 'testString'
        template_source_data_request_model['type'] = 'testString'
        template_source_data_request_model['uninstall_script_name'] = 'testString'
        template_source_data_request_model['values'] = 'testString'
        template_source_data_request_model['values_metadata'] = [{ 'foo': 'bar' }]
        template_source_data_request_model['variablestore'] = [workspace_variable_request_model]

        # Construct a dict representation of a TemplateRepoUpdateRequest model
        template_repo_update_request_model = {}
        template_repo_update_request_model['branch'] = 'testString'
        template_repo_update_request_model['release'] = 'testString'
        template_repo_update_request_model['repo_sha_value'] = 'testString'
        template_repo_update_request_model['repo_url'] = 'testString'
        template_repo_update_request_model['url'] = 'testString'

        # Construct a dict representation of a WorkspaceStatusUpdateRequest model
        workspace_status_update_request_model = {}
        workspace_status_update_request_model['frozen'] = True
        workspace_status_update_request_model['frozen_at'] = '2020-01-28T18:40:40.123456Z'
        workspace_status_update_request_model['frozen_by'] = 'testString'
        workspace_status_update_request_model['locked'] = True
        workspace_status_update_request_model['locked_by'] = 'testString'
        workspace_status_update_request_model['locked_time'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a WorkspaceStatusMessage model
        workspace_status_message_model = {}
        workspace_status_message_model['status_code'] = 'testString'
        workspace_status_message_model['status_msg'] = 'testString'

        # Set up parameter values
        w_id = 'testString'
        catalog_ref = catalog_ref_model
        description = 'testString'
        name = 'testString'
        shared_data = shared_target_data_model
        tags = ['testString']
        template_data = [template_source_data_request_model]
        template_repo = template_repo_update_request_model
        type = ['testString']
        workspace_status = workspace_status_update_request_model
        workspace_status_msg = workspace_status_message_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.replace_workspace(**req_copy)



class TestDeleteWorkspace():
    """
    Test Class for delete_workspace
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_workspace_all_params(self):
        """
        delete_workspace()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString')
        mock_response = '"operation_response"'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        refresh_token = 'testString'
        destroy_resources = 'testString'

        # Invoke method
        response = service.delete_workspace(
            w_id,
            refresh_token,
            destroy_resources=destroy_resources,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'destroy_resources={}'.format(destroy_resources) in query_string


    @responses.activate
    def test_delete_workspace_required_params(self):
        """
        test_delete_workspace_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString')
        mock_response = '"operation_response"'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        refresh_token = 'testString'

        # Invoke method
        response = service.delete_workspace(
            w_id,
            refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_workspace_value_error(self):
        """
        test_delete_workspace_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString')
        mock_response = '"operation_response"'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        refresh_token = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
            "refresh_token": refresh_token,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_workspace(**req_copy)



class TestUpdateWorkspace():
    """
    Test Class for update_workspace
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_workspace_all_params(self):
        """
        update_workspace()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString')
        mock_response = '{"applied_shareddata_ids": ["applied_shareddata_ids"], "catalog_ref": {"dry_run": false, "item_icon_url": "item_icon_url", "item_id": "item_id", "item_name": "item_name", "item_readme_url": "item_readme_url", "item_url": "item_url", "launch_url": "launch_url", "offering_version": "offering_version"}, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "crn": "crn", "description": "description", "id": "id", "last_health_check_at": "2019-01-01T12:00:00", "location": "location", "name": "name", "resource_group": "resource_group", "runtime_data": [{"engine_cmd": "engine_cmd", "engine_name": "engine_name", "engine_version": "engine_version", "id": "id", "log_store_url": "log_store_url", "output_values": [{"anyKey": "anyValue"}], "resources": [[{"anyKey": "anyValue"}]], "state_store_url": "state_store_url"}], "shared_data": {"cluster_id": "cluster_id", "cluster_name": "cluster_name", "entitlement_keys": [{"anyKey": "anyValue"}], "namespace": "namespace", "region": "region", "resource_group_id": "resource_group_id"}, "status": "status", "tags": ["tags"], "template_data": [{"env_values": [{"hidden": true, "name": "name", "secure": true, "value": "value"}], "folder": "folder", "has_githubtoken": false, "id": "id", "template_type": "template_type", "uninstall_script_name": "uninstall_script_name", "values": "values", "values_metadata": [{"anyKey": "anyValue"}], "values_url": "values_url", "variablestore": [{"description": "description", "name": "name", "secure": true, "type": "type", "value": "value"}]}], "template_ref": "template_ref", "template_repo": {"branch": "branch", "full_url": "full_url", "has_uploadedgitrepotar": true, "release": "release", "repo_sha_value": "repo_sha_value", "repo_url": "repo_url", "url": "url"}, "type": ["type"], "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "workspace_status": {"frozen": true, "frozen_at": "2019-01-01T12:00:00", "frozen_by": "frozen_by", "locked": true, "locked_by": "locked_by", "locked_time": "2019-01-01T12:00:00"}, "workspace_status_msg": {"status_code": "status_code", "status_msg": "status_msg"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CatalogRef model
        catalog_ref_model = {}
        catalog_ref_model['dry_run'] = True
        catalog_ref_model['item_icon_url'] = 'testString'
        catalog_ref_model['item_id'] = 'testString'
        catalog_ref_model['item_name'] = 'testString'
        catalog_ref_model['item_readme_url'] = 'testString'
        catalog_ref_model['item_url'] = 'testString'
        catalog_ref_model['launch_url'] = 'testString'
        catalog_ref_model['offering_version'] = 'testString'

        # Construct a dict representation of a SharedTargetData model
        shared_target_data_model = {}
        shared_target_data_model['cluster_created_on'] = 'testString'
        shared_target_data_model['cluster_id'] = 'testString'
        shared_target_data_model['cluster_name'] = 'testString'
        shared_target_data_model['cluster_type'] = 'testString'
        shared_target_data_model['entitlement_keys'] = [{ 'foo': 'bar' }]
        shared_target_data_model['namespace'] = 'testString'
        shared_target_data_model['region'] = 'testString'
        shared_target_data_model['resource_group_id'] = 'testString'
        shared_target_data_model['worker_count'] = 26
        shared_target_data_model['worker_machine_type'] = 'testString'

        # Construct a dict representation of a WorkspaceVariableRequest model
        workspace_variable_request_model = {}
        workspace_variable_request_model['description'] = 'testString'
        workspace_variable_request_model['name'] = 'testString'
        workspace_variable_request_model['secure'] = True
        workspace_variable_request_model['type'] = 'testString'
        workspace_variable_request_model['use_default'] = True
        workspace_variable_request_model['value'] = 'testString'

        # Construct a dict representation of a TemplateSourceDataRequest model
        template_source_data_request_model = {}
        template_source_data_request_model['env_values'] = [{ 'foo': 'bar' }]
        template_source_data_request_model['folder'] = 'testString'
        template_source_data_request_model['init_state_file'] = 'testString'
        template_source_data_request_model['type'] = 'testString'
        template_source_data_request_model['uninstall_script_name'] = 'testString'
        template_source_data_request_model['values'] = 'testString'
        template_source_data_request_model['values_metadata'] = [{ 'foo': 'bar' }]
        template_source_data_request_model['variablestore'] = [workspace_variable_request_model]

        # Construct a dict representation of a TemplateRepoUpdateRequest model
        template_repo_update_request_model = {}
        template_repo_update_request_model['branch'] = 'testString'
        template_repo_update_request_model['release'] = 'testString'
        template_repo_update_request_model['repo_sha_value'] = 'testString'
        template_repo_update_request_model['repo_url'] = 'testString'
        template_repo_update_request_model['url'] = 'testString'

        # Construct a dict representation of a WorkspaceStatusUpdateRequest model
        workspace_status_update_request_model = {}
        workspace_status_update_request_model['frozen'] = True
        workspace_status_update_request_model['frozen_at'] = '2020-01-28T18:40:40.123456Z'
        workspace_status_update_request_model['frozen_by'] = 'testString'
        workspace_status_update_request_model['locked'] = True
        workspace_status_update_request_model['locked_by'] = 'testString'
        workspace_status_update_request_model['locked_time'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a WorkspaceStatusMessage model
        workspace_status_message_model = {}
        workspace_status_message_model['status_code'] = 'testString'
        workspace_status_message_model['status_msg'] = 'testString'

        # Set up parameter values
        w_id = 'testString'
        catalog_ref = catalog_ref_model
        description = 'testString'
        name = 'testString'
        shared_data = shared_target_data_model
        tags = ['testString']
        template_data = [template_source_data_request_model]
        template_repo = template_repo_update_request_model
        type = ['testString']
        workspace_status = workspace_status_update_request_model
        workspace_status_msg = workspace_status_message_model

        # Invoke method
        response = service.update_workspace(
            w_id,
            catalog_ref=catalog_ref,
            description=description,
            name=name,
            shared_data=shared_data,
            tags=tags,
            template_data=template_data,
            template_repo=template_repo,
            type=type,
            workspace_status=workspace_status,
            workspace_status_msg=workspace_status_msg,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['catalog_ref'] == catalog_ref_model
        assert req_body['description'] == 'testString'
        assert req_body['name'] == 'testString'
        assert req_body['shared_data'] == shared_target_data_model
        assert req_body['tags'] == ['testString']
        assert req_body['template_data'] == [template_source_data_request_model]
        assert req_body['template_repo'] == template_repo_update_request_model
        assert req_body['type'] == ['testString']
        assert req_body['workspace_status'] == workspace_status_update_request_model
        assert req_body['workspace_status_msg'] == workspace_status_message_model


    @responses.activate
    def test_update_workspace_value_error(self):
        """
        test_update_workspace_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString')
        mock_response = '{"applied_shareddata_ids": ["applied_shareddata_ids"], "catalog_ref": {"dry_run": false, "item_icon_url": "item_icon_url", "item_id": "item_id", "item_name": "item_name", "item_readme_url": "item_readme_url", "item_url": "item_url", "launch_url": "launch_url", "offering_version": "offering_version"}, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "crn": "crn", "description": "description", "id": "id", "last_health_check_at": "2019-01-01T12:00:00", "location": "location", "name": "name", "resource_group": "resource_group", "runtime_data": [{"engine_cmd": "engine_cmd", "engine_name": "engine_name", "engine_version": "engine_version", "id": "id", "log_store_url": "log_store_url", "output_values": [{"anyKey": "anyValue"}], "resources": [[{"anyKey": "anyValue"}]], "state_store_url": "state_store_url"}], "shared_data": {"cluster_id": "cluster_id", "cluster_name": "cluster_name", "entitlement_keys": [{"anyKey": "anyValue"}], "namespace": "namespace", "region": "region", "resource_group_id": "resource_group_id"}, "status": "status", "tags": ["tags"], "template_data": [{"env_values": [{"hidden": true, "name": "name", "secure": true, "value": "value"}], "folder": "folder", "has_githubtoken": false, "id": "id", "template_type": "template_type", "uninstall_script_name": "uninstall_script_name", "values": "values", "values_metadata": [{"anyKey": "anyValue"}], "values_url": "values_url", "variablestore": [{"description": "description", "name": "name", "secure": true, "type": "type", "value": "value"}]}], "template_ref": "template_ref", "template_repo": {"branch": "branch", "full_url": "full_url", "has_uploadedgitrepotar": true, "release": "release", "repo_sha_value": "repo_sha_value", "repo_url": "repo_url", "url": "url"}, "type": ["type"], "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "workspace_status": {"frozen": true, "frozen_at": "2019-01-01T12:00:00", "frozen_by": "frozen_by", "locked": true, "locked_by": "locked_by", "locked_time": "2019-01-01T12:00:00"}, "workspace_status_msg": {"status_code": "status_code", "status_msg": "status_msg"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CatalogRef model
        catalog_ref_model = {}
        catalog_ref_model['dry_run'] = True
        catalog_ref_model['item_icon_url'] = 'testString'
        catalog_ref_model['item_id'] = 'testString'
        catalog_ref_model['item_name'] = 'testString'
        catalog_ref_model['item_readme_url'] = 'testString'
        catalog_ref_model['item_url'] = 'testString'
        catalog_ref_model['launch_url'] = 'testString'
        catalog_ref_model['offering_version'] = 'testString'

        # Construct a dict representation of a SharedTargetData model
        shared_target_data_model = {}
        shared_target_data_model['cluster_created_on'] = 'testString'
        shared_target_data_model['cluster_id'] = 'testString'
        shared_target_data_model['cluster_name'] = 'testString'
        shared_target_data_model['cluster_type'] = 'testString'
        shared_target_data_model['entitlement_keys'] = [{ 'foo': 'bar' }]
        shared_target_data_model['namespace'] = 'testString'
        shared_target_data_model['region'] = 'testString'
        shared_target_data_model['resource_group_id'] = 'testString'
        shared_target_data_model['worker_count'] = 26
        shared_target_data_model['worker_machine_type'] = 'testString'

        # Construct a dict representation of a WorkspaceVariableRequest model
        workspace_variable_request_model = {}
        workspace_variable_request_model['description'] = 'testString'
        workspace_variable_request_model['name'] = 'testString'
        workspace_variable_request_model['secure'] = True
        workspace_variable_request_model['type'] = 'testString'
        workspace_variable_request_model['use_default'] = True
        workspace_variable_request_model['value'] = 'testString'

        # Construct a dict representation of a TemplateSourceDataRequest model
        template_source_data_request_model = {}
        template_source_data_request_model['env_values'] = [{ 'foo': 'bar' }]
        template_source_data_request_model['folder'] = 'testString'
        template_source_data_request_model['init_state_file'] = 'testString'
        template_source_data_request_model['type'] = 'testString'
        template_source_data_request_model['uninstall_script_name'] = 'testString'
        template_source_data_request_model['values'] = 'testString'
        template_source_data_request_model['values_metadata'] = [{ 'foo': 'bar' }]
        template_source_data_request_model['variablestore'] = [workspace_variable_request_model]

        # Construct a dict representation of a TemplateRepoUpdateRequest model
        template_repo_update_request_model = {}
        template_repo_update_request_model['branch'] = 'testString'
        template_repo_update_request_model['release'] = 'testString'
        template_repo_update_request_model['repo_sha_value'] = 'testString'
        template_repo_update_request_model['repo_url'] = 'testString'
        template_repo_update_request_model['url'] = 'testString'

        # Construct a dict representation of a WorkspaceStatusUpdateRequest model
        workspace_status_update_request_model = {}
        workspace_status_update_request_model['frozen'] = True
        workspace_status_update_request_model['frozen_at'] = '2020-01-28T18:40:40.123456Z'
        workspace_status_update_request_model['frozen_by'] = 'testString'
        workspace_status_update_request_model['locked'] = True
        workspace_status_update_request_model['locked_by'] = 'testString'
        workspace_status_update_request_model['locked_time'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a WorkspaceStatusMessage model
        workspace_status_message_model = {}
        workspace_status_message_model['status_code'] = 'testString'
        workspace_status_message_model['status_msg'] = 'testString'

        # Set up parameter values
        w_id = 'testString'
        catalog_ref = catalog_ref_model
        description = 'testString'
        name = 'testString'
        shared_data = shared_target_data_model
        tags = ['testString']
        template_data = [template_source_data_request_model]
        template_repo = template_repo_update_request_model
        type = ['testString']
        workspace_status = workspace_status_update_request_model
        workspace_status_msg = workspace_status_message_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_workspace(**req_copy)



class TestUploadTemplateTar():
    """
    Test Class for upload_template_tar
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_upload_template_tar_all_params(self):
        """
        upload_template_tar()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/template_data/testString/template_repo_upload')
        mock_response = '{"file_value": "file_value", "has_received_file": false, "id": "id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        t_id = 'testString'
        file = io.BytesIO(b'This is a mock file.').getvalue()
        file_content_type = 'testString'

        # Invoke method
        response = service.upload_template_tar(
            w_id,
            t_id,
            file=file,
            file_content_type=file_content_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_upload_template_tar_required_params(self):
        """
        test_upload_template_tar_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/template_data/testString/template_repo_upload')
        mock_response = '{"file_value": "file_value", "has_received_file": false, "id": "id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        t_id = 'testString'

        # Invoke method
        response = service.upload_template_tar(
            w_id,
            t_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_upload_template_tar_value_error(self):
        """
        test_upload_template_tar_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/template_data/testString/template_repo_upload')
        mock_response = '{"file_value": "file_value", "has_received_file": false, "id": "id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        t_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
            "t_id": t_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.upload_template_tar(**req_copy)



class TestGetWorkspaceReadme():
    """
    Test Class for get_workspace_readme
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_workspace_readme_all_params(self):
        """
        get_workspace_readme()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/templates/readme')
        mock_response = '{"readme": "readme"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        ref = 'testString'
        formatted = 'markdown'

        # Invoke method
        response = service.get_workspace_readme(
            w_id,
            ref=ref,
            formatted=formatted,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'ref={}'.format(ref) in query_string
        assert 'formatted={}'.format(formatted) in query_string


    @responses.activate
    def test_get_workspace_readme_required_params(self):
        """
        test_get_workspace_readme_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/templates/readme')
        mock_response = '{"readme": "readme"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'

        # Invoke method
        response = service.get_workspace_readme(
            w_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_workspace_readme_value_error(self):
        """
        test_get_workspace_readme_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/templates/readme')
        mock_response = '{"readme": "readme"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_workspace_readme(**req_copy)



# endregion
##############################################################################
# End of Service: Workspaces
##############################################################################

##############################################################################
# Start of Service: WorkspaceActivities
##############################################################################
# region

class TestListWorkspaceActivities():
    """
    Test Class for list_workspace_activities
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_workspace_activities_all_params(self):
        """
        list_workspace_activities()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/actions')
        mock_response = '{"actions": [{"action_id": "action_id", "message": ["message"], "name": "name", "performed_at": "2019-01-01T12:00:00", "performed_by": "performed_by", "status": "status", "templates": [{"end_time": "2019-01-01T12:00:00", "log_summary": {"activity_status": "activity_status", "detected_template_type": "detected_template_type", "discarded_files": 15, "error": "error", "resources_added": 15, "resources_destroyed": 19, "resources_modified": 18, "scanned_files": 13, "template_variable_count": 23, "time_taken": 10}, "log_url": "log_url", "message": "message", "start_time": "2019-01-01T12:00:00", "status": "status", "template_id": "template_id", "template_type": "template_type"}]}], "workspace_id": "workspace_id", "workspace_name": "workspace_name"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        offset = 0
        limit = 1

        # Invoke method
        response = service.list_workspace_activities(
            w_id,
            offset=offset,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'offset={}'.format(offset) in query_string
        assert 'limit={}'.format(limit) in query_string


    @responses.activate
    def test_list_workspace_activities_required_params(self):
        """
        test_list_workspace_activities_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/actions')
        mock_response = '{"actions": [{"action_id": "action_id", "message": ["message"], "name": "name", "performed_at": "2019-01-01T12:00:00", "performed_by": "performed_by", "status": "status", "templates": [{"end_time": "2019-01-01T12:00:00", "log_summary": {"activity_status": "activity_status", "detected_template_type": "detected_template_type", "discarded_files": 15, "error": "error", "resources_added": 15, "resources_destroyed": 19, "resources_modified": 18, "scanned_files": 13, "template_variable_count": 23, "time_taken": 10}, "log_url": "log_url", "message": "message", "start_time": "2019-01-01T12:00:00", "status": "status", "template_id": "template_id", "template_type": "template_type"}]}], "workspace_id": "workspace_id", "workspace_name": "workspace_name"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'

        # Invoke method
        response = service.list_workspace_activities(
            w_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_workspace_activities_value_error(self):
        """
        test_list_workspace_activities_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/actions')
        mock_response = '{"actions": [{"action_id": "action_id", "message": ["message"], "name": "name", "performed_at": "2019-01-01T12:00:00", "performed_by": "performed_by", "status": "status", "templates": [{"end_time": "2019-01-01T12:00:00", "log_summary": {"activity_status": "activity_status", "detected_template_type": "detected_template_type", "discarded_files": 15, "error": "error", "resources_added": 15, "resources_destroyed": 19, "resources_modified": 18, "scanned_files": 13, "template_variable_count": 23, "time_taken": 10}, "log_url": "log_url", "message": "message", "start_time": "2019-01-01T12:00:00", "status": "status", "template_id": "template_id", "template_type": "template_type"}]}], "workspace_id": "workspace_id", "workspace_name": "workspace_name"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_workspace_activities(**req_copy)



class TestGetWorkspaceActivity():
    """
    Test Class for get_workspace_activity
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_workspace_activity_all_params(self):
        """
        get_workspace_activity()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/actions/testString')
        mock_response = '{"action_id": "action_id", "message": ["message"], "name": "name", "performed_at": "2019-01-01T12:00:00", "performed_by": "performed_by", "status": "status", "templates": [{"end_time": "2019-01-01T12:00:00", "log_summary": {"activity_status": "activity_status", "detected_template_type": "detected_template_type", "discarded_files": 15, "error": "error", "resources_added": 15, "resources_destroyed": 19, "resources_modified": 18, "scanned_files": 13, "template_variable_count": 23, "time_taken": 10}, "log_url": "log_url", "message": "message", "start_time": "2019-01-01T12:00:00", "status": "status", "template_id": "template_id", "template_type": "template_type"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        activity_id = 'testString'

        # Invoke method
        response = service.get_workspace_activity(
            w_id,
            activity_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_workspace_activity_value_error(self):
        """
        test_get_workspace_activity_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/actions/testString')
        mock_response = '{"action_id": "action_id", "message": ["message"], "name": "name", "performed_at": "2019-01-01T12:00:00", "performed_by": "performed_by", "status": "status", "templates": [{"end_time": "2019-01-01T12:00:00", "log_summary": {"activity_status": "activity_status", "detected_template_type": "detected_template_type", "discarded_files": 15, "error": "error", "resources_added": 15, "resources_destroyed": 19, "resources_modified": 18, "scanned_files": 13, "template_variable_count": 23, "time_taken": 10}, "log_url": "log_url", "message": "message", "start_time": "2019-01-01T12:00:00", "status": "status", "template_id": "template_id", "template_type": "template_type"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        activity_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
            "activity_id": activity_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_workspace_activity(**req_copy)



class TestDeleteWorkspaceActivity():
    """
    Test Class for delete_workspace_activity
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_workspace_activity_all_params(self):
        """
        delete_workspace_activity()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/actions/testString')
        mock_response = '{"activityid": "activityid"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        w_id = 'testString'
        activity_id = 'testString'

        # Invoke method
        response = service.delete_workspace_activity(
            w_id,
            activity_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_delete_workspace_activity_value_error(self):
        """
        test_delete_workspace_activity_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/actions/testString')
        mock_response = '{"activityid": "activityid"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        w_id = 'testString'
        activity_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
            "activity_id": activity_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_workspace_activity(**req_copy)



class TestApplyWorkspaceCommand():
    """
    Test Class for apply_workspace_command
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_apply_workspace_command_all_params(self):
        """
        apply_workspace_command()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/apply')
        mock_response = '{"activityid": "activityid"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a WorkspaceActivityOptionsTemplate model
        workspace_activity_options_template_model = {}
        workspace_activity_options_template_model['target'] = ['testString']
        workspace_activity_options_template_model['tf_vars'] = ['testString']

        # Set up parameter values
        w_id = 'testString'
        refresh_token = 'testString'
        action_options = workspace_activity_options_template_model

        # Invoke method
        response = service.apply_workspace_command(
            w_id,
            refresh_token,
            action_options=action_options,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['action_options'] == workspace_activity_options_template_model


    @responses.activate
    def test_apply_workspace_command_value_error(self):
        """
        test_apply_workspace_command_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/apply')
        mock_response = '{"activityid": "activityid"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a WorkspaceActivityOptionsTemplate model
        workspace_activity_options_template_model = {}
        workspace_activity_options_template_model['target'] = ['testString']
        workspace_activity_options_template_model['tf_vars'] = ['testString']

        # Set up parameter values
        w_id = 'testString'
        refresh_token = 'testString'
        action_options = workspace_activity_options_template_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
            "refresh_token": refresh_token,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.apply_workspace_command(**req_copy)



class TestDestroyWorkspaceCommand():
    """
    Test Class for destroy_workspace_command
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_destroy_workspace_command_all_params(self):
        """
        destroy_workspace_command()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/destroy')
        mock_response = '{"activityid": "activityid"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a WorkspaceActivityOptionsTemplate model
        workspace_activity_options_template_model = {}
        workspace_activity_options_template_model['target'] = ['testString']
        workspace_activity_options_template_model['tf_vars'] = ['testString']

        # Set up parameter values
        w_id = 'testString'
        refresh_token = 'testString'
        action_options = workspace_activity_options_template_model

        # Invoke method
        response = service.destroy_workspace_command(
            w_id,
            refresh_token,
            action_options=action_options,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['action_options'] == workspace_activity_options_template_model


    @responses.activate
    def test_destroy_workspace_command_value_error(self):
        """
        test_destroy_workspace_command_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/destroy')
        mock_response = '{"activityid": "activityid"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a WorkspaceActivityOptionsTemplate model
        workspace_activity_options_template_model = {}
        workspace_activity_options_template_model['target'] = ['testString']
        workspace_activity_options_template_model['tf_vars'] = ['testString']

        # Set up parameter values
        w_id = 'testString'
        refresh_token = 'testString'
        action_options = workspace_activity_options_template_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
            "refresh_token": refresh_token,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.destroy_workspace_command(**req_copy)



class TestPlanWorkspaceCommand():
    """
    Test Class for plan_workspace_command
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_plan_workspace_command_all_params(self):
        """
        plan_workspace_command()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/plan')
        mock_response = '{"activityid": "activityid"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        w_id = 'testString'
        refresh_token = 'testString'

        # Invoke method
        response = service.plan_workspace_command(
            w_id,
            refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_plan_workspace_command_value_error(self):
        """
        test_plan_workspace_command_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/plan')
        mock_response = '{"activityid": "activityid"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        w_id = 'testString'
        refresh_token = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
            "refresh_token": refresh_token,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.plan_workspace_command(**req_copy)



class TestRefreshWorkspaceCommand():
    """
    Test Class for refresh_workspace_command
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_refresh_workspace_command_all_params(self):
        """
        refresh_workspace_command()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/refresh')
        mock_response = '{"activityid": "activityid"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        w_id = 'testString'
        refresh_token = 'testString'

        # Invoke method
        response = service.refresh_workspace_command(
            w_id,
            refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_refresh_workspace_command_value_error(self):
        """
        test_refresh_workspace_command_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/refresh')
        mock_response = '{"activityid": "activityid"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        w_id = 'testString'
        refresh_token = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
            "refresh_token": refresh_token,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.refresh_workspace_command(**req_copy)



# endregion
##############################################################################
# End of Service: WorkspaceActivities
##############################################################################

##############################################################################
# Start of Service: WorkspaceInputs
##############################################################################
# region

class TestGetWorkspaceInputs():
    """
    Test Class for get_workspace_inputs
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_workspace_inputs_all_params(self):
        """
        get_workspace_inputs()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/template_data/testString/values')
        mock_response = '{"values_metadata": [{"anyKey": "anyValue"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        t_id = 'testString'

        # Invoke method
        response = service.get_workspace_inputs(
            w_id,
            t_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_workspace_inputs_value_error(self):
        """
        test_get_workspace_inputs_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/template_data/testString/values')
        mock_response = '{"values_metadata": [{"anyKey": "anyValue"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        t_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
            "t_id": t_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_workspace_inputs(**req_copy)



class TestReplaceWorkspaceInputs():
    """
    Test Class for replace_workspace_inputs
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_replace_workspace_inputs_all_params(self):
        """
        replace_workspace_inputs()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/template_data/testString/values')
        mock_response = '{"env_values": [{"anyKey": "anyValue"}], "values": "values", "variablestore": [{"description": "description", "name": "name", "secure": true, "type": "type", "value": "value"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a WorkspaceVariableRequest model
        workspace_variable_request_model = {}
        workspace_variable_request_model['description'] = 'testString'
        workspace_variable_request_model['name'] = 'testString'
        workspace_variable_request_model['secure'] = True
        workspace_variable_request_model['type'] = 'testString'
        workspace_variable_request_model['use_default'] = True
        workspace_variable_request_model['value'] = 'testString'

        # Set up parameter values
        w_id = 'testString'
        t_id = 'testString'
        env_values = [{ 'foo': 'bar' }]
        values = 'testString'
        variablestore = [workspace_variable_request_model]

        # Invoke method
        response = service.replace_workspace_inputs(
            w_id,
            t_id,
            env_values=env_values,
            values=values,
            variablestore=variablestore,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['env_values'] == [{ 'foo': 'bar' }]
        assert req_body['values'] == 'testString'
        assert req_body['variablestore'] == [workspace_variable_request_model]


    @responses.activate
    def test_replace_workspace_inputs_value_error(self):
        """
        test_replace_workspace_inputs_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/template_data/testString/values')
        mock_response = '{"env_values": [{"anyKey": "anyValue"}], "values": "values", "variablestore": [{"description": "description", "name": "name", "secure": true, "type": "type", "value": "value"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a WorkspaceVariableRequest model
        workspace_variable_request_model = {}
        workspace_variable_request_model['description'] = 'testString'
        workspace_variable_request_model['name'] = 'testString'
        workspace_variable_request_model['secure'] = True
        workspace_variable_request_model['type'] = 'testString'
        workspace_variable_request_model['use_default'] = True
        workspace_variable_request_model['value'] = 'testString'

        # Set up parameter values
        w_id = 'testString'
        t_id = 'testString'
        env_values = [{ 'foo': 'bar' }]
        values = 'testString'
        variablestore = [workspace_variable_request_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
            "t_id": t_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.replace_workspace_inputs(**req_copy)



class TestGetAllWorkspaceInputs():
    """
    Test Class for get_all_workspace_inputs
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_all_workspace_inputs_all_params(self):
        """
        get_all_workspace_inputs()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/templates/values')
        mock_response = '{"runtime_data": [{"engine_cmd": "engine_cmd", "engine_name": "engine_name", "engine_version": "engine_version", "id": "id", "log_store_url": "log_store_url", "output_values": [{"anyKey": "anyValue"}], "resources": [[{"anyKey": "anyValue"}]], "state_store_url": "state_store_url"}], "shared_data": {"cluster_created_on": "cluster_created_on", "cluster_id": "cluster_id", "cluster_name": "cluster_name", "cluster_type": "cluster_type", "entitlement_keys": [{"anyKey": "anyValue"}], "namespace": "namespace", "region": "region", "resource_group_id": "resource_group_id", "worker_count": 12, "worker_machine_type": "worker_machine_type"}, "template_data": [{"env_values": [{"hidden": true, "name": "name", "secure": true, "value": "value"}], "folder": "folder", "has_githubtoken": false, "id": "id", "template_type": "template_type", "uninstall_script_name": "uninstall_script_name", "values": "values", "values_metadata": [{"anyKey": "anyValue"}], "values_url": "values_url", "variablestore": [{"description": "description", "name": "name", "secure": true, "type": "type", "value": "value"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'

        # Invoke method
        response = service.get_all_workspace_inputs(
            w_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_all_workspace_inputs_value_error(self):
        """
        test_get_all_workspace_inputs_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/templates/values')
        mock_response = '{"runtime_data": [{"engine_cmd": "engine_cmd", "engine_name": "engine_name", "engine_version": "engine_version", "id": "id", "log_store_url": "log_store_url", "output_values": [{"anyKey": "anyValue"}], "resources": [[{"anyKey": "anyValue"}]], "state_store_url": "state_store_url"}], "shared_data": {"cluster_created_on": "cluster_created_on", "cluster_id": "cluster_id", "cluster_name": "cluster_name", "cluster_type": "cluster_type", "entitlement_keys": [{"anyKey": "anyValue"}], "namespace": "namespace", "region": "region", "resource_group_id": "resource_group_id", "worker_count": 12, "worker_machine_type": "worker_machine_type"}, "template_data": [{"env_values": [{"hidden": true, "name": "name", "secure": true, "value": "value"}], "folder": "folder", "has_githubtoken": false, "id": "id", "template_type": "template_type", "uninstall_script_name": "uninstall_script_name", "values": "values", "values_metadata": [{"anyKey": "anyValue"}], "values_url": "values_url", "variablestore": [{"description": "description", "name": "name", "secure": true, "type": "type", "value": "value"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_all_workspace_inputs(**req_copy)



class TestGetWorkspaceInputMetadata():
    """
    Test Class for get_workspace_input_metadata
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_workspace_input_metadata_all_params(self):
        """
        get_workspace_input_metadata()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/template_data/testString/values_metadata')
        mock_response = '[{"anyKey": "anyValue"}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        t_id = 'testString'

        # Invoke method
        response = service.get_workspace_input_metadata(
            w_id,
            t_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_workspace_input_metadata_value_error(self):
        """
        test_get_workspace_input_metadata_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/template_data/testString/values_metadata')
        mock_response = '[{"anyKey": "anyValue"}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        t_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
            "t_id": t_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_workspace_input_metadata(**req_copy)



# endregion
##############################################################################
# End of Service: WorkspaceInputs
##############################################################################

##############################################################################
# Start of Service: WorkspaceOutputs
##############################################################################
# region

class TestGetWorkspaceOutputs():
    """
    Test Class for get_workspace_outputs
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_workspace_outputs_all_params(self):
        """
        get_workspace_outputs()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/output_values')
        mock_response = '[{"folder": "folder", "id": "id", "output_values": [{"anyKey": "anyValue"}], "value_type": "value_type"}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'

        # Invoke method
        response = service.get_workspace_outputs(
            w_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_workspace_outputs_value_error(self):
        """
        test_get_workspace_outputs_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/output_values')
        mock_response = '[{"folder": "folder", "id": "id", "output_values": [{"anyKey": "anyValue"}], "value_type": "value_type"}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_workspace_outputs(**req_copy)



class TestGetWorkspaceResources():
    """
    Test Class for get_workspace_resources
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_workspace_resources_all_params(self):
        """
        get_workspace_resources()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/resources')
        mock_response = '[{"folder": "folder", "id": "id", "null_resources": [{"anyKey": "anyValue"}], "related_resources": [{"anyKey": "anyValue"}], "resources": [{"anyKey": "anyValue"}], "resources_count": 15, "template_type": "template_type"}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'

        # Invoke method
        response = service.get_workspace_resources(
            w_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_workspace_resources_value_error(self):
        """
        test_get_workspace_resources_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/resources')
        mock_response = '[{"folder": "folder", "id": "id", "null_resources": [{"anyKey": "anyValue"}], "related_resources": [{"anyKey": "anyValue"}], "resources": [{"anyKey": "anyValue"}], "resources_count": 15, "template_type": "template_type"}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_workspace_resources(**req_copy)



class TestGetWorkspaceState():
    """
    Test Class for get_workspace_state
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_workspace_state_all_params(self):
        """
        get_workspace_state()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/state_stores')
        mock_response = '{"runtime_data": [{"engine_name": "engine_name", "engine_version": "engine_version", "id": "id", "state_store_url": "state_store_url"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'

        # Invoke method
        response = service.get_workspace_state(
            w_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_workspace_state_value_error(self):
        """
        test_get_workspace_state_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/state_stores')
        mock_response = '{"runtime_data": [{"engine_name": "engine_name", "engine_version": "engine_version", "id": "id", "state_store_url": "state_store_url"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_workspace_state(**req_copy)



class TestGetWorkspaceTemplateState():
    """
    Test Class for get_workspace_template_state
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_workspace_template_state_all_params(self):
        """
        get_workspace_template_state()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/runtime_data/testString/state_store')
        mock_response = '{"version": 7, "terraform_version": "terraform_version", "serial": 6, "lineage": "lineage", "modules": [{"anyKey": "anyValue"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        t_id = 'testString'

        # Invoke method
        response = service.get_workspace_template_state(
            w_id,
            t_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_workspace_template_state_value_error(self):
        """
        test_get_workspace_template_state_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/runtime_data/testString/state_store')
        mock_response = '{"version": 7, "terraform_version": "terraform_version", "serial": 6, "lineage": "lineage", "modules": [{"anyKey": "anyValue"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        t_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
            "t_id": t_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_workspace_template_state(**req_copy)



# endregion
##############################################################################
# End of Service: WorkspaceOutputs
##############################################################################

##############################################################################
# Start of Service: WorkspaceLogs
##############################################################################
# region

class TestGetWorkspaceActivityLogs():
    """
    Test Class for get_workspace_activity_logs
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_workspace_activity_logs_all_params(self):
        """
        get_workspace_activity_logs()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/actions/testString/logs')
        mock_response = '{"action_id": "action_id", "name": "name", "templates": [{"log_url": "log_url", "template_id": "template_id", "template_type": "template_type"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        activity_id = 'testString'

        # Invoke method
        response = service.get_workspace_activity_logs(
            w_id,
            activity_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_workspace_activity_logs_value_error(self):
        """
        test_get_workspace_activity_logs_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/actions/testString/logs')
        mock_response = '{"action_id": "action_id", "name": "name", "templates": [{"log_url": "log_url", "template_id": "template_id", "template_type": "template_type"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        activity_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
            "activity_id": activity_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_workspace_activity_logs(**req_copy)



class TestGetWorkspaceLogUrls():
    """
    Test Class for get_workspace_log_urls
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_workspace_log_urls_all_params(self):
        """
        get_workspace_log_urls()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/log_stores')
        mock_response = '{"runtime_data": [{"engine_name": "engine_name", "engine_version": "engine_version", "id": "id", "log_store_url": "log_store_url"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'

        # Invoke method
        response = service.get_workspace_log_urls(
            w_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_workspace_log_urls_value_error(self):
        """
        test_get_workspace_log_urls_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/log_stores')
        mock_response = '{"runtime_data": [{"engine_name": "engine_name", "engine_version": "engine_version", "id": "id", "log_store_url": "log_store_url"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_workspace_log_urls(**req_copy)



class TestGetTemplateLogs():
    """
    Test Class for get_template_logs
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_template_logs_all_params(self):
        """
        get_template_logs()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/runtime_data/testString/log_store')
        mock_response = '"operation_response"'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        t_id = 'testString'
        log_tf_cmd = True
        log_tf_prefix = True
        log_tf_null_resource = True
        log_tf_ansible = True

        # Invoke method
        response = service.get_template_logs(
            w_id,
            t_id,
            log_tf_cmd=log_tf_cmd,
            log_tf_prefix=log_tf_prefix,
            log_tf_null_resource=log_tf_null_resource,
            log_tf_ansible=log_tf_ansible,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'log_tf_cmd={}'.format('true' if log_tf_cmd else 'false') in query_string
        assert 'log_tf_prefix={}'.format('true' if log_tf_prefix else 'false') in query_string
        assert 'log_tf_null_resource={}'.format('true' if log_tf_null_resource else 'false') in query_string
        assert 'log_tf_ansible={}'.format('true' if log_tf_ansible else 'false') in query_string


    @responses.activate
    def test_get_template_logs_required_params(self):
        """
        test_get_template_logs_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/runtime_data/testString/log_store')
        mock_response = '"operation_response"'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        t_id = 'testString'

        # Invoke method
        response = service.get_template_logs(
            w_id,
            t_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_template_logs_value_error(self):
        """
        test_get_template_logs_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/runtime_data/testString/log_store')
        mock_response = '"operation_response"'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        t_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
            "t_id": t_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_template_logs(**req_copy)



class TestGetTemplateActivityLog():
    """
    Test Class for get_template_activity_log
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_template_activity_log_all_params(self):
        """
        get_template_activity_log()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/runtime_data/testString/log_store/actions/testString')
        mock_response = '"operation_response"'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        t_id = 'testString'
        activity_id = 'testString'
        log_tf_cmd = True
        log_tf_prefix = True
        log_tf_null_resource = True
        log_tf_ansible = True

        # Invoke method
        response = service.get_template_activity_log(
            w_id,
            t_id,
            activity_id,
            log_tf_cmd=log_tf_cmd,
            log_tf_prefix=log_tf_prefix,
            log_tf_null_resource=log_tf_null_resource,
            log_tf_ansible=log_tf_ansible,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'log_tf_cmd={}'.format('true' if log_tf_cmd else 'false') in query_string
        assert 'log_tf_prefix={}'.format('true' if log_tf_prefix else 'false') in query_string
        assert 'log_tf_null_resource={}'.format('true' if log_tf_null_resource else 'false') in query_string
        assert 'log_tf_ansible={}'.format('true' if log_tf_ansible else 'false') in query_string


    @responses.activate
    def test_get_template_activity_log_required_params(self):
        """
        test_get_template_activity_log_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/runtime_data/testString/log_store/actions/testString')
        mock_response = '"operation_response"'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        t_id = 'testString'
        activity_id = 'testString'

        # Invoke method
        response = service.get_template_activity_log(
            w_id,
            t_id,
            activity_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_template_activity_log_value_error(self):
        """
        test_get_template_activity_log_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspaces/testString/runtime_data/testString/log_store/actions/testString')
        mock_response = '"operation_response"'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        w_id = 'testString'
        t_id = 'testString'
        activity_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "w_id": w_id,
            "t_id": t_id,
            "activity_id": activity_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_template_activity_log(**req_copy)



# endregion
##############################################################################
# End of Service: WorkspaceLogs
##############################################################################

##############################################################################
# Start of Service: WorkspaceBulkJobs
##############################################################################
# region

class TestCreateWorkspaceDeletionJob():
    """
    Test Class for create_workspace_deletion_job
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_workspace_deletion_job_all_params(self):
        """
        create_workspace_deletion_job()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspace_jobs')
        mock_response = '{"job": "job", "job_id": "job_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        refresh_token = 'testString'
        new_delete_workspaces = True
        new_destroy_resources = True
        new_job = 'testString'
        new_version = 'testString'
        new_workspaces = ['testString']
        destroy_resources = 'testString'

        # Invoke method
        response = service.create_workspace_deletion_job(
            refresh_token,
            new_delete_workspaces=new_delete_workspaces,
            new_destroy_resources=new_destroy_resources,
            new_job=new_job,
            new_version=new_version,
            new_workspaces=new_workspaces,
            destroy_resources=destroy_resources,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'destroy_resources={}'.format(destroy_resources) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['delete_workspaces'] == True
        assert req_body['destroy_resources'] == True
        assert req_body['job'] == 'testString'
        assert req_body['version'] == 'testString'
        assert req_body['workspaces'] == ['testString']


    @responses.activate
    def test_create_workspace_deletion_job_required_params(self):
        """
        test_create_workspace_deletion_job_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspace_jobs')
        mock_response = '{"job": "job", "job_id": "job_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        refresh_token = 'testString'
        new_delete_workspaces = True
        new_destroy_resources = True
        new_job = 'testString'
        new_version = 'testString'
        new_workspaces = ['testString']

        # Invoke method
        response = service.create_workspace_deletion_job(
            refresh_token,
            new_delete_workspaces=new_delete_workspaces,
            new_destroy_resources=new_destroy_resources,
            new_job=new_job,
            new_version=new_version,
            new_workspaces=new_workspaces,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['delete_workspaces'] == True
        assert req_body['destroy_resources'] == True
        assert req_body['job'] == 'testString'
        assert req_body['version'] == 'testString'
        assert req_body['workspaces'] == ['testString']


    @responses.activate
    def test_create_workspace_deletion_job_value_error(self):
        """
        test_create_workspace_deletion_job_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspace_jobs')
        mock_response = '{"job": "job", "job_id": "job_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        refresh_token = 'testString'
        new_delete_workspaces = True
        new_destroy_resources = True
        new_job = 'testString'
        new_version = 'testString'
        new_workspaces = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "refresh_token": refresh_token,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_workspace_deletion_job(**req_copy)



class TestGetWorkspaceDeletionJobStatus():
    """
    Test Class for get_workspace_deletion_job_status
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_workspace_deletion_job_status_all_params(self):
        """
        get_workspace_deletion_job_status()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspace_jobs/testString/status')
        mock_response = '{"job_status": {"failed": ["failed"], "in_progress": ["in_progress"], "success": ["success"], "last_updated_on": "2019-01-01T12:00:00"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        wj_id = 'testString'

        # Invoke method
        response = service.get_workspace_deletion_job_status(
            wj_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_workspace_deletion_job_status_value_error(self):
        """
        test_get_workspace_deletion_job_status_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/workspace_jobs/testString/status')
        mock_response = '{"job_status": {"failed": ["failed"], "in_progress": ["in_progress"], "success": ["success"], "last_updated_on": "2019-01-01T12:00:00"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        wj_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "wj_id": wj_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_workspace_deletion_job_status(**req_copy)



# endregion
##############################################################################
# End of Service: WorkspaceBulkJobs
##############################################################################

##############################################################################
# Start of Service: Actions
##############################################################################
# region

class TestCreateAction():
    """
    Test Class for create_action
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_action_all_params(self):
        """
        create_action()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/actions')
        mock_response = '{"name": "Stop Action", "description": "This Action can be used to Stop the targets", "location": "us_south", "resource_group": "resource_group", "tags": ["tags"], "user_state": {"state": "draft", "set_by": "set_by", "set_at": "2019-01-01T12:00:00"}, "source_readme_url": "source_readme_url", "source": {"source_type": "local", "git": {"git_repo_url": "git_repo_url", "git_token": "git_token", "git_repo_folder": "git_repo_folder", "git_release": "git_release", "git_branch": "git_branch"}}, "source_type": "local", "command_parameter": "command_parameter", "bastion": {"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}, "targets": [{"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}], "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "outputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "trigger_record_id": "trigger_record_id", "id": "id", "crn": "crn", "account": "account", "source_created_at": "2019-01-01T12:00:00", "source_created_by": "source_created_by", "source_updated_at": "2019-01-01T12:00:00", "source_updated_by": "source_updated_by", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "namespace": "namespace", "state": {"status_code": "normal", "status_message": "status_message"}, "playbook_names": ["playbook_names"], "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a UserState model
        user_state_model = {}
        user_state_model['state'] = 'draft'
        user_state_model['set_by'] = 'testString'
        user_state_model['set_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a ExternalSourceGit model
        external_source_git_model = {}
        external_source_git_model['git_repo_url'] = 'testString'
        external_source_git_model['git_token'] = 'testString'
        external_source_git_model['git_repo_folder'] = 'testString'
        external_source_git_model['git_release'] = 'testString'
        external_source_git_model['git_branch'] = 'testString'

        # Construct a dict representation of a ExternalSource model
        external_source_model = {}
        external_source_model['source_type'] = 'local'
        external_source_model['git'] = external_source_git_model

        # Construct a dict representation of a SystemLock model
        system_lock_model = {}
        system_lock_model['sys_locked'] = True
        system_lock_model['sys_locked_by'] = 'testString'
        system_lock_model['sys_locked_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a TargetResourceset model
        target_resourceset_model = {}
        target_resourceset_model['name'] = 'testString'
        target_resourceset_model['type'] = 'testString'
        target_resourceset_model['description'] = 'testString'
        target_resourceset_model['resource_query'] = 'testString'
        target_resourceset_model['credential'] = 'testString'
        target_resourceset_model['sys_lock'] = system_lock_model

        # Construct a dict representation of a VariableMetadata model
        variable_metadata_model = {}
        variable_metadata_model['type'] = 'boolean'
        variable_metadata_model['aliases'] = ['testString']
        variable_metadata_model['description'] = 'testString'
        variable_metadata_model['default_value'] = 'testString'
        variable_metadata_model['secure'] = True
        variable_metadata_model['immutable'] = True
        variable_metadata_model['hidden'] = True
        variable_metadata_model['options'] = ['testString']
        variable_metadata_model['min_value'] = 38
        variable_metadata_model['max_value'] = 38
        variable_metadata_model['min_length'] = 38
        variable_metadata_model['max_length'] = 38
        variable_metadata_model['matches'] = 'testString'
        variable_metadata_model['position'] = 38
        variable_metadata_model['group_by'] = 'testString'
        variable_metadata_model['source'] = 'testString'

        # Construct a dict representation of a VariableData model
        variable_data_model = {}
        variable_data_model['name'] = 'testString'
        variable_data_model['value'] = 'testString'
        variable_data_model['metadata'] = variable_metadata_model

        # Construct a dict representation of a ActionState model
        action_state_model = {}
        action_state_model['status_code'] = 'normal'
        action_state_model['status_message'] = 'testString'

        # Set up parameter values
        name = 'Stop Action'
        description = 'This Action can be used to Stop the targets'
        location = 'us_south'
        resource_group = 'testString'
        tags = ['testString']
        user_state = user_state_model
        source_readme_url = 'testString'
        source = external_source_model
        source_type = 'local'
        command_parameter = 'testString'
        bastion = target_resourceset_model
        targets = [target_resourceset_model]
        inputs = [variable_data_model]
        outputs = [variable_data_model]
        settings = [variable_data_model]
        trigger_record_id = 'testString'
        state = action_state_model
        sys_lock = system_lock_model
        x_github_token = 'testString'

        # Invoke method
        response = service.create_action(
            name=name,
            description=description,
            location=location,
            resource_group=resource_group,
            tags=tags,
            user_state=user_state,
            source_readme_url=source_readme_url,
            source=source,
            source_type=source_type,
            command_parameter=command_parameter,
            bastion=bastion,
            targets=targets,
            inputs=inputs,
            outputs=outputs,
            settings=settings,
            trigger_record_id=trigger_record_id,
            state=state,
            sys_lock=sys_lock,
            x_github_token=x_github_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'Stop Action'
        assert req_body['description'] == 'This Action can be used to Stop the targets'
        assert req_body['location'] == 'us_south'
        assert req_body['resource_group'] == 'testString'
        assert req_body['tags'] == ['testString']
        assert req_body['user_state'] == user_state_model
        assert req_body['source_readme_url'] == 'testString'
        assert req_body['source'] == external_source_model
        assert req_body['source_type'] == 'local'
        assert req_body['command_parameter'] == 'testString'
        assert req_body['bastion'] == target_resourceset_model
        assert req_body['targets'] == [target_resourceset_model]
        assert req_body['inputs'] == [variable_data_model]
        assert req_body['outputs'] == [variable_data_model]
        assert req_body['settings'] == [variable_data_model]
        assert req_body['trigger_record_id'] == 'testString'
        assert req_body['state'] == action_state_model
        assert req_body['sys_lock'] == system_lock_model


    @responses.activate
    def test_create_action_required_params(self):
        """
        test_create_action_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/actions')
        mock_response = '{"name": "Stop Action", "description": "This Action can be used to Stop the targets", "location": "us_south", "resource_group": "resource_group", "tags": ["tags"], "user_state": {"state": "draft", "set_by": "set_by", "set_at": "2019-01-01T12:00:00"}, "source_readme_url": "source_readme_url", "source": {"source_type": "local", "git": {"git_repo_url": "git_repo_url", "git_token": "git_token", "git_repo_folder": "git_repo_folder", "git_release": "git_release", "git_branch": "git_branch"}}, "source_type": "local", "command_parameter": "command_parameter", "bastion": {"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}, "targets": [{"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}], "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "outputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "trigger_record_id": "trigger_record_id", "id": "id", "crn": "crn", "account": "account", "source_created_at": "2019-01-01T12:00:00", "source_created_by": "source_created_by", "source_updated_at": "2019-01-01T12:00:00", "source_updated_by": "source_updated_by", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "namespace": "namespace", "state": {"status_code": "normal", "status_message": "status_message"}, "playbook_names": ["playbook_names"], "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a UserState model
        user_state_model = {}
        user_state_model['state'] = 'draft'
        user_state_model['set_by'] = 'testString'
        user_state_model['set_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a ExternalSourceGit model
        external_source_git_model = {}
        external_source_git_model['git_repo_url'] = 'testString'
        external_source_git_model['git_token'] = 'testString'
        external_source_git_model['git_repo_folder'] = 'testString'
        external_source_git_model['git_release'] = 'testString'
        external_source_git_model['git_branch'] = 'testString'

        # Construct a dict representation of a ExternalSource model
        external_source_model = {}
        external_source_model['source_type'] = 'local'
        external_source_model['git'] = external_source_git_model

        # Construct a dict representation of a SystemLock model
        system_lock_model = {}
        system_lock_model['sys_locked'] = True
        system_lock_model['sys_locked_by'] = 'testString'
        system_lock_model['sys_locked_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a TargetResourceset model
        target_resourceset_model = {}
        target_resourceset_model['name'] = 'testString'
        target_resourceset_model['type'] = 'testString'
        target_resourceset_model['description'] = 'testString'
        target_resourceset_model['resource_query'] = 'testString'
        target_resourceset_model['credential'] = 'testString'
        target_resourceset_model['sys_lock'] = system_lock_model

        # Construct a dict representation of a VariableMetadata model
        variable_metadata_model = {}
        variable_metadata_model['type'] = 'boolean'
        variable_metadata_model['aliases'] = ['testString']
        variable_metadata_model['description'] = 'testString'
        variable_metadata_model['default_value'] = 'testString'
        variable_metadata_model['secure'] = True
        variable_metadata_model['immutable'] = True
        variable_metadata_model['hidden'] = True
        variable_metadata_model['options'] = ['testString']
        variable_metadata_model['min_value'] = 38
        variable_metadata_model['max_value'] = 38
        variable_metadata_model['min_length'] = 38
        variable_metadata_model['max_length'] = 38
        variable_metadata_model['matches'] = 'testString'
        variable_metadata_model['position'] = 38
        variable_metadata_model['group_by'] = 'testString'
        variable_metadata_model['source'] = 'testString'

        # Construct a dict representation of a VariableData model
        variable_data_model = {}
        variable_data_model['name'] = 'testString'
        variable_data_model['value'] = 'testString'
        variable_data_model['metadata'] = variable_metadata_model

        # Construct a dict representation of a ActionState model
        action_state_model = {}
        action_state_model['status_code'] = 'normal'
        action_state_model['status_message'] = 'testString'

        # Set up parameter values
        name = 'Stop Action'
        description = 'This Action can be used to Stop the targets'
        location = 'us_south'
        resource_group = 'testString'
        tags = ['testString']
        user_state = user_state_model
        source_readme_url = 'testString'
        source = external_source_model
        source_type = 'local'
        command_parameter = 'testString'
        bastion = target_resourceset_model
        targets = [target_resourceset_model]
        inputs = [variable_data_model]
        outputs = [variable_data_model]
        settings = [variable_data_model]
        trigger_record_id = 'testString'
        state = action_state_model
        sys_lock = system_lock_model

        # Invoke method
        response = service.create_action(
            name=name,
            description=description,
            location=location,
            resource_group=resource_group,
            tags=tags,
            user_state=user_state,
            source_readme_url=source_readme_url,
            source=source,
            source_type=source_type,
            command_parameter=command_parameter,
            bastion=bastion,
            targets=targets,
            inputs=inputs,
            outputs=outputs,
            settings=settings,
            trigger_record_id=trigger_record_id,
            state=state,
            sys_lock=sys_lock,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'Stop Action'
        assert req_body['description'] == 'This Action can be used to Stop the targets'
        assert req_body['location'] == 'us_south'
        assert req_body['resource_group'] == 'testString'
        assert req_body['tags'] == ['testString']
        assert req_body['user_state'] == user_state_model
        assert req_body['source_readme_url'] == 'testString'
        assert req_body['source'] == external_source_model
        assert req_body['source_type'] == 'local'
        assert req_body['command_parameter'] == 'testString'
        assert req_body['bastion'] == target_resourceset_model
        assert req_body['targets'] == [target_resourceset_model]
        assert req_body['inputs'] == [variable_data_model]
        assert req_body['outputs'] == [variable_data_model]
        assert req_body['settings'] == [variable_data_model]
        assert req_body['trigger_record_id'] == 'testString'
        assert req_body['state'] == action_state_model
        assert req_body['sys_lock'] == system_lock_model


class TestListActions():
    """
    Test Class for list_actions
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_actions_all_params(self):
        """
        list_actions()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/actions')
        mock_response = '{"total_count": 11, "limit": 5, "offset": 6, "actions": [{"name": "Stop Action", "description": "This Action can be used to Stop the targets", "id": "id", "crn": "crn", "location": "us_south", "resource_group": "resource_group", "namespace": "namespace", "tags": ["tags"], "playbook_name": "playbook_name", "user_state": {"state": "draft", "set_by": "set_by", "set_at": "2019-01-01T12:00:00"}, "state": {"status_code": "normal", "status_message": "status_message"}, "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        offset = 0
        limit = 1
        sort = 'testString'
        profile = 'ids'

        # Invoke method
        response = service.list_actions(
            offset=offset,
            limit=limit,
            sort=sort,
            profile=profile,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'offset={}'.format(offset) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'profile={}'.format(profile) in query_string


    @responses.activate
    def test_list_actions_required_params(self):
        """
        test_list_actions_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/actions')
        mock_response = '{"total_count": 11, "limit": 5, "offset": 6, "actions": [{"name": "Stop Action", "description": "This Action can be used to Stop the targets", "id": "id", "crn": "crn", "location": "us_south", "resource_group": "resource_group", "namespace": "namespace", "tags": ["tags"], "playbook_name": "playbook_name", "user_state": {"state": "draft", "set_by": "set_by", "set_at": "2019-01-01T12:00:00"}, "state": {"status_code": "normal", "status_message": "status_message"}, "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_actions()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestGetAction():
    """
    Test Class for get_action
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_action_all_params(self):
        """
        get_action()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/actions/testString')
        mock_response = '{"name": "Stop Action", "description": "This Action can be used to Stop the targets", "location": "us_south", "resource_group": "resource_group", "tags": ["tags"], "user_state": {"state": "draft", "set_by": "set_by", "set_at": "2019-01-01T12:00:00"}, "source_readme_url": "source_readme_url", "source": {"source_type": "local", "git": {"git_repo_url": "git_repo_url", "git_token": "git_token", "git_repo_folder": "git_repo_folder", "git_release": "git_release", "git_branch": "git_branch"}}, "source_type": "local", "command_parameter": "command_parameter", "bastion": {"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}, "targets": [{"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}], "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "outputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "trigger_record_id": "trigger_record_id", "id": "id", "crn": "crn", "account": "account", "source_created_at": "2019-01-01T12:00:00", "source_created_by": "source_created_by", "source_updated_at": "2019-01-01T12:00:00", "source_updated_by": "source_updated_by", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "namespace": "namespace", "state": {"status_code": "normal", "status_message": "status_message"}, "playbook_names": ["playbook_names"], "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        action_id = 'testString'
        profile = 'summary'

        # Invoke method
        response = service.get_action(
            action_id,
            profile=profile,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'profile={}'.format(profile) in query_string


    @responses.activate
    def test_get_action_required_params(self):
        """
        test_get_action_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/actions/testString')
        mock_response = '{"name": "Stop Action", "description": "This Action can be used to Stop the targets", "location": "us_south", "resource_group": "resource_group", "tags": ["tags"], "user_state": {"state": "draft", "set_by": "set_by", "set_at": "2019-01-01T12:00:00"}, "source_readme_url": "source_readme_url", "source": {"source_type": "local", "git": {"git_repo_url": "git_repo_url", "git_token": "git_token", "git_repo_folder": "git_repo_folder", "git_release": "git_release", "git_branch": "git_branch"}}, "source_type": "local", "command_parameter": "command_parameter", "bastion": {"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}, "targets": [{"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}], "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "outputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "trigger_record_id": "trigger_record_id", "id": "id", "crn": "crn", "account": "account", "source_created_at": "2019-01-01T12:00:00", "source_created_by": "source_created_by", "source_updated_at": "2019-01-01T12:00:00", "source_updated_by": "source_updated_by", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "namespace": "namespace", "state": {"status_code": "normal", "status_message": "status_message"}, "playbook_names": ["playbook_names"], "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        action_id = 'testString'

        # Invoke method
        response = service.get_action(
            action_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_action_value_error(self):
        """
        test_get_action_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/actions/testString')
        mock_response = '{"name": "Stop Action", "description": "This Action can be used to Stop the targets", "location": "us_south", "resource_group": "resource_group", "tags": ["tags"], "user_state": {"state": "draft", "set_by": "set_by", "set_at": "2019-01-01T12:00:00"}, "source_readme_url": "source_readme_url", "source": {"source_type": "local", "git": {"git_repo_url": "git_repo_url", "git_token": "git_token", "git_repo_folder": "git_repo_folder", "git_release": "git_release", "git_branch": "git_branch"}}, "source_type": "local", "command_parameter": "command_parameter", "bastion": {"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}, "targets": [{"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}], "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "outputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "trigger_record_id": "trigger_record_id", "id": "id", "crn": "crn", "account": "account", "source_created_at": "2019-01-01T12:00:00", "source_created_by": "source_created_by", "source_updated_at": "2019-01-01T12:00:00", "source_updated_by": "source_updated_by", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "namespace": "namespace", "state": {"status_code": "normal", "status_message": "status_message"}, "playbook_names": ["playbook_names"], "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        action_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "action_id": action_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_action(**req_copy)



class TestDeleteAction():
    """
    Test Class for delete_action
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_action_all_params(self):
        """
        delete_action()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/actions/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        action_id = 'testString'
        force = True
        propagate = True

        # Invoke method
        response = service.delete_action(
            action_id,
            force=force,
            propagate=propagate,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_action_required_params(self):
        """
        test_delete_action_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/actions/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        action_id = 'testString'

        # Invoke method
        response = service.delete_action(
            action_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_action_value_error(self):
        """
        test_delete_action_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/actions/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        action_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "action_id": action_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_action(**req_copy)



class TestUpdateAction():
    """
    Test Class for update_action
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_action_all_params(self):
        """
        update_action()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/actions/testString')
        mock_response = '{"name": "Stop Action", "description": "This Action can be used to Stop the targets", "location": "us_south", "resource_group": "resource_group", "tags": ["tags"], "user_state": {"state": "draft", "set_by": "set_by", "set_at": "2019-01-01T12:00:00"}, "source_readme_url": "source_readme_url", "source": {"source_type": "local", "git": {"git_repo_url": "git_repo_url", "git_token": "git_token", "git_repo_folder": "git_repo_folder", "git_release": "git_release", "git_branch": "git_branch"}}, "source_type": "local", "command_parameter": "command_parameter", "bastion": {"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}, "targets": [{"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}], "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "outputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "trigger_record_id": "trigger_record_id", "id": "id", "crn": "crn", "account": "account", "source_created_at": "2019-01-01T12:00:00", "source_created_by": "source_created_by", "source_updated_at": "2019-01-01T12:00:00", "source_updated_by": "source_updated_by", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "namespace": "namespace", "state": {"status_code": "normal", "status_message": "status_message"}, "playbook_names": ["playbook_names"], "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a UserState model
        user_state_model = {}
        user_state_model['state'] = 'draft'
        user_state_model['set_by'] = 'testString'
        user_state_model['set_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a ExternalSourceGit model
        external_source_git_model = {}
        external_source_git_model['git_repo_url'] = 'testString'
        external_source_git_model['git_token'] = 'testString'
        external_source_git_model['git_repo_folder'] = 'testString'
        external_source_git_model['git_release'] = 'testString'
        external_source_git_model['git_branch'] = 'testString'

        # Construct a dict representation of a ExternalSource model
        external_source_model = {}
        external_source_model['source_type'] = 'local'
        external_source_model['git'] = external_source_git_model

        # Construct a dict representation of a SystemLock model
        system_lock_model = {}
        system_lock_model['sys_locked'] = True
        system_lock_model['sys_locked_by'] = 'testString'
        system_lock_model['sys_locked_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a TargetResourceset model
        target_resourceset_model = {}
        target_resourceset_model['name'] = 'testString'
        target_resourceset_model['type'] = 'testString'
        target_resourceset_model['description'] = 'testString'
        target_resourceset_model['resource_query'] = 'testString'
        target_resourceset_model['credential'] = 'testString'
        target_resourceset_model['sys_lock'] = system_lock_model

        # Construct a dict representation of a VariableMetadata model
        variable_metadata_model = {}
        variable_metadata_model['type'] = 'boolean'
        variable_metadata_model['aliases'] = ['testString']
        variable_metadata_model['description'] = 'testString'
        variable_metadata_model['default_value'] = 'testString'
        variable_metadata_model['secure'] = True
        variable_metadata_model['immutable'] = True
        variable_metadata_model['hidden'] = True
        variable_metadata_model['options'] = ['testString']
        variable_metadata_model['min_value'] = 38
        variable_metadata_model['max_value'] = 38
        variable_metadata_model['min_length'] = 38
        variable_metadata_model['max_length'] = 38
        variable_metadata_model['matches'] = 'testString'
        variable_metadata_model['position'] = 38
        variable_metadata_model['group_by'] = 'testString'
        variable_metadata_model['source'] = 'testString'

        # Construct a dict representation of a VariableData model
        variable_data_model = {}
        variable_data_model['name'] = 'testString'
        variable_data_model['value'] = 'testString'
        variable_data_model['metadata'] = variable_metadata_model

        # Construct a dict representation of a ActionState model
        action_state_model = {}
        action_state_model['status_code'] = 'normal'
        action_state_model['status_message'] = 'testString'

        # Set up parameter values
        action_id = 'testString'
        name = 'Stop Action'
        description = 'This Action can be used to Stop the targets'
        location = 'us_south'
        resource_group = 'testString'
        tags = ['testString']
        user_state = user_state_model
        source_readme_url = 'testString'
        source = external_source_model
        source_type = 'local'
        command_parameter = 'testString'
        bastion = target_resourceset_model
        targets = [target_resourceset_model]
        inputs = [variable_data_model]
        outputs = [variable_data_model]
        settings = [variable_data_model]
        trigger_record_id = 'testString'
        state = action_state_model
        sys_lock = system_lock_model
        x_github_token = 'testString'

        # Invoke method
        response = service.update_action(
            action_id,
            name=name,
            description=description,
            location=location,
            resource_group=resource_group,
            tags=tags,
            user_state=user_state,
            source_readme_url=source_readme_url,
            source=source,
            source_type=source_type,
            command_parameter=command_parameter,
            bastion=bastion,
            targets=targets,
            inputs=inputs,
            outputs=outputs,
            settings=settings,
            trigger_record_id=trigger_record_id,
            state=state,
            sys_lock=sys_lock,
            x_github_token=x_github_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'Stop Action'
        assert req_body['description'] == 'This Action can be used to Stop the targets'
        assert req_body['location'] == 'us_south'
        assert req_body['resource_group'] == 'testString'
        assert req_body['tags'] == ['testString']
        assert req_body['user_state'] == user_state_model
        assert req_body['source_readme_url'] == 'testString'
        assert req_body['source'] == external_source_model
        assert req_body['source_type'] == 'local'
        assert req_body['command_parameter'] == 'testString'
        assert req_body['bastion'] == target_resourceset_model
        assert req_body['targets'] == [target_resourceset_model]
        assert req_body['inputs'] == [variable_data_model]
        assert req_body['outputs'] == [variable_data_model]
        assert req_body['settings'] == [variable_data_model]
        assert req_body['trigger_record_id'] == 'testString'
        assert req_body['state'] == action_state_model
        assert req_body['sys_lock'] == system_lock_model


    @responses.activate
    def test_update_action_required_params(self):
        """
        test_update_action_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/actions/testString')
        mock_response = '{"name": "Stop Action", "description": "This Action can be used to Stop the targets", "location": "us_south", "resource_group": "resource_group", "tags": ["tags"], "user_state": {"state": "draft", "set_by": "set_by", "set_at": "2019-01-01T12:00:00"}, "source_readme_url": "source_readme_url", "source": {"source_type": "local", "git": {"git_repo_url": "git_repo_url", "git_token": "git_token", "git_repo_folder": "git_repo_folder", "git_release": "git_release", "git_branch": "git_branch"}}, "source_type": "local", "command_parameter": "command_parameter", "bastion": {"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}, "targets": [{"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}], "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "outputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "trigger_record_id": "trigger_record_id", "id": "id", "crn": "crn", "account": "account", "source_created_at": "2019-01-01T12:00:00", "source_created_by": "source_created_by", "source_updated_at": "2019-01-01T12:00:00", "source_updated_by": "source_updated_by", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "namespace": "namespace", "state": {"status_code": "normal", "status_message": "status_message"}, "playbook_names": ["playbook_names"], "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a UserState model
        user_state_model = {}
        user_state_model['state'] = 'draft'
        user_state_model['set_by'] = 'testString'
        user_state_model['set_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a ExternalSourceGit model
        external_source_git_model = {}
        external_source_git_model['git_repo_url'] = 'testString'
        external_source_git_model['git_token'] = 'testString'
        external_source_git_model['git_repo_folder'] = 'testString'
        external_source_git_model['git_release'] = 'testString'
        external_source_git_model['git_branch'] = 'testString'

        # Construct a dict representation of a ExternalSource model
        external_source_model = {}
        external_source_model['source_type'] = 'local'
        external_source_model['git'] = external_source_git_model

        # Construct a dict representation of a SystemLock model
        system_lock_model = {}
        system_lock_model['sys_locked'] = True
        system_lock_model['sys_locked_by'] = 'testString'
        system_lock_model['sys_locked_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a TargetResourceset model
        target_resourceset_model = {}
        target_resourceset_model['name'] = 'testString'
        target_resourceset_model['type'] = 'testString'
        target_resourceset_model['description'] = 'testString'
        target_resourceset_model['resource_query'] = 'testString'
        target_resourceset_model['credential'] = 'testString'
        target_resourceset_model['sys_lock'] = system_lock_model

        # Construct a dict representation of a VariableMetadata model
        variable_metadata_model = {}
        variable_metadata_model['type'] = 'boolean'
        variable_metadata_model['aliases'] = ['testString']
        variable_metadata_model['description'] = 'testString'
        variable_metadata_model['default_value'] = 'testString'
        variable_metadata_model['secure'] = True
        variable_metadata_model['immutable'] = True
        variable_metadata_model['hidden'] = True
        variable_metadata_model['options'] = ['testString']
        variable_metadata_model['min_value'] = 38
        variable_metadata_model['max_value'] = 38
        variable_metadata_model['min_length'] = 38
        variable_metadata_model['max_length'] = 38
        variable_metadata_model['matches'] = 'testString'
        variable_metadata_model['position'] = 38
        variable_metadata_model['group_by'] = 'testString'
        variable_metadata_model['source'] = 'testString'

        # Construct a dict representation of a VariableData model
        variable_data_model = {}
        variable_data_model['name'] = 'testString'
        variable_data_model['value'] = 'testString'
        variable_data_model['metadata'] = variable_metadata_model

        # Construct a dict representation of a ActionState model
        action_state_model = {}
        action_state_model['status_code'] = 'normal'
        action_state_model['status_message'] = 'testString'

        # Set up parameter values
        action_id = 'testString'
        name = 'Stop Action'
        description = 'This Action can be used to Stop the targets'
        location = 'us_south'
        resource_group = 'testString'
        tags = ['testString']
        user_state = user_state_model
        source_readme_url = 'testString'
        source = external_source_model
        source_type = 'local'
        command_parameter = 'testString'
        bastion = target_resourceset_model
        targets = [target_resourceset_model]
        inputs = [variable_data_model]
        outputs = [variable_data_model]
        settings = [variable_data_model]
        trigger_record_id = 'testString'
        state = action_state_model
        sys_lock = system_lock_model

        # Invoke method
        response = service.update_action(
            action_id,
            name=name,
            description=description,
            location=location,
            resource_group=resource_group,
            tags=tags,
            user_state=user_state,
            source_readme_url=source_readme_url,
            source=source,
            source_type=source_type,
            command_parameter=command_parameter,
            bastion=bastion,
            targets=targets,
            inputs=inputs,
            outputs=outputs,
            settings=settings,
            trigger_record_id=trigger_record_id,
            state=state,
            sys_lock=sys_lock,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'Stop Action'
        assert req_body['description'] == 'This Action can be used to Stop the targets'
        assert req_body['location'] == 'us_south'
        assert req_body['resource_group'] == 'testString'
        assert req_body['tags'] == ['testString']
        assert req_body['user_state'] == user_state_model
        assert req_body['source_readme_url'] == 'testString'
        assert req_body['source'] == external_source_model
        assert req_body['source_type'] == 'local'
        assert req_body['command_parameter'] == 'testString'
        assert req_body['bastion'] == target_resourceset_model
        assert req_body['targets'] == [target_resourceset_model]
        assert req_body['inputs'] == [variable_data_model]
        assert req_body['outputs'] == [variable_data_model]
        assert req_body['settings'] == [variable_data_model]
        assert req_body['trigger_record_id'] == 'testString'
        assert req_body['state'] == action_state_model
        assert req_body['sys_lock'] == system_lock_model


    @responses.activate
    def test_update_action_value_error(self):
        """
        test_update_action_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/actions/testString')
        mock_response = '{"name": "Stop Action", "description": "This Action can be used to Stop the targets", "location": "us_south", "resource_group": "resource_group", "tags": ["tags"], "user_state": {"state": "draft", "set_by": "set_by", "set_at": "2019-01-01T12:00:00"}, "source_readme_url": "source_readme_url", "source": {"source_type": "local", "git": {"git_repo_url": "git_repo_url", "git_token": "git_token", "git_repo_folder": "git_repo_folder", "git_release": "git_release", "git_branch": "git_branch"}}, "source_type": "local", "command_parameter": "command_parameter", "bastion": {"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}, "targets": [{"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}], "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "outputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "trigger_record_id": "trigger_record_id", "id": "id", "crn": "crn", "account": "account", "source_created_at": "2019-01-01T12:00:00", "source_created_by": "source_created_by", "source_updated_at": "2019-01-01T12:00:00", "source_updated_by": "source_updated_by", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "namespace": "namespace", "state": {"status_code": "normal", "status_message": "status_message"}, "playbook_names": ["playbook_names"], "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a UserState model
        user_state_model = {}
        user_state_model['state'] = 'draft'
        user_state_model['set_by'] = 'testString'
        user_state_model['set_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a ExternalSourceGit model
        external_source_git_model = {}
        external_source_git_model['git_repo_url'] = 'testString'
        external_source_git_model['git_token'] = 'testString'
        external_source_git_model['git_repo_folder'] = 'testString'
        external_source_git_model['git_release'] = 'testString'
        external_source_git_model['git_branch'] = 'testString'

        # Construct a dict representation of a ExternalSource model
        external_source_model = {}
        external_source_model['source_type'] = 'local'
        external_source_model['git'] = external_source_git_model

        # Construct a dict representation of a SystemLock model
        system_lock_model = {}
        system_lock_model['sys_locked'] = True
        system_lock_model['sys_locked_by'] = 'testString'
        system_lock_model['sys_locked_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a TargetResourceset model
        target_resourceset_model = {}
        target_resourceset_model['name'] = 'testString'
        target_resourceset_model['type'] = 'testString'
        target_resourceset_model['description'] = 'testString'
        target_resourceset_model['resource_query'] = 'testString'
        target_resourceset_model['credential'] = 'testString'
        target_resourceset_model['sys_lock'] = system_lock_model

        # Construct a dict representation of a VariableMetadata model
        variable_metadata_model = {}
        variable_metadata_model['type'] = 'boolean'
        variable_metadata_model['aliases'] = ['testString']
        variable_metadata_model['description'] = 'testString'
        variable_metadata_model['default_value'] = 'testString'
        variable_metadata_model['secure'] = True
        variable_metadata_model['immutable'] = True
        variable_metadata_model['hidden'] = True
        variable_metadata_model['options'] = ['testString']
        variable_metadata_model['min_value'] = 38
        variable_metadata_model['max_value'] = 38
        variable_metadata_model['min_length'] = 38
        variable_metadata_model['max_length'] = 38
        variable_metadata_model['matches'] = 'testString'
        variable_metadata_model['position'] = 38
        variable_metadata_model['group_by'] = 'testString'
        variable_metadata_model['source'] = 'testString'

        # Construct a dict representation of a VariableData model
        variable_data_model = {}
        variable_data_model['name'] = 'testString'
        variable_data_model['value'] = 'testString'
        variable_data_model['metadata'] = variable_metadata_model

        # Construct a dict representation of a ActionState model
        action_state_model = {}
        action_state_model['status_code'] = 'normal'
        action_state_model['status_message'] = 'testString'

        # Set up parameter values
        action_id = 'testString'
        name = 'Stop Action'
        description = 'This Action can be used to Stop the targets'
        location = 'us_south'
        resource_group = 'testString'
        tags = ['testString']
        user_state = user_state_model
        source_readme_url = 'testString'
        source = external_source_model
        source_type = 'local'
        command_parameter = 'testString'
        bastion = target_resourceset_model
        targets = [target_resourceset_model]
        inputs = [variable_data_model]
        outputs = [variable_data_model]
        settings = [variable_data_model]
        trigger_record_id = 'testString'
        state = action_state_model
        sys_lock = system_lock_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "action_id": action_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_action(**req_copy)



# endregion
##############################################################################
# End of Service: Actions
##############################################################################

##############################################################################
# Start of Service: Jobs
##############################################################################
# region

class TestCreateJob():
    """
    Test Class for create_job
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_job_all_params(self):
        """
        create_job()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/jobs')
        mock_response = '{"command_object": "workspace", "command_object_id": "command_object_id", "command_name": "workspace_init_flow", "command_parameter": "command_parameter", "command_options": ["command_options"], "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "tags": ["tags"], "id": "id", "name": "name", "description": "description", "location": "us_south", "resource_group": "resource_group", "submitted_at": "2019-01-01T12:00:00", "submitted_by": "submitted_by", "start_at": "2019-01-01T12:00:00", "end_at": "2019-01-01T12:00:00", "duration": "duration", "status": {"action_job_status": {"action_name": "action_name", "status_code": "job_pending", "status_message": "status_message", "bastion_status_code": "none", "bastion_status_message": "bastion_status_message", "targets_status_code": "none", "targets_status_message": "targets_status_message", "updated_at": "2019-01-01T12:00:00"}}, "data": {"job_type": "repo_download_job", "action_job_data": {"action_name": "action_name", "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "outputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "updated_at": "2019-01-01T12:00:00"}}, "targets": [{"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}], "bastion": {"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}, "log_summary": {"job_id": "job_id", "job_type": "repo_download_job", "log_start_at": "2019-01-01T12:00:00", "log_analyzed_till": "2019-01-01T12:00:00", "elapsed_time": 12, "log_errors": [{"error_code": "error_code", "error_msg": "error_msg", "error_count": 11}], "repo_download_job": {"scanned_file_count": 18, "quarantined_file_count": 22, "detected_filetype": "detected_filetype", "inputs_count": "inputs_count", "outputs_count": "outputs_count"}, "action_job": {"target_count": 12, "task_count": 10, "play_count": 10, "recap": {"target": ["target"], "ok": 2, "changed": 7, "failed": 6, "skipped": 7, "unreachable": 11}}}, "log_store_url": "log_store_url", "state_store_url": "state_store_url", "results_url": "results_url", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a VariableMetadata model
        variable_metadata_model = {}
        variable_metadata_model['type'] = 'boolean'
        variable_metadata_model['aliases'] = ['testString']
        variable_metadata_model['description'] = 'testString'
        variable_metadata_model['default_value'] = 'testString'
        variable_metadata_model['secure'] = True
        variable_metadata_model['immutable'] = True
        variable_metadata_model['hidden'] = True
        variable_metadata_model['options'] = ['testString']
        variable_metadata_model['min_value'] = 38
        variable_metadata_model['max_value'] = 38
        variable_metadata_model['min_length'] = 38
        variable_metadata_model['max_length'] = 38
        variable_metadata_model['matches'] = 'testString'
        variable_metadata_model['position'] = 38
        variable_metadata_model['group_by'] = 'testString'
        variable_metadata_model['source'] = 'testString'

        # Construct a dict representation of a VariableData model
        variable_data_model = {}
        variable_data_model['name'] = 'testString'
        variable_data_model['value'] = 'testString'
        variable_data_model['metadata'] = variable_metadata_model

        # Construct a dict representation of a JobStatusAction model
        job_status_action_model = {}
        job_status_action_model['action_name'] = 'testString'
        job_status_action_model['status_code'] = 'job_pending'
        job_status_action_model['status_message'] = 'testString'
        job_status_action_model['bastion_status_code'] = 'none'
        job_status_action_model['bastion_status_message'] = 'testString'
        job_status_action_model['targets_status_code'] = 'none'
        job_status_action_model['targets_status_message'] = 'testString'
        job_status_action_model['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a JobStatus model
        job_status_model = {}
        job_status_model['action_job_status'] = job_status_action_model

        # Construct a dict representation of a JobDataAction model
        job_data_action_model = {}
        job_data_action_model['action_name'] = 'testString'
        job_data_action_model['inputs'] = [variable_data_model]
        job_data_action_model['outputs'] = [variable_data_model]
        job_data_action_model['settings'] = [variable_data_model]
        job_data_action_model['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a JobData model
        job_data_model = {}
        job_data_model['job_type'] = 'repo_download_job'
        job_data_model['action_job_data'] = job_data_action_model

        # Construct a dict representation of a SystemLock model
        system_lock_model = {}
        system_lock_model['sys_locked'] = True
        system_lock_model['sys_locked_by'] = 'testString'
        system_lock_model['sys_locked_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a TargetResourceset model
        target_resourceset_model = {}
        target_resourceset_model['name'] = 'testString'
        target_resourceset_model['type'] = 'testString'
        target_resourceset_model['description'] = 'testString'
        target_resourceset_model['resource_query'] = 'testString'
        target_resourceset_model['credential'] = 'testString'
        target_resourceset_model['sys_lock'] = system_lock_model

        # Construct a dict representation of a JobLogSummaryRepoDownloadJob model
        job_log_summary_repo_download_job_model = {}

        # Construct a dict representation of a JobLogSummaryActionJobRecap model
        job_log_summary_action_job_recap_model = {}
        job_log_summary_action_job_recap_model['target'] = ['testString']
        job_log_summary_action_job_recap_model['ok'] = 72.5
        job_log_summary_action_job_recap_model['changed'] = 72.5
        job_log_summary_action_job_recap_model['failed'] = 72.5
        job_log_summary_action_job_recap_model['skipped'] = 72.5
        job_log_summary_action_job_recap_model['unreachable'] = 72.5

        # Construct a dict representation of a JobLogSummaryActionJob model
        job_log_summary_action_job_model = {}
        job_log_summary_action_job_model['recap'] = job_log_summary_action_job_recap_model

        # Construct a dict representation of a JobLogSummary model
        job_log_summary_model = {}
        job_log_summary_model['job_type'] = 'repo_download_job'
        job_log_summary_model['repo_download_job'] = job_log_summary_repo_download_job_model
        job_log_summary_model['action_job'] = job_log_summary_action_job_model

        # Set up parameter values
        refresh_token = 'testString'
        command_object = 'workspace'
        command_object_id = 'testString'
        command_name = 'workspace_init_flow'
        command_parameter = 'testString'
        command_options = ['testString']
        inputs = [variable_data_model]
        settings = [variable_data_model]
        tags = ['testString']
        location = 'us_south'
        status = job_status_model
        data = job_data_model
        bastion = target_resourceset_model
        log_summary = job_log_summary_model

        # Invoke method
        response = service.create_job(
            refresh_token,
            command_object=command_object,
            command_object_id=command_object_id,
            command_name=command_name,
            command_parameter=command_parameter,
            command_options=command_options,
            inputs=inputs,
            settings=settings,
            tags=tags,
            location=location,
            status=status,
            data=data,
            bastion=bastion,
            log_summary=log_summary,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['command_object'] == 'workspace'
        assert req_body['command_object_id'] == 'testString'
        assert req_body['command_name'] == 'workspace_init_flow'
        assert req_body['command_parameter'] == 'testString'
        assert req_body['command_options'] == ['testString']
        assert req_body['inputs'] == [variable_data_model]
        assert req_body['settings'] == [variable_data_model]
        assert req_body['tags'] == ['testString']
        assert req_body['location'] == 'us_south'
        assert req_body['status'] == job_status_model
        assert req_body['data'] == job_data_model
        assert req_body['bastion'] == target_resourceset_model
        assert req_body['log_summary'] == job_log_summary_model


    @responses.activate
    def test_create_job_value_error(self):
        """
        test_create_job_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/jobs')
        mock_response = '{"command_object": "workspace", "command_object_id": "command_object_id", "command_name": "workspace_init_flow", "command_parameter": "command_parameter", "command_options": ["command_options"], "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "tags": ["tags"], "id": "id", "name": "name", "description": "description", "location": "us_south", "resource_group": "resource_group", "submitted_at": "2019-01-01T12:00:00", "submitted_by": "submitted_by", "start_at": "2019-01-01T12:00:00", "end_at": "2019-01-01T12:00:00", "duration": "duration", "status": {"action_job_status": {"action_name": "action_name", "status_code": "job_pending", "status_message": "status_message", "bastion_status_code": "none", "bastion_status_message": "bastion_status_message", "targets_status_code": "none", "targets_status_message": "targets_status_message", "updated_at": "2019-01-01T12:00:00"}}, "data": {"job_type": "repo_download_job", "action_job_data": {"action_name": "action_name", "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "outputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "updated_at": "2019-01-01T12:00:00"}}, "targets": [{"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}], "bastion": {"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}, "log_summary": {"job_id": "job_id", "job_type": "repo_download_job", "log_start_at": "2019-01-01T12:00:00", "log_analyzed_till": "2019-01-01T12:00:00", "elapsed_time": 12, "log_errors": [{"error_code": "error_code", "error_msg": "error_msg", "error_count": 11}], "repo_download_job": {"scanned_file_count": 18, "quarantined_file_count": 22, "detected_filetype": "detected_filetype", "inputs_count": "inputs_count", "outputs_count": "outputs_count"}, "action_job": {"target_count": 12, "task_count": 10, "play_count": 10, "recap": {"target": ["target"], "ok": 2, "changed": 7, "failed": 6, "skipped": 7, "unreachable": 11}}}, "log_store_url": "log_store_url", "state_store_url": "state_store_url", "results_url": "results_url", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a VariableMetadata model
        variable_metadata_model = {}
        variable_metadata_model['type'] = 'boolean'
        variable_metadata_model['aliases'] = ['testString']
        variable_metadata_model['description'] = 'testString'
        variable_metadata_model['default_value'] = 'testString'
        variable_metadata_model['secure'] = True
        variable_metadata_model['immutable'] = True
        variable_metadata_model['hidden'] = True
        variable_metadata_model['options'] = ['testString']
        variable_metadata_model['min_value'] = 38
        variable_metadata_model['max_value'] = 38
        variable_metadata_model['min_length'] = 38
        variable_metadata_model['max_length'] = 38
        variable_metadata_model['matches'] = 'testString'
        variable_metadata_model['position'] = 38
        variable_metadata_model['group_by'] = 'testString'
        variable_metadata_model['source'] = 'testString'

        # Construct a dict representation of a VariableData model
        variable_data_model = {}
        variable_data_model['name'] = 'testString'
        variable_data_model['value'] = 'testString'
        variable_data_model['metadata'] = variable_metadata_model

        # Construct a dict representation of a JobStatusAction model
        job_status_action_model = {}
        job_status_action_model['action_name'] = 'testString'
        job_status_action_model['status_code'] = 'job_pending'
        job_status_action_model['status_message'] = 'testString'
        job_status_action_model['bastion_status_code'] = 'none'
        job_status_action_model['bastion_status_message'] = 'testString'
        job_status_action_model['targets_status_code'] = 'none'
        job_status_action_model['targets_status_message'] = 'testString'
        job_status_action_model['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a JobStatus model
        job_status_model = {}
        job_status_model['action_job_status'] = job_status_action_model

        # Construct a dict representation of a JobDataAction model
        job_data_action_model = {}
        job_data_action_model['action_name'] = 'testString'
        job_data_action_model['inputs'] = [variable_data_model]
        job_data_action_model['outputs'] = [variable_data_model]
        job_data_action_model['settings'] = [variable_data_model]
        job_data_action_model['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a JobData model
        job_data_model = {}
        job_data_model['job_type'] = 'repo_download_job'
        job_data_model['action_job_data'] = job_data_action_model

        # Construct a dict representation of a SystemLock model
        system_lock_model = {}
        system_lock_model['sys_locked'] = True
        system_lock_model['sys_locked_by'] = 'testString'
        system_lock_model['sys_locked_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a TargetResourceset model
        target_resourceset_model = {}
        target_resourceset_model['name'] = 'testString'
        target_resourceset_model['type'] = 'testString'
        target_resourceset_model['description'] = 'testString'
        target_resourceset_model['resource_query'] = 'testString'
        target_resourceset_model['credential'] = 'testString'
        target_resourceset_model['sys_lock'] = system_lock_model

        # Construct a dict representation of a JobLogSummaryRepoDownloadJob model
        job_log_summary_repo_download_job_model = {}

        # Construct a dict representation of a JobLogSummaryActionJobRecap model
        job_log_summary_action_job_recap_model = {}
        job_log_summary_action_job_recap_model['target'] = ['testString']
        job_log_summary_action_job_recap_model['ok'] = 72.5
        job_log_summary_action_job_recap_model['changed'] = 72.5
        job_log_summary_action_job_recap_model['failed'] = 72.5
        job_log_summary_action_job_recap_model['skipped'] = 72.5
        job_log_summary_action_job_recap_model['unreachable'] = 72.5

        # Construct a dict representation of a JobLogSummaryActionJob model
        job_log_summary_action_job_model = {}
        job_log_summary_action_job_model['recap'] = job_log_summary_action_job_recap_model

        # Construct a dict representation of a JobLogSummary model
        job_log_summary_model = {}
        job_log_summary_model['job_type'] = 'repo_download_job'
        job_log_summary_model['repo_download_job'] = job_log_summary_repo_download_job_model
        job_log_summary_model['action_job'] = job_log_summary_action_job_model

        # Set up parameter values
        refresh_token = 'testString'
        command_object = 'workspace'
        command_object_id = 'testString'
        command_name = 'workspace_init_flow'
        command_parameter = 'testString'
        command_options = ['testString']
        inputs = [variable_data_model]
        settings = [variable_data_model]
        tags = ['testString']
        location = 'us_south'
        status = job_status_model
        data = job_data_model
        bastion = target_resourceset_model
        log_summary = job_log_summary_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "refresh_token": refresh_token,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_job(**req_copy)



class TestListJobs():
    """
    Test Class for list_jobs
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_jobs_all_params(self):
        """
        list_jobs()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/jobs')
        mock_response = '{"total_count": 11, "limit": 5, "offset": 6, "jobs": [{"id": "id", "name": "name", "description": "description", "command_object": "workspace", "command_object_id": "command_object_id", "command_name": "workspace_init_flow", "tags": ["tags"], "location": "us_south", "resource_group": "resource_group", "targets": [{"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}], "submitted_at": "2019-01-01T12:00:00", "submitted_by": "submitted_by", "duration": "duration", "start_at": "2019-01-01T12:00:00", "end_at": "2019-01-01T12:00:00", "status": {"action_job_status": {"action_name": "action_name", "status_code": "job_pending", "status_message": "status_message", "bastion_status_code": "none", "bastion_status_message": "bastion_status_message", "targets_status_code": "none", "targets_status_message": "targets_status_message", "updated_at": "2019-01-01T12:00:00"}}, "log_summary": {"job_id": "job_id", "job_type": "repo_download_job", "log_start_at": "2019-01-01T12:00:00", "log_analyzed_till": "2019-01-01T12:00:00", "elapsed_time": 12, "log_errors": [{"error_code": "error_code", "error_msg": "error_msg", "error_count": 11}], "repo_download_job": {"scanned_file_count": 18, "quarantined_file_count": 22, "detected_filetype": "detected_filetype", "inputs_count": "inputs_count", "outputs_count": "outputs_count"}, "action_job": {"target_count": 12, "task_count": 10, "play_count": 10, "recap": {"target": ["target"], "ok": 2, "changed": 7, "failed": 6, "skipped": 7, "unreachable": 11}}}, "updated_at": "2019-01-01T12:00:00"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        offset = 0
        limit = 1
        sort = 'testString'
        profile = 'ids'
        resource = 'workspaces'
        action_id = 'testString'
        list = 'all'

        # Invoke method
        response = service.list_jobs(
            offset=offset,
            limit=limit,
            sort=sort,
            profile=profile,
            resource=resource,
            action_id=action_id,
            list=list,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'offset={}'.format(offset) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'profile={}'.format(profile) in query_string
        assert 'resource={}'.format(resource) in query_string
        assert 'action_id={}'.format(action_id) in query_string
        assert 'list={}'.format(list) in query_string


    @responses.activate
    def test_list_jobs_required_params(self):
        """
        test_list_jobs_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/jobs')
        mock_response = '{"total_count": 11, "limit": 5, "offset": 6, "jobs": [{"id": "id", "name": "name", "description": "description", "command_object": "workspace", "command_object_id": "command_object_id", "command_name": "workspace_init_flow", "tags": ["tags"], "location": "us_south", "resource_group": "resource_group", "targets": [{"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}], "submitted_at": "2019-01-01T12:00:00", "submitted_by": "submitted_by", "duration": "duration", "start_at": "2019-01-01T12:00:00", "end_at": "2019-01-01T12:00:00", "status": {"action_job_status": {"action_name": "action_name", "status_code": "job_pending", "status_message": "status_message", "bastion_status_code": "none", "bastion_status_message": "bastion_status_message", "targets_status_code": "none", "targets_status_message": "targets_status_message", "updated_at": "2019-01-01T12:00:00"}}, "log_summary": {"job_id": "job_id", "job_type": "repo_download_job", "log_start_at": "2019-01-01T12:00:00", "log_analyzed_till": "2019-01-01T12:00:00", "elapsed_time": 12, "log_errors": [{"error_code": "error_code", "error_msg": "error_msg", "error_count": 11}], "repo_download_job": {"scanned_file_count": 18, "quarantined_file_count": 22, "detected_filetype": "detected_filetype", "inputs_count": "inputs_count", "outputs_count": "outputs_count"}, "action_job": {"target_count": 12, "task_count": 10, "play_count": 10, "recap": {"target": ["target"], "ok": 2, "changed": 7, "failed": 6, "skipped": 7, "unreachable": 11}}}, "updated_at": "2019-01-01T12:00:00"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_jobs()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestReplaceJob():
    """
    Test Class for replace_job
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_replace_job_all_params(self):
        """
        replace_job()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/jobs/testString')
        mock_response = '{"command_object": "workspace", "command_object_id": "command_object_id", "command_name": "workspace_init_flow", "command_parameter": "command_parameter", "command_options": ["command_options"], "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "tags": ["tags"], "id": "id", "name": "name", "description": "description", "location": "us_south", "resource_group": "resource_group", "submitted_at": "2019-01-01T12:00:00", "submitted_by": "submitted_by", "start_at": "2019-01-01T12:00:00", "end_at": "2019-01-01T12:00:00", "duration": "duration", "status": {"action_job_status": {"action_name": "action_name", "status_code": "job_pending", "status_message": "status_message", "bastion_status_code": "none", "bastion_status_message": "bastion_status_message", "targets_status_code": "none", "targets_status_message": "targets_status_message", "updated_at": "2019-01-01T12:00:00"}}, "data": {"job_type": "repo_download_job", "action_job_data": {"action_name": "action_name", "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "outputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "updated_at": "2019-01-01T12:00:00"}}, "targets": [{"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}], "bastion": {"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}, "log_summary": {"job_id": "job_id", "job_type": "repo_download_job", "log_start_at": "2019-01-01T12:00:00", "log_analyzed_till": "2019-01-01T12:00:00", "elapsed_time": 12, "log_errors": [{"error_code": "error_code", "error_msg": "error_msg", "error_count": 11}], "repo_download_job": {"scanned_file_count": 18, "quarantined_file_count": 22, "detected_filetype": "detected_filetype", "inputs_count": "inputs_count", "outputs_count": "outputs_count"}, "action_job": {"target_count": 12, "task_count": 10, "play_count": 10, "recap": {"target": ["target"], "ok": 2, "changed": 7, "failed": 6, "skipped": 7, "unreachable": 11}}}, "log_store_url": "log_store_url", "state_store_url": "state_store_url", "results_url": "results_url", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a VariableMetadata model
        variable_metadata_model = {}
        variable_metadata_model['type'] = 'boolean'
        variable_metadata_model['aliases'] = ['testString']
        variable_metadata_model['description'] = 'testString'
        variable_metadata_model['default_value'] = 'testString'
        variable_metadata_model['secure'] = True
        variable_metadata_model['immutable'] = True
        variable_metadata_model['hidden'] = True
        variable_metadata_model['options'] = ['testString']
        variable_metadata_model['min_value'] = 38
        variable_metadata_model['max_value'] = 38
        variable_metadata_model['min_length'] = 38
        variable_metadata_model['max_length'] = 38
        variable_metadata_model['matches'] = 'testString'
        variable_metadata_model['position'] = 38
        variable_metadata_model['group_by'] = 'testString'
        variable_metadata_model['source'] = 'testString'

        # Construct a dict representation of a VariableData model
        variable_data_model = {}
        variable_data_model['name'] = 'testString'
        variable_data_model['value'] = 'testString'
        variable_data_model['metadata'] = variable_metadata_model

        # Construct a dict representation of a JobStatusAction model
        job_status_action_model = {}
        job_status_action_model['action_name'] = 'testString'
        job_status_action_model['status_code'] = 'job_pending'
        job_status_action_model['status_message'] = 'testString'
        job_status_action_model['bastion_status_code'] = 'none'
        job_status_action_model['bastion_status_message'] = 'testString'
        job_status_action_model['targets_status_code'] = 'none'
        job_status_action_model['targets_status_message'] = 'testString'
        job_status_action_model['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a JobStatus model
        job_status_model = {}
        job_status_model['action_job_status'] = job_status_action_model

        # Construct a dict representation of a JobDataAction model
        job_data_action_model = {}
        job_data_action_model['action_name'] = 'testString'
        job_data_action_model['inputs'] = [variable_data_model]
        job_data_action_model['outputs'] = [variable_data_model]
        job_data_action_model['settings'] = [variable_data_model]
        job_data_action_model['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a JobData model
        job_data_model = {}
        job_data_model['job_type'] = 'repo_download_job'
        job_data_model['action_job_data'] = job_data_action_model

        # Construct a dict representation of a SystemLock model
        system_lock_model = {}
        system_lock_model['sys_locked'] = True
        system_lock_model['sys_locked_by'] = 'testString'
        system_lock_model['sys_locked_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a TargetResourceset model
        target_resourceset_model = {}
        target_resourceset_model['name'] = 'testString'
        target_resourceset_model['type'] = 'testString'
        target_resourceset_model['description'] = 'testString'
        target_resourceset_model['resource_query'] = 'testString'
        target_resourceset_model['credential'] = 'testString'
        target_resourceset_model['sys_lock'] = system_lock_model

        # Construct a dict representation of a JobLogSummaryRepoDownloadJob model
        job_log_summary_repo_download_job_model = {}

        # Construct a dict representation of a JobLogSummaryActionJobRecap model
        job_log_summary_action_job_recap_model = {}
        job_log_summary_action_job_recap_model['target'] = ['testString']
        job_log_summary_action_job_recap_model['ok'] = 72.5
        job_log_summary_action_job_recap_model['changed'] = 72.5
        job_log_summary_action_job_recap_model['failed'] = 72.5
        job_log_summary_action_job_recap_model['skipped'] = 72.5
        job_log_summary_action_job_recap_model['unreachable'] = 72.5

        # Construct a dict representation of a JobLogSummaryActionJob model
        job_log_summary_action_job_model = {}
        job_log_summary_action_job_model['recap'] = job_log_summary_action_job_recap_model

        # Construct a dict representation of a JobLogSummary model
        job_log_summary_model = {}
        job_log_summary_model['job_type'] = 'repo_download_job'
        job_log_summary_model['repo_download_job'] = job_log_summary_repo_download_job_model
        job_log_summary_model['action_job'] = job_log_summary_action_job_model

        # Set up parameter values
        job_id = 'testString'
        refresh_token = 'testString'
        command_object = 'workspace'
        command_object_id = 'testString'
        command_name = 'workspace_init_flow'
        command_parameter = 'testString'
        command_options = ['testString']
        inputs = [variable_data_model]
        settings = [variable_data_model]
        tags = ['testString']
        location = 'us_south'
        status = job_status_model
        data = job_data_model
        bastion = target_resourceset_model
        log_summary = job_log_summary_model

        # Invoke method
        response = service.replace_job(
            job_id,
            refresh_token,
            command_object=command_object,
            command_object_id=command_object_id,
            command_name=command_name,
            command_parameter=command_parameter,
            command_options=command_options,
            inputs=inputs,
            settings=settings,
            tags=tags,
            location=location,
            status=status,
            data=data,
            bastion=bastion,
            log_summary=log_summary,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['command_object'] == 'workspace'
        assert req_body['command_object_id'] == 'testString'
        assert req_body['command_name'] == 'workspace_init_flow'
        assert req_body['command_parameter'] == 'testString'
        assert req_body['command_options'] == ['testString']
        assert req_body['inputs'] == [variable_data_model]
        assert req_body['settings'] == [variable_data_model]
        assert req_body['tags'] == ['testString']
        assert req_body['location'] == 'us_south'
        assert req_body['status'] == job_status_model
        assert req_body['data'] == job_data_model
        assert req_body['bastion'] == target_resourceset_model
        assert req_body['log_summary'] == job_log_summary_model


    @responses.activate
    def test_replace_job_value_error(self):
        """
        test_replace_job_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/jobs/testString')
        mock_response = '{"command_object": "workspace", "command_object_id": "command_object_id", "command_name": "workspace_init_flow", "command_parameter": "command_parameter", "command_options": ["command_options"], "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "tags": ["tags"], "id": "id", "name": "name", "description": "description", "location": "us_south", "resource_group": "resource_group", "submitted_at": "2019-01-01T12:00:00", "submitted_by": "submitted_by", "start_at": "2019-01-01T12:00:00", "end_at": "2019-01-01T12:00:00", "duration": "duration", "status": {"action_job_status": {"action_name": "action_name", "status_code": "job_pending", "status_message": "status_message", "bastion_status_code": "none", "bastion_status_message": "bastion_status_message", "targets_status_code": "none", "targets_status_message": "targets_status_message", "updated_at": "2019-01-01T12:00:00"}}, "data": {"job_type": "repo_download_job", "action_job_data": {"action_name": "action_name", "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "outputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "updated_at": "2019-01-01T12:00:00"}}, "targets": [{"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}], "bastion": {"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}, "log_summary": {"job_id": "job_id", "job_type": "repo_download_job", "log_start_at": "2019-01-01T12:00:00", "log_analyzed_till": "2019-01-01T12:00:00", "elapsed_time": 12, "log_errors": [{"error_code": "error_code", "error_msg": "error_msg", "error_count": 11}], "repo_download_job": {"scanned_file_count": 18, "quarantined_file_count": 22, "detected_filetype": "detected_filetype", "inputs_count": "inputs_count", "outputs_count": "outputs_count"}, "action_job": {"target_count": 12, "task_count": 10, "play_count": 10, "recap": {"target": ["target"], "ok": 2, "changed": 7, "failed": 6, "skipped": 7, "unreachable": 11}}}, "log_store_url": "log_store_url", "state_store_url": "state_store_url", "results_url": "results_url", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a VariableMetadata model
        variable_metadata_model = {}
        variable_metadata_model['type'] = 'boolean'
        variable_metadata_model['aliases'] = ['testString']
        variable_metadata_model['description'] = 'testString'
        variable_metadata_model['default_value'] = 'testString'
        variable_metadata_model['secure'] = True
        variable_metadata_model['immutable'] = True
        variable_metadata_model['hidden'] = True
        variable_metadata_model['options'] = ['testString']
        variable_metadata_model['min_value'] = 38
        variable_metadata_model['max_value'] = 38
        variable_metadata_model['min_length'] = 38
        variable_metadata_model['max_length'] = 38
        variable_metadata_model['matches'] = 'testString'
        variable_metadata_model['position'] = 38
        variable_metadata_model['group_by'] = 'testString'
        variable_metadata_model['source'] = 'testString'

        # Construct a dict representation of a VariableData model
        variable_data_model = {}
        variable_data_model['name'] = 'testString'
        variable_data_model['value'] = 'testString'
        variable_data_model['metadata'] = variable_metadata_model

        # Construct a dict representation of a JobStatusAction model
        job_status_action_model = {}
        job_status_action_model['action_name'] = 'testString'
        job_status_action_model['status_code'] = 'job_pending'
        job_status_action_model['status_message'] = 'testString'
        job_status_action_model['bastion_status_code'] = 'none'
        job_status_action_model['bastion_status_message'] = 'testString'
        job_status_action_model['targets_status_code'] = 'none'
        job_status_action_model['targets_status_message'] = 'testString'
        job_status_action_model['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a JobStatus model
        job_status_model = {}
        job_status_model['action_job_status'] = job_status_action_model

        # Construct a dict representation of a JobDataAction model
        job_data_action_model = {}
        job_data_action_model['action_name'] = 'testString'
        job_data_action_model['inputs'] = [variable_data_model]
        job_data_action_model['outputs'] = [variable_data_model]
        job_data_action_model['settings'] = [variable_data_model]
        job_data_action_model['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a JobData model
        job_data_model = {}
        job_data_model['job_type'] = 'repo_download_job'
        job_data_model['action_job_data'] = job_data_action_model

        # Construct a dict representation of a SystemLock model
        system_lock_model = {}
        system_lock_model['sys_locked'] = True
        system_lock_model['sys_locked_by'] = 'testString'
        system_lock_model['sys_locked_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a dict representation of a TargetResourceset model
        target_resourceset_model = {}
        target_resourceset_model['name'] = 'testString'
        target_resourceset_model['type'] = 'testString'
        target_resourceset_model['description'] = 'testString'
        target_resourceset_model['resource_query'] = 'testString'
        target_resourceset_model['credential'] = 'testString'
        target_resourceset_model['sys_lock'] = system_lock_model

        # Construct a dict representation of a JobLogSummaryRepoDownloadJob model
        job_log_summary_repo_download_job_model = {}

        # Construct a dict representation of a JobLogSummaryActionJobRecap model
        job_log_summary_action_job_recap_model = {}
        job_log_summary_action_job_recap_model['target'] = ['testString']
        job_log_summary_action_job_recap_model['ok'] = 72.5
        job_log_summary_action_job_recap_model['changed'] = 72.5
        job_log_summary_action_job_recap_model['failed'] = 72.5
        job_log_summary_action_job_recap_model['skipped'] = 72.5
        job_log_summary_action_job_recap_model['unreachable'] = 72.5

        # Construct a dict representation of a JobLogSummaryActionJob model
        job_log_summary_action_job_model = {}
        job_log_summary_action_job_model['recap'] = job_log_summary_action_job_recap_model

        # Construct a dict representation of a JobLogSummary model
        job_log_summary_model = {}
        job_log_summary_model['job_type'] = 'repo_download_job'
        job_log_summary_model['repo_download_job'] = job_log_summary_repo_download_job_model
        job_log_summary_model['action_job'] = job_log_summary_action_job_model

        # Set up parameter values
        job_id = 'testString'
        refresh_token = 'testString'
        command_object = 'workspace'
        command_object_id = 'testString'
        command_name = 'workspace_init_flow'
        command_parameter = 'testString'
        command_options = ['testString']
        inputs = [variable_data_model]
        settings = [variable_data_model]
        tags = ['testString']
        location = 'us_south'
        status = job_status_model
        data = job_data_model
        bastion = target_resourceset_model
        log_summary = job_log_summary_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "job_id": job_id,
            "refresh_token": refresh_token,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.replace_job(**req_copy)



class TestDeleteJob():
    """
    Test Class for delete_job
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_job_all_params(self):
        """
        delete_job()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/jobs/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        job_id = 'testString'
        refresh_token = 'testString'
        force = True
        propagate = True

        # Invoke method
        response = service.delete_job(
            job_id,
            refresh_token,
            force=force,
            propagate=propagate,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_job_required_params(self):
        """
        test_delete_job_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/jobs/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        job_id = 'testString'
        refresh_token = 'testString'

        # Invoke method
        response = service.delete_job(
            job_id,
            refresh_token,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_job_value_error(self):
        """
        test_delete_job_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/jobs/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        job_id = 'testString'
        refresh_token = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "job_id": job_id,
            "refresh_token": refresh_token,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_job(**req_copy)



class TestGetJob():
    """
    Test Class for get_job
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_job_all_params(self):
        """
        get_job()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/jobs/testString')
        mock_response = '{"command_object": "workspace", "command_object_id": "command_object_id", "command_name": "workspace_init_flow", "command_parameter": "command_parameter", "command_options": ["command_options"], "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "tags": ["tags"], "id": "id", "name": "name", "description": "description", "location": "us_south", "resource_group": "resource_group", "submitted_at": "2019-01-01T12:00:00", "submitted_by": "submitted_by", "start_at": "2019-01-01T12:00:00", "end_at": "2019-01-01T12:00:00", "duration": "duration", "status": {"action_job_status": {"action_name": "action_name", "status_code": "job_pending", "status_message": "status_message", "bastion_status_code": "none", "bastion_status_message": "bastion_status_message", "targets_status_code": "none", "targets_status_message": "targets_status_message", "updated_at": "2019-01-01T12:00:00"}}, "data": {"job_type": "repo_download_job", "action_job_data": {"action_name": "action_name", "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "outputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "updated_at": "2019-01-01T12:00:00"}}, "targets": [{"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}], "bastion": {"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}, "log_summary": {"job_id": "job_id", "job_type": "repo_download_job", "log_start_at": "2019-01-01T12:00:00", "log_analyzed_till": "2019-01-01T12:00:00", "elapsed_time": 12, "log_errors": [{"error_code": "error_code", "error_msg": "error_msg", "error_count": 11}], "repo_download_job": {"scanned_file_count": 18, "quarantined_file_count": 22, "detected_filetype": "detected_filetype", "inputs_count": "inputs_count", "outputs_count": "outputs_count"}, "action_job": {"target_count": 12, "task_count": 10, "play_count": 10, "recap": {"target": ["target"], "ok": 2, "changed": 7, "failed": 6, "skipped": 7, "unreachable": 11}}}, "log_store_url": "log_store_url", "state_store_url": "state_store_url", "results_url": "results_url", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        job_id = 'testString'
        profile = 'summary'

        # Invoke method
        response = service.get_job(
            job_id,
            profile=profile,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'profile={}'.format(profile) in query_string


    @responses.activate
    def test_get_job_required_params(self):
        """
        test_get_job_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/jobs/testString')
        mock_response = '{"command_object": "workspace", "command_object_id": "command_object_id", "command_name": "workspace_init_flow", "command_parameter": "command_parameter", "command_options": ["command_options"], "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "tags": ["tags"], "id": "id", "name": "name", "description": "description", "location": "us_south", "resource_group": "resource_group", "submitted_at": "2019-01-01T12:00:00", "submitted_by": "submitted_by", "start_at": "2019-01-01T12:00:00", "end_at": "2019-01-01T12:00:00", "duration": "duration", "status": {"action_job_status": {"action_name": "action_name", "status_code": "job_pending", "status_message": "status_message", "bastion_status_code": "none", "bastion_status_message": "bastion_status_message", "targets_status_code": "none", "targets_status_message": "targets_status_message", "updated_at": "2019-01-01T12:00:00"}}, "data": {"job_type": "repo_download_job", "action_job_data": {"action_name": "action_name", "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "outputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "updated_at": "2019-01-01T12:00:00"}}, "targets": [{"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}], "bastion": {"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}, "log_summary": {"job_id": "job_id", "job_type": "repo_download_job", "log_start_at": "2019-01-01T12:00:00", "log_analyzed_till": "2019-01-01T12:00:00", "elapsed_time": 12, "log_errors": [{"error_code": "error_code", "error_msg": "error_msg", "error_count": 11}], "repo_download_job": {"scanned_file_count": 18, "quarantined_file_count": 22, "detected_filetype": "detected_filetype", "inputs_count": "inputs_count", "outputs_count": "outputs_count"}, "action_job": {"target_count": 12, "task_count": 10, "play_count": 10, "recap": {"target": ["target"], "ok": 2, "changed": 7, "failed": 6, "skipped": 7, "unreachable": 11}}}, "log_store_url": "log_store_url", "state_store_url": "state_store_url", "results_url": "results_url", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        job_id = 'testString'

        # Invoke method
        response = service.get_job(
            job_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_job_value_error(self):
        """
        test_get_job_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/jobs/testString')
        mock_response = '{"command_object": "workspace", "command_object_id": "command_object_id", "command_name": "workspace_init_flow", "command_parameter": "command_parameter", "command_options": ["command_options"], "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "tags": ["tags"], "id": "id", "name": "name", "description": "description", "location": "us_south", "resource_group": "resource_group", "submitted_at": "2019-01-01T12:00:00", "submitted_by": "submitted_by", "start_at": "2019-01-01T12:00:00", "end_at": "2019-01-01T12:00:00", "duration": "duration", "status": {"action_job_status": {"action_name": "action_name", "status_code": "job_pending", "status_message": "status_message", "bastion_status_code": "none", "bastion_status_message": "bastion_status_message", "targets_status_code": "none", "targets_status_message": "targets_status_message", "updated_at": "2019-01-01T12:00:00"}}, "data": {"job_type": "repo_download_job", "action_job_data": {"action_name": "action_name", "inputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "outputs": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "settings": [{"name": "name", "value": "value", "metadata": {"type": "boolean", "aliases": ["aliases"], "description": "description", "default_value": "default_value", "secure": true, "immutable": false, "hidden": true, "options": ["options"], "min_value": 9, "max_value": 9, "min_length": 10, "max_length": 10, "matches": "matches", "position": 8, "group_by": "group_by", "source": "source"}, "link": "link"}], "updated_at": "2019-01-01T12:00:00"}}, "targets": [{"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}], "bastion": {"name": "name", "type": "type", "description": "description", "resource_query": "resource_query", "credential": "credential", "id": "id", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "sys_lock": {"sys_locked": true, "sys_locked_by": "sys_locked_by", "sys_locked_at": "2019-01-01T12:00:00"}, "resource_ids": ["resource_ids"]}, "log_summary": {"job_id": "job_id", "job_type": "repo_download_job", "log_start_at": "2019-01-01T12:00:00", "log_analyzed_till": "2019-01-01T12:00:00", "elapsed_time": 12, "log_errors": [{"error_code": "error_code", "error_msg": "error_msg", "error_count": 11}], "repo_download_job": {"scanned_file_count": 18, "quarantined_file_count": 22, "detected_filetype": "detected_filetype", "inputs_count": "inputs_count", "outputs_count": "outputs_count"}, "action_job": {"target_count": 12, "task_count": 10, "play_count": 10, "recap": {"target": ["target"], "ok": 2, "changed": 7, "failed": 6, "skipped": 7, "unreachable": 11}}}, "log_store_url": "log_store_url", "state_store_url": "state_store_url", "results_url": "results_url", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        job_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "job_id": job_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_job(**req_copy)



class TestListJobLogs():
    """
    Test Class for list_job_logs
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_job_logs_all_params(self):
        """
        list_job_logs()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/jobs/testString/logs')
        mock_response = '{"job_id": "job_id", "job_name": "job_name", "log_summary": {"job_id": "job_id", "job_type": "repo_download_job", "log_start_at": "2019-01-01T12:00:00", "log_analyzed_till": "2019-01-01T12:00:00", "elapsed_time": 12, "log_errors": [{"error_code": "error_code", "error_msg": "error_msg", "error_count": 11}], "repo_download_job": {"scanned_file_count": 18, "quarantined_file_count": 22, "detected_filetype": "detected_filetype", "inputs_count": "inputs_count", "outputs_count": "outputs_count"}, "action_job": {"target_count": 12, "task_count": 10, "play_count": 10, "recap": {"target": ["target"], "ok": 2, "changed": 7, "failed": 6, "skipped": 7, "unreachable": 11}}}, "format": "json", "details": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        job_id = 'testString'

        # Invoke method
        response = service.list_job_logs(
            job_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_list_job_logs_value_error(self):
        """
        test_list_job_logs_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/jobs/testString/logs')
        mock_response = '{"job_id": "job_id", "job_name": "job_name", "log_summary": {"job_id": "job_id", "job_type": "repo_download_job", "log_start_at": "2019-01-01T12:00:00", "log_analyzed_till": "2019-01-01T12:00:00", "elapsed_time": 12, "log_errors": [{"error_code": "error_code", "error_msg": "error_msg", "error_count": 11}], "repo_download_job": {"scanned_file_count": 18, "quarantined_file_count": 22, "detected_filetype": "detected_filetype", "inputs_count": "inputs_count", "outputs_count": "outputs_count"}, "action_job": {"target_count": 12, "task_count": 10, "play_count": 10, "recap": {"target": ["target"], "ok": 2, "changed": 7, "failed": 6, "skipped": 7, "unreachable": 11}}}, "format": "json", "details": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        job_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "job_id": job_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_job_logs(**req_copy)



class TestListJobStates():
    """
    Test Class for list_job_states
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_job_states_all_params(self):
        """
        list_job_states()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/jobs/testString/states')
        mock_response = '{"job_id": "job_id", "job_name": "job_name", "summary": [{"name": "name", "type": "number", "value": "value"}], "format": "format", "details": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        job_id = 'testString'

        # Invoke method
        response = service.list_job_states(
            job_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_list_job_states_value_error(self):
        """
        test_list_job_states_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/jobs/testString/states')
        mock_response = '{"job_id": "job_id", "job_name": "job_name", "summary": [{"name": "name", "type": "number", "value": "value"}], "format": "format", "details": "VGhpcyBpcyBhbiBlbmNvZGVkIGJ5dGUgYXJyYXku", "updated_at": "2019-01-01T12:00:00"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        job_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "job_id": job_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_job_states(**req_copy)



# endregion
##############################################################################
# End of Service: Jobs
##############################################################################

##############################################################################
# Start of Service: Datasets
##############################################################################
# region

class TestListSharedDatasets():
    """
    Test Class for list_shared_datasets
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_shared_datasets_all_params(self):
        """
        list_shared_datasets()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/shared_datasets')
        mock_response = '{"count": 5, "shared_datasets": [{"account": "account", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "description": "description", "effected_workspace_ids": ["effected_workspace_ids"], "resource_group": "resource_group", "shared_dataset_data": [{"default_value": "default_value", "description": "description", "hidden": true, "immutable": false, "matches": "matches", "max_value": "max_value", "max_value_len": "max_value_len", "min_value": "min_value", "min_value_len": "min_value_len", "options": ["options"], "override_value": "override_value", "secure": true, "var_aliases": ["var_aliases"], "var_name": "var_name", "var_ref": "var_ref", "var_type": "var_type"}], "shared_dataset_id": "shared_dataset_id", "shared_dataset_name": "shared_dataset_name", "shared_dataset_type": ["shared_dataset_type"], "state": "state", "tags": ["tags"], "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "version": "version"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_shared_datasets()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestCreateSharedDataset():
    """
    Test Class for create_shared_dataset
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_shared_dataset_all_params(self):
        """
        create_shared_dataset()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/shared_datasets')
        mock_response = '{"account": "account", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "description": "description", "effected_workspace_ids": ["effected_workspace_ids"], "resource_group": "resource_group", "shared_dataset_data": [{"default_value": "default_value", "description": "description", "hidden": true, "immutable": false, "matches": "matches", "max_value": "max_value", "max_value_len": "max_value_len", "min_value": "min_value", "min_value_len": "min_value_len", "options": ["options"], "override_value": "override_value", "secure": true, "var_aliases": ["var_aliases"], "var_name": "var_name", "var_ref": "var_ref", "var_type": "var_type"}], "shared_dataset_id": "shared_dataset_id", "shared_dataset_name": "shared_dataset_name", "shared_dataset_type": ["shared_dataset_type"], "state": "state", "tags": ["tags"], "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "version": "version"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a SharedDatasetData model
        shared_dataset_data_model = {}
        shared_dataset_data_model['default_value'] = 'testString'
        shared_dataset_data_model['description'] = 'testString'
        shared_dataset_data_model['hidden'] = True
        shared_dataset_data_model['immutable'] = True
        shared_dataset_data_model['matches'] = 'testString'
        shared_dataset_data_model['max_value'] = 'testString'
        shared_dataset_data_model['max_value_len'] = 'testString'
        shared_dataset_data_model['min_value'] = 'testString'
        shared_dataset_data_model['min_value_len'] = 'testString'
        shared_dataset_data_model['options'] = ['testString']
        shared_dataset_data_model['override_value'] = 'testString'
        shared_dataset_data_model['secure'] = True
        shared_dataset_data_model['var_aliases'] = ['testString']
        shared_dataset_data_model['var_name'] = 'testString'
        shared_dataset_data_model['var_ref'] = 'testString'
        shared_dataset_data_model['var_type'] = 'testString'

        # Set up parameter values
        auto_propagate_change = True
        description = 'testString'
        effected_workspace_ids = ['testString']
        resource_group = 'testString'
        shared_dataset_data = [shared_dataset_data_model]
        shared_dataset_name = 'testString'
        shared_dataset_source_name = 'testString'
        shared_dataset_type = ['testString']
        tags = ['testString']
        version = 'testString'

        # Invoke method
        response = service.create_shared_dataset(
            auto_propagate_change=auto_propagate_change,
            description=description,
            effected_workspace_ids=effected_workspace_ids,
            resource_group=resource_group,
            shared_dataset_data=shared_dataset_data,
            shared_dataset_name=shared_dataset_name,
            shared_dataset_source_name=shared_dataset_source_name,
            shared_dataset_type=shared_dataset_type,
            tags=tags,
            version=version,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['auto_propagate_change'] == True
        assert req_body['description'] == 'testString'
        assert req_body['effected_workspace_ids'] == ['testString']
        assert req_body['resource_group'] == 'testString'
        assert req_body['shared_dataset_data'] == [shared_dataset_data_model]
        assert req_body['shared_dataset_name'] == 'testString'
        assert req_body['shared_dataset_source_name'] == 'testString'
        assert req_body['shared_dataset_type'] == ['testString']
        assert req_body['tags'] == ['testString']
        assert req_body['version'] == 'testString'


class TestGetSharedDataset():
    """
    Test Class for get_shared_dataset
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_shared_dataset_all_params(self):
        """
        get_shared_dataset()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/shared_datasets/testString')
        mock_response = '{"account": "account", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "description": "description", "effected_workspace_ids": ["effected_workspace_ids"], "resource_group": "resource_group", "shared_dataset_data": [{"default_value": "default_value", "description": "description", "hidden": true, "immutable": false, "matches": "matches", "max_value": "max_value", "max_value_len": "max_value_len", "min_value": "min_value", "min_value_len": "min_value_len", "options": ["options"], "override_value": "override_value", "secure": true, "var_aliases": ["var_aliases"], "var_name": "var_name", "var_ref": "var_ref", "var_type": "var_type"}], "shared_dataset_id": "shared_dataset_id", "shared_dataset_name": "shared_dataset_name", "shared_dataset_type": ["shared_dataset_type"], "state": "state", "tags": ["tags"], "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "version": "version"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        sd_id = 'testString'

        # Invoke method
        response = service.get_shared_dataset(
            sd_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_shared_dataset_value_error(self):
        """
        test_get_shared_dataset_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/shared_datasets/testString')
        mock_response = '{"account": "account", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "description": "description", "effected_workspace_ids": ["effected_workspace_ids"], "resource_group": "resource_group", "shared_dataset_data": [{"default_value": "default_value", "description": "description", "hidden": true, "immutable": false, "matches": "matches", "max_value": "max_value", "max_value_len": "max_value_len", "min_value": "min_value", "min_value_len": "min_value_len", "options": ["options"], "override_value": "override_value", "secure": true, "var_aliases": ["var_aliases"], "var_name": "var_name", "var_ref": "var_ref", "var_type": "var_type"}], "shared_dataset_id": "shared_dataset_id", "shared_dataset_name": "shared_dataset_name", "shared_dataset_type": ["shared_dataset_type"], "state": "state", "tags": ["tags"], "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "version": "version"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        sd_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "sd_id": sd_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_shared_dataset(**req_copy)



class TestReplaceSharedDataset():
    """
    Test Class for replace_shared_dataset
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_replace_shared_dataset_all_params(self):
        """
        replace_shared_dataset()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/shared_datasets/testString')
        mock_response = '{"account": "account", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "description": "description", "effected_workspace_ids": ["effected_workspace_ids"], "resource_group": "resource_group", "shared_dataset_data": [{"default_value": "default_value", "description": "description", "hidden": true, "immutable": false, "matches": "matches", "max_value": "max_value", "max_value_len": "max_value_len", "min_value": "min_value", "min_value_len": "min_value_len", "options": ["options"], "override_value": "override_value", "secure": true, "var_aliases": ["var_aliases"], "var_name": "var_name", "var_ref": "var_ref", "var_type": "var_type"}], "shared_dataset_id": "shared_dataset_id", "shared_dataset_name": "shared_dataset_name", "shared_dataset_type": ["shared_dataset_type"], "state": "state", "tags": ["tags"], "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "version": "version"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a SharedDatasetData model
        shared_dataset_data_model = {}
        shared_dataset_data_model['default_value'] = 'testString'
        shared_dataset_data_model['description'] = 'testString'
        shared_dataset_data_model['hidden'] = True
        shared_dataset_data_model['immutable'] = True
        shared_dataset_data_model['matches'] = 'testString'
        shared_dataset_data_model['max_value'] = 'testString'
        shared_dataset_data_model['max_value_len'] = 'testString'
        shared_dataset_data_model['min_value'] = 'testString'
        shared_dataset_data_model['min_value_len'] = 'testString'
        shared_dataset_data_model['options'] = ['testString']
        shared_dataset_data_model['override_value'] = 'testString'
        shared_dataset_data_model['secure'] = True
        shared_dataset_data_model['var_aliases'] = ['testString']
        shared_dataset_data_model['var_name'] = 'testString'
        shared_dataset_data_model['var_ref'] = 'testString'
        shared_dataset_data_model['var_type'] = 'testString'

        # Set up parameter values
        sd_id = 'testString'
        auto_propagate_change = True
        description = 'testString'
        effected_workspace_ids = ['testString']
        resource_group = 'testString'
        shared_dataset_data = [shared_dataset_data_model]
        shared_dataset_name = 'testString'
        shared_dataset_source_name = 'testString'
        shared_dataset_type = ['testString']
        tags = ['testString']
        version = 'testString'

        # Invoke method
        response = service.replace_shared_dataset(
            sd_id,
            auto_propagate_change=auto_propagate_change,
            description=description,
            effected_workspace_ids=effected_workspace_ids,
            resource_group=resource_group,
            shared_dataset_data=shared_dataset_data,
            shared_dataset_name=shared_dataset_name,
            shared_dataset_source_name=shared_dataset_source_name,
            shared_dataset_type=shared_dataset_type,
            tags=tags,
            version=version,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['auto_propagate_change'] == True
        assert req_body['description'] == 'testString'
        assert req_body['effected_workspace_ids'] == ['testString']
        assert req_body['resource_group'] == 'testString'
        assert req_body['shared_dataset_data'] == [shared_dataset_data_model]
        assert req_body['shared_dataset_name'] == 'testString'
        assert req_body['shared_dataset_source_name'] == 'testString'
        assert req_body['shared_dataset_type'] == ['testString']
        assert req_body['tags'] == ['testString']
        assert req_body['version'] == 'testString'


    @responses.activate
    def test_replace_shared_dataset_value_error(self):
        """
        test_replace_shared_dataset_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/shared_datasets/testString')
        mock_response = '{"account": "account", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "description": "description", "effected_workspace_ids": ["effected_workspace_ids"], "resource_group": "resource_group", "shared_dataset_data": [{"default_value": "default_value", "description": "description", "hidden": true, "immutable": false, "matches": "matches", "max_value": "max_value", "max_value_len": "max_value_len", "min_value": "min_value", "min_value_len": "min_value_len", "options": ["options"], "override_value": "override_value", "secure": true, "var_aliases": ["var_aliases"], "var_name": "var_name", "var_ref": "var_ref", "var_type": "var_type"}], "shared_dataset_id": "shared_dataset_id", "shared_dataset_name": "shared_dataset_name", "shared_dataset_type": ["shared_dataset_type"], "state": "state", "tags": ["tags"], "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "version": "version"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a SharedDatasetData model
        shared_dataset_data_model = {}
        shared_dataset_data_model['default_value'] = 'testString'
        shared_dataset_data_model['description'] = 'testString'
        shared_dataset_data_model['hidden'] = True
        shared_dataset_data_model['immutable'] = True
        shared_dataset_data_model['matches'] = 'testString'
        shared_dataset_data_model['max_value'] = 'testString'
        shared_dataset_data_model['max_value_len'] = 'testString'
        shared_dataset_data_model['min_value'] = 'testString'
        shared_dataset_data_model['min_value_len'] = 'testString'
        shared_dataset_data_model['options'] = ['testString']
        shared_dataset_data_model['override_value'] = 'testString'
        shared_dataset_data_model['secure'] = True
        shared_dataset_data_model['var_aliases'] = ['testString']
        shared_dataset_data_model['var_name'] = 'testString'
        shared_dataset_data_model['var_ref'] = 'testString'
        shared_dataset_data_model['var_type'] = 'testString'

        # Set up parameter values
        sd_id = 'testString'
        auto_propagate_change = True
        description = 'testString'
        effected_workspace_ids = ['testString']
        resource_group = 'testString'
        shared_dataset_data = [shared_dataset_data_model]
        shared_dataset_name = 'testString'
        shared_dataset_source_name = 'testString'
        shared_dataset_type = ['testString']
        tags = ['testString']
        version = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "sd_id": sd_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.replace_shared_dataset(**req_copy)



class TestDeleteSharedDataset():
    """
    Test Class for delete_shared_dataset
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_shared_dataset_all_params(self):
        """
        delete_shared_dataset()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/shared_datasets/testString')
        mock_response = '{"account": "account", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "description": "description", "effected_workspace_ids": ["effected_workspace_ids"], "resource_group": "resource_group", "shared_dataset_data": [{"default_value": "default_value", "description": "description", "hidden": true, "immutable": false, "matches": "matches", "max_value": "max_value", "max_value_len": "max_value_len", "min_value": "min_value", "min_value_len": "min_value_len", "options": ["options"], "override_value": "override_value", "secure": true, "var_aliases": ["var_aliases"], "var_name": "var_name", "var_ref": "var_ref", "var_type": "var_type"}], "shared_dataset_id": "shared_dataset_id", "shared_dataset_name": "shared_dataset_name", "shared_dataset_type": ["shared_dataset_type"], "state": "state", "tags": ["tags"], "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "version": "version"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        sd_id = 'testString'

        # Invoke method
        response = service.delete_shared_dataset(
            sd_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_shared_dataset_value_error(self):
        """
        test_delete_shared_dataset_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/shared_datasets/testString')
        mock_response = '{"account": "account", "created_at": "2019-01-01T12:00:00", "created_by": "created_by", "description": "description", "effected_workspace_ids": ["effected_workspace_ids"], "resource_group": "resource_group", "shared_dataset_data": [{"default_value": "default_value", "description": "description", "hidden": true, "immutable": false, "matches": "matches", "max_value": "max_value", "max_value_len": "max_value_len", "min_value": "min_value", "min_value_len": "min_value_len", "options": ["options"], "override_value": "override_value", "secure": true, "var_aliases": ["var_aliases"], "var_name": "var_name", "var_ref": "var_ref", "var_type": "var_type"}], "shared_dataset_id": "shared_dataset_id", "shared_dataset_name": "shared_dataset_name", "shared_dataset_type": ["shared_dataset_type"], "state": "state", "tags": ["tags"], "updated_at": "2019-01-01T12:00:00", "updated_by": "updated_by", "version": "version"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        sd_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "sd_id": sd_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_shared_dataset(**req_copy)



# endregion
##############################################################################
# End of Service: Datasets
##############################################################################

##############################################################################
# Start of Service: SettingsKms
##############################################################################
# region

class TestGetKmsSettings():
    """
    Test Class for get_kms_settings
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_kms_settings_all_params(self):
        """
        get_kms_settings()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/settings/kms')
        mock_response = '{"location": "location", "encryption_scheme": "encryption_scheme", "resource_group": "resource_group", "primary_crk": {"kms_name": "kms_name", "kms_private_endpoint": "kms_private_endpoint", "key_crn": "key_crn"}, "secondary_crk": {"kms_name": "kms_name", "kms_private_endpoint": "kms_private_endpoint", "key_crn": "key_crn"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        location = 'testString'

        # Invoke method
        response = service.get_kms_settings(
            location,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'location={}'.format(location) in query_string


    @responses.activate
    def test_get_kms_settings_value_error(self):
        """
        test_get_kms_settings_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/settings/kms')
        mock_response = '{"location": "location", "encryption_scheme": "encryption_scheme", "resource_group": "resource_group", "primary_crk": {"kms_name": "kms_name", "kms_private_endpoint": "kms_private_endpoint", "key_crn": "key_crn"}, "secondary_crk": {"kms_name": "kms_name", "kms_private_endpoint": "kms_private_endpoint", "key_crn": "key_crn"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        location = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "location": location,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_kms_settings(**req_copy)



class TestReplaceKmsSettings():
    """
    Test Class for replace_kms_settings
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_replace_kms_settings_all_params(self):
        """
        replace_kms_settings()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/settings/kms')
        mock_response = '{"location": "location", "encryption_scheme": "encryption_scheme", "resource_group": "resource_group", "primary_crk": {"kms_name": "kms_name", "kms_private_endpoint": "kms_private_endpoint", "key_crn": "key_crn"}, "secondary_crk": {"kms_name": "kms_name", "kms_private_endpoint": "kms_private_endpoint", "key_crn": "key_crn"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a KMSSettingsPrimaryCrk model
        kms_settings_primary_crk_model = {}
        kms_settings_primary_crk_model['kms_name'] = 'testString'
        kms_settings_primary_crk_model['kms_private_endpoint'] = 'testString'
        kms_settings_primary_crk_model['key_crn'] = 'testString'

        # Construct a dict representation of a KMSSettingsSecondaryCrk model
        kms_settings_secondary_crk_model = {}
        kms_settings_secondary_crk_model['kms_name'] = 'testString'
        kms_settings_secondary_crk_model['kms_private_endpoint'] = 'testString'
        kms_settings_secondary_crk_model['key_crn'] = 'testString'

        # Set up parameter values
        location = 'testString'
        encryption_scheme = 'testString'
        resource_group = 'testString'
        primary_crk = kms_settings_primary_crk_model
        secondary_crk = kms_settings_secondary_crk_model

        # Invoke method
        response = service.replace_kms_settings(
            location=location,
            encryption_scheme=encryption_scheme,
            resource_group=resource_group,
            primary_crk=primary_crk,
            secondary_crk=secondary_crk,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['location'] == 'testString'
        assert req_body['encryption_scheme'] == 'testString'
        assert req_body['resource_group'] == 'testString'
        assert req_body['primary_crk'] == kms_settings_primary_crk_model
        assert req_body['secondary_crk'] == kms_settings_secondary_crk_model


class TestGetDiscoveredKmsInstances():
    """
    Test Class for get_discovered_kms_instances
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_discovered_kms_instances_all_params(self):
        """
        get_discovered_kms_instances()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/settings/kms_instances')
        mock_response = '{"total_count": 11, "limit": 5, "offset": 6, "kms_instances": [{"location": "location", "encryption_scheme": "encryption_scheme", "resource_group": "resource_group", "kms_crn": "kms_crn", "kms_name": "kms_name", "kms_private_endpoint": "kms_private_endpoint", "kms_public_endpoint": "kms_public_endpoint", "keys": [{"name": "name", "crn": "crn", "error": "error"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        encryption_scheme = 'testString'
        location = 'testString'
        resource_group = 'testString'
        limit = 1
        sort = 'testString'

        # Invoke method
        response = service.get_discovered_kms_instances(
            encryption_scheme,
            location,
            resource_group=resource_group,
            limit=limit,
            sort=sort,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'encryption_scheme={}'.format(encryption_scheme) in query_string
        assert 'location={}'.format(location) in query_string
        assert 'resource_group={}'.format(resource_group) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'sort={}'.format(sort) in query_string


    @responses.activate
    def test_get_discovered_kms_instances_required_params(self):
        """
        test_get_discovered_kms_instances_required_params()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/settings/kms_instances')
        mock_response = '{"total_count": 11, "limit": 5, "offset": 6, "kms_instances": [{"location": "location", "encryption_scheme": "encryption_scheme", "resource_group": "resource_group", "kms_crn": "kms_crn", "kms_name": "kms_name", "kms_private_endpoint": "kms_private_endpoint", "kms_public_endpoint": "kms_public_endpoint", "keys": [{"name": "name", "crn": "crn", "error": "error"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        encryption_scheme = 'testString'
        location = 'testString'

        # Invoke method
        response = service.get_discovered_kms_instances(
            encryption_scheme,
            location,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'encryption_scheme={}'.format(encryption_scheme) in query_string
        assert 'location={}'.format(location) in query_string


    @responses.activate
    def test_get_discovered_kms_instances_value_error(self):
        """
        test_get_discovered_kms_instances_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v2/settings/kms_instances')
        mock_response = '{"total_count": 11, "limit": 5, "offset": 6, "kms_instances": [{"location": "location", "encryption_scheme": "encryption_scheme", "resource_group": "resource_group", "kms_crn": "kms_crn", "kms_name": "kms_name", "kms_private_endpoint": "kms_private_endpoint", "kms_public_endpoint": "kms_public_endpoint", "keys": [{"name": "name", "crn": "crn", "error": "error"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        encryption_scheme = 'testString'
        location = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "encryption_scheme": encryption_scheme,
            "location": location,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_discovered_kms_instances(**req_copy)



# endregion
##############################################################################
# End of Service: SettingsKms
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestAction():
    """
    Test Class for Action
    """

    def test_action_serialization(self):
        """
        Test serialization/deserialization for Action
        """

        # Construct dict forms of any model objects needed in order to build this model.

        user_state_model = {} # UserState
        user_state_model['state'] = 'draft'
        user_state_model['set_by'] = 'testString'
        user_state_model['set_at'] = '2020-01-28T18:40:40.123456Z'

        external_source_git_model = {} # ExternalSourceGit
        external_source_git_model['git_repo_url'] = 'testString'
        external_source_git_model['git_token'] = 'testString'
        external_source_git_model['git_repo_folder'] = 'testString'
        external_source_git_model['git_release'] = 'testString'
        external_source_git_model['git_branch'] = 'testString'

        external_source_model = {} # ExternalSource
        external_source_model['source_type'] = 'local'
        external_source_model['git'] = external_source_git_model

        system_lock_model = {} # SystemLock
        system_lock_model['sys_locked'] = True
        system_lock_model['sys_locked_by'] = 'testString'
        system_lock_model['sys_locked_at'] = '2020-01-28T18:40:40.123456Z'

        target_resourceset_model = {} # TargetResourceset
        target_resourceset_model['name'] = 'testString'
        target_resourceset_model['type'] = 'testString'
        target_resourceset_model['description'] = 'testString'
        target_resourceset_model['resource_query'] = 'testString'
        target_resourceset_model['credential'] = 'testString'
        target_resourceset_model['id'] = 'testString'
        target_resourceset_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        target_resourceset_model['created_by'] = 'testString'
        target_resourceset_model['updated_at'] = '2020-01-28T18:40:40.123456Z'
        target_resourceset_model['updated_by'] = 'testString'
        target_resourceset_model['sys_lock'] = system_lock_model
        target_resourceset_model['resource_ids'] = ['testString']

        variable_metadata_model = {} # VariableMetadata
        variable_metadata_model['type'] = 'boolean'
        variable_metadata_model['aliases'] = ['testString']
        variable_metadata_model['description'] = 'testString'
        variable_metadata_model['default_value'] = 'testString'
        variable_metadata_model['secure'] = True
        variable_metadata_model['immutable'] = True
        variable_metadata_model['hidden'] = True
        variable_metadata_model['options'] = ['testString']
        variable_metadata_model['min_value'] = 38
        variable_metadata_model['max_value'] = 38
        variable_metadata_model['min_length'] = 38
        variable_metadata_model['max_length'] = 38
        variable_metadata_model['matches'] = 'testString'
        variable_metadata_model['position'] = 38
        variable_metadata_model['group_by'] = 'testString'
        variable_metadata_model['source'] = 'testString'

        variable_data_model = {} # VariableData
        variable_data_model['name'] = 'testString'
        variable_data_model['value'] = 'testString'
        variable_data_model['metadata'] = variable_metadata_model
        variable_data_model['link'] = 'testString'

        action_state_model = {} # ActionState
        action_state_model['status_code'] = 'normal'
        action_state_model['status_message'] = 'testString'

        # Construct a json representation of a Action model
        action_model_json = {}
        action_model_json['name'] = 'Stop Action'
        action_model_json['description'] = 'This Action can be used to Stop the targets'
        action_model_json['location'] = 'us_south'
        action_model_json['resource_group'] = 'testString'
        action_model_json['tags'] = ['testString']
        action_model_json['user_state'] = user_state_model
        action_model_json['source_readme_url'] = 'testString'
        action_model_json['source'] = external_source_model
        action_model_json['source_type'] = 'local'
        action_model_json['command_parameter'] = 'testString'
        action_model_json['bastion'] = target_resourceset_model
        action_model_json['targets'] = [target_resourceset_model]
        action_model_json['inputs'] = [variable_data_model]
        action_model_json['outputs'] = [variable_data_model]
        action_model_json['settings'] = [variable_data_model]
        action_model_json['trigger_record_id'] = 'testString'
        action_model_json['id'] = 'testString'
        action_model_json['crn'] = 'testString'
        action_model_json['account'] = 'testString'
        action_model_json['source_created_at'] = '2020-01-28T18:40:40.123456Z'
        action_model_json['source_created_by'] = 'testString'
        action_model_json['source_updated_at'] = '2020-01-28T18:40:40.123456Z'
        action_model_json['source_updated_by'] = 'testString'
        action_model_json['created_at'] = '2020-01-28T18:40:40.123456Z'
        action_model_json['created_by'] = 'testString'
        action_model_json['updated_at'] = '2020-01-28T18:40:40.123456Z'
        action_model_json['updated_by'] = 'testString'
        action_model_json['namespace'] = 'testString'
        action_model_json['state'] = action_state_model
        action_model_json['playbook_names'] = ['testString']
        action_model_json['sys_lock'] = system_lock_model

        # Construct a model instance of Action by calling from_dict on the json representation
        action_model = Action.from_dict(action_model_json)
        assert action_model != False

        # Construct a model instance of Action by calling from_dict on the json representation
        action_model_dict = Action.from_dict(action_model_json).__dict__
        action_model2 = Action(**action_model_dict)

        # Verify the model instances are equivalent
        assert action_model == action_model2

        # Convert model instance back to dict and verify no loss of data
        action_model_json2 = action_model.to_dict()
        assert action_model_json2 == action_model_json

class TestActionList():
    """
    Test Class for ActionList
    """

    def test_action_list_serialization(self):
        """
        Test serialization/deserialization for ActionList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        user_state_model = {} # UserState
        user_state_model['state'] = 'draft'
        user_state_model['set_by'] = 'testString'
        user_state_model['set_at'] = '2020-01-28T18:40:40.123456Z'

        action_lite_state_model = {} # ActionLiteState
        action_lite_state_model['status_code'] = 'normal'
        action_lite_state_model['status_message'] = 'testString'

        system_lock_model = {} # SystemLock
        system_lock_model['sys_locked'] = True
        system_lock_model['sys_locked_by'] = 'testString'
        system_lock_model['sys_locked_at'] = '2020-01-28T18:40:40.123456Z'

        action_lite_model = {} # ActionLite
        action_lite_model['name'] = 'Stop Action'
        action_lite_model['description'] = 'This Action can be used to Stop the targets'
        action_lite_model['id'] = 'testString'
        action_lite_model['crn'] = 'testString'
        action_lite_model['location'] = 'us_south'
        action_lite_model['resource_group'] = 'testString'
        action_lite_model['namespace'] = 'testString'
        action_lite_model['tags'] = ['testString']
        action_lite_model['playbook_name'] = 'testString'
        action_lite_model['user_state'] = user_state_model
        action_lite_model['state'] = action_lite_state_model
        action_lite_model['sys_lock'] = system_lock_model
        action_lite_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        action_lite_model['created_by'] = 'testString'
        action_lite_model['updated_at'] = '2020-01-28T18:40:40.123456Z'
        action_lite_model['updated_by'] = 'testString'

        # Construct a json representation of a ActionList model
        action_list_model_json = {}
        action_list_model_json['total_count'] = 26
        action_list_model_json['limit'] = 26
        action_list_model_json['offset'] = 26
        action_list_model_json['actions'] = [action_lite_model]

        # Construct a model instance of ActionList by calling from_dict on the json representation
        action_list_model = ActionList.from_dict(action_list_model_json)
        assert action_list_model != False

        # Construct a model instance of ActionList by calling from_dict on the json representation
        action_list_model_dict = ActionList.from_dict(action_list_model_json).__dict__
        action_list_model2 = ActionList(**action_list_model_dict)

        # Verify the model instances are equivalent
        assert action_list_model == action_list_model2

        # Convert model instance back to dict and verify no loss of data
        action_list_model_json2 = action_list_model.to_dict()
        assert action_list_model_json2 == action_list_model_json

class TestActionLite():
    """
    Test Class for ActionLite
    """

    def test_action_lite_serialization(self):
        """
        Test serialization/deserialization for ActionLite
        """

        # Construct dict forms of any model objects needed in order to build this model.

        user_state_model = {} # UserState
        user_state_model['state'] = 'draft'
        user_state_model['set_by'] = 'testString'
        user_state_model['set_at'] = '2020-01-28T18:40:40.123456Z'

        action_lite_state_model = {} # ActionLiteState
        action_lite_state_model['status_code'] = 'normal'
        action_lite_state_model['status_message'] = 'testString'

        system_lock_model = {} # SystemLock
        system_lock_model['sys_locked'] = True
        system_lock_model['sys_locked_by'] = 'testString'
        system_lock_model['sys_locked_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a ActionLite model
        action_lite_model_json = {}
        action_lite_model_json['name'] = 'Stop Action'
        action_lite_model_json['description'] = 'This Action can be used to Stop the targets'
        action_lite_model_json['id'] = 'testString'
        action_lite_model_json['crn'] = 'testString'
        action_lite_model_json['location'] = 'us_south'
        action_lite_model_json['resource_group'] = 'testString'
        action_lite_model_json['namespace'] = 'testString'
        action_lite_model_json['tags'] = ['testString']
        action_lite_model_json['playbook_name'] = 'testString'
        action_lite_model_json['user_state'] = user_state_model
        action_lite_model_json['state'] = action_lite_state_model
        action_lite_model_json['sys_lock'] = system_lock_model
        action_lite_model_json['created_at'] = '2020-01-28T18:40:40.123456Z'
        action_lite_model_json['created_by'] = 'testString'
        action_lite_model_json['updated_at'] = '2020-01-28T18:40:40.123456Z'
        action_lite_model_json['updated_by'] = 'testString'

        # Construct a model instance of ActionLite by calling from_dict on the json representation
        action_lite_model = ActionLite.from_dict(action_lite_model_json)
        assert action_lite_model != False

        # Construct a model instance of ActionLite by calling from_dict on the json representation
        action_lite_model_dict = ActionLite.from_dict(action_lite_model_json).__dict__
        action_lite_model2 = ActionLite(**action_lite_model_dict)

        # Verify the model instances are equivalent
        assert action_lite_model == action_lite_model2

        # Convert model instance back to dict and verify no loss of data
        action_lite_model_json2 = action_lite_model.to_dict()
        assert action_lite_model_json2 == action_lite_model_json

class TestActionLiteState():
    """
    Test Class for ActionLiteState
    """

    def test_action_lite_state_serialization(self):
        """
        Test serialization/deserialization for ActionLiteState
        """

        # Construct a json representation of a ActionLiteState model
        action_lite_state_model_json = {}
        action_lite_state_model_json['status_code'] = 'normal'
        action_lite_state_model_json['status_message'] = 'testString'

        # Construct a model instance of ActionLiteState by calling from_dict on the json representation
        action_lite_state_model = ActionLiteState.from_dict(action_lite_state_model_json)
        assert action_lite_state_model != False

        # Construct a model instance of ActionLiteState by calling from_dict on the json representation
        action_lite_state_model_dict = ActionLiteState.from_dict(action_lite_state_model_json).__dict__
        action_lite_state_model2 = ActionLiteState(**action_lite_state_model_dict)

        # Verify the model instances are equivalent
        assert action_lite_state_model == action_lite_state_model2

        # Convert model instance back to dict and verify no loss of data
        action_lite_state_model_json2 = action_lite_state_model.to_dict()
        assert action_lite_state_model_json2 == action_lite_state_model_json

class TestActionState():
    """
    Test Class for ActionState
    """

    def test_action_state_serialization(self):
        """
        Test serialization/deserialization for ActionState
        """

        # Construct a json representation of a ActionState model
        action_state_model_json = {}
        action_state_model_json['status_code'] = 'normal'
        action_state_model_json['status_message'] = 'testString'

        # Construct a model instance of ActionState by calling from_dict on the json representation
        action_state_model = ActionState.from_dict(action_state_model_json)
        assert action_state_model != False

        # Construct a model instance of ActionState by calling from_dict on the json representation
        action_state_model_dict = ActionState.from_dict(action_state_model_json).__dict__
        action_state_model2 = ActionState(**action_state_model_dict)

        # Verify the model instances are equivalent
        assert action_state_model == action_state_model2

        # Convert model instance back to dict and verify no loss of data
        action_state_model_json2 = action_state_model.to_dict()
        assert action_state_model_json2 == action_state_model_json

class TestCatalogRef():
    """
    Test Class for CatalogRef
    """

    def test_catalog_ref_serialization(self):
        """
        Test serialization/deserialization for CatalogRef
        """

        # Construct a json representation of a CatalogRef model
        catalog_ref_model_json = {}
        catalog_ref_model_json['dry_run'] = True
        catalog_ref_model_json['item_icon_url'] = 'testString'
        catalog_ref_model_json['item_id'] = 'testString'
        catalog_ref_model_json['item_name'] = 'testString'
        catalog_ref_model_json['item_readme_url'] = 'testString'
        catalog_ref_model_json['item_url'] = 'testString'
        catalog_ref_model_json['launch_url'] = 'testString'
        catalog_ref_model_json['offering_version'] = 'testString'

        # Construct a model instance of CatalogRef by calling from_dict on the json representation
        catalog_ref_model = CatalogRef.from_dict(catalog_ref_model_json)
        assert catalog_ref_model != False

        # Construct a model instance of CatalogRef by calling from_dict on the json representation
        catalog_ref_model_dict = CatalogRef.from_dict(catalog_ref_model_json).__dict__
        catalog_ref_model2 = CatalogRef(**catalog_ref_model_dict)

        # Verify the model instances are equivalent
        assert catalog_ref_model == catalog_ref_model2

        # Convert model instance back to dict and verify no loss of data
        catalog_ref_model_json2 = catalog_ref_model.to_dict()
        assert catalog_ref_model_json2 == catalog_ref_model_json

class TestEnvVariableResponse():
    """
    Test Class for EnvVariableResponse
    """

    def test_env_variable_response_serialization(self):
        """
        Test serialization/deserialization for EnvVariableResponse
        """

        # Construct a json representation of a EnvVariableResponse model
        env_variable_response_model_json = {}
        env_variable_response_model_json['hidden'] = True
        env_variable_response_model_json['name'] = 'testString'
        env_variable_response_model_json['secure'] = True
        env_variable_response_model_json['value'] = 'testString'

        # Construct a model instance of EnvVariableResponse by calling from_dict on the json representation
        env_variable_response_model = EnvVariableResponse.from_dict(env_variable_response_model_json)
        assert env_variable_response_model != False

        # Construct a model instance of EnvVariableResponse by calling from_dict on the json representation
        env_variable_response_model_dict = EnvVariableResponse.from_dict(env_variable_response_model_json).__dict__
        env_variable_response_model2 = EnvVariableResponse(**env_variable_response_model_dict)

        # Verify the model instances are equivalent
        assert env_variable_response_model == env_variable_response_model2

        # Convert model instance back to dict and verify no loss of data
        env_variable_response_model_json2 = env_variable_response_model.to_dict()
        assert env_variable_response_model_json2 == env_variable_response_model_json

class TestExternalSource():
    """
    Test Class for ExternalSource
    """

    def test_external_source_serialization(self):
        """
        Test serialization/deserialization for ExternalSource
        """

        # Construct dict forms of any model objects needed in order to build this model.

        external_source_git_model = {} # ExternalSourceGit
        external_source_git_model['git_repo_url'] = 'testString'
        external_source_git_model['git_token'] = 'testString'
        external_source_git_model['git_repo_folder'] = 'testString'
        external_source_git_model['git_release'] = 'testString'
        external_source_git_model['git_branch'] = 'testString'

        # Construct a json representation of a ExternalSource model
        external_source_model_json = {}
        external_source_model_json['source_type'] = 'local'
        external_source_model_json['git'] = external_source_git_model

        # Construct a model instance of ExternalSource by calling from_dict on the json representation
        external_source_model = ExternalSource.from_dict(external_source_model_json)
        assert external_source_model != False

        # Construct a model instance of ExternalSource by calling from_dict on the json representation
        external_source_model_dict = ExternalSource.from_dict(external_source_model_json).__dict__
        external_source_model2 = ExternalSource(**external_source_model_dict)

        # Verify the model instances are equivalent
        assert external_source_model == external_source_model2

        # Convert model instance back to dict and verify no loss of data
        external_source_model_json2 = external_source_model.to_dict()
        assert external_source_model_json2 == external_source_model_json

class TestExternalSourceGit():
    """
    Test Class for ExternalSourceGit
    """

    def test_external_source_git_serialization(self):
        """
        Test serialization/deserialization for ExternalSourceGit
        """

        # Construct a json representation of a ExternalSourceGit model
        external_source_git_model_json = {}
        external_source_git_model_json['git_repo_url'] = 'testString'
        external_source_git_model_json['git_token'] = 'testString'
        external_source_git_model_json['git_repo_folder'] = 'testString'
        external_source_git_model_json['git_release'] = 'testString'
        external_source_git_model_json['git_branch'] = 'testString'

        # Construct a model instance of ExternalSourceGit by calling from_dict on the json representation
        external_source_git_model = ExternalSourceGit.from_dict(external_source_git_model_json)
        assert external_source_git_model != False

        # Construct a model instance of ExternalSourceGit by calling from_dict on the json representation
        external_source_git_model_dict = ExternalSourceGit.from_dict(external_source_git_model_json).__dict__
        external_source_git_model2 = ExternalSourceGit(**external_source_git_model_dict)

        # Verify the model instances are equivalent
        assert external_source_git_model == external_source_git_model2

        # Convert model instance back to dict and verify no loss of data
        external_source_git_model_json2 = external_source_git_model.to_dict()
        assert external_source_git_model_json2 == external_source_git_model_json

class TestJob():
    """
    Test Class for Job
    """

    def test_job_serialization(self):
        """
        Test serialization/deserialization for Job
        """

        # Construct dict forms of any model objects needed in order to build this model.

        variable_metadata_model = {} # VariableMetadata
        variable_metadata_model['type'] = 'boolean'
        variable_metadata_model['aliases'] = ['testString']
        variable_metadata_model['description'] = 'testString'
        variable_metadata_model['default_value'] = 'testString'
        variable_metadata_model['secure'] = True
        variable_metadata_model['immutable'] = True
        variable_metadata_model['hidden'] = True
        variable_metadata_model['options'] = ['testString']
        variable_metadata_model['min_value'] = 38
        variable_metadata_model['max_value'] = 38
        variable_metadata_model['min_length'] = 38
        variable_metadata_model['max_length'] = 38
        variable_metadata_model['matches'] = 'testString'
        variable_metadata_model['position'] = 38
        variable_metadata_model['group_by'] = 'testString'
        variable_metadata_model['source'] = 'testString'

        variable_data_model = {} # VariableData
        variable_data_model['name'] = 'testString'
        variable_data_model['value'] = 'testString'
        variable_data_model['metadata'] = variable_metadata_model
        variable_data_model['link'] = 'testString'

        job_status_action_model = {} # JobStatusAction
        job_status_action_model['action_name'] = 'testString'
        job_status_action_model['status_code'] = 'job_pending'
        job_status_action_model['status_message'] = 'testString'
        job_status_action_model['bastion_status_code'] = 'none'
        job_status_action_model['bastion_status_message'] = 'testString'
        job_status_action_model['targets_status_code'] = 'none'
        job_status_action_model['targets_status_message'] = 'testString'
        job_status_action_model['updated_at'] = '2020-01-28T18:40:40.123456Z'

        job_status_model = {} # JobStatus
        job_status_model['action_job_status'] = job_status_action_model

        job_data_action_model = {} # JobDataAction
        job_data_action_model['action_name'] = 'testString'
        job_data_action_model['inputs'] = [variable_data_model]
        job_data_action_model['outputs'] = [variable_data_model]
        job_data_action_model['settings'] = [variable_data_model]
        job_data_action_model['updated_at'] = '2020-01-28T18:40:40.123456Z'

        job_data_model = {} # JobData
        job_data_model['job_type'] = 'repo_download_job'
        job_data_model['action_job_data'] = job_data_action_model

        system_lock_model = {} # SystemLock
        system_lock_model['sys_locked'] = True
        system_lock_model['sys_locked_by'] = 'testString'
        system_lock_model['sys_locked_at'] = '2020-01-28T18:40:40.123456Z'

        target_resourceset_model = {} # TargetResourceset
        target_resourceset_model['name'] = 'testString'
        target_resourceset_model['type'] = 'testString'
        target_resourceset_model['description'] = 'testString'
        target_resourceset_model['resource_query'] = 'testString'
        target_resourceset_model['credential'] = 'testString'
        target_resourceset_model['id'] = 'testString'
        target_resourceset_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        target_resourceset_model['created_by'] = 'testString'
        target_resourceset_model['updated_at'] = '2020-01-28T18:40:40.123456Z'
        target_resourceset_model['updated_by'] = 'testString'
        target_resourceset_model['sys_lock'] = system_lock_model
        target_resourceset_model['resource_ids'] = ['testString']

        job_log_summary_log_errors_item_model = {} # JobLogSummaryLogErrorsItem
        job_log_summary_log_errors_item_model['error_code'] = 'testString'
        job_log_summary_log_errors_item_model['error_msg'] = 'testString'
        job_log_summary_log_errors_item_model['error_count'] = 72.5

        job_log_summary_repo_download_job_model = {} # JobLogSummaryRepoDownloadJob
        job_log_summary_repo_download_job_model['scanned_file_count'] = 72.5
        job_log_summary_repo_download_job_model['quarantined_file_count'] = 72.5
        job_log_summary_repo_download_job_model['detected_filetype'] = 'testString'
        job_log_summary_repo_download_job_model['inputs_count'] = 'testString'
        job_log_summary_repo_download_job_model['outputs_count'] = 'testString'

        job_log_summary_action_job_recap_model = {} # JobLogSummaryActionJobRecap
        job_log_summary_action_job_recap_model['target'] = ['testString']
        job_log_summary_action_job_recap_model['ok'] = 72.5
        job_log_summary_action_job_recap_model['changed'] = 72.5
        job_log_summary_action_job_recap_model['failed'] = 72.5
        job_log_summary_action_job_recap_model['skipped'] = 72.5
        job_log_summary_action_job_recap_model['unreachable'] = 72.5

        job_log_summary_action_job_model = {} # JobLogSummaryActionJob
        job_log_summary_action_job_model['target_count'] = 72.5
        job_log_summary_action_job_model['task_count'] = 72.5
        job_log_summary_action_job_model['play_count'] = 72.5
        job_log_summary_action_job_model['recap'] = job_log_summary_action_job_recap_model

        job_log_summary_model = {} # JobLogSummary
        job_log_summary_model['job_id'] = 'testString'
        job_log_summary_model['job_type'] = 'repo_download_job'
        job_log_summary_model['log_start_at'] = '2020-01-28T18:40:40.123456Z'
        job_log_summary_model['log_analyzed_till'] = '2020-01-28T18:40:40.123456Z'
        job_log_summary_model['elapsed_time'] = 72.5
        job_log_summary_model['log_errors'] = [job_log_summary_log_errors_item_model]
        job_log_summary_model['repo_download_job'] = job_log_summary_repo_download_job_model
        job_log_summary_model['action_job'] = job_log_summary_action_job_model

        # Construct a json representation of a Job model
        job_model_json = {}
        job_model_json['command_object'] = 'workspace'
        job_model_json['command_object_id'] = 'testString'
        job_model_json['command_name'] = 'workspace_init_flow'
        job_model_json['command_parameter'] = 'testString'
        job_model_json['command_options'] = ['testString']
        job_model_json['inputs'] = [variable_data_model]
        job_model_json['settings'] = [variable_data_model]
        job_model_json['tags'] = ['testString']
        job_model_json['id'] = 'testString'
        job_model_json['name'] = 'testString'
        job_model_json['description'] = 'testString'
        job_model_json['location'] = 'us_south'
        job_model_json['resource_group'] = 'testString'
        job_model_json['submitted_at'] = '2020-01-28T18:40:40.123456Z'
        job_model_json['submitted_by'] = 'testString'
        job_model_json['start_at'] = '2020-01-28T18:40:40.123456Z'
        job_model_json['end_at'] = '2020-01-28T18:40:40.123456Z'
        job_model_json['duration'] = 'testString'
        job_model_json['status'] = job_status_model
        job_model_json['data'] = job_data_model
        job_model_json['targets'] = [target_resourceset_model]
        job_model_json['bastion'] = target_resourceset_model
        job_model_json['log_summary'] = job_log_summary_model
        job_model_json['log_store_url'] = 'testString'
        job_model_json['state_store_url'] = 'testString'
        job_model_json['results_url'] = 'testString'
        job_model_json['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of Job by calling from_dict on the json representation
        job_model = Job.from_dict(job_model_json)
        assert job_model != False

        # Construct a model instance of Job by calling from_dict on the json representation
        job_model_dict = Job.from_dict(job_model_json).__dict__
        job_model2 = Job(**job_model_dict)

        # Verify the model instances are equivalent
        assert job_model == job_model2

        # Convert model instance back to dict and verify no loss of data
        job_model_json2 = job_model.to_dict()
        assert job_model_json2 == job_model_json

class TestJobData():
    """
    Test Class for JobData
    """

    def test_job_data_serialization(self):
        """
        Test serialization/deserialization for JobData
        """

        # Construct dict forms of any model objects needed in order to build this model.

        variable_metadata_model = {} # VariableMetadata
        variable_metadata_model['type'] = 'boolean'
        variable_metadata_model['aliases'] = ['testString']
        variable_metadata_model['description'] = 'testString'
        variable_metadata_model['default_value'] = 'testString'
        variable_metadata_model['secure'] = True
        variable_metadata_model['immutable'] = True
        variable_metadata_model['hidden'] = True
        variable_metadata_model['options'] = ['testString']
        variable_metadata_model['min_value'] = 38
        variable_metadata_model['max_value'] = 38
        variable_metadata_model['min_length'] = 38
        variable_metadata_model['max_length'] = 38
        variable_metadata_model['matches'] = 'testString'
        variable_metadata_model['position'] = 38
        variable_metadata_model['group_by'] = 'testString'
        variable_metadata_model['source'] = 'testString'

        variable_data_model = {} # VariableData
        variable_data_model['name'] = 'testString'
        variable_data_model['value'] = 'testString'
        variable_data_model['metadata'] = variable_metadata_model
        variable_data_model['link'] = 'testString'

        job_data_action_model = {} # JobDataAction
        job_data_action_model['action_name'] = 'testString'
        job_data_action_model['inputs'] = [variable_data_model]
        job_data_action_model['outputs'] = [variable_data_model]
        job_data_action_model['settings'] = [variable_data_model]
        job_data_action_model['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a JobData model
        job_data_model_json = {}
        job_data_model_json['job_type'] = 'repo_download_job'
        job_data_model_json['action_job_data'] = job_data_action_model

        # Construct a model instance of JobData by calling from_dict on the json representation
        job_data_model = JobData.from_dict(job_data_model_json)
        assert job_data_model != False

        # Construct a model instance of JobData by calling from_dict on the json representation
        job_data_model_dict = JobData.from_dict(job_data_model_json).__dict__
        job_data_model2 = JobData(**job_data_model_dict)

        # Verify the model instances are equivalent
        assert job_data_model == job_data_model2

        # Convert model instance back to dict and verify no loss of data
        job_data_model_json2 = job_data_model.to_dict()
        assert job_data_model_json2 == job_data_model_json

class TestJobDataAction():
    """
    Test Class for JobDataAction
    """

    def test_job_data_action_serialization(self):
        """
        Test serialization/deserialization for JobDataAction
        """

        # Construct dict forms of any model objects needed in order to build this model.

        variable_metadata_model = {} # VariableMetadata
        variable_metadata_model['type'] = 'boolean'
        variable_metadata_model['aliases'] = ['testString']
        variable_metadata_model['description'] = 'testString'
        variable_metadata_model['default_value'] = 'testString'
        variable_metadata_model['secure'] = True
        variable_metadata_model['immutable'] = True
        variable_metadata_model['hidden'] = True
        variable_metadata_model['options'] = ['testString']
        variable_metadata_model['min_value'] = 38
        variable_metadata_model['max_value'] = 38
        variable_metadata_model['min_length'] = 38
        variable_metadata_model['max_length'] = 38
        variable_metadata_model['matches'] = 'testString'
        variable_metadata_model['position'] = 38
        variable_metadata_model['group_by'] = 'testString'
        variable_metadata_model['source'] = 'testString'

        variable_data_model = {} # VariableData
        variable_data_model['name'] = 'testString'
        variable_data_model['value'] = 'testString'
        variable_data_model['metadata'] = variable_metadata_model
        variable_data_model['link'] = 'testString'

        # Construct a json representation of a JobDataAction model
        job_data_action_model_json = {}
        job_data_action_model_json['action_name'] = 'testString'
        job_data_action_model_json['inputs'] = [variable_data_model]
        job_data_action_model_json['outputs'] = [variable_data_model]
        job_data_action_model_json['settings'] = [variable_data_model]
        job_data_action_model_json['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of JobDataAction by calling from_dict on the json representation
        job_data_action_model = JobDataAction.from_dict(job_data_action_model_json)
        assert job_data_action_model != False

        # Construct a model instance of JobDataAction by calling from_dict on the json representation
        job_data_action_model_dict = JobDataAction.from_dict(job_data_action_model_json).__dict__
        job_data_action_model2 = JobDataAction(**job_data_action_model_dict)

        # Verify the model instances are equivalent
        assert job_data_action_model == job_data_action_model2

        # Convert model instance back to dict and verify no loss of data
        job_data_action_model_json2 = job_data_action_model.to_dict()
        assert job_data_action_model_json2 == job_data_action_model_json

class TestJobList():
    """
    Test Class for JobList
    """

    def test_job_list_serialization(self):
        """
        Test serialization/deserialization for JobList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        system_lock_model = {} # SystemLock
        system_lock_model['sys_locked'] = True
        system_lock_model['sys_locked_by'] = 'testString'
        system_lock_model['sys_locked_at'] = '2020-01-28T18:40:40.123456Z'

        target_resourceset_model = {} # TargetResourceset
        target_resourceset_model['name'] = 'testString'
        target_resourceset_model['type'] = 'testString'
        target_resourceset_model['description'] = 'testString'
        target_resourceset_model['resource_query'] = 'testString'
        target_resourceset_model['credential'] = 'testString'
        target_resourceset_model['id'] = 'testString'
        target_resourceset_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        target_resourceset_model['created_by'] = 'testString'
        target_resourceset_model['updated_at'] = '2020-01-28T18:40:40.123456Z'
        target_resourceset_model['updated_by'] = 'testString'
        target_resourceset_model['sys_lock'] = system_lock_model
        target_resourceset_model['resource_ids'] = ['testString']

        job_status_action_model = {} # JobStatusAction
        job_status_action_model['action_name'] = 'testString'
        job_status_action_model['status_code'] = 'job_pending'
        job_status_action_model['status_message'] = 'testString'
        job_status_action_model['bastion_status_code'] = 'none'
        job_status_action_model['bastion_status_message'] = 'testString'
        job_status_action_model['targets_status_code'] = 'none'
        job_status_action_model['targets_status_message'] = 'testString'
        job_status_action_model['updated_at'] = '2020-01-28T18:40:40.123456Z'

        job_status_model = {} # JobStatus
        job_status_model['action_job_status'] = job_status_action_model

        job_log_summary_log_errors_item_model = {} # JobLogSummaryLogErrorsItem
        job_log_summary_log_errors_item_model['error_code'] = 'testString'
        job_log_summary_log_errors_item_model['error_msg'] = 'testString'
        job_log_summary_log_errors_item_model['error_count'] = 72.5

        job_log_summary_repo_download_job_model = {} # JobLogSummaryRepoDownloadJob
        job_log_summary_repo_download_job_model['scanned_file_count'] = 72.5
        job_log_summary_repo_download_job_model['quarantined_file_count'] = 72.5
        job_log_summary_repo_download_job_model['detected_filetype'] = 'testString'
        job_log_summary_repo_download_job_model['inputs_count'] = 'testString'
        job_log_summary_repo_download_job_model['outputs_count'] = 'testString'

        job_log_summary_action_job_recap_model = {} # JobLogSummaryActionJobRecap
        job_log_summary_action_job_recap_model['target'] = ['testString']
        job_log_summary_action_job_recap_model['ok'] = 72.5
        job_log_summary_action_job_recap_model['changed'] = 72.5
        job_log_summary_action_job_recap_model['failed'] = 72.5
        job_log_summary_action_job_recap_model['skipped'] = 72.5
        job_log_summary_action_job_recap_model['unreachable'] = 72.5

        job_log_summary_action_job_model = {} # JobLogSummaryActionJob
        job_log_summary_action_job_model['target_count'] = 72.5
        job_log_summary_action_job_model['task_count'] = 72.5
        job_log_summary_action_job_model['play_count'] = 72.5
        job_log_summary_action_job_model['recap'] = job_log_summary_action_job_recap_model

        job_log_summary_model = {} # JobLogSummary
        job_log_summary_model['job_id'] = 'testString'
        job_log_summary_model['job_type'] = 'repo_download_job'
        job_log_summary_model['log_start_at'] = '2020-01-28T18:40:40.123456Z'
        job_log_summary_model['log_analyzed_till'] = '2020-01-28T18:40:40.123456Z'
        job_log_summary_model['elapsed_time'] = 72.5
        job_log_summary_model['log_errors'] = [job_log_summary_log_errors_item_model]
        job_log_summary_model['repo_download_job'] = job_log_summary_repo_download_job_model
        job_log_summary_model['action_job'] = job_log_summary_action_job_model

        job_lite_model = {} # JobLite
        job_lite_model['id'] = 'testString'
        job_lite_model['name'] = 'testString'
        job_lite_model['description'] = 'testString'
        job_lite_model['command_object'] = 'workspace'
        job_lite_model['command_object_id'] = 'testString'
        job_lite_model['command_name'] = 'workspace_init_flow'
        job_lite_model['tags'] = ['testString']
        job_lite_model['location'] = 'us_south'
        job_lite_model['resource_group'] = 'testString'
        job_lite_model['targets'] = [target_resourceset_model]
        job_lite_model['submitted_at'] = '2020-01-28T18:40:40.123456Z'
        job_lite_model['submitted_by'] = 'testString'
        job_lite_model['duration'] = 'testString'
        job_lite_model['start_at'] = '2020-01-28T18:40:40.123456Z'
        job_lite_model['end_at'] = '2020-01-28T18:40:40.123456Z'
        job_lite_model['status'] = job_status_model
        job_lite_model['log_summary'] = job_log_summary_model
        job_lite_model['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a JobList model
        job_list_model_json = {}
        job_list_model_json['total_count'] = 26
        job_list_model_json['limit'] = 26
        job_list_model_json['offset'] = 26
        job_list_model_json['jobs'] = [job_lite_model]

        # Construct a model instance of JobList by calling from_dict on the json representation
        job_list_model = JobList.from_dict(job_list_model_json)
        assert job_list_model != False

        # Construct a model instance of JobList by calling from_dict on the json representation
        job_list_model_dict = JobList.from_dict(job_list_model_json).__dict__
        job_list_model2 = JobList(**job_list_model_dict)

        # Verify the model instances are equivalent
        assert job_list_model == job_list_model2

        # Convert model instance back to dict and verify no loss of data
        job_list_model_json2 = job_list_model.to_dict()
        assert job_list_model_json2 == job_list_model_json

class TestJobLite():
    """
    Test Class for JobLite
    """

    def test_job_lite_serialization(self):
        """
        Test serialization/deserialization for JobLite
        """

        # Construct dict forms of any model objects needed in order to build this model.

        system_lock_model = {} # SystemLock
        system_lock_model['sys_locked'] = True
        system_lock_model['sys_locked_by'] = 'testString'
        system_lock_model['sys_locked_at'] = '2020-01-28T18:40:40.123456Z'

        target_resourceset_model = {} # TargetResourceset
        target_resourceset_model['name'] = 'testString'
        target_resourceset_model['type'] = 'testString'
        target_resourceset_model['description'] = 'testString'
        target_resourceset_model['resource_query'] = 'testString'
        target_resourceset_model['credential'] = 'testString'
        target_resourceset_model['id'] = 'testString'
        target_resourceset_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        target_resourceset_model['created_by'] = 'testString'
        target_resourceset_model['updated_at'] = '2020-01-28T18:40:40.123456Z'
        target_resourceset_model['updated_by'] = 'testString'
        target_resourceset_model['sys_lock'] = system_lock_model
        target_resourceset_model['resource_ids'] = ['testString']

        job_status_action_model = {} # JobStatusAction
        job_status_action_model['action_name'] = 'testString'
        job_status_action_model['status_code'] = 'job_pending'
        job_status_action_model['status_message'] = 'testString'
        job_status_action_model['bastion_status_code'] = 'none'
        job_status_action_model['bastion_status_message'] = 'testString'
        job_status_action_model['targets_status_code'] = 'none'
        job_status_action_model['targets_status_message'] = 'testString'
        job_status_action_model['updated_at'] = '2020-01-28T18:40:40.123456Z'

        job_status_model = {} # JobStatus
        job_status_model['action_job_status'] = job_status_action_model

        job_log_summary_log_errors_item_model = {} # JobLogSummaryLogErrorsItem
        job_log_summary_log_errors_item_model['error_code'] = 'testString'
        job_log_summary_log_errors_item_model['error_msg'] = 'testString'
        job_log_summary_log_errors_item_model['error_count'] = 72.5

        job_log_summary_repo_download_job_model = {} # JobLogSummaryRepoDownloadJob
        job_log_summary_repo_download_job_model['scanned_file_count'] = 72.5
        job_log_summary_repo_download_job_model['quarantined_file_count'] = 72.5
        job_log_summary_repo_download_job_model['detected_filetype'] = 'testString'
        job_log_summary_repo_download_job_model['inputs_count'] = 'testString'
        job_log_summary_repo_download_job_model['outputs_count'] = 'testString'

        job_log_summary_action_job_recap_model = {} # JobLogSummaryActionJobRecap
        job_log_summary_action_job_recap_model['target'] = ['testString']
        job_log_summary_action_job_recap_model['ok'] = 72.5
        job_log_summary_action_job_recap_model['changed'] = 72.5
        job_log_summary_action_job_recap_model['failed'] = 72.5
        job_log_summary_action_job_recap_model['skipped'] = 72.5
        job_log_summary_action_job_recap_model['unreachable'] = 72.5

        job_log_summary_action_job_model = {} # JobLogSummaryActionJob
        job_log_summary_action_job_model['target_count'] = 72.5
        job_log_summary_action_job_model['task_count'] = 72.5
        job_log_summary_action_job_model['play_count'] = 72.5
        job_log_summary_action_job_model['recap'] = job_log_summary_action_job_recap_model

        job_log_summary_model = {} # JobLogSummary
        job_log_summary_model['job_id'] = 'testString'
        job_log_summary_model['job_type'] = 'repo_download_job'
        job_log_summary_model['log_start_at'] = '2020-01-28T18:40:40.123456Z'
        job_log_summary_model['log_analyzed_till'] = '2020-01-28T18:40:40.123456Z'
        job_log_summary_model['elapsed_time'] = 72.5
        job_log_summary_model['log_errors'] = [job_log_summary_log_errors_item_model]
        job_log_summary_model['repo_download_job'] = job_log_summary_repo_download_job_model
        job_log_summary_model['action_job'] = job_log_summary_action_job_model

        # Construct a json representation of a JobLite model
        job_lite_model_json = {}
        job_lite_model_json['id'] = 'testString'
        job_lite_model_json['name'] = 'testString'
        job_lite_model_json['description'] = 'testString'
        job_lite_model_json['command_object'] = 'workspace'
        job_lite_model_json['command_object_id'] = 'testString'
        job_lite_model_json['command_name'] = 'workspace_init_flow'
        job_lite_model_json['tags'] = ['testString']
        job_lite_model_json['location'] = 'us_south'
        job_lite_model_json['resource_group'] = 'testString'
        job_lite_model_json['targets'] = [target_resourceset_model]
        job_lite_model_json['submitted_at'] = '2020-01-28T18:40:40.123456Z'
        job_lite_model_json['submitted_by'] = 'testString'
        job_lite_model_json['duration'] = 'testString'
        job_lite_model_json['start_at'] = '2020-01-28T18:40:40.123456Z'
        job_lite_model_json['end_at'] = '2020-01-28T18:40:40.123456Z'
        job_lite_model_json['status'] = job_status_model
        job_lite_model_json['log_summary'] = job_log_summary_model
        job_lite_model_json['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of JobLite by calling from_dict on the json representation
        job_lite_model = JobLite.from_dict(job_lite_model_json)
        assert job_lite_model != False

        # Construct a model instance of JobLite by calling from_dict on the json representation
        job_lite_model_dict = JobLite.from_dict(job_lite_model_json).__dict__
        job_lite_model2 = JobLite(**job_lite_model_dict)

        # Verify the model instances are equivalent
        assert job_lite_model == job_lite_model2

        # Convert model instance back to dict and verify no loss of data
        job_lite_model_json2 = job_lite_model.to_dict()
        assert job_lite_model_json2 == job_lite_model_json

class TestJobLog():
    """
    Test Class for JobLog
    """

    def test_job_log_serialization(self):
        """
        Test serialization/deserialization for JobLog
        """

        # Construct dict forms of any model objects needed in order to build this model.

        job_log_summary_log_errors_item_model = {} # JobLogSummaryLogErrorsItem
        job_log_summary_log_errors_item_model['error_code'] = 'testString'
        job_log_summary_log_errors_item_model['error_msg'] = 'testString'
        job_log_summary_log_errors_item_model['error_count'] = 72.5

        job_log_summary_repo_download_job_model = {} # JobLogSummaryRepoDownloadJob
        job_log_summary_repo_download_job_model['scanned_file_count'] = 72.5
        job_log_summary_repo_download_job_model['quarantined_file_count'] = 72.5
        job_log_summary_repo_download_job_model['detected_filetype'] = 'testString'
        job_log_summary_repo_download_job_model['inputs_count'] = 'testString'
        job_log_summary_repo_download_job_model['outputs_count'] = 'testString'

        job_log_summary_action_job_recap_model = {} # JobLogSummaryActionJobRecap
        job_log_summary_action_job_recap_model['target'] = ['testString']
        job_log_summary_action_job_recap_model['ok'] = 72.5
        job_log_summary_action_job_recap_model['changed'] = 72.5
        job_log_summary_action_job_recap_model['failed'] = 72.5
        job_log_summary_action_job_recap_model['skipped'] = 72.5
        job_log_summary_action_job_recap_model['unreachable'] = 72.5

        job_log_summary_action_job_model = {} # JobLogSummaryActionJob
        job_log_summary_action_job_model['target_count'] = 72.5
        job_log_summary_action_job_model['task_count'] = 72.5
        job_log_summary_action_job_model['play_count'] = 72.5
        job_log_summary_action_job_model['recap'] = job_log_summary_action_job_recap_model

        job_log_summary_model = {} # JobLogSummary
        job_log_summary_model['job_id'] = 'testString'
        job_log_summary_model['job_type'] = 'repo_download_job'
        job_log_summary_model['log_start_at'] = '2020-01-28T18:40:40.123456Z'
        job_log_summary_model['log_analyzed_till'] = '2020-01-28T18:40:40.123456Z'
        job_log_summary_model['elapsed_time'] = 72.5
        job_log_summary_model['log_errors'] = [job_log_summary_log_errors_item_model]
        job_log_summary_model['repo_download_job'] = job_log_summary_repo_download_job_model
        job_log_summary_model['action_job'] = job_log_summary_action_job_model

        # Construct a json representation of a JobLog model
        job_log_model_json = {}
        job_log_model_json['job_id'] = 'testString'
        job_log_model_json['job_name'] = 'testString'
        job_log_model_json['log_summary'] = job_log_summary_model
        job_log_model_json['format'] = 'json'
        job_log_model_json['details'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        job_log_model_json['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of JobLog by calling from_dict on the json representation
        job_log_model = JobLog.from_dict(job_log_model_json)
        assert job_log_model != False

        # Construct a model instance of JobLog by calling from_dict on the json representation
        job_log_model_dict = JobLog.from_dict(job_log_model_json).__dict__
        job_log_model2 = JobLog(**job_log_model_dict)

        # Verify the model instances are equivalent
        assert job_log_model == job_log_model2

        # Convert model instance back to dict and verify no loss of data
        job_log_model_json2 = job_log_model.to_dict()
        assert job_log_model_json2 == job_log_model_json

class TestJobLogSummary():
    """
    Test Class for JobLogSummary
    """

    def test_job_log_summary_serialization(self):
        """
        Test serialization/deserialization for JobLogSummary
        """

        # Construct dict forms of any model objects needed in order to build this model.

        job_log_summary_log_errors_item_model = {} # JobLogSummaryLogErrorsItem
        job_log_summary_log_errors_item_model['error_code'] = 'testString'
        job_log_summary_log_errors_item_model['error_msg'] = 'testString'
        job_log_summary_log_errors_item_model['error_count'] = 72.5

        job_log_summary_repo_download_job_model = {} # JobLogSummaryRepoDownloadJob
        job_log_summary_repo_download_job_model['scanned_file_count'] = 72.5
        job_log_summary_repo_download_job_model['quarantined_file_count'] = 72.5
        job_log_summary_repo_download_job_model['detected_filetype'] = 'testString'
        job_log_summary_repo_download_job_model['inputs_count'] = 'testString'
        job_log_summary_repo_download_job_model['outputs_count'] = 'testString'

        job_log_summary_action_job_recap_model = {} # JobLogSummaryActionJobRecap
        job_log_summary_action_job_recap_model['target'] = ['testString']
        job_log_summary_action_job_recap_model['ok'] = 72.5
        job_log_summary_action_job_recap_model['changed'] = 72.5
        job_log_summary_action_job_recap_model['failed'] = 72.5
        job_log_summary_action_job_recap_model['skipped'] = 72.5
        job_log_summary_action_job_recap_model['unreachable'] = 72.5

        job_log_summary_action_job_model = {} # JobLogSummaryActionJob
        job_log_summary_action_job_model['target_count'] = 72.5
        job_log_summary_action_job_model['task_count'] = 72.5
        job_log_summary_action_job_model['play_count'] = 72.5
        job_log_summary_action_job_model['recap'] = job_log_summary_action_job_recap_model

        # Construct a json representation of a JobLogSummary model
        job_log_summary_model_json = {}
        job_log_summary_model_json['job_id'] = 'testString'
        job_log_summary_model_json['job_type'] = 'repo_download_job'
        job_log_summary_model_json['log_start_at'] = '2020-01-28T18:40:40.123456Z'
        job_log_summary_model_json['log_analyzed_till'] = '2020-01-28T18:40:40.123456Z'
        job_log_summary_model_json['elapsed_time'] = 72.5
        job_log_summary_model_json['log_errors'] = [job_log_summary_log_errors_item_model]
        job_log_summary_model_json['repo_download_job'] = job_log_summary_repo_download_job_model
        job_log_summary_model_json['action_job'] = job_log_summary_action_job_model

        # Construct a model instance of JobLogSummary by calling from_dict on the json representation
        job_log_summary_model = JobLogSummary.from_dict(job_log_summary_model_json)
        assert job_log_summary_model != False

        # Construct a model instance of JobLogSummary by calling from_dict on the json representation
        job_log_summary_model_dict = JobLogSummary.from_dict(job_log_summary_model_json).__dict__
        job_log_summary_model2 = JobLogSummary(**job_log_summary_model_dict)

        # Verify the model instances are equivalent
        assert job_log_summary_model == job_log_summary_model2

        # Convert model instance back to dict and verify no loss of data
        job_log_summary_model_json2 = job_log_summary_model.to_dict()
        assert job_log_summary_model_json2 == job_log_summary_model_json

class TestJobLogSummaryActionJob():
    """
    Test Class for JobLogSummaryActionJob
    """

    def test_job_log_summary_action_job_serialization(self):
        """
        Test serialization/deserialization for JobLogSummaryActionJob
        """

        # Construct dict forms of any model objects needed in order to build this model.

        job_log_summary_action_job_recap_model = {} # JobLogSummaryActionJobRecap
        job_log_summary_action_job_recap_model['target'] = ['testString']
        job_log_summary_action_job_recap_model['ok'] = 72.5
        job_log_summary_action_job_recap_model['changed'] = 72.5
        job_log_summary_action_job_recap_model['failed'] = 72.5
        job_log_summary_action_job_recap_model['skipped'] = 72.5
        job_log_summary_action_job_recap_model['unreachable'] = 72.5

        # Construct a json representation of a JobLogSummaryActionJob model
        job_log_summary_action_job_model_json = {}
        job_log_summary_action_job_model_json['target_count'] = 72.5
        job_log_summary_action_job_model_json['task_count'] = 72.5
        job_log_summary_action_job_model_json['play_count'] = 72.5
        job_log_summary_action_job_model_json['recap'] = job_log_summary_action_job_recap_model

        # Construct a model instance of JobLogSummaryActionJob by calling from_dict on the json representation
        job_log_summary_action_job_model = JobLogSummaryActionJob.from_dict(job_log_summary_action_job_model_json)
        assert job_log_summary_action_job_model != False

        # Construct a model instance of JobLogSummaryActionJob by calling from_dict on the json representation
        job_log_summary_action_job_model_dict = JobLogSummaryActionJob.from_dict(job_log_summary_action_job_model_json).__dict__
        job_log_summary_action_job_model2 = JobLogSummaryActionJob(**job_log_summary_action_job_model_dict)

        # Verify the model instances are equivalent
        assert job_log_summary_action_job_model == job_log_summary_action_job_model2

        # Convert model instance back to dict and verify no loss of data
        job_log_summary_action_job_model_json2 = job_log_summary_action_job_model.to_dict()
        assert job_log_summary_action_job_model_json2 == job_log_summary_action_job_model_json

class TestJobLogSummaryActionJobRecap():
    """
    Test Class for JobLogSummaryActionJobRecap
    """

    def test_job_log_summary_action_job_recap_serialization(self):
        """
        Test serialization/deserialization for JobLogSummaryActionJobRecap
        """

        # Construct a json representation of a JobLogSummaryActionJobRecap model
        job_log_summary_action_job_recap_model_json = {}
        job_log_summary_action_job_recap_model_json['target'] = ['testString']
        job_log_summary_action_job_recap_model_json['ok'] = 72.5
        job_log_summary_action_job_recap_model_json['changed'] = 72.5
        job_log_summary_action_job_recap_model_json['failed'] = 72.5
        job_log_summary_action_job_recap_model_json['skipped'] = 72.5
        job_log_summary_action_job_recap_model_json['unreachable'] = 72.5

        # Construct a model instance of JobLogSummaryActionJobRecap by calling from_dict on the json representation
        job_log_summary_action_job_recap_model = JobLogSummaryActionJobRecap.from_dict(job_log_summary_action_job_recap_model_json)
        assert job_log_summary_action_job_recap_model != False

        # Construct a model instance of JobLogSummaryActionJobRecap by calling from_dict on the json representation
        job_log_summary_action_job_recap_model_dict = JobLogSummaryActionJobRecap.from_dict(job_log_summary_action_job_recap_model_json).__dict__
        job_log_summary_action_job_recap_model2 = JobLogSummaryActionJobRecap(**job_log_summary_action_job_recap_model_dict)

        # Verify the model instances are equivalent
        assert job_log_summary_action_job_recap_model == job_log_summary_action_job_recap_model2

        # Convert model instance back to dict and verify no loss of data
        job_log_summary_action_job_recap_model_json2 = job_log_summary_action_job_recap_model.to_dict()
        assert job_log_summary_action_job_recap_model_json2 == job_log_summary_action_job_recap_model_json

class TestJobLogSummaryLogErrorsItem():
    """
    Test Class for JobLogSummaryLogErrorsItem
    """

    def test_job_log_summary_log_errors_item_serialization(self):
        """
        Test serialization/deserialization for JobLogSummaryLogErrorsItem
        """

        # Construct a json representation of a JobLogSummaryLogErrorsItem model
        job_log_summary_log_errors_item_model_json = {}
        job_log_summary_log_errors_item_model_json['error_code'] = 'testString'
        job_log_summary_log_errors_item_model_json['error_msg'] = 'testString'
        job_log_summary_log_errors_item_model_json['error_count'] = 72.5

        # Construct a model instance of JobLogSummaryLogErrorsItem by calling from_dict on the json representation
        job_log_summary_log_errors_item_model = JobLogSummaryLogErrorsItem.from_dict(job_log_summary_log_errors_item_model_json)
        assert job_log_summary_log_errors_item_model != False

        # Construct a model instance of JobLogSummaryLogErrorsItem by calling from_dict on the json representation
        job_log_summary_log_errors_item_model_dict = JobLogSummaryLogErrorsItem.from_dict(job_log_summary_log_errors_item_model_json).__dict__
        job_log_summary_log_errors_item_model2 = JobLogSummaryLogErrorsItem(**job_log_summary_log_errors_item_model_dict)

        # Verify the model instances are equivalent
        assert job_log_summary_log_errors_item_model == job_log_summary_log_errors_item_model2

        # Convert model instance back to dict and verify no loss of data
        job_log_summary_log_errors_item_model_json2 = job_log_summary_log_errors_item_model.to_dict()
        assert job_log_summary_log_errors_item_model_json2 == job_log_summary_log_errors_item_model_json

class TestJobLogSummaryRepoDownloadJob():
    """
    Test Class for JobLogSummaryRepoDownloadJob
    """

    def test_job_log_summary_repo_download_job_serialization(self):
        """
        Test serialization/deserialization for JobLogSummaryRepoDownloadJob
        """

        # Construct a json representation of a JobLogSummaryRepoDownloadJob model
        job_log_summary_repo_download_job_model_json = {}
        job_log_summary_repo_download_job_model_json['scanned_file_count'] = 72.5
        job_log_summary_repo_download_job_model_json['quarantined_file_count'] = 72.5
        job_log_summary_repo_download_job_model_json['detected_filetype'] = 'testString'
        job_log_summary_repo_download_job_model_json['inputs_count'] = 'testString'
        job_log_summary_repo_download_job_model_json['outputs_count'] = 'testString'

        # Construct a model instance of JobLogSummaryRepoDownloadJob by calling from_dict on the json representation
        job_log_summary_repo_download_job_model = JobLogSummaryRepoDownloadJob.from_dict(job_log_summary_repo_download_job_model_json)
        assert job_log_summary_repo_download_job_model != False

        # Construct a model instance of JobLogSummaryRepoDownloadJob by calling from_dict on the json representation
        job_log_summary_repo_download_job_model_dict = JobLogSummaryRepoDownloadJob.from_dict(job_log_summary_repo_download_job_model_json).__dict__
        job_log_summary_repo_download_job_model2 = JobLogSummaryRepoDownloadJob(**job_log_summary_repo_download_job_model_dict)

        # Verify the model instances are equivalent
        assert job_log_summary_repo_download_job_model == job_log_summary_repo_download_job_model2

        # Convert model instance back to dict and verify no loss of data
        job_log_summary_repo_download_job_model_json2 = job_log_summary_repo_download_job_model.to_dict()
        assert job_log_summary_repo_download_job_model_json2 == job_log_summary_repo_download_job_model_json

class TestJobStateData():
    """
    Test Class for JobStateData
    """

    def test_job_state_data_serialization(self):
        """
        Test serialization/deserialization for JobStateData
        """

        # Construct dict forms of any model objects needed in order to build this model.

        job_state_data_summary_item_model = {} # JobStateDataSummaryItem
        job_state_data_summary_item_model['name'] = 'testString'
        job_state_data_summary_item_model['type'] = 'number'
        job_state_data_summary_item_model['value'] = 'testString'

        # Construct a json representation of a JobStateData model
        job_state_data_model_json = {}
        job_state_data_model_json['job_id'] = 'testString'
        job_state_data_model_json['job_name'] = 'testString'
        job_state_data_model_json['summary'] = [job_state_data_summary_item_model]
        job_state_data_model_json['format'] = 'testString'
        job_state_data_model_json['details'] = 'VGhpcyBpcyBhIG1vY2sgYnl0ZSBhcnJheSB2YWx1ZS4='
        job_state_data_model_json['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of JobStateData by calling from_dict on the json representation
        job_state_data_model = JobStateData.from_dict(job_state_data_model_json)
        assert job_state_data_model != False

        # Construct a model instance of JobStateData by calling from_dict on the json representation
        job_state_data_model_dict = JobStateData.from_dict(job_state_data_model_json).__dict__
        job_state_data_model2 = JobStateData(**job_state_data_model_dict)

        # Verify the model instances are equivalent
        assert job_state_data_model == job_state_data_model2

        # Convert model instance back to dict and verify no loss of data
        job_state_data_model_json2 = job_state_data_model.to_dict()
        assert job_state_data_model_json2 == job_state_data_model_json

class TestJobStateDataSummaryItem():
    """
    Test Class for JobStateDataSummaryItem
    """

    def test_job_state_data_summary_item_serialization(self):
        """
        Test serialization/deserialization for JobStateDataSummaryItem
        """

        # Construct a json representation of a JobStateDataSummaryItem model
        job_state_data_summary_item_model_json = {}
        job_state_data_summary_item_model_json['name'] = 'testString'
        job_state_data_summary_item_model_json['type'] = 'number'
        job_state_data_summary_item_model_json['value'] = 'testString'

        # Construct a model instance of JobStateDataSummaryItem by calling from_dict on the json representation
        job_state_data_summary_item_model = JobStateDataSummaryItem.from_dict(job_state_data_summary_item_model_json)
        assert job_state_data_summary_item_model != False

        # Construct a model instance of JobStateDataSummaryItem by calling from_dict on the json representation
        job_state_data_summary_item_model_dict = JobStateDataSummaryItem.from_dict(job_state_data_summary_item_model_json).__dict__
        job_state_data_summary_item_model2 = JobStateDataSummaryItem(**job_state_data_summary_item_model_dict)

        # Verify the model instances are equivalent
        assert job_state_data_summary_item_model == job_state_data_summary_item_model2

        # Convert model instance back to dict and verify no loss of data
        job_state_data_summary_item_model_json2 = job_state_data_summary_item_model.to_dict()
        assert job_state_data_summary_item_model_json2 == job_state_data_summary_item_model_json

class TestJobStatus():
    """
    Test Class for JobStatus
    """

    def test_job_status_serialization(self):
        """
        Test serialization/deserialization for JobStatus
        """

        # Construct dict forms of any model objects needed in order to build this model.

        job_status_action_model = {} # JobStatusAction
        job_status_action_model['action_name'] = 'testString'
        job_status_action_model['status_code'] = 'job_pending'
        job_status_action_model['status_message'] = 'testString'
        job_status_action_model['bastion_status_code'] = 'none'
        job_status_action_model['bastion_status_message'] = 'testString'
        job_status_action_model['targets_status_code'] = 'none'
        job_status_action_model['targets_status_message'] = 'testString'
        job_status_action_model['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a JobStatus model
        job_status_model_json = {}
        job_status_model_json['action_job_status'] = job_status_action_model

        # Construct a model instance of JobStatus by calling from_dict on the json representation
        job_status_model = JobStatus.from_dict(job_status_model_json)
        assert job_status_model != False

        # Construct a model instance of JobStatus by calling from_dict on the json representation
        job_status_model_dict = JobStatus.from_dict(job_status_model_json).__dict__
        job_status_model2 = JobStatus(**job_status_model_dict)

        # Verify the model instances are equivalent
        assert job_status_model == job_status_model2

        # Convert model instance back to dict and verify no loss of data
        job_status_model_json2 = job_status_model.to_dict()
        assert job_status_model_json2 == job_status_model_json

class TestJobStatusAction():
    """
    Test Class for JobStatusAction
    """

    def test_job_status_action_serialization(self):
        """
        Test serialization/deserialization for JobStatusAction
        """

        # Construct a json representation of a JobStatusAction model
        job_status_action_model_json = {}
        job_status_action_model_json['action_name'] = 'testString'
        job_status_action_model_json['status_code'] = 'job_pending'
        job_status_action_model_json['status_message'] = 'testString'
        job_status_action_model_json['bastion_status_code'] = 'none'
        job_status_action_model_json['bastion_status_message'] = 'testString'
        job_status_action_model_json['targets_status_code'] = 'none'
        job_status_action_model_json['targets_status_message'] = 'testString'
        job_status_action_model_json['updated_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of JobStatusAction by calling from_dict on the json representation
        job_status_action_model = JobStatusAction.from_dict(job_status_action_model_json)
        assert job_status_action_model != False

        # Construct a model instance of JobStatusAction by calling from_dict on the json representation
        job_status_action_model_dict = JobStatusAction.from_dict(job_status_action_model_json).__dict__
        job_status_action_model2 = JobStatusAction(**job_status_action_model_dict)

        # Verify the model instances are equivalent
        assert job_status_action_model == job_status_action_model2

        # Convert model instance back to dict and verify no loss of data
        job_status_action_model_json2 = job_status_action_model.to_dict()
        assert job_status_action_model_json2 == job_status_action_model_json

class TestJobStatusType():
    """
    Test Class for JobStatusType
    """

    def test_job_status_type_serialization(self):
        """
        Test serialization/deserialization for JobStatusType
        """

        # Construct a json representation of a JobStatusType model
        job_status_type_model_json = {}
        job_status_type_model_json['failed'] = ['testString']
        job_status_type_model_json['in_progress'] = ['testString']
        job_status_type_model_json['success'] = ['testString']
        job_status_type_model_json['last_updated_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of JobStatusType by calling from_dict on the json representation
        job_status_type_model = JobStatusType.from_dict(job_status_type_model_json)
        assert job_status_type_model != False

        # Construct a model instance of JobStatusType by calling from_dict on the json representation
        job_status_type_model_dict = JobStatusType.from_dict(job_status_type_model_json).__dict__
        job_status_type_model2 = JobStatusType(**job_status_type_model_dict)

        # Verify the model instances are equivalent
        assert job_status_type_model == job_status_type_model2

        # Convert model instance back to dict and verify no loss of data
        job_status_type_model_json2 = job_status_type_model.to_dict()
        assert job_status_type_model_json2 == job_status_type_model_json

class TestKMSDiscovery():
    """
    Test Class for KMSDiscovery
    """

    def test_kms_discovery_serialization(self):
        """
        Test serialization/deserialization for KMSDiscovery
        """

        # Construct dict forms of any model objects needed in order to build this model.

        kms_instances_keys_item_model = {} # KMSInstancesKeysItem
        kms_instances_keys_item_model['name'] = 'testString'
        kms_instances_keys_item_model['crn'] = 'testString'
        kms_instances_keys_item_model['error'] = 'testString'

        kms_instances_model = {} # KMSInstances
        kms_instances_model['location'] = 'testString'
        kms_instances_model['encryption_scheme'] = 'testString'
        kms_instances_model['resource_group'] = 'testString'
        kms_instances_model['kms_crn'] = 'testString'
        kms_instances_model['kms_name'] = 'testString'
        kms_instances_model['kms_private_endpoint'] = 'testString'
        kms_instances_model['kms_public_endpoint'] = 'testString'
        kms_instances_model['keys'] = [kms_instances_keys_item_model]

        # Construct a json representation of a KMSDiscovery model
        kms_discovery_model_json = {}
        kms_discovery_model_json['total_count'] = 26
        kms_discovery_model_json['limit'] = 26
        kms_discovery_model_json['offset'] = 26
        kms_discovery_model_json['kms_instances'] = [kms_instances_model]

        # Construct a model instance of KMSDiscovery by calling from_dict on the json representation
        kms_discovery_model = KMSDiscovery.from_dict(kms_discovery_model_json)
        assert kms_discovery_model != False

        # Construct a model instance of KMSDiscovery by calling from_dict on the json representation
        kms_discovery_model_dict = KMSDiscovery.from_dict(kms_discovery_model_json).__dict__
        kms_discovery_model2 = KMSDiscovery(**kms_discovery_model_dict)

        # Verify the model instances are equivalent
        assert kms_discovery_model == kms_discovery_model2

        # Convert model instance back to dict and verify no loss of data
        kms_discovery_model_json2 = kms_discovery_model.to_dict()
        assert kms_discovery_model_json2 == kms_discovery_model_json

class TestKMSInstances():
    """
    Test Class for KMSInstances
    """

    def test_kms_instances_serialization(self):
        """
        Test serialization/deserialization for KMSInstances
        """

        # Construct dict forms of any model objects needed in order to build this model.

        kms_instances_keys_item_model = {} # KMSInstancesKeysItem
        kms_instances_keys_item_model['name'] = 'testString'
        kms_instances_keys_item_model['crn'] = 'testString'
        kms_instances_keys_item_model['error'] = 'testString'

        # Construct a json representation of a KMSInstances model
        kms_instances_model_json = {}
        kms_instances_model_json['location'] = 'testString'
        kms_instances_model_json['encryption_scheme'] = 'testString'
        kms_instances_model_json['resource_group'] = 'testString'
        kms_instances_model_json['kms_crn'] = 'testString'
        kms_instances_model_json['kms_name'] = 'testString'
        kms_instances_model_json['kms_private_endpoint'] = 'testString'
        kms_instances_model_json['kms_public_endpoint'] = 'testString'
        kms_instances_model_json['keys'] = [kms_instances_keys_item_model]

        # Construct a model instance of KMSInstances by calling from_dict on the json representation
        kms_instances_model = KMSInstances.from_dict(kms_instances_model_json)
        assert kms_instances_model != False

        # Construct a model instance of KMSInstances by calling from_dict on the json representation
        kms_instances_model_dict = KMSInstances.from_dict(kms_instances_model_json).__dict__
        kms_instances_model2 = KMSInstances(**kms_instances_model_dict)

        # Verify the model instances are equivalent
        assert kms_instances_model == kms_instances_model2

        # Convert model instance back to dict and verify no loss of data
        kms_instances_model_json2 = kms_instances_model.to_dict()
        assert kms_instances_model_json2 == kms_instances_model_json

class TestKMSInstancesKeysItem():
    """
    Test Class for KMSInstancesKeysItem
    """

    def test_kms_instances_keys_item_serialization(self):
        """
        Test serialization/deserialization for KMSInstancesKeysItem
        """

        # Construct a json representation of a KMSInstancesKeysItem model
        kms_instances_keys_item_model_json = {}
        kms_instances_keys_item_model_json['name'] = 'testString'
        kms_instances_keys_item_model_json['crn'] = 'testString'
        kms_instances_keys_item_model_json['error'] = 'testString'

        # Construct a model instance of KMSInstancesKeysItem by calling from_dict on the json representation
        kms_instances_keys_item_model = KMSInstancesKeysItem.from_dict(kms_instances_keys_item_model_json)
        assert kms_instances_keys_item_model != False

        # Construct a model instance of KMSInstancesKeysItem by calling from_dict on the json representation
        kms_instances_keys_item_model_dict = KMSInstancesKeysItem.from_dict(kms_instances_keys_item_model_json).__dict__
        kms_instances_keys_item_model2 = KMSInstancesKeysItem(**kms_instances_keys_item_model_dict)

        # Verify the model instances are equivalent
        assert kms_instances_keys_item_model == kms_instances_keys_item_model2

        # Convert model instance back to dict and verify no loss of data
        kms_instances_keys_item_model_json2 = kms_instances_keys_item_model.to_dict()
        assert kms_instances_keys_item_model_json2 == kms_instances_keys_item_model_json

class TestKMSSettings():
    """
    Test Class for KMSSettings
    """

    def test_kms_settings_serialization(self):
        """
        Test serialization/deserialization for KMSSettings
        """

        # Construct dict forms of any model objects needed in order to build this model.

        kms_settings_primary_crk_model = {} # KMSSettingsPrimaryCrk
        kms_settings_primary_crk_model['kms_name'] = 'testString'
        kms_settings_primary_crk_model['kms_private_endpoint'] = 'testString'
        kms_settings_primary_crk_model['key_crn'] = 'testString'

        kms_settings_secondary_crk_model = {} # KMSSettingsSecondaryCrk
        kms_settings_secondary_crk_model['kms_name'] = 'testString'
        kms_settings_secondary_crk_model['kms_private_endpoint'] = 'testString'
        kms_settings_secondary_crk_model['key_crn'] = 'testString'

        # Construct a json representation of a KMSSettings model
        kms_settings_model_json = {}
        kms_settings_model_json['location'] = 'testString'
        kms_settings_model_json['encryption_scheme'] = 'testString'
        kms_settings_model_json['resource_group'] = 'testString'
        kms_settings_model_json['primary_crk'] = kms_settings_primary_crk_model
        kms_settings_model_json['secondary_crk'] = kms_settings_secondary_crk_model

        # Construct a model instance of KMSSettings by calling from_dict on the json representation
        kms_settings_model = KMSSettings.from_dict(kms_settings_model_json)
        assert kms_settings_model != False

        # Construct a model instance of KMSSettings by calling from_dict on the json representation
        kms_settings_model_dict = KMSSettings.from_dict(kms_settings_model_json).__dict__
        kms_settings_model2 = KMSSettings(**kms_settings_model_dict)

        # Verify the model instances are equivalent
        assert kms_settings_model == kms_settings_model2

        # Convert model instance back to dict and verify no loss of data
        kms_settings_model_json2 = kms_settings_model.to_dict()
        assert kms_settings_model_json2 == kms_settings_model_json

class TestKMSSettingsPrimaryCrk():
    """
    Test Class for KMSSettingsPrimaryCrk
    """

    def test_kms_settings_primary_crk_serialization(self):
        """
        Test serialization/deserialization for KMSSettingsPrimaryCrk
        """

        # Construct a json representation of a KMSSettingsPrimaryCrk model
        kms_settings_primary_crk_model_json = {}
        kms_settings_primary_crk_model_json['kms_name'] = 'testString'
        kms_settings_primary_crk_model_json['kms_private_endpoint'] = 'testString'
        kms_settings_primary_crk_model_json['key_crn'] = 'testString'

        # Construct a model instance of KMSSettingsPrimaryCrk by calling from_dict on the json representation
        kms_settings_primary_crk_model = KMSSettingsPrimaryCrk.from_dict(kms_settings_primary_crk_model_json)
        assert kms_settings_primary_crk_model != False

        # Construct a model instance of KMSSettingsPrimaryCrk by calling from_dict on the json representation
        kms_settings_primary_crk_model_dict = KMSSettingsPrimaryCrk.from_dict(kms_settings_primary_crk_model_json).__dict__
        kms_settings_primary_crk_model2 = KMSSettingsPrimaryCrk(**kms_settings_primary_crk_model_dict)

        # Verify the model instances are equivalent
        assert kms_settings_primary_crk_model == kms_settings_primary_crk_model2

        # Convert model instance back to dict and verify no loss of data
        kms_settings_primary_crk_model_json2 = kms_settings_primary_crk_model.to_dict()
        assert kms_settings_primary_crk_model_json2 == kms_settings_primary_crk_model_json

class TestKMSSettingsSecondaryCrk():
    """
    Test Class for KMSSettingsSecondaryCrk
    """

    def test_kms_settings_secondary_crk_serialization(self):
        """
        Test serialization/deserialization for KMSSettingsSecondaryCrk
        """

        # Construct a json representation of a KMSSettingsSecondaryCrk model
        kms_settings_secondary_crk_model_json = {}
        kms_settings_secondary_crk_model_json['kms_name'] = 'testString'
        kms_settings_secondary_crk_model_json['kms_private_endpoint'] = 'testString'
        kms_settings_secondary_crk_model_json['key_crn'] = 'testString'

        # Construct a model instance of KMSSettingsSecondaryCrk by calling from_dict on the json representation
        kms_settings_secondary_crk_model = KMSSettingsSecondaryCrk.from_dict(kms_settings_secondary_crk_model_json)
        assert kms_settings_secondary_crk_model != False

        # Construct a model instance of KMSSettingsSecondaryCrk by calling from_dict on the json representation
        kms_settings_secondary_crk_model_dict = KMSSettingsSecondaryCrk.from_dict(kms_settings_secondary_crk_model_json).__dict__
        kms_settings_secondary_crk_model2 = KMSSettingsSecondaryCrk(**kms_settings_secondary_crk_model_dict)

        # Verify the model instances are equivalent
        assert kms_settings_secondary_crk_model == kms_settings_secondary_crk_model2

        # Convert model instance back to dict and verify no loss of data
        kms_settings_secondary_crk_model_json2 = kms_settings_secondary_crk_model.to_dict()
        assert kms_settings_secondary_crk_model_json2 == kms_settings_secondary_crk_model_json

class TestLogStoreResponse():
    """
    Test Class for LogStoreResponse
    """

    def test_log_store_response_serialization(self):
        """
        Test serialization/deserialization for LogStoreResponse
        """

        # Construct a json representation of a LogStoreResponse model
        log_store_response_model_json = {}
        log_store_response_model_json['engine_name'] = 'testString'
        log_store_response_model_json['engine_version'] = 'testString'
        log_store_response_model_json['id'] = 'testString'
        log_store_response_model_json['log_store_url'] = 'testString'

        # Construct a model instance of LogStoreResponse by calling from_dict on the json representation
        log_store_response_model = LogStoreResponse.from_dict(log_store_response_model_json)
        assert log_store_response_model != False

        # Construct a model instance of LogStoreResponse by calling from_dict on the json representation
        log_store_response_model_dict = LogStoreResponse.from_dict(log_store_response_model_json).__dict__
        log_store_response_model2 = LogStoreResponse(**log_store_response_model_dict)

        # Verify the model instances are equivalent
        assert log_store_response_model == log_store_response_model2

        # Convert model instance back to dict and verify no loss of data
        log_store_response_model_json2 = log_store_response_model.to_dict()
        assert log_store_response_model_json2 == log_store_response_model_json

class TestLogStoreResponseList():
    """
    Test Class for LogStoreResponseList
    """

    def test_log_store_response_list_serialization(self):
        """
        Test serialization/deserialization for LogStoreResponseList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        log_store_response_model = {} # LogStoreResponse
        log_store_response_model['engine_name'] = 'testString'
        log_store_response_model['engine_version'] = 'testString'
        log_store_response_model['id'] = 'testString'
        log_store_response_model['log_store_url'] = 'testString'

        # Construct a json representation of a LogStoreResponseList model
        log_store_response_list_model_json = {}
        log_store_response_list_model_json['runtime_data'] = [log_store_response_model]

        # Construct a model instance of LogStoreResponseList by calling from_dict on the json representation
        log_store_response_list_model = LogStoreResponseList.from_dict(log_store_response_list_model_json)
        assert log_store_response_list_model != False

        # Construct a model instance of LogStoreResponseList by calling from_dict on the json representation
        log_store_response_list_model_dict = LogStoreResponseList.from_dict(log_store_response_list_model_json).__dict__
        log_store_response_list_model2 = LogStoreResponseList(**log_store_response_list_model_dict)

        # Verify the model instances are equivalent
        assert log_store_response_list_model == log_store_response_list_model2

        # Convert model instance back to dict and verify no loss of data
        log_store_response_list_model_json2 = log_store_response_list_model.to_dict()
        assert log_store_response_list_model_json2 == log_store_response_list_model_json

class TestLogSummary():
    """
    Test Class for LogSummary
    """

    def test_log_summary_serialization(self):
        """
        Test serialization/deserialization for LogSummary
        """

        # Construct a json representation of a LogSummary model
        log_summary_model_json = {}
        log_summary_model_json['activity_status'] = 'testString'
        log_summary_model_json['detected_template_type'] = 'testString'
        log_summary_model_json['discarded_files'] = 26
        log_summary_model_json['error'] = 'testString'
        log_summary_model_json['resources_added'] = 26
        log_summary_model_json['resources_destroyed'] = 26
        log_summary_model_json['resources_modified'] = 26
        log_summary_model_json['scanned_files'] = 26
        log_summary_model_json['template_variable_count'] = 26
        log_summary_model_json['time_taken'] = 72.5

        # Construct a model instance of LogSummary by calling from_dict on the json representation
        log_summary_model = LogSummary.from_dict(log_summary_model_json)
        assert log_summary_model != False

        # Construct a model instance of LogSummary by calling from_dict on the json representation
        log_summary_model_dict = LogSummary.from_dict(log_summary_model_json).__dict__
        log_summary_model2 = LogSummary(**log_summary_model_dict)

        # Verify the model instances are equivalent
        assert log_summary_model == log_summary_model2

        # Convert model instance back to dict and verify no loss of data
        log_summary_model_json2 = log_summary_model.to_dict()
        assert log_summary_model_json2 == log_summary_model_json

class TestOutputValuesItem():
    """
    Test Class for OutputValuesItem
    """

    def test_output_values_item_serialization(self):
        """
        Test serialization/deserialization for OutputValuesItem
        """

        # Construct a json representation of a OutputValuesItem model
        output_values_item_model_json = {}
        output_values_item_model_json['folder'] = 'testString'
        output_values_item_model_json['id'] = 'testString'
        output_values_item_model_json['output_values'] = [{ 'foo': 'bar' }]
        output_values_item_model_json['value_type'] = 'testString'

        # Construct a model instance of OutputValuesItem by calling from_dict on the json representation
        output_values_item_model = OutputValuesItem.from_dict(output_values_item_model_json)
        assert output_values_item_model != False

        # Construct a model instance of OutputValuesItem by calling from_dict on the json representation
        output_values_item_model_dict = OutputValuesItem.from_dict(output_values_item_model_json).__dict__
        output_values_item_model2 = OutputValuesItem(**output_values_item_model_dict)

        # Verify the model instances are equivalent
        assert output_values_item_model == output_values_item_model2

        # Convert model instance back to dict and verify no loss of data
        output_values_item_model_json2 = output_values_item_model.to_dict()
        assert output_values_item_model_json2 == output_values_item_model_json

class TestResourceGroupResponse():
    """
    Test Class for ResourceGroupResponse
    """

    def test_resource_group_response_serialization(self):
        """
        Test serialization/deserialization for ResourceGroupResponse
        """

        # Construct a json representation of a ResourceGroupResponse model
        resource_group_response_model_json = {}
        resource_group_response_model_json['account_id'] = 'testString'
        resource_group_response_model_json['crn'] = 'testString'
        resource_group_response_model_json['default'] = True
        resource_group_response_model_json['name'] = 'testString'
        resource_group_response_model_json['resource_group_id'] = 'testString'
        resource_group_response_model_json['state'] = 'testString'

        # Construct a model instance of ResourceGroupResponse by calling from_dict on the json representation
        resource_group_response_model = ResourceGroupResponse.from_dict(resource_group_response_model_json)
        assert resource_group_response_model != False

        # Construct a model instance of ResourceGroupResponse by calling from_dict on the json representation
        resource_group_response_model_dict = ResourceGroupResponse.from_dict(resource_group_response_model_json).__dict__
        resource_group_response_model2 = ResourceGroupResponse(**resource_group_response_model_dict)

        # Verify the model instances are equivalent
        assert resource_group_response_model == resource_group_response_model2

        # Convert model instance back to dict and verify no loss of data
        resource_group_response_model_json2 = resource_group_response_model.to_dict()
        assert resource_group_response_model_json2 == resource_group_response_model_json

class TestSchematicsLocations():
    """
    Test Class for SchematicsLocations
    """

    def test_schematics_locations_serialization(self):
        """
        Test serialization/deserialization for SchematicsLocations
        """

        # Construct a json representation of a SchematicsLocations model
        schematics_locations_model_json = {}
        schematics_locations_model_json['country'] = 'testString'
        schematics_locations_model_json['geography'] = 'testString'
        schematics_locations_model_json['id'] = 'testString'
        schematics_locations_model_json['kind'] = 'testString'
        schematics_locations_model_json['metro'] = 'testString'
        schematics_locations_model_json['multizone_metro'] = 'testString'
        schematics_locations_model_json['name'] = 'testString'

        # Construct a model instance of SchematicsLocations by calling from_dict on the json representation
        schematics_locations_model = SchematicsLocations.from_dict(schematics_locations_model_json)
        assert schematics_locations_model != False

        # Construct a model instance of SchematicsLocations by calling from_dict on the json representation
        schematics_locations_model_dict = SchematicsLocations.from_dict(schematics_locations_model_json).__dict__
        schematics_locations_model2 = SchematicsLocations(**schematics_locations_model_dict)

        # Verify the model instances are equivalent
        assert schematics_locations_model == schematics_locations_model2

        # Convert model instance back to dict and verify no loss of data
        schematics_locations_model_json2 = schematics_locations_model.to_dict()
        assert schematics_locations_model_json2 == schematics_locations_model_json

class TestSharedDatasetData():
    """
    Test Class for SharedDatasetData
    """

    def test_shared_dataset_data_serialization(self):
        """
        Test serialization/deserialization for SharedDatasetData
        """

        # Construct a json representation of a SharedDatasetData model
        shared_dataset_data_model_json = {}
        shared_dataset_data_model_json['default_value'] = 'testString'
        shared_dataset_data_model_json['description'] = 'testString'
        shared_dataset_data_model_json['hidden'] = True
        shared_dataset_data_model_json['immutable'] = True
        shared_dataset_data_model_json['matches'] = 'testString'
        shared_dataset_data_model_json['max_value'] = 'testString'
        shared_dataset_data_model_json['max_value_len'] = 'testString'
        shared_dataset_data_model_json['min_value'] = 'testString'
        shared_dataset_data_model_json['min_value_len'] = 'testString'
        shared_dataset_data_model_json['options'] = ['testString']
        shared_dataset_data_model_json['override_value'] = 'testString'
        shared_dataset_data_model_json['secure'] = True
        shared_dataset_data_model_json['var_aliases'] = ['testString']
        shared_dataset_data_model_json['var_name'] = 'testString'
        shared_dataset_data_model_json['var_ref'] = 'testString'
        shared_dataset_data_model_json['var_type'] = 'testString'

        # Construct a model instance of SharedDatasetData by calling from_dict on the json representation
        shared_dataset_data_model = SharedDatasetData.from_dict(shared_dataset_data_model_json)
        assert shared_dataset_data_model != False

        # Construct a model instance of SharedDatasetData by calling from_dict on the json representation
        shared_dataset_data_model_dict = SharedDatasetData.from_dict(shared_dataset_data_model_json).__dict__
        shared_dataset_data_model2 = SharedDatasetData(**shared_dataset_data_model_dict)

        # Verify the model instances are equivalent
        assert shared_dataset_data_model == shared_dataset_data_model2

        # Convert model instance back to dict and verify no loss of data
        shared_dataset_data_model_json2 = shared_dataset_data_model.to_dict()
        assert shared_dataset_data_model_json2 == shared_dataset_data_model_json

class TestSharedDatasetResponse():
    """
    Test Class for SharedDatasetResponse
    """

    def test_shared_dataset_response_serialization(self):
        """
        Test serialization/deserialization for SharedDatasetResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        shared_dataset_data_model = {} # SharedDatasetData
        shared_dataset_data_model['default_value'] = 'testString'
        shared_dataset_data_model['description'] = 'testString'
        shared_dataset_data_model['hidden'] = True
        shared_dataset_data_model['immutable'] = True
        shared_dataset_data_model['matches'] = 'testString'
        shared_dataset_data_model['max_value'] = 'testString'
        shared_dataset_data_model['max_value_len'] = 'testString'
        shared_dataset_data_model['min_value'] = 'testString'
        shared_dataset_data_model['min_value_len'] = 'testString'
        shared_dataset_data_model['options'] = ['testString']
        shared_dataset_data_model['override_value'] = 'testString'
        shared_dataset_data_model['secure'] = True
        shared_dataset_data_model['var_aliases'] = ['testString']
        shared_dataset_data_model['var_name'] = 'testString'
        shared_dataset_data_model['var_ref'] = 'testString'
        shared_dataset_data_model['var_type'] = 'testString'

        # Construct a json representation of a SharedDatasetResponse model
        shared_dataset_response_model_json = {}
        shared_dataset_response_model_json['account'] = 'testString'
        shared_dataset_response_model_json['created_at'] = '2020-01-28T18:40:40.123456Z'
        shared_dataset_response_model_json['created_by'] = 'testString'
        shared_dataset_response_model_json['description'] = 'testString'
        shared_dataset_response_model_json['effected_workspace_ids'] = ['testString']
        shared_dataset_response_model_json['resource_group'] = 'testString'
        shared_dataset_response_model_json['shared_dataset_data'] = [shared_dataset_data_model]
        shared_dataset_response_model_json['shared_dataset_id'] = 'testString'
        shared_dataset_response_model_json['shared_dataset_name'] = 'testString'
        shared_dataset_response_model_json['shared_dataset_type'] = ['testString']
        shared_dataset_response_model_json['state'] = 'testString'
        shared_dataset_response_model_json['tags'] = ['testString']
        shared_dataset_response_model_json['updated_at'] = '2020-01-28T18:40:40.123456Z'
        shared_dataset_response_model_json['updated_by'] = 'testString'
        shared_dataset_response_model_json['version'] = 'testString'

        # Construct a model instance of SharedDatasetResponse by calling from_dict on the json representation
        shared_dataset_response_model = SharedDatasetResponse.from_dict(shared_dataset_response_model_json)
        assert shared_dataset_response_model != False

        # Construct a model instance of SharedDatasetResponse by calling from_dict on the json representation
        shared_dataset_response_model_dict = SharedDatasetResponse.from_dict(shared_dataset_response_model_json).__dict__
        shared_dataset_response_model2 = SharedDatasetResponse(**shared_dataset_response_model_dict)

        # Verify the model instances are equivalent
        assert shared_dataset_response_model == shared_dataset_response_model2

        # Convert model instance back to dict and verify no loss of data
        shared_dataset_response_model_json2 = shared_dataset_response_model.to_dict()
        assert shared_dataset_response_model_json2 == shared_dataset_response_model_json

class TestSharedDatasetResponseList():
    """
    Test Class for SharedDatasetResponseList
    """

    def test_shared_dataset_response_list_serialization(self):
        """
        Test serialization/deserialization for SharedDatasetResponseList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        shared_dataset_data_model = {} # SharedDatasetData
        shared_dataset_data_model['default_value'] = 'testString'
        shared_dataset_data_model['description'] = 'testString'
        shared_dataset_data_model['hidden'] = True
        shared_dataset_data_model['immutable'] = True
        shared_dataset_data_model['matches'] = 'testString'
        shared_dataset_data_model['max_value'] = 'testString'
        shared_dataset_data_model['max_value_len'] = 'testString'
        shared_dataset_data_model['min_value'] = 'testString'
        shared_dataset_data_model['min_value_len'] = 'testString'
        shared_dataset_data_model['options'] = ['testString']
        shared_dataset_data_model['override_value'] = 'testString'
        shared_dataset_data_model['secure'] = True
        shared_dataset_data_model['var_aliases'] = ['testString']
        shared_dataset_data_model['var_name'] = 'testString'
        shared_dataset_data_model['var_ref'] = 'testString'
        shared_dataset_data_model['var_type'] = 'testString'

        shared_dataset_response_model = {} # SharedDatasetResponse
        shared_dataset_response_model['account'] = 'testString'
        shared_dataset_response_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        shared_dataset_response_model['created_by'] = 'testString'
        shared_dataset_response_model['description'] = 'testString'
        shared_dataset_response_model['effected_workspace_ids'] = ['testString']
        shared_dataset_response_model['resource_group'] = 'testString'
        shared_dataset_response_model['shared_dataset_data'] = [shared_dataset_data_model]
        shared_dataset_response_model['shared_dataset_id'] = 'testString'
        shared_dataset_response_model['shared_dataset_name'] = 'testString'
        shared_dataset_response_model['shared_dataset_type'] = ['testString']
        shared_dataset_response_model['state'] = 'testString'
        shared_dataset_response_model['tags'] = ['testString']
        shared_dataset_response_model['updated_at'] = '2020-01-28T18:40:40.123456Z'
        shared_dataset_response_model['updated_by'] = 'testString'
        shared_dataset_response_model['version'] = 'testString'

        # Construct a json representation of a SharedDatasetResponseList model
        shared_dataset_response_list_model_json = {}
        shared_dataset_response_list_model_json['count'] = 26
        shared_dataset_response_list_model_json['shared_datasets'] = [shared_dataset_response_model]

        # Construct a model instance of SharedDatasetResponseList by calling from_dict on the json representation
        shared_dataset_response_list_model = SharedDatasetResponseList.from_dict(shared_dataset_response_list_model_json)
        assert shared_dataset_response_list_model != False

        # Construct a model instance of SharedDatasetResponseList by calling from_dict on the json representation
        shared_dataset_response_list_model_dict = SharedDatasetResponseList.from_dict(shared_dataset_response_list_model_json).__dict__
        shared_dataset_response_list_model2 = SharedDatasetResponseList(**shared_dataset_response_list_model_dict)

        # Verify the model instances are equivalent
        assert shared_dataset_response_list_model == shared_dataset_response_list_model2

        # Convert model instance back to dict and verify no loss of data
        shared_dataset_response_list_model_json2 = shared_dataset_response_list_model.to_dict()
        assert shared_dataset_response_list_model_json2 == shared_dataset_response_list_model_json

class TestSharedTargetData():
    """
    Test Class for SharedTargetData
    """

    def test_shared_target_data_serialization(self):
        """
        Test serialization/deserialization for SharedTargetData
        """

        # Construct a json representation of a SharedTargetData model
        shared_target_data_model_json = {}
        shared_target_data_model_json['cluster_created_on'] = 'testString'
        shared_target_data_model_json['cluster_id'] = 'testString'
        shared_target_data_model_json['cluster_name'] = 'testString'
        shared_target_data_model_json['cluster_type'] = 'testString'
        shared_target_data_model_json['entitlement_keys'] = [{ 'foo': 'bar' }]
        shared_target_data_model_json['namespace'] = 'testString'
        shared_target_data_model_json['region'] = 'testString'
        shared_target_data_model_json['resource_group_id'] = 'testString'
        shared_target_data_model_json['worker_count'] = 26
        shared_target_data_model_json['worker_machine_type'] = 'testString'

        # Construct a model instance of SharedTargetData by calling from_dict on the json representation
        shared_target_data_model = SharedTargetData.from_dict(shared_target_data_model_json)
        assert shared_target_data_model != False

        # Construct a model instance of SharedTargetData by calling from_dict on the json representation
        shared_target_data_model_dict = SharedTargetData.from_dict(shared_target_data_model_json).__dict__
        shared_target_data_model2 = SharedTargetData(**shared_target_data_model_dict)

        # Verify the model instances are equivalent
        assert shared_target_data_model == shared_target_data_model2

        # Convert model instance back to dict and verify no loss of data
        shared_target_data_model_json2 = shared_target_data_model.to_dict()
        assert shared_target_data_model_json2 == shared_target_data_model_json

class TestSharedTargetDataResponse():
    """
    Test Class for SharedTargetDataResponse
    """

    def test_shared_target_data_response_serialization(self):
        """
        Test serialization/deserialization for SharedTargetDataResponse
        """

        # Construct a json representation of a SharedTargetDataResponse model
        shared_target_data_response_model_json = {}
        shared_target_data_response_model_json['cluster_id'] = 'testString'
        shared_target_data_response_model_json['cluster_name'] = 'testString'
        shared_target_data_response_model_json['entitlement_keys'] = [{ 'foo': 'bar' }]
        shared_target_data_response_model_json['namespace'] = 'testString'
        shared_target_data_response_model_json['region'] = 'testString'
        shared_target_data_response_model_json['resource_group_id'] = 'testString'

        # Construct a model instance of SharedTargetDataResponse by calling from_dict on the json representation
        shared_target_data_response_model = SharedTargetDataResponse.from_dict(shared_target_data_response_model_json)
        assert shared_target_data_response_model != False

        # Construct a model instance of SharedTargetDataResponse by calling from_dict on the json representation
        shared_target_data_response_model_dict = SharedTargetDataResponse.from_dict(shared_target_data_response_model_json).__dict__
        shared_target_data_response_model2 = SharedTargetDataResponse(**shared_target_data_response_model_dict)

        # Verify the model instances are equivalent
        assert shared_target_data_response_model == shared_target_data_response_model2

        # Convert model instance back to dict and verify no loss of data
        shared_target_data_response_model_json2 = shared_target_data_response_model.to_dict()
        assert shared_target_data_response_model_json2 == shared_target_data_response_model_json

class TestStateStoreResponse():
    """
    Test Class for StateStoreResponse
    """

    def test_state_store_response_serialization(self):
        """
        Test serialization/deserialization for StateStoreResponse
        """

        # Construct a json representation of a StateStoreResponse model
        state_store_response_model_json = {}
        state_store_response_model_json['engine_name'] = 'testString'
        state_store_response_model_json['engine_version'] = 'testString'
        state_store_response_model_json['id'] = 'testString'
        state_store_response_model_json['state_store_url'] = 'testString'

        # Construct a model instance of StateStoreResponse by calling from_dict on the json representation
        state_store_response_model = StateStoreResponse.from_dict(state_store_response_model_json)
        assert state_store_response_model != False

        # Construct a model instance of StateStoreResponse by calling from_dict on the json representation
        state_store_response_model_dict = StateStoreResponse.from_dict(state_store_response_model_json).__dict__
        state_store_response_model2 = StateStoreResponse(**state_store_response_model_dict)

        # Verify the model instances are equivalent
        assert state_store_response_model == state_store_response_model2

        # Convert model instance back to dict and verify no loss of data
        state_store_response_model_json2 = state_store_response_model.to_dict()
        assert state_store_response_model_json2 == state_store_response_model_json

class TestStateStoreResponseList():
    """
    Test Class for StateStoreResponseList
    """

    def test_state_store_response_list_serialization(self):
        """
        Test serialization/deserialization for StateStoreResponseList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        state_store_response_model = {} # StateStoreResponse
        state_store_response_model['engine_name'] = 'testString'
        state_store_response_model['engine_version'] = 'testString'
        state_store_response_model['id'] = 'testString'
        state_store_response_model['state_store_url'] = 'testString'

        # Construct a json representation of a StateStoreResponseList model
        state_store_response_list_model_json = {}
        state_store_response_list_model_json['runtime_data'] = [state_store_response_model]

        # Construct a model instance of StateStoreResponseList by calling from_dict on the json representation
        state_store_response_list_model = StateStoreResponseList.from_dict(state_store_response_list_model_json)
        assert state_store_response_list_model != False

        # Construct a model instance of StateStoreResponseList by calling from_dict on the json representation
        state_store_response_list_model_dict = StateStoreResponseList.from_dict(state_store_response_list_model_json).__dict__
        state_store_response_list_model2 = StateStoreResponseList(**state_store_response_list_model_dict)

        # Verify the model instances are equivalent
        assert state_store_response_list_model == state_store_response_list_model2

        # Convert model instance back to dict and verify no loss of data
        state_store_response_list_model_json2 = state_store_response_list_model.to_dict()
        assert state_store_response_list_model_json2 == state_store_response_list_model_json

class TestSystemLock():
    """
    Test Class for SystemLock
    """

    def test_system_lock_serialization(self):
        """
        Test serialization/deserialization for SystemLock
        """

        # Construct a json representation of a SystemLock model
        system_lock_model_json = {}
        system_lock_model_json['sys_locked'] = True
        system_lock_model_json['sys_locked_by'] = 'testString'
        system_lock_model_json['sys_locked_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of SystemLock by calling from_dict on the json representation
        system_lock_model = SystemLock.from_dict(system_lock_model_json)
        assert system_lock_model != False

        # Construct a model instance of SystemLock by calling from_dict on the json representation
        system_lock_model_dict = SystemLock.from_dict(system_lock_model_json).__dict__
        system_lock_model2 = SystemLock(**system_lock_model_dict)

        # Verify the model instances are equivalent
        assert system_lock_model == system_lock_model2

        # Convert model instance back to dict and verify no loss of data
        system_lock_model_json2 = system_lock_model.to_dict()
        assert system_lock_model_json2 == system_lock_model_json

class TestTargetResourceset():
    """
    Test Class for TargetResourceset
    """

    def test_target_resourceset_serialization(self):
        """
        Test serialization/deserialization for TargetResourceset
        """

        # Construct dict forms of any model objects needed in order to build this model.

        system_lock_model = {} # SystemLock
        system_lock_model['sys_locked'] = True
        system_lock_model['sys_locked_by'] = 'testString'
        system_lock_model['sys_locked_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a TargetResourceset model
        target_resourceset_model_json = {}
        target_resourceset_model_json['name'] = 'testString'
        target_resourceset_model_json['type'] = 'testString'
        target_resourceset_model_json['description'] = 'testString'
        target_resourceset_model_json['resource_query'] = 'testString'
        target_resourceset_model_json['credential'] = 'testString'
        target_resourceset_model_json['id'] = 'testString'
        target_resourceset_model_json['created_at'] = '2020-01-28T18:40:40.123456Z'
        target_resourceset_model_json['created_by'] = 'testString'
        target_resourceset_model_json['updated_at'] = '2020-01-28T18:40:40.123456Z'
        target_resourceset_model_json['updated_by'] = 'testString'
        target_resourceset_model_json['sys_lock'] = system_lock_model
        target_resourceset_model_json['resource_ids'] = ['testString']

        # Construct a model instance of TargetResourceset by calling from_dict on the json representation
        target_resourceset_model = TargetResourceset.from_dict(target_resourceset_model_json)
        assert target_resourceset_model != False

        # Construct a model instance of TargetResourceset by calling from_dict on the json representation
        target_resourceset_model_dict = TargetResourceset.from_dict(target_resourceset_model_json).__dict__
        target_resourceset_model2 = TargetResourceset(**target_resourceset_model_dict)

        # Verify the model instances are equivalent
        assert target_resourceset_model == target_resourceset_model2

        # Convert model instance back to dict and verify no loss of data
        target_resourceset_model_json2 = target_resourceset_model.to_dict()
        assert target_resourceset_model_json2 == target_resourceset_model_json

class TestTemplateReadme():
    """
    Test Class for TemplateReadme
    """

    def test_template_readme_serialization(self):
        """
        Test serialization/deserialization for TemplateReadme
        """

        # Construct a json representation of a TemplateReadme model
        template_readme_model_json = {}
        template_readme_model_json['readme'] = 'testString'

        # Construct a model instance of TemplateReadme by calling from_dict on the json representation
        template_readme_model = TemplateReadme.from_dict(template_readme_model_json)
        assert template_readme_model != False

        # Construct a model instance of TemplateReadme by calling from_dict on the json representation
        template_readme_model_dict = TemplateReadme.from_dict(template_readme_model_json).__dict__
        template_readme_model2 = TemplateReadme(**template_readme_model_dict)

        # Verify the model instances are equivalent
        assert template_readme_model == template_readme_model2

        # Convert model instance back to dict and verify no loss of data
        template_readme_model_json2 = template_readme_model.to_dict()
        assert template_readme_model_json2 == template_readme_model_json

class TestTemplateRepoRequest():
    """
    Test Class for TemplateRepoRequest
    """

    def test_template_repo_request_serialization(self):
        """
        Test serialization/deserialization for TemplateRepoRequest
        """

        # Construct a json representation of a TemplateRepoRequest model
        template_repo_request_model_json = {}
        template_repo_request_model_json['branch'] = 'testString'
        template_repo_request_model_json['release'] = 'testString'
        template_repo_request_model_json['repo_sha_value'] = 'testString'
        template_repo_request_model_json['repo_url'] = 'testString'
        template_repo_request_model_json['url'] = 'testString'

        # Construct a model instance of TemplateRepoRequest by calling from_dict on the json representation
        template_repo_request_model = TemplateRepoRequest.from_dict(template_repo_request_model_json)
        assert template_repo_request_model != False

        # Construct a model instance of TemplateRepoRequest by calling from_dict on the json representation
        template_repo_request_model_dict = TemplateRepoRequest.from_dict(template_repo_request_model_json).__dict__
        template_repo_request_model2 = TemplateRepoRequest(**template_repo_request_model_dict)

        # Verify the model instances are equivalent
        assert template_repo_request_model == template_repo_request_model2

        # Convert model instance back to dict and verify no loss of data
        template_repo_request_model_json2 = template_repo_request_model.to_dict()
        assert template_repo_request_model_json2 == template_repo_request_model_json

class TestTemplateRepoResponse():
    """
    Test Class for TemplateRepoResponse
    """

    def test_template_repo_response_serialization(self):
        """
        Test serialization/deserialization for TemplateRepoResponse
        """

        # Construct a json representation of a TemplateRepoResponse model
        template_repo_response_model_json = {}
        template_repo_response_model_json['branch'] = 'testString'
        template_repo_response_model_json['full_url'] = 'testString'
        template_repo_response_model_json['has_uploadedgitrepotar'] = True
        template_repo_response_model_json['release'] = 'testString'
        template_repo_response_model_json['repo_sha_value'] = 'testString'
        template_repo_response_model_json['repo_url'] = 'testString'
        template_repo_response_model_json['url'] = 'testString'

        # Construct a model instance of TemplateRepoResponse by calling from_dict on the json representation
        template_repo_response_model = TemplateRepoResponse.from_dict(template_repo_response_model_json)
        assert template_repo_response_model != False

        # Construct a model instance of TemplateRepoResponse by calling from_dict on the json representation
        template_repo_response_model_dict = TemplateRepoResponse.from_dict(template_repo_response_model_json).__dict__
        template_repo_response_model2 = TemplateRepoResponse(**template_repo_response_model_dict)

        # Verify the model instances are equivalent
        assert template_repo_response_model == template_repo_response_model2

        # Convert model instance back to dict and verify no loss of data
        template_repo_response_model_json2 = template_repo_response_model.to_dict()
        assert template_repo_response_model_json2 == template_repo_response_model_json

class TestTemplateRepoTarUploadResponse():
    """
    Test Class for TemplateRepoTarUploadResponse
    """

    def test_template_repo_tar_upload_response_serialization(self):
        """
        Test serialization/deserialization for TemplateRepoTarUploadResponse
        """

        # Construct a json representation of a TemplateRepoTarUploadResponse model
        template_repo_tar_upload_response_model_json = {}
        template_repo_tar_upload_response_model_json['file_value'] = 'testString'
        template_repo_tar_upload_response_model_json['has_received_file'] = True
        template_repo_tar_upload_response_model_json['id'] = 'testString'

        # Construct a model instance of TemplateRepoTarUploadResponse by calling from_dict on the json representation
        template_repo_tar_upload_response_model = TemplateRepoTarUploadResponse.from_dict(template_repo_tar_upload_response_model_json)
        assert template_repo_tar_upload_response_model != False

        # Construct a model instance of TemplateRepoTarUploadResponse by calling from_dict on the json representation
        template_repo_tar_upload_response_model_dict = TemplateRepoTarUploadResponse.from_dict(template_repo_tar_upload_response_model_json).__dict__
        template_repo_tar_upload_response_model2 = TemplateRepoTarUploadResponse(**template_repo_tar_upload_response_model_dict)

        # Verify the model instances are equivalent
        assert template_repo_tar_upload_response_model == template_repo_tar_upload_response_model2

        # Convert model instance back to dict and verify no loss of data
        template_repo_tar_upload_response_model_json2 = template_repo_tar_upload_response_model.to_dict()
        assert template_repo_tar_upload_response_model_json2 == template_repo_tar_upload_response_model_json

class TestTemplateRepoUpdateRequest():
    """
    Test Class for TemplateRepoUpdateRequest
    """

    def test_template_repo_update_request_serialization(self):
        """
        Test serialization/deserialization for TemplateRepoUpdateRequest
        """

        # Construct a json representation of a TemplateRepoUpdateRequest model
        template_repo_update_request_model_json = {}
        template_repo_update_request_model_json['branch'] = 'testString'
        template_repo_update_request_model_json['release'] = 'testString'
        template_repo_update_request_model_json['repo_sha_value'] = 'testString'
        template_repo_update_request_model_json['repo_url'] = 'testString'
        template_repo_update_request_model_json['url'] = 'testString'

        # Construct a model instance of TemplateRepoUpdateRequest by calling from_dict on the json representation
        template_repo_update_request_model = TemplateRepoUpdateRequest.from_dict(template_repo_update_request_model_json)
        assert template_repo_update_request_model != False

        # Construct a model instance of TemplateRepoUpdateRequest by calling from_dict on the json representation
        template_repo_update_request_model_dict = TemplateRepoUpdateRequest.from_dict(template_repo_update_request_model_json).__dict__
        template_repo_update_request_model2 = TemplateRepoUpdateRequest(**template_repo_update_request_model_dict)

        # Verify the model instances are equivalent
        assert template_repo_update_request_model == template_repo_update_request_model2

        # Convert model instance back to dict and verify no loss of data
        template_repo_update_request_model_json2 = template_repo_update_request_model.to_dict()
        assert template_repo_update_request_model_json2 == template_repo_update_request_model_json

class TestTemplateResources():
    """
    Test Class for TemplateResources
    """

    def test_template_resources_serialization(self):
        """
        Test serialization/deserialization for TemplateResources
        """

        # Construct a json representation of a TemplateResources model
        template_resources_model_json = {}
        template_resources_model_json['folder'] = 'testString'
        template_resources_model_json['id'] = 'testString'
        template_resources_model_json['null_resources'] = [{ 'foo': 'bar' }]
        template_resources_model_json['related_resources'] = [{ 'foo': 'bar' }]
        template_resources_model_json['resources'] = [{ 'foo': 'bar' }]
        template_resources_model_json['resources_count'] = 26
        template_resources_model_json['template_type'] = 'testString'

        # Construct a model instance of TemplateResources by calling from_dict on the json representation
        template_resources_model = TemplateResources.from_dict(template_resources_model_json)
        assert template_resources_model != False

        # Construct a model instance of TemplateResources by calling from_dict on the json representation
        template_resources_model_dict = TemplateResources.from_dict(template_resources_model_json).__dict__
        template_resources_model2 = TemplateResources(**template_resources_model_dict)

        # Verify the model instances are equivalent
        assert template_resources_model == template_resources_model2

        # Convert model instance back to dict and verify no loss of data
        template_resources_model_json2 = template_resources_model.to_dict()
        assert template_resources_model_json2 == template_resources_model_json

class TestTemplateRunTimeDataResponse():
    """
    Test Class for TemplateRunTimeDataResponse
    """

    def test_template_run_time_data_response_serialization(self):
        """
        Test serialization/deserialization for TemplateRunTimeDataResponse
        """

        # Construct a json representation of a TemplateRunTimeDataResponse model
        template_run_time_data_response_model_json = {}
        template_run_time_data_response_model_json['engine_cmd'] = 'testString'
        template_run_time_data_response_model_json['engine_name'] = 'testString'
        template_run_time_data_response_model_json['engine_version'] = 'testString'
        template_run_time_data_response_model_json['id'] = 'testString'
        template_run_time_data_response_model_json['log_store_url'] = 'testString'
        template_run_time_data_response_model_json['output_values'] = [{ 'foo': 'bar' }]
        template_run_time_data_response_model_json['resources'] = [[{ 'foo': 'bar' }]]
        template_run_time_data_response_model_json['state_store_url'] = 'testString'

        # Construct a model instance of TemplateRunTimeDataResponse by calling from_dict on the json representation
        template_run_time_data_response_model = TemplateRunTimeDataResponse.from_dict(template_run_time_data_response_model_json)
        assert template_run_time_data_response_model != False

        # Construct a model instance of TemplateRunTimeDataResponse by calling from_dict on the json representation
        template_run_time_data_response_model_dict = TemplateRunTimeDataResponse.from_dict(template_run_time_data_response_model_json).__dict__
        template_run_time_data_response_model2 = TemplateRunTimeDataResponse(**template_run_time_data_response_model_dict)

        # Verify the model instances are equivalent
        assert template_run_time_data_response_model == template_run_time_data_response_model2

        # Convert model instance back to dict and verify no loss of data
        template_run_time_data_response_model_json2 = template_run_time_data_response_model.to_dict()
        assert template_run_time_data_response_model_json2 == template_run_time_data_response_model_json

class TestTemplateSourceDataRequest():
    """
    Test Class for TemplateSourceDataRequest
    """

    def test_template_source_data_request_serialization(self):
        """
        Test serialization/deserialization for TemplateSourceDataRequest
        """

        # Construct dict forms of any model objects needed in order to build this model.

        workspace_variable_request_model = {} # WorkspaceVariableRequest
        workspace_variable_request_model['description'] = 'testString'
        workspace_variable_request_model['name'] = 'testString'
        workspace_variable_request_model['secure'] = True
        workspace_variable_request_model['type'] = 'testString'
        workspace_variable_request_model['use_default'] = True
        workspace_variable_request_model['value'] = 'testString'

        # Construct a json representation of a TemplateSourceDataRequest model
        template_source_data_request_model_json = {}
        template_source_data_request_model_json['env_values'] = [{ 'foo': 'bar' }]
        template_source_data_request_model_json['folder'] = 'testString'
        template_source_data_request_model_json['init_state_file'] = 'testString'
        template_source_data_request_model_json['type'] = 'testString'
        template_source_data_request_model_json['uninstall_script_name'] = 'testString'
        template_source_data_request_model_json['values'] = 'testString'
        template_source_data_request_model_json['values_metadata'] = [{ 'foo': 'bar' }]
        template_source_data_request_model_json['variablestore'] = [workspace_variable_request_model]

        # Construct a model instance of TemplateSourceDataRequest by calling from_dict on the json representation
        template_source_data_request_model = TemplateSourceDataRequest.from_dict(template_source_data_request_model_json)
        assert template_source_data_request_model != False

        # Construct a model instance of TemplateSourceDataRequest by calling from_dict on the json representation
        template_source_data_request_model_dict = TemplateSourceDataRequest.from_dict(template_source_data_request_model_json).__dict__
        template_source_data_request_model2 = TemplateSourceDataRequest(**template_source_data_request_model_dict)

        # Verify the model instances are equivalent
        assert template_source_data_request_model == template_source_data_request_model2

        # Convert model instance back to dict and verify no loss of data
        template_source_data_request_model_json2 = template_source_data_request_model.to_dict()
        assert template_source_data_request_model_json2 == template_source_data_request_model_json

class TestTemplateSourceDataResponse():
    """
    Test Class for TemplateSourceDataResponse
    """

    def test_template_source_data_response_serialization(self):
        """
        Test serialization/deserialization for TemplateSourceDataResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        env_variable_response_model = {} # EnvVariableResponse
        env_variable_response_model['hidden'] = True
        env_variable_response_model['name'] = 'testString'
        env_variable_response_model['secure'] = True
        env_variable_response_model['value'] = 'testString'

        workspace_variable_response_model = {} # WorkspaceVariableResponse
        workspace_variable_response_model['description'] = 'testString'
        workspace_variable_response_model['name'] = 'testString'
        workspace_variable_response_model['secure'] = True
        workspace_variable_response_model['type'] = 'testString'
        workspace_variable_response_model['value'] = 'testString'

        # Construct a json representation of a TemplateSourceDataResponse model
        template_source_data_response_model_json = {}
        template_source_data_response_model_json['env_values'] = [env_variable_response_model]
        template_source_data_response_model_json['folder'] = 'testString'
        template_source_data_response_model_json['has_githubtoken'] = True
        template_source_data_response_model_json['id'] = 'testString'
        template_source_data_response_model_json['template_type'] = 'testString'
        template_source_data_response_model_json['uninstall_script_name'] = 'testString'
        template_source_data_response_model_json['values'] = 'testString'
        template_source_data_response_model_json['values_metadata'] = [{ 'foo': 'bar' }]
        template_source_data_response_model_json['values_url'] = 'testString'
        template_source_data_response_model_json['variablestore'] = [workspace_variable_response_model]

        # Construct a model instance of TemplateSourceDataResponse by calling from_dict on the json representation
        template_source_data_response_model = TemplateSourceDataResponse.from_dict(template_source_data_response_model_json)
        assert template_source_data_response_model != False

        # Construct a model instance of TemplateSourceDataResponse by calling from_dict on the json representation
        template_source_data_response_model_dict = TemplateSourceDataResponse.from_dict(template_source_data_response_model_json).__dict__
        template_source_data_response_model2 = TemplateSourceDataResponse(**template_source_data_response_model_dict)

        # Verify the model instances are equivalent
        assert template_source_data_response_model == template_source_data_response_model2

        # Convert model instance back to dict and verify no loss of data
        template_source_data_response_model_json2 = template_source_data_response_model.to_dict()
        assert template_source_data_response_model_json2 == template_source_data_response_model_json

class TestTemplateStateStore():
    """
    Test Class for TemplateStateStore
    """

    def test_template_state_store_serialization(self):
        """
        Test serialization/deserialization for TemplateStateStore
        """

        # Construct a json representation of a TemplateStateStore model
        template_state_store_model_json = {}
        template_state_store_model_json['version'] = 72.5
        template_state_store_model_json['terraform_version'] = 'testString'
        template_state_store_model_json['serial'] = 72.5
        template_state_store_model_json['lineage'] = 'testString'
        template_state_store_model_json['modules'] = [{ 'foo': 'bar' }]

        # Construct a model instance of TemplateStateStore by calling from_dict on the json representation
        template_state_store_model = TemplateStateStore.from_dict(template_state_store_model_json)
        assert template_state_store_model != False

        # Construct a model instance of TemplateStateStore by calling from_dict on the json representation
        template_state_store_model_dict = TemplateStateStore.from_dict(template_state_store_model_json).__dict__
        template_state_store_model2 = TemplateStateStore(**template_state_store_model_dict)

        # Verify the model instances are equivalent
        assert template_state_store_model == template_state_store_model2

        # Convert model instance back to dict and verify no loss of data
        template_state_store_model_json2 = template_state_store_model.to_dict()
        assert template_state_store_model_json2 == template_state_store_model_json

class TestTemplateValues():
    """
    Test Class for TemplateValues
    """

    def test_template_values_serialization(self):
        """
        Test serialization/deserialization for TemplateValues
        """

        # Construct a json representation of a TemplateValues model
        template_values_model_json = {}
        template_values_model_json['values_metadata'] = [{ 'foo': 'bar' }]

        # Construct a model instance of TemplateValues by calling from_dict on the json representation
        template_values_model = TemplateValues.from_dict(template_values_model_json)
        assert template_values_model != False

        # Construct a model instance of TemplateValues by calling from_dict on the json representation
        template_values_model_dict = TemplateValues.from_dict(template_values_model_json).__dict__
        template_values_model2 = TemplateValues(**template_values_model_dict)

        # Verify the model instances are equivalent
        assert template_values_model == template_values_model2

        # Convert model instance back to dict and verify no loss of data
        template_values_model_json2 = template_values_model.to_dict()
        assert template_values_model_json2 == template_values_model_json

class TestUserState():
    """
    Test Class for UserState
    """

    def test_user_state_serialization(self):
        """
        Test serialization/deserialization for UserState
        """

        # Construct a json representation of a UserState model
        user_state_model_json = {}
        user_state_model_json['state'] = 'draft'
        user_state_model_json['set_by'] = 'testString'
        user_state_model_json['set_at'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of UserState by calling from_dict on the json representation
        user_state_model = UserState.from_dict(user_state_model_json)
        assert user_state_model != False

        # Construct a model instance of UserState by calling from_dict on the json representation
        user_state_model_dict = UserState.from_dict(user_state_model_json).__dict__
        user_state_model2 = UserState(**user_state_model_dict)

        # Verify the model instances are equivalent
        assert user_state_model == user_state_model2

        # Convert model instance back to dict and verify no loss of data
        user_state_model_json2 = user_state_model.to_dict()
        assert user_state_model_json2 == user_state_model_json

class TestUserValues():
    """
    Test Class for UserValues
    """

    def test_user_values_serialization(self):
        """
        Test serialization/deserialization for UserValues
        """

        # Construct dict forms of any model objects needed in order to build this model.

        workspace_variable_response_model = {} # WorkspaceVariableResponse
        workspace_variable_response_model['description'] = 'testString'
        workspace_variable_response_model['name'] = 'testString'
        workspace_variable_response_model['secure'] = True
        workspace_variable_response_model['type'] = 'testString'
        workspace_variable_response_model['value'] = 'testString'

        # Construct a json representation of a UserValues model
        user_values_model_json = {}
        user_values_model_json['env_values'] = [{ 'foo': 'bar' }]
        user_values_model_json['values'] = 'testString'
        user_values_model_json['variablestore'] = [workspace_variable_response_model]

        # Construct a model instance of UserValues by calling from_dict on the json representation
        user_values_model = UserValues.from_dict(user_values_model_json)
        assert user_values_model != False

        # Construct a model instance of UserValues by calling from_dict on the json representation
        user_values_model_dict = UserValues.from_dict(user_values_model_json).__dict__
        user_values_model2 = UserValues(**user_values_model_dict)

        # Verify the model instances are equivalent
        assert user_values_model == user_values_model2

        # Convert model instance back to dict and verify no loss of data
        user_values_model_json2 = user_values_model.to_dict()
        assert user_values_model_json2 == user_values_model_json

class TestVariableData():
    """
    Test Class for VariableData
    """

    def test_variable_data_serialization(self):
        """
        Test serialization/deserialization for VariableData
        """

        # Construct dict forms of any model objects needed in order to build this model.

        variable_metadata_model = {} # VariableMetadata
        variable_metadata_model['type'] = 'boolean'
        variable_metadata_model['aliases'] = ['testString']
        variable_metadata_model['description'] = 'testString'
        variable_metadata_model['default_value'] = 'testString'
        variable_metadata_model['secure'] = True
        variable_metadata_model['immutable'] = True
        variable_metadata_model['hidden'] = True
        variable_metadata_model['options'] = ['testString']
        variable_metadata_model['min_value'] = 38
        variable_metadata_model['max_value'] = 38
        variable_metadata_model['min_length'] = 38
        variable_metadata_model['max_length'] = 38
        variable_metadata_model['matches'] = 'testString'
        variable_metadata_model['position'] = 38
        variable_metadata_model['group_by'] = 'testString'
        variable_metadata_model['source'] = 'testString'

        # Construct a json representation of a VariableData model
        variable_data_model_json = {}
        variable_data_model_json['name'] = 'testString'
        variable_data_model_json['value'] = 'testString'
        variable_data_model_json['metadata'] = variable_metadata_model
        variable_data_model_json['link'] = 'testString'

        # Construct a model instance of VariableData by calling from_dict on the json representation
        variable_data_model = VariableData.from_dict(variable_data_model_json)
        assert variable_data_model != False

        # Construct a model instance of VariableData by calling from_dict on the json representation
        variable_data_model_dict = VariableData.from_dict(variable_data_model_json).__dict__
        variable_data_model2 = VariableData(**variable_data_model_dict)

        # Verify the model instances are equivalent
        assert variable_data_model == variable_data_model2

        # Convert model instance back to dict and verify no loss of data
        variable_data_model_json2 = variable_data_model.to_dict()
        assert variable_data_model_json2 == variable_data_model_json

class TestVariableMetadata():
    """
    Test Class for VariableMetadata
    """

    def test_variable_metadata_serialization(self):
        """
        Test serialization/deserialization for VariableMetadata
        """

        # Construct a json representation of a VariableMetadata model
        variable_metadata_model_json = {}
        variable_metadata_model_json['type'] = 'boolean'
        variable_metadata_model_json['aliases'] = ['testString']
        variable_metadata_model_json['description'] = 'testString'
        variable_metadata_model_json['default_value'] = 'testString'
        variable_metadata_model_json['secure'] = True
        variable_metadata_model_json['immutable'] = True
        variable_metadata_model_json['hidden'] = True
        variable_metadata_model_json['options'] = ['testString']
        variable_metadata_model_json['min_value'] = 38
        variable_metadata_model_json['max_value'] = 38
        variable_metadata_model_json['min_length'] = 38
        variable_metadata_model_json['max_length'] = 38
        variable_metadata_model_json['matches'] = 'testString'
        variable_metadata_model_json['position'] = 38
        variable_metadata_model_json['group_by'] = 'testString'
        variable_metadata_model_json['source'] = 'testString'

        # Construct a model instance of VariableMetadata by calling from_dict on the json representation
        variable_metadata_model = VariableMetadata.from_dict(variable_metadata_model_json)
        assert variable_metadata_model != False

        # Construct a model instance of VariableMetadata by calling from_dict on the json representation
        variable_metadata_model_dict = VariableMetadata.from_dict(variable_metadata_model_json).__dict__
        variable_metadata_model2 = VariableMetadata(**variable_metadata_model_dict)

        # Verify the model instances are equivalent
        assert variable_metadata_model == variable_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        variable_metadata_model_json2 = variable_metadata_model.to_dict()
        assert variable_metadata_model_json2 == variable_metadata_model_json

class TestVersionResponse():
    """
    Test Class for VersionResponse
    """

    def test_version_response_serialization(self):
        """
        Test serialization/deserialization for VersionResponse
        """

        # Construct a json representation of a VersionResponse model
        version_response_model_json = {}
        version_response_model_json['builddate'] = 'testString'
        version_response_model_json['buildno'] = 'testString'
        version_response_model_json['commitsha'] = 'testString'
        version_response_model_json['helm_provider_version'] = 'testString'
        version_response_model_json['helm_version'] = 'testString'
        version_response_model_json['supported_template_types'] = [{ 'foo': 'bar' }]
        version_response_model_json['terraform_provider_version'] = 'testString'
        version_response_model_json['terraform_version'] = 'testString'

        # Construct a model instance of VersionResponse by calling from_dict on the json representation
        version_response_model = VersionResponse.from_dict(version_response_model_json)
        assert version_response_model != False

        # Construct a model instance of VersionResponse by calling from_dict on the json representation
        version_response_model_dict = VersionResponse.from_dict(version_response_model_json).__dict__
        version_response_model2 = VersionResponse(**version_response_model_dict)

        # Verify the model instances are equivalent
        assert version_response_model == version_response_model2

        # Convert model instance back to dict and verify no loss of data
        version_response_model_json2 = version_response_model.to_dict()
        assert version_response_model_json2 == version_response_model_json

class TestWorkspaceActivities():
    """
    Test Class for WorkspaceActivities
    """

    def test_workspace_activities_serialization(self):
        """
        Test serialization/deserialization for WorkspaceActivities
        """

        # Construct dict forms of any model objects needed in order to build this model.

        log_summary_model = {} # LogSummary
        log_summary_model['activity_status'] = 'testString'
        log_summary_model['detected_template_type'] = 'testString'
        log_summary_model['discarded_files'] = 26
        log_summary_model['error'] = 'testString'
        log_summary_model['resources_added'] = 26
        log_summary_model['resources_destroyed'] = 26
        log_summary_model['resources_modified'] = 26
        log_summary_model['scanned_files'] = 26
        log_summary_model['template_variable_count'] = 26
        log_summary_model['time_taken'] = 72.5

        workspace_activity_template_model = {} # WorkspaceActivityTemplate
        workspace_activity_template_model['end_time'] = '2020-01-28T18:40:40.123456Z'
        workspace_activity_template_model['log_summary'] = log_summary_model
        workspace_activity_template_model['log_url'] = 'testString'
        workspace_activity_template_model['message'] = 'testString'
        workspace_activity_template_model['start_time'] = '2020-01-28T18:40:40.123456Z'
        workspace_activity_template_model['status'] = 'testString'
        workspace_activity_template_model['template_id'] = 'testString'
        workspace_activity_template_model['template_type'] = 'testString'

        workspace_activity_model = {} # WorkspaceActivity
        workspace_activity_model['action_id'] = 'testString'
        workspace_activity_model['message'] = ['testString']
        workspace_activity_model['name'] = 'testString'
        workspace_activity_model['performed_at'] = '2020-01-28T18:40:40.123456Z'
        workspace_activity_model['performed_by'] = 'testString'
        workspace_activity_model['status'] = 'testString'
        workspace_activity_model['templates'] = [workspace_activity_template_model]

        # Construct a json representation of a WorkspaceActivities model
        workspace_activities_model_json = {}
        workspace_activities_model_json['actions'] = [workspace_activity_model]
        workspace_activities_model_json['workspace_id'] = 'testString'
        workspace_activities_model_json['workspace_name'] = 'testString'

        # Construct a model instance of WorkspaceActivities by calling from_dict on the json representation
        workspace_activities_model = WorkspaceActivities.from_dict(workspace_activities_model_json)
        assert workspace_activities_model != False

        # Construct a model instance of WorkspaceActivities by calling from_dict on the json representation
        workspace_activities_model_dict = WorkspaceActivities.from_dict(workspace_activities_model_json).__dict__
        workspace_activities_model2 = WorkspaceActivities(**workspace_activities_model_dict)

        # Verify the model instances are equivalent
        assert workspace_activities_model == workspace_activities_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_activities_model_json2 = workspace_activities_model.to_dict()
        assert workspace_activities_model_json2 == workspace_activities_model_json

class TestWorkspaceActivity():
    """
    Test Class for WorkspaceActivity
    """

    def test_workspace_activity_serialization(self):
        """
        Test serialization/deserialization for WorkspaceActivity
        """

        # Construct dict forms of any model objects needed in order to build this model.

        log_summary_model = {} # LogSummary
        log_summary_model['activity_status'] = 'testString'
        log_summary_model['detected_template_type'] = 'testString'
        log_summary_model['discarded_files'] = 26
        log_summary_model['error'] = 'testString'
        log_summary_model['resources_added'] = 26
        log_summary_model['resources_destroyed'] = 26
        log_summary_model['resources_modified'] = 26
        log_summary_model['scanned_files'] = 26
        log_summary_model['template_variable_count'] = 26
        log_summary_model['time_taken'] = 72.5

        workspace_activity_template_model = {} # WorkspaceActivityTemplate
        workspace_activity_template_model['end_time'] = '2020-01-28T18:40:40.123456Z'
        workspace_activity_template_model['log_summary'] = log_summary_model
        workspace_activity_template_model['log_url'] = 'testString'
        workspace_activity_template_model['message'] = 'testString'
        workspace_activity_template_model['start_time'] = '2020-01-28T18:40:40.123456Z'
        workspace_activity_template_model['status'] = 'testString'
        workspace_activity_template_model['template_id'] = 'testString'
        workspace_activity_template_model['template_type'] = 'testString'

        # Construct a json representation of a WorkspaceActivity model
        workspace_activity_model_json = {}
        workspace_activity_model_json['action_id'] = 'testString'
        workspace_activity_model_json['message'] = ['testString']
        workspace_activity_model_json['name'] = 'testString'
        workspace_activity_model_json['performed_at'] = '2020-01-28T18:40:40.123456Z'
        workspace_activity_model_json['performed_by'] = 'testString'
        workspace_activity_model_json['status'] = 'testString'
        workspace_activity_model_json['templates'] = [workspace_activity_template_model]

        # Construct a model instance of WorkspaceActivity by calling from_dict on the json representation
        workspace_activity_model = WorkspaceActivity.from_dict(workspace_activity_model_json)
        assert workspace_activity_model != False

        # Construct a model instance of WorkspaceActivity by calling from_dict on the json representation
        workspace_activity_model_dict = WorkspaceActivity.from_dict(workspace_activity_model_json).__dict__
        workspace_activity_model2 = WorkspaceActivity(**workspace_activity_model_dict)

        # Verify the model instances are equivalent
        assert workspace_activity_model == workspace_activity_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_activity_model_json2 = workspace_activity_model.to_dict()
        assert workspace_activity_model_json2 == workspace_activity_model_json

class TestWorkspaceActivityApplyResult():
    """
    Test Class for WorkspaceActivityApplyResult
    """

    def test_workspace_activity_apply_result_serialization(self):
        """
        Test serialization/deserialization for WorkspaceActivityApplyResult
        """

        # Construct a json representation of a WorkspaceActivityApplyResult model
        workspace_activity_apply_result_model_json = {}
        workspace_activity_apply_result_model_json['activityid'] = 'testString'

        # Construct a model instance of WorkspaceActivityApplyResult by calling from_dict on the json representation
        workspace_activity_apply_result_model = WorkspaceActivityApplyResult.from_dict(workspace_activity_apply_result_model_json)
        assert workspace_activity_apply_result_model != False

        # Construct a model instance of WorkspaceActivityApplyResult by calling from_dict on the json representation
        workspace_activity_apply_result_model_dict = WorkspaceActivityApplyResult.from_dict(workspace_activity_apply_result_model_json).__dict__
        workspace_activity_apply_result_model2 = WorkspaceActivityApplyResult(**workspace_activity_apply_result_model_dict)

        # Verify the model instances are equivalent
        assert workspace_activity_apply_result_model == workspace_activity_apply_result_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_activity_apply_result_model_json2 = workspace_activity_apply_result_model.to_dict()
        assert workspace_activity_apply_result_model_json2 == workspace_activity_apply_result_model_json

class TestWorkspaceActivityDestroyResult():
    """
    Test Class for WorkspaceActivityDestroyResult
    """

    def test_workspace_activity_destroy_result_serialization(self):
        """
        Test serialization/deserialization for WorkspaceActivityDestroyResult
        """

        # Construct a json representation of a WorkspaceActivityDestroyResult model
        workspace_activity_destroy_result_model_json = {}
        workspace_activity_destroy_result_model_json['activityid'] = 'testString'

        # Construct a model instance of WorkspaceActivityDestroyResult by calling from_dict on the json representation
        workspace_activity_destroy_result_model = WorkspaceActivityDestroyResult.from_dict(workspace_activity_destroy_result_model_json)
        assert workspace_activity_destroy_result_model != False

        # Construct a model instance of WorkspaceActivityDestroyResult by calling from_dict on the json representation
        workspace_activity_destroy_result_model_dict = WorkspaceActivityDestroyResult.from_dict(workspace_activity_destroy_result_model_json).__dict__
        workspace_activity_destroy_result_model2 = WorkspaceActivityDestroyResult(**workspace_activity_destroy_result_model_dict)

        # Verify the model instances are equivalent
        assert workspace_activity_destroy_result_model == workspace_activity_destroy_result_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_activity_destroy_result_model_json2 = workspace_activity_destroy_result_model.to_dict()
        assert workspace_activity_destroy_result_model_json2 == workspace_activity_destroy_result_model_json

class TestWorkspaceActivityLogs():
    """
    Test Class for WorkspaceActivityLogs
    """

    def test_workspace_activity_logs_serialization(self):
        """
        Test serialization/deserialization for WorkspaceActivityLogs
        """

        # Construct dict forms of any model objects needed in order to build this model.

        workspace_activity_template_logs_model = {} # WorkspaceActivityTemplateLogs
        workspace_activity_template_logs_model['log_url'] = 'testString'
        workspace_activity_template_logs_model['template_id'] = 'testString'
        workspace_activity_template_logs_model['template_type'] = 'testString'

        # Construct a json representation of a WorkspaceActivityLogs model
        workspace_activity_logs_model_json = {}
        workspace_activity_logs_model_json['action_id'] = 'testString'
        workspace_activity_logs_model_json['name'] = 'testString'
        workspace_activity_logs_model_json['templates'] = [workspace_activity_template_logs_model]

        # Construct a model instance of WorkspaceActivityLogs by calling from_dict on the json representation
        workspace_activity_logs_model = WorkspaceActivityLogs.from_dict(workspace_activity_logs_model_json)
        assert workspace_activity_logs_model != False

        # Construct a model instance of WorkspaceActivityLogs by calling from_dict on the json representation
        workspace_activity_logs_model_dict = WorkspaceActivityLogs.from_dict(workspace_activity_logs_model_json).__dict__
        workspace_activity_logs_model2 = WorkspaceActivityLogs(**workspace_activity_logs_model_dict)

        # Verify the model instances are equivalent
        assert workspace_activity_logs_model == workspace_activity_logs_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_activity_logs_model_json2 = workspace_activity_logs_model.to_dict()
        assert workspace_activity_logs_model_json2 == workspace_activity_logs_model_json

class TestWorkspaceActivityOptionsTemplate():
    """
    Test Class for WorkspaceActivityOptionsTemplate
    """

    def test_workspace_activity_options_template_serialization(self):
        """
        Test serialization/deserialization for WorkspaceActivityOptionsTemplate
        """

        # Construct a json representation of a WorkspaceActivityOptionsTemplate model
        workspace_activity_options_template_model_json = {}
        workspace_activity_options_template_model_json['target'] = ['testString']
        workspace_activity_options_template_model_json['tf_vars'] = ['testString']

        # Construct a model instance of WorkspaceActivityOptionsTemplate by calling from_dict on the json representation
        workspace_activity_options_template_model = WorkspaceActivityOptionsTemplate.from_dict(workspace_activity_options_template_model_json)
        assert workspace_activity_options_template_model != False

        # Construct a model instance of WorkspaceActivityOptionsTemplate by calling from_dict on the json representation
        workspace_activity_options_template_model_dict = WorkspaceActivityOptionsTemplate.from_dict(workspace_activity_options_template_model_json).__dict__
        workspace_activity_options_template_model2 = WorkspaceActivityOptionsTemplate(**workspace_activity_options_template_model_dict)

        # Verify the model instances are equivalent
        assert workspace_activity_options_template_model == workspace_activity_options_template_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_activity_options_template_model_json2 = workspace_activity_options_template_model.to_dict()
        assert workspace_activity_options_template_model_json2 == workspace_activity_options_template_model_json

class TestWorkspaceActivityPlanResult():
    """
    Test Class for WorkspaceActivityPlanResult
    """

    def test_workspace_activity_plan_result_serialization(self):
        """
        Test serialization/deserialization for WorkspaceActivityPlanResult
        """

        # Construct a json representation of a WorkspaceActivityPlanResult model
        workspace_activity_plan_result_model_json = {}
        workspace_activity_plan_result_model_json['activityid'] = 'testString'

        # Construct a model instance of WorkspaceActivityPlanResult by calling from_dict on the json representation
        workspace_activity_plan_result_model = WorkspaceActivityPlanResult.from_dict(workspace_activity_plan_result_model_json)
        assert workspace_activity_plan_result_model != False

        # Construct a model instance of WorkspaceActivityPlanResult by calling from_dict on the json representation
        workspace_activity_plan_result_model_dict = WorkspaceActivityPlanResult.from_dict(workspace_activity_plan_result_model_json).__dict__
        workspace_activity_plan_result_model2 = WorkspaceActivityPlanResult(**workspace_activity_plan_result_model_dict)

        # Verify the model instances are equivalent
        assert workspace_activity_plan_result_model == workspace_activity_plan_result_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_activity_plan_result_model_json2 = workspace_activity_plan_result_model.to_dict()
        assert workspace_activity_plan_result_model_json2 == workspace_activity_plan_result_model_json

class TestWorkspaceActivityRefreshResult():
    """
    Test Class for WorkspaceActivityRefreshResult
    """

    def test_workspace_activity_refresh_result_serialization(self):
        """
        Test serialization/deserialization for WorkspaceActivityRefreshResult
        """

        # Construct a json representation of a WorkspaceActivityRefreshResult model
        workspace_activity_refresh_result_model_json = {}
        workspace_activity_refresh_result_model_json['activityid'] = 'testString'

        # Construct a model instance of WorkspaceActivityRefreshResult by calling from_dict on the json representation
        workspace_activity_refresh_result_model = WorkspaceActivityRefreshResult.from_dict(workspace_activity_refresh_result_model_json)
        assert workspace_activity_refresh_result_model != False

        # Construct a model instance of WorkspaceActivityRefreshResult by calling from_dict on the json representation
        workspace_activity_refresh_result_model_dict = WorkspaceActivityRefreshResult.from_dict(workspace_activity_refresh_result_model_json).__dict__
        workspace_activity_refresh_result_model2 = WorkspaceActivityRefreshResult(**workspace_activity_refresh_result_model_dict)

        # Verify the model instances are equivalent
        assert workspace_activity_refresh_result_model == workspace_activity_refresh_result_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_activity_refresh_result_model_json2 = workspace_activity_refresh_result_model.to_dict()
        assert workspace_activity_refresh_result_model_json2 == workspace_activity_refresh_result_model_json

class TestWorkspaceActivityTemplate():
    """
    Test Class for WorkspaceActivityTemplate
    """

    def test_workspace_activity_template_serialization(self):
        """
        Test serialization/deserialization for WorkspaceActivityTemplate
        """

        # Construct dict forms of any model objects needed in order to build this model.

        log_summary_model = {} # LogSummary
        log_summary_model['activity_status'] = 'testString'
        log_summary_model['detected_template_type'] = 'testString'
        log_summary_model['discarded_files'] = 26
        log_summary_model['error'] = 'testString'
        log_summary_model['resources_added'] = 26
        log_summary_model['resources_destroyed'] = 26
        log_summary_model['resources_modified'] = 26
        log_summary_model['scanned_files'] = 26
        log_summary_model['template_variable_count'] = 26
        log_summary_model['time_taken'] = 72.5

        # Construct a json representation of a WorkspaceActivityTemplate model
        workspace_activity_template_model_json = {}
        workspace_activity_template_model_json['end_time'] = '2020-01-28T18:40:40.123456Z'
        workspace_activity_template_model_json['log_summary'] = log_summary_model
        workspace_activity_template_model_json['log_url'] = 'testString'
        workspace_activity_template_model_json['message'] = 'testString'
        workspace_activity_template_model_json['start_time'] = '2020-01-28T18:40:40.123456Z'
        workspace_activity_template_model_json['status'] = 'testString'
        workspace_activity_template_model_json['template_id'] = 'testString'
        workspace_activity_template_model_json['template_type'] = 'testString'

        # Construct a model instance of WorkspaceActivityTemplate by calling from_dict on the json representation
        workspace_activity_template_model = WorkspaceActivityTemplate.from_dict(workspace_activity_template_model_json)
        assert workspace_activity_template_model != False

        # Construct a model instance of WorkspaceActivityTemplate by calling from_dict on the json representation
        workspace_activity_template_model_dict = WorkspaceActivityTemplate.from_dict(workspace_activity_template_model_json).__dict__
        workspace_activity_template_model2 = WorkspaceActivityTemplate(**workspace_activity_template_model_dict)

        # Verify the model instances are equivalent
        assert workspace_activity_template_model == workspace_activity_template_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_activity_template_model_json2 = workspace_activity_template_model.to_dict()
        assert workspace_activity_template_model_json2 == workspace_activity_template_model_json

class TestWorkspaceActivityTemplateLogs():
    """
    Test Class for WorkspaceActivityTemplateLogs
    """

    def test_workspace_activity_template_logs_serialization(self):
        """
        Test serialization/deserialization for WorkspaceActivityTemplateLogs
        """

        # Construct a json representation of a WorkspaceActivityTemplateLogs model
        workspace_activity_template_logs_model_json = {}
        workspace_activity_template_logs_model_json['log_url'] = 'testString'
        workspace_activity_template_logs_model_json['template_id'] = 'testString'
        workspace_activity_template_logs_model_json['template_type'] = 'testString'

        # Construct a model instance of WorkspaceActivityTemplateLogs by calling from_dict on the json representation
        workspace_activity_template_logs_model = WorkspaceActivityTemplateLogs.from_dict(workspace_activity_template_logs_model_json)
        assert workspace_activity_template_logs_model != False

        # Construct a model instance of WorkspaceActivityTemplateLogs by calling from_dict on the json representation
        workspace_activity_template_logs_model_dict = WorkspaceActivityTemplateLogs.from_dict(workspace_activity_template_logs_model_json).__dict__
        workspace_activity_template_logs_model2 = WorkspaceActivityTemplateLogs(**workspace_activity_template_logs_model_dict)

        # Verify the model instances are equivalent
        assert workspace_activity_template_logs_model == workspace_activity_template_logs_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_activity_template_logs_model_json2 = workspace_activity_template_logs_model.to_dict()
        assert workspace_activity_template_logs_model_json2 == workspace_activity_template_logs_model_json

class TestWorkspaceBulkDeleteResponse():
    """
    Test Class for WorkspaceBulkDeleteResponse
    """

    def test_workspace_bulk_delete_response_serialization(self):
        """
        Test serialization/deserialization for WorkspaceBulkDeleteResponse
        """

        # Construct a json representation of a WorkspaceBulkDeleteResponse model
        workspace_bulk_delete_response_model_json = {}
        workspace_bulk_delete_response_model_json['job'] = 'testString'
        workspace_bulk_delete_response_model_json['job_id'] = 'testString'

        # Construct a model instance of WorkspaceBulkDeleteResponse by calling from_dict on the json representation
        workspace_bulk_delete_response_model = WorkspaceBulkDeleteResponse.from_dict(workspace_bulk_delete_response_model_json)
        assert workspace_bulk_delete_response_model != False

        # Construct a model instance of WorkspaceBulkDeleteResponse by calling from_dict on the json representation
        workspace_bulk_delete_response_model_dict = WorkspaceBulkDeleteResponse.from_dict(workspace_bulk_delete_response_model_json).__dict__
        workspace_bulk_delete_response_model2 = WorkspaceBulkDeleteResponse(**workspace_bulk_delete_response_model_dict)

        # Verify the model instances are equivalent
        assert workspace_bulk_delete_response_model == workspace_bulk_delete_response_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_bulk_delete_response_model_json2 = workspace_bulk_delete_response_model.to_dict()
        assert workspace_bulk_delete_response_model_json2 == workspace_bulk_delete_response_model_json

class TestWorkspaceJobResponse():
    """
    Test Class for WorkspaceJobResponse
    """

    def test_workspace_job_response_serialization(self):
        """
        Test serialization/deserialization for WorkspaceJobResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        job_status_type_model = {} # JobStatusType
        job_status_type_model['failed'] = ['testString']
        job_status_type_model['in_progress'] = ['testString']
        job_status_type_model['success'] = ['testString']
        job_status_type_model['last_updated_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a WorkspaceJobResponse model
        workspace_job_response_model_json = {}
        workspace_job_response_model_json['job_status'] = job_status_type_model

        # Construct a model instance of WorkspaceJobResponse by calling from_dict on the json representation
        workspace_job_response_model = WorkspaceJobResponse.from_dict(workspace_job_response_model_json)
        assert workspace_job_response_model != False

        # Construct a model instance of WorkspaceJobResponse by calling from_dict on the json representation
        workspace_job_response_model_dict = WorkspaceJobResponse.from_dict(workspace_job_response_model_json).__dict__
        workspace_job_response_model2 = WorkspaceJobResponse(**workspace_job_response_model_dict)

        # Verify the model instances are equivalent
        assert workspace_job_response_model == workspace_job_response_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_job_response_model_json2 = workspace_job_response_model.to_dict()
        assert workspace_job_response_model_json2 == workspace_job_response_model_json

class TestWorkspaceResponse():
    """
    Test Class for WorkspaceResponse
    """

    def test_workspace_response_serialization(self):
        """
        Test serialization/deserialization for WorkspaceResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        catalog_ref_model = {} # CatalogRef
        catalog_ref_model['dry_run'] = True
        catalog_ref_model['item_icon_url'] = 'testString'
        catalog_ref_model['item_id'] = 'testString'
        catalog_ref_model['item_name'] = 'testString'
        catalog_ref_model['item_readme_url'] = 'testString'
        catalog_ref_model['item_url'] = 'testString'
        catalog_ref_model['launch_url'] = 'testString'
        catalog_ref_model['offering_version'] = 'testString'

        template_run_time_data_response_model = {} # TemplateRunTimeDataResponse
        template_run_time_data_response_model['engine_cmd'] = 'testString'
        template_run_time_data_response_model['engine_name'] = 'testString'
        template_run_time_data_response_model['engine_version'] = 'testString'
        template_run_time_data_response_model['id'] = 'testString'
        template_run_time_data_response_model['log_store_url'] = 'testString'
        template_run_time_data_response_model['output_values'] = [{ 'foo': 'bar' }]
        template_run_time_data_response_model['resources'] = [[{ 'foo': 'bar' }]]
        template_run_time_data_response_model['state_store_url'] = 'testString'

        shared_target_data_response_model = {} # SharedTargetDataResponse
        shared_target_data_response_model['cluster_id'] = 'testString'
        shared_target_data_response_model['cluster_name'] = 'testString'
        shared_target_data_response_model['entitlement_keys'] = [{ 'foo': 'bar' }]
        shared_target_data_response_model['namespace'] = 'testString'
        shared_target_data_response_model['region'] = 'testString'
        shared_target_data_response_model['resource_group_id'] = 'testString'

        env_variable_response_model = {} # EnvVariableResponse
        env_variable_response_model['hidden'] = True
        env_variable_response_model['name'] = 'testString'
        env_variable_response_model['secure'] = True
        env_variable_response_model['value'] = 'testString'

        workspace_variable_response_model = {} # WorkspaceVariableResponse
        workspace_variable_response_model['description'] = 'testString'
        workspace_variable_response_model['name'] = 'testString'
        workspace_variable_response_model['secure'] = True
        workspace_variable_response_model['type'] = 'testString'
        workspace_variable_response_model['value'] = 'testString'

        template_source_data_response_model = {} # TemplateSourceDataResponse
        template_source_data_response_model['env_values'] = [env_variable_response_model]
        template_source_data_response_model['folder'] = 'testString'
        template_source_data_response_model['has_githubtoken'] = True
        template_source_data_response_model['id'] = 'testString'
        template_source_data_response_model['template_type'] = 'testString'
        template_source_data_response_model['uninstall_script_name'] = 'testString'
        template_source_data_response_model['values'] = 'testString'
        template_source_data_response_model['values_metadata'] = [{ 'foo': 'bar' }]
        template_source_data_response_model['values_url'] = 'testString'
        template_source_data_response_model['variablestore'] = [workspace_variable_response_model]

        template_repo_response_model = {} # TemplateRepoResponse
        template_repo_response_model['branch'] = 'testString'
        template_repo_response_model['full_url'] = 'testString'
        template_repo_response_model['has_uploadedgitrepotar'] = True
        template_repo_response_model['release'] = 'testString'
        template_repo_response_model['repo_sha_value'] = 'testString'
        template_repo_response_model['repo_url'] = 'testString'
        template_repo_response_model['url'] = 'testString'

        workspace_status_response_model = {} # WorkspaceStatusResponse
        workspace_status_response_model['frozen'] = True
        workspace_status_response_model['frozen_at'] = '2020-01-28T18:40:40.123456Z'
        workspace_status_response_model['frozen_by'] = 'testString'
        workspace_status_response_model['locked'] = True
        workspace_status_response_model['locked_by'] = 'testString'
        workspace_status_response_model['locked_time'] = '2020-01-28T18:40:40.123456Z'

        workspace_status_message_model = {} # WorkspaceStatusMessage
        workspace_status_message_model['status_code'] = 'testString'
        workspace_status_message_model['status_msg'] = 'testString'

        # Construct a json representation of a WorkspaceResponse model
        workspace_response_model_json = {}
        workspace_response_model_json['applied_shareddata_ids'] = ['testString']
        workspace_response_model_json['catalog_ref'] = catalog_ref_model
        workspace_response_model_json['created_at'] = '2020-01-28T18:40:40.123456Z'
        workspace_response_model_json['created_by'] = 'testString'
        workspace_response_model_json['crn'] = 'testString'
        workspace_response_model_json['description'] = 'testString'
        workspace_response_model_json['id'] = 'testString'
        workspace_response_model_json['last_health_check_at'] = '2020-01-28T18:40:40.123456Z'
        workspace_response_model_json['location'] = 'testString'
        workspace_response_model_json['name'] = 'testString'
        workspace_response_model_json['resource_group'] = 'testString'
        workspace_response_model_json['runtime_data'] = [template_run_time_data_response_model]
        workspace_response_model_json['shared_data'] = shared_target_data_response_model
        workspace_response_model_json['status'] = 'testString'
        workspace_response_model_json['tags'] = ['testString']
        workspace_response_model_json['template_data'] = [template_source_data_response_model]
        workspace_response_model_json['template_ref'] = 'testString'
        workspace_response_model_json['template_repo'] = template_repo_response_model
        workspace_response_model_json['type'] = ['testString']
        workspace_response_model_json['updated_at'] = '2020-01-28T18:40:40.123456Z'
        workspace_response_model_json['updated_by'] = 'testString'
        workspace_response_model_json['workspace_status'] = workspace_status_response_model
        workspace_response_model_json['workspace_status_msg'] = workspace_status_message_model

        # Construct a model instance of WorkspaceResponse by calling from_dict on the json representation
        workspace_response_model = WorkspaceResponse.from_dict(workspace_response_model_json)
        assert workspace_response_model != False

        # Construct a model instance of WorkspaceResponse by calling from_dict on the json representation
        workspace_response_model_dict = WorkspaceResponse.from_dict(workspace_response_model_json).__dict__
        workspace_response_model2 = WorkspaceResponse(**workspace_response_model_dict)

        # Verify the model instances are equivalent
        assert workspace_response_model == workspace_response_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_response_model_json2 = workspace_response_model.to_dict()
        assert workspace_response_model_json2 == workspace_response_model_json

class TestWorkspaceResponseList():
    """
    Test Class for WorkspaceResponseList
    """

    def test_workspace_response_list_serialization(self):
        """
        Test serialization/deserialization for WorkspaceResponseList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        catalog_ref_model = {} # CatalogRef
        catalog_ref_model['dry_run'] = True
        catalog_ref_model['item_icon_url'] = 'testString'
        catalog_ref_model['item_id'] = 'testString'
        catalog_ref_model['item_name'] = 'testString'
        catalog_ref_model['item_readme_url'] = 'testString'
        catalog_ref_model['item_url'] = 'testString'
        catalog_ref_model['launch_url'] = 'testString'
        catalog_ref_model['offering_version'] = 'testString'

        template_run_time_data_response_model = {} # TemplateRunTimeDataResponse
        template_run_time_data_response_model['engine_cmd'] = 'testString'
        template_run_time_data_response_model['engine_name'] = 'testString'
        template_run_time_data_response_model['engine_version'] = 'testString'
        template_run_time_data_response_model['id'] = 'testString'
        template_run_time_data_response_model['log_store_url'] = 'testString'
        template_run_time_data_response_model['output_values'] = [{ 'foo': 'bar' }]
        template_run_time_data_response_model['resources'] = [[{ 'foo': 'bar' }]]
        template_run_time_data_response_model['state_store_url'] = 'testString'

        shared_target_data_response_model = {} # SharedTargetDataResponse
        shared_target_data_response_model['cluster_id'] = 'testString'
        shared_target_data_response_model['cluster_name'] = 'testString'
        shared_target_data_response_model['entitlement_keys'] = [{ 'foo': 'bar' }]
        shared_target_data_response_model['namespace'] = 'testString'
        shared_target_data_response_model['region'] = 'testString'
        shared_target_data_response_model['resource_group_id'] = 'testString'

        env_variable_response_model = {} # EnvVariableResponse
        env_variable_response_model['hidden'] = True
        env_variable_response_model['name'] = 'testString'
        env_variable_response_model['secure'] = True
        env_variable_response_model['value'] = 'testString'

        workspace_variable_response_model = {} # WorkspaceVariableResponse
        workspace_variable_response_model['description'] = 'testString'
        workspace_variable_response_model['name'] = 'testString'
        workspace_variable_response_model['secure'] = True
        workspace_variable_response_model['type'] = 'testString'
        workspace_variable_response_model['value'] = 'testString'

        template_source_data_response_model = {} # TemplateSourceDataResponse
        template_source_data_response_model['env_values'] = [env_variable_response_model]
        template_source_data_response_model['folder'] = 'testString'
        template_source_data_response_model['has_githubtoken'] = True
        template_source_data_response_model['id'] = 'testString'
        template_source_data_response_model['template_type'] = 'testString'
        template_source_data_response_model['uninstall_script_name'] = 'testString'
        template_source_data_response_model['values'] = 'testString'
        template_source_data_response_model['values_metadata'] = [{ 'foo': 'bar' }]
        template_source_data_response_model['values_url'] = 'testString'
        template_source_data_response_model['variablestore'] = [workspace_variable_response_model]

        template_repo_response_model = {} # TemplateRepoResponse
        template_repo_response_model['branch'] = 'testString'
        template_repo_response_model['full_url'] = 'testString'
        template_repo_response_model['has_uploadedgitrepotar'] = True
        template_repo_response_model['release'] = 'testString'
        template_repo_response_model['repo_sha_value'] = 'testString'
        template_repo_response_model['repo_url'] = 'testString'
        template_repo_response_model['url'] = 'testString'

        workspace_status_response_model = {} # WorkspaceStatusResponse
        workspace_status_response_model['frozen'] = True
        workspace_status_response_model['frozen_at'] = '2020-01-28T18:40:40.123456Z'
        workspace_status_response_model['frozen_by'] = 'testString'
        workspace_status_response_model['locked'] = True
        workspace_status_response_model['locked_by'] = 'testString'
        workspace_status_response_model['locked_time'] = '2020-01-28T18:40:40.123456Z'

        workspace_status_message_model = {} # WorkspaceStatusMessage
        workspace_status_message_model['status_code'] = 'testString'
        workspace_status_message_model['status_msg'] = 'testString'

        workspace_response_model = {} # WorkspaceResponse
        workspace_response_model['applied_shareddata_ids'] = ['testString']
        workspace_response_model['catalog_ref'] = catalog_ref_model
        workspace_response_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        workspace_response_model['created_by'] = 'testString'
        workspace_response_model['crn'] = 'testString'
        workspace_response_model['description'] = 'testString'
        workspace_response_model['id'] = 'testString'
        workspace_response_model['last_health_check_at'] = '2020-01-28T18:40:40.123456Z'
        workspace_response_model['location'] = 'testString'
        workspace_response_model['name'] = 'testString'
        workspace_response_model['resource_group'] = 'testString'
        workspace_response_model['runtime_data'] = [template_run_time_data_response_model]
        workspace_response_model['shared_data'] = shared_target_data_response_model
        workspace_response_model['status'] = 'testString'
        workspace_response_model['tags'] = ['testString']
        workspace_response_model['template_data'] = [template_source_data_response_model]
        workspace_response_model['template_ref'] = 'testString'
        workspace_response_model['template_repo'] = template_repo_response_model
        workspace_response_model['type'] = ['testString']
        workspace_response_model['updated_at'] = '2020-01-28T18:40:40.123456Z'
        workspace_response_model['updated_by'] = 'testString'
        workspace_response_model['workspace_status'] = workspace_status_response_model
        workspace_response_model['workspace_status_msg'] = workspace_status_message_model

        # Construct a json representation of a WorkspaceResponseList model
        workspace_response_list_model_json = {}
        workspace_response_list_model_json['count'] = 26
        workspace_response_list_model_json['limit'] = 26
        workspace_response_list_model_json['offset'] = 26
        workspace_response_list_model_json['workspaces'] = [workspace_response_model]

        # Construct a model instance of WorkspaceResponseList by calling from_dict on the json representation
        workspace_response_list_model = WorkspaceResponseList.from_dict(workspace_response_list_model_json)
        assert workspace_response_list_model != False

        # Construct a model instance of WorkspaceResponseList by calling from_dict on the json representation
        workspace_response_list_model_dict = WorkspaceResponseList.from_dict(workspace_response_list_model_json).__dict__
        workspace_response_list_model2 = WorkspaceResponseList(**workspace_response_list_model_dict)

        # Verify the model instances are equivalent
        assert workspace_response_list_model == workspace_response_list_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_response_list_model_json2 = workspace_response_list_model.to_dict()
        assert workspace_response_list_model_json2 == workspace_response_list_model_json

class TestWorkspaceStatusMessage():
    """
    Test Class for WorkspaceStatusMessage
    """

    def test_workspace_status_message_serialization(self):
        """
        Test serialization/deserialization for WorkspaceStatusMessage
        """

        # Construct a json representation of a WorkspaceStatusMessage model
        workspace_status_message_model_json = {}
        workspace_status_message_model_json['status_code'] = 'testString'
        workspace_status_message_model_json['status_msg'] = 'testString'

        # Construct a model instance of WorkspaceStatusMessage by calling from_dict on the json representation
        workspace_status_message_model = WorkspaceStatusMessage.from_dict(workspace_status_message_model_json)
        assert workspace_status_message_model != False

        # Construct a model instance of WorkspaceStatusMessage by calling from_dict on the json representation
        workspace_status_message_model_dict = WorkspaceStatusMessage.from_dict(workspace_status_message_model_json).__dict__
        workspace_status_message_model2 = WorkspaceStatusMessage(**workspace_status_message_model_dict)

        # Verify the model instances are equivalent
        assert workspace_status_message_model == workspace_status_message_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_status_message_model_json2 = workspace_status_message_model.to_dict()
        assert workspace_status_message_model_json2 == workspace_status_message_model_json

class TestWorkspaceStatusRequest():
    """
    Test Class for WorkspaceStatusRequest
    """

    def test_workspace_status_request_serialization(self):
        """
        Test serialization/deserialization for WorkspaceStatusRequest
        """

        # Construct a json representation of a WorkspaceStatusRequest model
        workspace_status_request_model_json = {}
        workspace_status_request_model_json['frozen'] = True
        workspace_status_request_model_json['frozen_at'] = '2020-01-28T18:40:40.123456Z'
        workspace_status_request_model_json['frozen_by'] = 'testString'
        workspace_status_request_model_json['locked'] = True
        workspace_status_request_model_json['locked_by'] = 'testString'
        workspace_status_request_model_json['locked_time'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of WorkspaceStatusRequest by calling from_dict on the json representation
        workspace_status_request_model = WorkspaceStatusRequest.from_dict(workspace_status_request_model_json)
        assert workspace_status_request_model != False

        # Construct a model instance of WorkspaceStatusRequest by calling from_dict on the json representation
        workspace_status_request_model_dict = WorkspaceStatusRequest.from_dict(workspace_status_request_model_json).__dict__
        workspace_status_request_model2 = WorkspaceStatusRequest(**workspace_status_request_model_dict)

        # Verify the model instances are equivalent
        assert workspace_status_request_model == workspace_status_request_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_status_request_model_json2 = workspace_status_request_model.to_dict()
        assert workspace_status_request_model_json2 == workspace_status_request_model_json

class TestWorkspaceStatusResponse():
    """
    Test Class for WorkspaceStatusResponse
    """

    def test_workspace_status_response_serialization(self):
        """
        Test serialization/deserialization for WorkspaceStatusResponse
        """

        # Construct a json representation of a WorkspaceStatusResponse model
        workspace_status_response_model_json = {}
        workspace_status_response_model_json['frozen'] = True
        workspace_status_response_model_json['frozen_at'] = '2020-01-28T18:40:40.123456Z'
        workspace_status_response_model_json['frozen_by'] = 'testString'
        workspace_status_response_model_json['locked'] = True
        workspace_status_response_model_json['locked_by'] = 'testString'
        workspace_status_response_model_json['locked_time'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of WorkspaceStatusResponse by calling from_dict on the json representation
        workspace_status_response_model = WorkspaceStatusResponse.from_dict(workspace_status_response_model_json)
        assert workspace_status_response_model != False

        # Construct a model instance of WorkspaceStatusResponse by calling from_dict on the json representation
        workspace_status_response_model_dict = WorkspaceStatusResponse.from_dict(workspace_status_response_model_json).__dict__
        workspace_status_response_model2 = WorkspaceStatusResponse(**workspace_status_response_model_dict)

        # Verify the model instances are equivalent
        assert workspace_status_response_model == workspace_status_response_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_status_response_model_json2 = workspace_status_response_model.to_dict()
        assert workspace_status_response_model_json2 == workspace_status_response_model_json

class TestWorkspaceStatusUpdateRequest():
    """
    Test Class for WorkspaceStatusUpdateRequest
    """

    def test_workspace_status_update_request_serialization(self):
        """
        Test serialization/deserialization for WorkspaceStatusUpdateRequest
        """

        # Construct a json representation of a WorkspaceStatusUpdateRequest model
        workspace_status_update_request_model_json = {}
        workspace_status_update_request_model_json['frozen'] = True
        workspace_status_update_request_model_json['frozen_at'] = '2020-01-28T18:40:40.123456Z'
        workspace_status_update_request_model_json['frozen_by'] = 'testString'
        workspace_status_update_request_model_json['locked'] = True
        workspace_status_update_request_model_json['locked_by'] = 'testString'
        workspace_status_update_request_model_json['locked_time'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of WorkspaceStatusUpdateRequest by calling from_dict on the json representation
        workspace_status_update_request_model = WorkspaceStatusUpdateRequest.from_dict(workspace_status_update_request_model_json)
        assert workspace_status_update_request_model != False

        # Construct a model instance of WorkspaceStatusUpdateRequest by calling from_dict on the json representation
        workspace_status_update_request_model_dict = WorkspaceStatusUpdateRequest.from_dict(workspace_status_update_request_model_json).__dict__
        workspace_status_update_request_model2 = WorkspaceStatusUpdateRequest(**workspace_status_update_request_model_dict)

        # Verify the model instances are equivalent
        assert workspace_status_update_request_model == workspace_status_update_request_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_status_update_request_model_json2 = workspace_status_update_request_model.to_dict()
        assert workspace_status_update_request_model_json2 == workspace_status_update_request_model_json

class TestWorkspaceTemplateValuesResponse():
    """
    Test Class for WorkspaceTemplateValuesResponse
    """

    def test_workspace_template_values_response_serialization(self):
        """
        Test serialization/deserialization for WorkspaceTemplateValuesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        template_run_time_data_response_model = {} # TemplateRunTimeDataResponse
        template_run_time_data_response_model['engine_cmd'] = 'testString'
        template_run_time_data_response_model['engine_name'] = 'testString'
        template_run_time_data_response_model['engine_version'] = 'testString'
        template_run_time_data_response_model['id'] = 'testString'
        template_run_time_data_response_model['log_store_url'] = 'testString'
        template_run_time_data_response_model['output_values'] = [{ 'foo': 'bar' }]
        template_run_time_data_response_model['resources'] = [[{ 'foo': 'bar' }]]
        template_run_time_data_response_model['state_store_url'] = 'testString'

        shared_target_data_model = {} # SharedTargetData
        shared_target_data_model['cluster_created_on'] = 'testString'
        shared_target_data_model['cluster_id'] = 'testString'
        shared_target_data_model['cluster_name'] = 'testString'
        shared_target_data_model['cluster_type'] = 'testString'
        shared_target_data_model['entitlement_keys'] = [{ 'foo': 'bar' }]
        shared_target_data_model['namespace'] = 'testString'
        shared_target_data_model['region'] = 'testString'
        shared_target_data_model['resource_group_id'] = 'testString'
        shared_target_data_model['worker_count'] = 26
        shared_target_data_model['worker_machine_type'] = 'testString'

        env_variable_response_model = {} # EnvVariableResponse
        env_variable_response_model['hidden'] = True
        env_variable_response_model['name'] = 'testString'
        env_variable_response_model['secure'] = True
        env_variable_response_model['value'] = 'testString'

        workspace_variable_response_model = {} # WorkspaceVariableResponse
        workspace_variable_response_model['description'] = 'testString'
        workspace_variable_response_model['name'] = 'testString'
        workspace_variable_response_model['secure'] = True
        workspace_variable_response_model['type'] = 'testString'
        workspace_variable_response_model['value'] = 'testString'

        template_source_data_response_model = {} # TemplateSourceDataResponse
        template_source_data_response_model['env_values'] = [env_variable_response_model]
        template_source_data_response_model['folder'] = 'testString'
        template_source_data_response_model['has_githubtoken'] = True
        template_source_data_response_model['id'] = 'testString'
        template_source_data_response_model['template_type'] = 'testString'
        template_source_data_response_model['uninstall_script_name'] = 'testString'
        template_source_data_response_model['values'] = 'testString'
        template_source_data_response_model['values_metadata'] = [{ 'foo': 'bar' }]
        template_source_data_response_model['values_url'] = 'testString'
        template_source_data_response_model['variablestore'] = [workspace_variable_response_model]

        # Construct a json representation of a WorkspaceTemplateValuesResponse model
        workspace_template_values_response_model_json = {}
        workspace_template_values_response_model_json['runtime_data'] = [template_run_time_data_response_model]
        workspace_template_values_response_model_json['shared_data'] = shared_target_data_model
        workspace_template_values_response_model_json['template_data'] = [template_source_data_response_model]

        # Construct a model instance of WorkspaceTemplateValuesResponse by calling from_dict on the json representation
        workspace_template_values_response_model = WorkspaceTemplateValuesResponse.from_dict(workspace_template_values_response_model_json)
        assert workspace_template_values_response_model != False

        # Construct a model instance of WorkspaceTemplateValuesResponse by calling from_dict on the json representation
        workspace_template_values_response_model_dict = WorkspaceTemplateValuesResponse.from_dict(workspace_template_values_response_model_json).__dict__
        workspace_template_values_response_model2 = WorkspaceTemplateValuesResponse(**workspace_template_values_response_model_dict)

        # Verify the model instances are equivalent
        assert workspace_template_values_response_model == workspace_template_values_response_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_template_values_response_model_json2 = workspace_template_values_response_model.to_dict()
        assert workspace_template_values_response_model_json2 == workspace_template_values_response_model_json

class TestWorkspaceVariableRequest():
    """
    Test Class for WorkspaceVariableRequest
    """

    def test_workspace_variable_request_serialization(self):
        """
        Test serialization/deserialization for WorkspaceVariableRequest
        """

        # Construct a json representation of a WorkspaceVariableRequest model
        workspace_variable_request_model_json = {}
        workspace_variable_request_model_json['description'] = 'testString'
        workspace_variable_request_model_json['name'] = 'testString'
        workspace_variable_request_model_json['secure'] = True
        workspace_variable_request_model_json['type'] = 'testString'
        workspace_variable_request_model_json['use_default'] = True
        workspace_variable_request_model_json['value'] = 'testString'

        # Construct a model instance of WorkspaceVariableRequest by calling from_dict on the json representation
        workspace_variable_request_model = WorkspaceVariableRequest.from_dict(workspace_variable_request_model_json)
        assert workspace_variable_request_model != False

        # Construct a model instance of WorkspaceVariableRequest by calling from_dict on the json representation
        workspace_variable_request_model_dict = WorkspaceVariableRequest.from_dict(workspace_variable_request_model_json).__dict__
        workspace_variable_request_model2 = WorkspaceVariableRequest(**workspace_variable_request_model_dict)

        # Verify the model instances are equivalent
        assert workspace_variable_request_model == workspace_variable_request_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_variable_request_model_json2 = workspace_variable_request_model.to_dict()
        assert workspace_variable_request_model_json2 == workspace_variable_request_model_json

class TestWorkspaceVariableResponse():
    """
    Test Class for WorkspaceVariableResponse
    """

    def test_workspace_variable_response_serialization(self):
        """
        Test serialization/deserialization for WorkspaceVariableResponse
        """

        # Construct a json representation of a WorkspaceVariableResponse model
        workspace_variable_response_model_json = {}
        workspace_variable_response_model_json['description'] = 'testString'
        workspace_variable_response_model_json['name'] = 'testString'
        workspace_variable_response_model_json['secure'] = True
        workspace_variable_response_model_json['type'] = 'testString'
        workspace_variable_response_model_json['value'] = 'testString'

        # Construct a model instance of WorkspaceVariableResponse by calling from_dict on the json representation
        workspace_variable_response_model = WorkspaceVariableResponse.from_dict(workspace_variable_response_model_json)
        assert workspace_variable_response_model != False

        # Construct a model instance of WorkspaceVariableResponse by calling from_dict on the json representation
        workspace_variable_response_model_dict = WorkspaceVariableResponse.from_dict(workspace_variable_response_model_json).__dict__
        workspace_variable_response_model2 = WorkspaceVariableResponse(**workspace_variable_response_model_dict)

        # Verify the model instances are equivalent
        assert workspace_variable_response_model == workspace_variable_response_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_variable_response_model_json2 = workspace_variable_response_model.to_dict()
        assert workspace_variable_response_model_json2 == workspace_variable_response_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
