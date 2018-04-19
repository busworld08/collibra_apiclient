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


class TagsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def resource_tag_resource_find_tags_get(self, **kwargs):  # noqa: E501
        """Returns tags matching given search criteria.  # noqa: E501

        Returns tags matching given search criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_tag_resource_find_tags_get(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used
        :param str name: 
        :param str name_match_mode: 
        :param int offset: The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>
        :return: JsonPagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_tag_resource_find_tags_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_tag_resource_find_tags_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_tag_resource_find_tags_get_with_http_info(self, **kwargs):  # noqa: E501
        """Returns tags matching given search criteria.  # noqa: E501

        Returns tags matching given search criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_tag_resource_find_tags_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used
        :param str name: 
        :param str name_match_mode: 
        :param int offset: The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>
        :return: JsonPagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'name', 'name_match_mode', 'offset']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_tag_resource_find_tags_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'name_match_mode' in params:
            query_params.append(('nameMatchMode', params['name_match_mode']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

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
            '/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonPagedResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_tag_resource_get_tag_get(self, tag_id, **kwargs):  # noqa: E501
        """Returns a tag identified by given id.  # noqa: E501

        Returns a tag identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_tag_resource_get_tag_get(tag_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tag_id: the <code>id</code> of the tag (required)
        :return: JsonTagImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_tag_resource_get_tag_get_with_http_info(tag_id, **kwargs)  # noqa: E501
        else:
            (data) = self.resource_tag_resource_get_tag_get_with_http_info(tag_id, **kwargs)  # noqa: E501
            return data

    def resource_tag_resource_get_tag_get_with_http_info(self, tag_id, **kwargs):  # noqa: E501
        """Returns a tag identified by given id.  # noqa: E501

        Returns a tag identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_tag_resource_get_tag_get_with_http_info(tag_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tag_id: the <code>id</code> of the tag (required)
        :return: JsonTagImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_tag_resource_get_tag_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag_id' is set
        if ('tag_id' not in params or
                params['tag_id'] is None):
            raise ValueError("Missing the required parameter `tag_id` when calling `resource_tag_resource_get_tag_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tag_id' in params:
            path_params['tagId'] = params['tag_id']  # noqa: E501

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
            '/tags/{tagId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonTagImpl',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_tag_resource_get_tags_by_asset_id_get(self, asset_id, **kwargs):  # noqa: E501
        """Retrieves all tags of given asset.  # noqa: E501

        Retrieves all tags of given asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_tag_resource_get_tags_by_asset_id_get(asset_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str asset_id: the <code>id</code> of an asset (required)
        :return: list[JsonTagImpl]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_tag_resource_get_tags_by_asset_id_get_with_http_info(asset_id, **kwargs)  # noqa: E501
        else:
            (data) = self.resource_tag_resource_get_tags_by_asset_id_get_with_http_info(asset_id, **kwargs)  # noqa: E501
            return data

    def resource_tag_resource_get_tags_by_asset_id_get_with_http_info(self, asset_id, **kwargs):  # noqa: E501
        """Retrieves all tags of given asset.  # noqa: E501

        Retrieves all tags of given asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_tag_resource_get_tags_by_asset_id_get_with_http_info(asset_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str asset_id: the <code>id</code> of an asset (required)
        :return: list[JsonTagImpl]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['asset_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_tag_resource_get_tags_by_asset_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'asset_id' is set
        if ('asset_id' not in params or
                params['asset_id'] is None):
            raise ValueError("Missing the required parameter `asset_id` when calling `resource_tag_resource_get_tags_by_asset_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_id' in params:
            path_params['assetId'] = params['asset_id']  # noqa: E501

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
            '/tags/asset/{assetId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[JsonTagImpl]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)