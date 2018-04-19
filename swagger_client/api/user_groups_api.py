# coding: utf-8

"""
    \"Data Governance Center: REST API v2\"

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UserGroupsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def resource_user_group_resource_add_user_group_post(self, **kwargs):  # noqa: E501
        """Adds new user group.  # noqa: E501

        Adds new user group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_user_group_resource_add_user_group_post(async=True)
        >>> result = thread.get()

        :param async bool
        :param JsonAddUserGroupRequest body: the properties of the user group to be added
        :return: JsonUserGroupImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_user_group_resource_add_user_group_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_user_group_resource_add_user_group_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_user_group_resource_add_user_group_post_with_http_info(self, **kwargs):  # noqa: E501
        """Adds new user group.  # noqa: E501

        Adds new user group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_user_group_resource_add_user_group_post_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param JsonAddUserGroupRequest body: the properties of the user group to be added
        :return: JsonUserGroupImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_user_group_resource_add_user_group_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/userGroups', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonUserGroupImpl',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_user_group_resource_add_user_to_user_group_post(self, user_group_id, **kwargs):  # noqa: E501
        """Adds users to existing user group.  # noqa: E501

        Adds users to existing user group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_user_group_resource_add_user_to_user_group_post(user_group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_group_id:  (required)
        :param JsonAddUsersToUserGroupRequest body: the properties needed to add users to given user group
        :return: list[JsonUserImpl]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_user_group_resource_add_user_to_user_group_post_with_http_info(user_group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.resource_user_group_resource_add_user_to_user_group_post_with_http_info(user_group_id, **kwargs)  # noqa: E501
            return data

    def resource_user_group_resource_add_user_to_user_group_post_with_http_info(self, user_group_id, **kwargs):  # noqa: E501
        """Adds users to existing user group.  # noqa: E501

        Adds users to existing user group.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_user_group_resource_add_user_to_user_group_post_with_http_info(user_group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_group_id:  (required)
        :param JsonAddUsersToUserGroupRequest body: the properties needed to add users to given user group
        :return: list[JsonUserImpl]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_group_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_user_group_resource_add_user_to_user_group_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_group_id' is set
        if ('user_group_id' not in params or
                params['user_group_id'] is None):
            raise ValueError("Missing the required parameter `user_group_id` when calling `resource_user_group_resource_add_user_to_user_group_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_group_id' in params:
            path_params['userGroupId'] = params['user_group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/userGroups/{userGroupId}/users', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[JsonUserImpl]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_user_group_resource_change_user_group_patch(self, user_group_id, **kwargs):  # noqa: E501
        """Changes the user group with the information that is present in the request.  # noqa: E501

        Changes the user group with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_user_group_resource_change_user_group_patch(user_group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_group_id: the <code>id</code> of the user group to be changed (required)
        :param JsonChangeUserGroupRequest body: the properties of the user group to be changed
        :return: JsonUserGroupImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_user_group_resource_change_user_group_patch_with_http_info(user_group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.resource_user_group_resource_change_user_group_patch_with_http_info(user_group_id, **kwargs)  # noqa: E501
            return data

    def resource_user_group_resource_change_user_group_patch_with_http_info(self, user_group_id, **kwargs):  # noqa: E501
        """Changes the user group with the information that is present in the request.  # noqa: E501

        Changes the user group with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_user_group_resource_change_user_group_patch_with_http_info(user_group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_group_id: the <code>id</code> of the user group to be changed (required)
        :param JsonChangeUserGroupRequest body: the properties of the user group to be changed
        :return: JsonUserGroupImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_group_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_user_group_resource_change_user_group_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_group_id' is set
        if ('user_group_id' not in params or
                params['user_group_id'] is None):
            raise ValueError("Missing the required parameter `user_group_id` when calling `resource_user_group_resource_change_user_group_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_group_id' in params:
            path_params['userGroupId'] = params['user_group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/userGroups/{userGroupId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonUserGroupImpl',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_user_group_resource_find_user_groups_get(self, **kwargs):  # noqa: E501
        """Returns user groups matching the given search criteria.  # noqa: E501

        Returns user groups matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned user groups satisfy all constraints that are specified in this search criteria. By default a result containing 1000 user groups is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_user_group_resource_find_user_groups_get(async=True)
        >>> result = thread.get()

        :param async bool
        :param bool include_everyone: 
        :param int limit: The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used
        :param str name: The name of the user group
        :param str name_match_mode: The match mode used to compare <code>name</code>.
        :param int offset: The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>
        :param str user_id: The <code>id</code> of the user who should belong to searched user groups
        :return: JsonUserGroupImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_user_group_resource_find_user_groups_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_user_group_resource_find_user_groups_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_user_group_resource_find_user_groups_get_with_http_info(self, **kwargs):  # noqa: E501
        """Returns user groups matching the given search criteria.  # noqa: E501

        Returns user groups matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned user groups satisfy all constraints that are specified in this search criteria. By default a result containing 1000 user groups is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_user_group_resource_find_user_groups_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param bool include_everyone: 
        :param int limit: The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used
        :param str name: The name of the user group
        :param str name_match_mode: The match mode used to compare <code>name</code>.
        :param int offset: The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>
        :param str user_id: The <code>id</code> of the user who should belong to searched user groups
        :return: JsonUserGroupImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['include_everyone', 'limit', 'name', 'name_match_mode', 'offset', 'user_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_user_group_resource_find_user_groups_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'include_everyone' in params:
            query_params.append(('includeEveryone', params['include_everyone']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'name_match_mode' in params:
            query_params.append(('nameMatchMode', params['name_match_mode']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'user_id' in params:
            query_params.append(('userId', params['user_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/userGroups', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonUserGroupImpl',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_user_group_resource_get_user_group_get(self, user_group_id, **kwargs):  # noqa: E501
        """Returns user group identified by given id.  # noqa: E501

        Returns user group identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_user_group_resource_get_user_group_get(user_group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_group_id: the <code>id</code> of the user group (required)
        :return: JsonUserGroupImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_user_group_resource_get_user_group_get_with_http_info(user_group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.resource_user_group_resource_get_user_group_get_with_http_info(user_group_id, **kwargs)  # noqa: E501
            return data

    def resource_user_group_resource_get_user_group_get_with_http_info(self, user_group_id, **kwargs):  # noqa: E501
        """Returns user group identified by given id.  # noqa: E501

        Returns user group identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_user_group_resource_get_user_group_get_with_http_info(user_group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_group_id: the <code>id</code> of the user group (required)
        :return: JsonUserGroupImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_group_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_user_group_resource_get_user_group_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_group_id' is set
        if ('user_group_id' not in params or
                params['user_group_id'] is None):
            raise ValueError("Missing the required parameter `user_group_id` when calling `resource_user_group_resource_get_user_group_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_group_id' in params:
            path_params['userGroupId'] = params['user_group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/userGroups/{userGroupId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonUserGroupImpl',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_user_group_resource_remove_user_group_delete(self, user_group_id, **kwargs):  # noqa: E501
        """Removes user group identified by given id.  # noqa: E501

        Removes user group identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_user_group_resource_remove_user_group_delete(user_group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_group_id: the <code>id</code> of the user group to remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_user_group_resource_remove_user_group_delete_with_http_info(user_group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.resource_user_group_resource_remove_user_group_delete_with_http_info(user_group_id, **kwargs)  # noqa: E501
            return data

    def resource_user_group_resource_remove_user_group_delete_with_http_info(self, user_group_id, **kwargs):  # noqa: E501
        """Removes user group identified by given id.  # noqa: E501

        Removes user group identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_user_group_resource_remove_user_group_delete_with_http_info(user_group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_group_id: the <code>id</code> of the user group to remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_group_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_user_group_resource_remove_user_group_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_group_id' is set
        if ('user_group_id' not in params or
                params['user_group_id'] is None):
            raise ValueError("Missing the required parameter `user_group_id` when calling `resource_user_group_resource_remove_user_group_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_group_id' in params:
            path_params['userGroupId'] = params['user_group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/userGroups/{userGroupId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_user_group_resource_remove_users_from_user_group_delete(self, user_group_id, **kwargs):  # noqa: E501
        """Removes users from the user group identified by given id.  # noqa: E501

        Removes users from the user group identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_user_group_resource_remove_users_from_user_group_delete(user_group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_group_id: the <code>id</code> of the user group (required)
        :param JsonRemoveUsersFromUserGroupRequest body: the properties needed to remove the users from given user group
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_user_group_resource_remove_users_from_user_group_delete_with_http_info(user_group_id, **kwargs)  # noqa: E501
        else:
            (data) = self.resource_user_group_resource_remove_users_from_user_group_delete_with_http_info(user_group_id, **kwargs)  # noqa: E501
            return data

    def resource_user_group_resource_remove_users_from_user_group_delete_with_http_info(self, user_group_id, **kwargs):  # noqa: E501
        """Removes users from the user group identified by given id.  # noqa: E501

        Removes users from the user group identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_user_group_resource_remove_users_from_user_group_delete_with_http_info(user_group_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str user_group_id: the <code>id</code> of the user group (required)
        :param JsonRemoveUsersFromUserGroupRequest body: the properties needed to remove the users from given user group
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_group_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_user_group_resource_remove_users_from_user_group_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_group_id' is set
        if ('user_group_id' not in params or
                params['user_group_id'] is None):
            raise ValueError("Missing the required parameter `user_group_id` when calling `resource_user_group_resource_remove_users_from_user_group_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'user_group_id' in params:
            path_params['userGroupId'] = params['user_group_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/userGroups/{userGroupId}/users', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)