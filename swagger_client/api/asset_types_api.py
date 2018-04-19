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


class AssetTypesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def resource_asset_type_resource_add_asset_type_post(self, **kwargs):  # noqa: E501
        """Adds new asset type.  # noqa: E501

        Adds new asset type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_asset_type_resource_add_asset_type_post(async=True)
        >>> result = thread.get()

        :param async bool
        :param JsonAddAssetTypeRequest body: the properties of the asset type to be added
        :return: JsonAssetTypeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_asset_type_resource_add_asset_type_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_asset_type_resource_add_asset_type_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_asset_type_resource_add_asset_type_post_with_http_info(self, **kwargs):  # noqa: E501
        """Adds new asset type.  # noqa: E501

        Adds new asset type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_asset_type_resource_add_asset_type_post_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param JsonAddAssetTypeRequest body: the properties of the asset type to be added
        :return: JsonAssetTypeImpl
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
                    " to method resource_asset_type_resource_add_asset_type_post" % key
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
            '/assetTypes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonAssetTypeImpl',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_asset_type_resource_add_asset_types_post(self, **kwargs):  # noqa: E501
        """Adds multiple asset types.  # noqa: E501

        Adds multiple asset types.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_asset_type_resource_add_asset_types_post(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[JsonAddAssetTypeRequest] body: the properties of the asset types to be added
        :return: list[JsonAssetTypeImpl]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_asset_type_resource_add_asset_types_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_asset_type_resource_add_asset_types_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_asset_type_resource_add_asset_types_post_with_http_info(self, **kwargs):  # noqa: E501
        """Adds multiple asset types.  # noqa: E501

        Adds multiple asset types.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_asset_type_resource_add_asset_types_post_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[JsonAddAssetTypeRequest] body: the properties of the asset types to be added
        :return: list[JsonAssetTypeImpl]
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
                    " to method resource_asset_type_resource_add_asset_types_post" % key
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
            '/assetTypes/bulk', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[JsonAssetTypeImpl]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_asset_type_resource_change_asset_type_patch(self, asset_type_id, **kwargs):  # noqa: E501
        """Changes the asset type with the information that is present in the request.  # noqa: E501

        Changes the asset type with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_asset_type_resource_change_asset_type_patch(asset_type_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str asset_type_id: the UUID of the asset type to be changed (required)
        :param JsonChangeAssetTypeRequest body: the properties of the asset type to be changed
        :return: JsonAssetTypeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_asset_type_resource_change_asset_type_patch_with_http_info(asset_type_id, **kwargs)  # noqa: E501
        else:
            (data) = self.resource_asset_type_resource_change_asset_type_patch_with_http_info(asset_type_id, **kwargs)  # noqa: E501
            return data

    def resource_asset_type_resource_change_asset_type_patch_with_http_info(self, asset_type_id, **kwargs):  # noqa: E501
        """Changes the asset type with the information that is present in the request.  # noqa: E501

        Changes the asset type with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_asset_type_resource_change_asset_type_patch_with_http_info(asset_type_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str asset_type_id: the UUID of the asset type to be changed (required)
        :param JsonChangeAssetTypeRequest body: the properties of the asset type to be changed
        :return: JsonAssetTypeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['asset_type_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_asset_type_resource_change_asset_type_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'asset_type_id' is set
        if ('asset_type_id' not in params or
                params['asset_type_id'] is None):
            raise ValueError("Missing the required parameter `asset_type_id` when calling `resource_asset_type_resource_change_asset_type_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_type_id' in params:
            path_params['assetTypeId'] = params['asset_type_id']  # noqa: E501

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
            '/assetTypes/{assetTypeId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonAssetTypeImpl',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_asset_type_resource_change_asset_types_patch(self, **kwargs):  # noqa: E501
        """Changes multiple asset types.  # noqa: E501

        Changes multiple asset types.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_asset_type_resource_change_asset_types_patch(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[JsonChangeAssetTypeRequest] body: the properties of the asset types to be changed
        :return: list[JsonAssetTypeImpl]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_asset_type_resource_change_asset_types_patch_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_asset_type_resource_change_asset_types_patch_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_asset_type_resource_change_asset_types_patch_with_http_info(self, **kwargs):  # noqa: E501
        """Changes multiple asset types.  # noqa: E501

        Changes multiple asset types.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_asset_type_resource_change_asset_types_patch_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[JsonChangeAssetTypeRequest] body: the properties of the asset types to be changed
        :return: list[JsonAssetTypeImpl]
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
                    " to method resource_asset_type_resource_change_asset_types_patch" % key
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
            '/assetTypes/bulk', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[JsonAssetTypeImpl]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_asset_type_resource_find_asset_types_get(self, **kwargs):  # noqa: E501
        """Returns asset types matching the given search criteria.  # noqa: E501

        Returns asset types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned asset types satisfy all constraints that are specified in this search criteria. By default a result containing 1000 asset types is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_asset_type_resource_find_asset_types_get(async=True)
        >>> result = thread.get()

        :param async bool
        :param bool exclude_meta: Whether the meta asset types should be excluded from search or not
        :param int limit: The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used
        :param str name: The name of the asset type to search for
        :param str name_match_mode: The match mode used to compare <code>name</code>
        :param int offset: The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>
        :param str parent_id: The <code>id</code> of the parent to find the asset types in
        :param bool top_level: Whether only top level asset types should be searched or not
        :return: JsonPagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_asset_type_resource_find_asset_types_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_asset_type_resource_find_asset_types_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_asset_type_resource_find_asset_types_get_with_http_info(self, **kwargs):  # noqa: E501
        """Returns asset types matching the given search criteria.  # noqa: E501

        Returns asset types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned asset types satisfy all constraints that are specified in this search criteria. By default a result containing 1000 asset types is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_asset_type_resource_find_asset_types_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param bool exclude_meta: Whether the meta asset types should be excluded from search or not
        :param int limit: The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used
        :param str name: The name of the asset type to search for
        :param str name_match_mode: The match mode used to compare <code>name</code>
        :param int offset: The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>
        :param str parent_id: The <code>id</code> of the parent to find the asset types in
        :param bool top_level: Whether only top level asset types should be searched or not
        :return: JsonPagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['exclude_meta', 'limit', 'name', 'name_match_mode', 'offset', 'parent_id', 'top_level']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_asset_type_resource_find_asset_types_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'exclude_meta' in params:
            query_params.append(('excludeMeta', params['exclude_meta']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'name_match_mode' in params:
            query_params.append(('nameMatchMode', params['name_match_mode']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'parent_id' in params:
            query_params.append(('parentId', params['parent_id']))  # noqa: E501
        if 'top_level' in params:
            query_params.append(('topLevel', params['top_level']))  # noqa: E501

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
            '/assetTypes', 'GET',
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

    def resource_asset_type_resource_find_sub_asset_types_get(self, asset_type_id, **kwargs):  # noqa: E501
        """Finds all the sub types of the asset type as described in the request object.  # noqa: E501

        Finds all the sub types of the asset type as described in the request object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_asset_type_resource_find_sub_asset_types_get(asset_type_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str asset_type_id:  (required)
        :param bool include_parent: Whether parent asset type should be included in the search result
        :return: JsonPagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_asset_type_resource_find_sub_asset_types_get_with_http_info(asset_type_id, **kwargs)  # noqa: E501
        else:
            (data) = self.resource_asset_type_resource_find_sub_asset_types_get_with_http_info(asset_type_id, **kwargs)  # noqa: E501
            return data

    def resource_asset_type_resource_find_sub_asset_types_get_with_http_info(self, asset_type_id, **kwargs):  # noqa: E501
        """Finds all the sub types of the asset type as described in the request object.  # noqa: E501

        Finds all the sub types of the asset type as described in the request object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_asset_type_resource_find_sub_asset_types_get_with_http_info(asset_type_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str asset_type_id:  (required)
        :param bool include_parent: Whether parent asset type should be included in the search result
        :return: JsonPagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['asset_type_id', 'include_parent']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_asset_type_resource_find_sub_asset_types_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'asset_type_id' is set
        if ('asset_type_id' not in params or
                params['asset_type_id'] is None):
            raise ValueError("Missing the required parameter `asset_type_id` when calling `resource_asset_type_resource_find_sub_asset_types_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_type_id' in params:
            path_params['assetTypeId'] = params['asset_type_id']  # noqa: E501

        query_params = []
        if 'include_parent' in params:
            query_params.append(('includeParent', params['include_parent']))  # noqa: E501

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
            '/assetTypes/{assetTypeId}/subTypes', 'GET',
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

    def resource_asset_type_resource_get_asset_type_get(self, asset_type_id, **kwargs):  # noqa: E501
        """Returns asset type identified by given UUID.  # noqa: E501

        Returns asset type identified by given UUID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_asset_type_resource_get_asset_type_get(asset_type_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str asset_type_id: the UUID of the asset type (required)
        :return: JsonAssetTypeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_asset_type_resource_get_asset_type_get_with_http_info(asset_type_id, **kwargs)  # noqa: E501
        else:
            (data) = self.resource_asset_type_resource_get_asset_type_get_with_http_info(asset_type_id, **kwargs)  # noqa: E501
            return data

    def resource_asset_type_resource_get_asset_type_get_with_http_info(self, asset_type_id, **kwargs):  # noqa: E501
        """Returns asset type identified by given UUID.  # noqa: E501

        Returns asset type identified by given UUID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_asset_type_resource_get_asset_type_get_with_http_info(asset_type_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str asset_type_id: the UUID of the asset type (required)
        :return: JsonAssetTypeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['asset_type_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_asset_type_resource_get_asset_type_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'asset_type_id' is set
        if ('asset_type_id' not in params or
                params['asset_type_id'] is None):
            raise ValueError("Missing the required parameter `asset_type_id` when calling `resource_asset_type_resource_get_asset_type_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_type_id' in params:
            path_params['assetTypeId'] = params['asset_type_id']  # noqa: E501

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
            '/assetTypes/{assetTypeId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonAssetTypeImpl',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_asset_type_resource_remove_asset_type_delete(self, asset_type_id, **kwargs):  # noqa: E501
        """Removes asset type identified by given UUID.  # noqa: E501

        Removes asset type identified by given UUID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_asset_type_resource_remove_asset_type_delete(asset_type_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str asset_type_id: the UUID of the asset type (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_asset_type_resource_remove_asset_type_delete_with_http_info(asset_type_id, **kwargs)  # noqa: E501
        else:
            (data) = self.resource_asset_type_resource_remove_asset_type_delete_with_http_info(asset_type_id, **kwargs)  # noqa: E501
            return data

    def resource_asset_type_resource_remove_asset_type_delete_with_http_info(self, asset_type_id, **kwargs):  # noqa: E501
        """Removes asset type identified by given UUID.  # noqa: E501

        Removes asset type identified by given UUID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_asset_type_resource_remove_asset_type_delete_with_http_info(asset_type_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str asset_type_id: the UUID of the asset type (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['asset_type_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_asset_type_resource_remove_asset_type_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'asset_type_id' is set
        if ('asset_type_id' not in params or
                params['asset_type_id'] is None):
            raise ValueError("Missing the required parameter `asset_type_id` when calling `resource_asset_type_resource_remove_asset_type_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'asset_type_id' in params:
            path_params['assetTypeId'] = params['asset_type_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/assetTypes/{assetTypeId}', 'DELETE',
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

    def resource_asset_type_resource_remove_asset_types_delete(self, **kwargs):  # noqa: E501
        """Removes multiple asset types.  # noqa: E501

        Removes multiple asset types.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_asset_type_resource_remove_asset_types_delete(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] body: the UUIDs of the asset types to be removed, i.e. [“6f685f90-1036-4d30-983a-a9bbcdd7b8f6”,\"174b6334-9804-495d-b659-43f53a5de8b8\"]
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_asset_type_resource_remove_asset_types_delete_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_asset_type_resource_remove_asset_types_delete_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_asset_type_resource_remove_asset_types_delete_with_http_info(self, **kwargs):  # noqa: E501
        """Removes multiple asset types.  # noqa: E501

        Removes multiple asset types.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_asset_type_resource_remove_asset_types_delete_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] body: the UUIDs of the asset types to be removed, i.e. [“6f685f90-1036-4d30-983a-a9bbcdd7b8f6”,\"174b6334-9804-495d-b659-43f53a5de8b8\"]
        :return: None
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
                    " to method resource_asset_type_resource_remove_asset_types_delete" % key
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
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/assetTypes/bulk', 'DELETE',
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