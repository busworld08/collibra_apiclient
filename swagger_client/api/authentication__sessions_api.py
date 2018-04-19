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


class AuthenticationSessionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def resource_session_resource_is_logged_in_get(self, **kwargs):  # noqa: E501
        """Gets current session (checks if user is logged in).  # noqa: E501

        Gets current session (checks if user is logged in). Returns <code>401</code> if the user is not authenticated and session does not exist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_session_resource_is_logged_in_get(async=True)
        >>> result = thread.get()

        :param async bool
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_session_resource_is_logged_in_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_session_resource_is_logged_in_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_session_resource_is_logged_in_get_with_http_info(self, **kwargs):  # noqa: E501
        """Gets current session (checks if user is logged in).  # noqa: E501

        Gets current session (checks if user is logged in). Returns <code>401</code> if the user is not authenticated and session does not exist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_session_resource_is_logged_in_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_session_resource_is_logged_in_get" % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth/sessions/current', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_session_resource_login_post(self, **kwargs):  # noqa: E501
        """Login.  # noqa: E501

        Login. Authenticates a user and creates a new session on the server. Once the user is authenticated then the returned session id can be used to access DGC REST Api in subsequent requests. The method additionally returns the JSESSIONID cookie in a <code>Set-Cookie</code> header. If user already has an open session then this session will be terminated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_session_resource_login_post(async=True)
        >>> result = thread.get()

        :param async bool
        :param JsonLoginRequest body: 
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_session_resource_login_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_session_resource_login_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_session_resource_login_post_with_http_info(self, **kwargs):  # noqa: E501
        """Login.  # noqa: E501

        Login. Authenticates a user and creates a new session on the server. Once the user is authenticated then the returned session id can be used to access DGC REST Api in subsequent requests. The method additionally returns the JSESSIONID cookie in a <code>Set-Cookie</code> header. If user already has an open session then this session will be terminated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_session_resource_login_post_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param JsonLoginRequest body: 
        :return: file
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
                    " to method resource_session_resource_login_post" % key
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
            '/auth/sessions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_session_resource_logout_delete(self, **kwargs):  # noqa: E501
        """Logout.  # noqa: E501

        Logout. Logs current user out and destroys the active session. Returns <code>401</code> if user is not authenticated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_session_resource_logout_delete(async=True)
        >>> result = thread.get()

        :param async bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_session_resource_logout_delete_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_session_resource_logout_delete_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_session_resource_logout_delete_with_http_info(self, **kwargs):  # noqa: E501
        """Logout.  # noqa: E501

        Logout. Logs current user out and destroys the active session. Returns <code>401</code> if user is not authenticated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_session_resource_logout_delete_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_session_resource_logout_delete" % key
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
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/auth/sessions/current', 'DELETE',
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