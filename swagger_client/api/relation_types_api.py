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


class RelationTypesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def resource_relation_type_resource_add_relation_type_post(self, **kwargs):  # noqa: E501
        """Adds new relation type.  # noqa: E501

        Adds new relation type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_type_resource_add_relation_type_post(async=True)
        >>> result = thread.get()

        :param async bool
        :param JsonAddRelationTypeRequest body: the properties of the relation type to be added
        :return: JsonRelationTypeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_relation_type_resource_add_relation_type_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_relation_type_resource_add_relation_type_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_relation_type_resource_add_relation_type_post_with_http_info(self, **kwargs):  # noqa: E501
        """Adds new relation type.  # noqa: E501

        Adds new relation type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_type_resource_add_relation_type_post_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param JsonAddRelationTypeRequest body: the properties of the relation type to be added
        :return: JsonRelationTypeImpl
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
                    " to method resource_relation_type_resource_add_relation_type_post" % key
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
            '/relationTypes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonRelationTypeImpl',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_relation_type_resource_add_relation_types_post(self, **kwargs):  # noqa: E501
        """Adds multiple relation types.  # noqa: E501

        Adds multiple relation types.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_type_resource_add_relation_types_post(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[JsonAddRelationTypeRequest] body: the properties of the relation types to be added
        :return: list[JsonRelationTypeImpl]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_relation_type_resource_add_relation_types_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_relation_type_resource_add_relation_types_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_relation_type_resource_add_relation_types_post_with_http_info(self, **kwargs):  # noqa: E501
        """Adds multiple relation types.  # noqa: E501

        Adds multiple relation types.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_type_resource_add_relation_types_post_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[JsonAddRelationTypeRequest] body: the properties of the relation types to be added
        :return: list[JsonRelationTypeImpl]
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
                    " to method resource_relation_type_resource_add_relation_types_post" % key
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
            '/relationTypes/bulk', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[JsonRelationTypeImpl]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_relation_type_resource_change_relation_type_patch(self, relation_type_id, **kwargs):  # noqa: E501
        """Changes the relation type with the information that is present in the request.  # noqa: E501

        Changes the relation type with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_type_resource_change_relation_type_patch(relation_type_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str relation_type_id: the <code>id</code> of the relation type to be changed (required)
        :param JsonChangeRelationTypeRequest body: the properties of the relation type to be changed
        :return: JsonRelationTypeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_relation_type_resource_change_relation_type_patch_with_http_info(relation_type_id, **kwargs)  # noqa: E501
        else:
            (data) = self.resource_relation_type_resource_change_relation_type_patch_with_http_info(relation_type_id, **kwargs)  # noqa: E501
            return data

    def resource_relation_type_resource_change_relation_type_patch_with_http_info(self, relation_type_id, **kwargs):  # noqa: E501
        """Changes the relation type with the information that is present in the request.  # noqa: E501

        Changes the relation type with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_type_resource_change_relation_type_patch_with_http_info(relation_type_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str relation_type_id: the <code>id</code> of the relation type to be changed (required)
        :param JsonChangeRelationTypeRequest body: the properties of the relation type to be changed
        :return: JsonRelationTypeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['relation_type_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_relation_type_resource_change_relation_type_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'relation_type_id' is set
        if ('relation_type_id' not in params or
                params['relation_type_id'] is None):
            raise ValueError("Missing the required parameter `relation_type_id` when calling `resource_relation_type_resource_change_relation_type_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'relation_type_id' in params:
            path_params['relationTypeId'] = params['relation_type_id']  # noqa: E501

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
            '/relationTypes/{relationTypeId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonRelationTypeImpl',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_relation_type_resource_change_relation_types_patch(self, **kwargs):  # noqa: E501
        """Changes multiple relation types.  # noqa: E501

        Changes multiple relation types.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_type_resource_change_relation_types_patch(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[JsonChangeRelationTypeRequest] body: the properties of the relation types to be changed
        :return: list[JsonRelationTypeImpl]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_relation_type_resource_change_relation_types_patch_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_relation_type_resource_change_relation_types_patch_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_relation_type_resource_change_relation_types_patch_with_http_info(self, **kwargs):  # noqa: E501
        """Changes multiple relation types.  # noqa: E501

        Changes multiple relation types.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_type_resource_change_relation_types_patch_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[JsonChangeRelationTypeRequest] body: the properties of the relation types to be changed
        :return: list[JsonRelationTypeImpl]
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
                    " to method resource_relation_type_resource_change_relation_types_patch" % key
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
            '/relationTypes/bulk', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[JsonRelationTypeImpl]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_relation_type_resource_find_relation_types_get(self, **kwargs):  # noqa: E501
        """Returns relation types matching the given search criteria.  # noqa: E501

        Returns relation types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned relation types satisfy all constraints that are specified in this search criteria. By default a result containing 1000 relation types is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_type_resource_find_relation_types_get(async=True)
        >>> result = thread.get()

        :param async bool
        :param str co_role: The name of the role that the target plays to search for
        :param int limit: The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used
        :param int offset: The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>
        :param str role: The name of the role that the source plays to search for
        :param str role_co_role_logical_operator: The logical operator determining how to combine the role and coRole criteria: AND or OR
        :param str sort_field: The field that should be used as reference for sorting
        :param str sort_order: The order of sorting
        :param str source_type_id: The <code>id</code> of the source type of the relation type to search for
        :param str source_type_name: The name of the source type of the relation type to search for
        :param str target_type_id: The <code>id</code> of the target type of the relation type to search for
        :param str target_type_name: The name of the target type of the relation type to search for
        :return: JsonPagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_relation_type_resource_find_relation_types_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_relation_type_resource_find_relation_types_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_relation_type_resource_find_relation_types_get_with_http_info(self, **kwargs):  # noqa: E501
        """Returns relation types matching the given search criteria.  # noqa: E501

        Returns relation types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned relation types satisfy all constraints that are specified in this search criteria. By default a result containing 1000 relation types is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_type_resource_find_relation_types_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str co_role: The name of the role that the target plays to search for
        :param int limit: The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used
        :param int offset: The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>
        :param str role: The name of the role that the source plays to search for
        :param str role_co_role_logical_operator: The logical operator determining how to combine the role and coRole criteria: AND or OR
        :param str sort_field: The field that should be used as reference for sorting
        :param str sort_order: The order of sorting
        :param str source_type_id: The <code>id</code> of the source type of the relation type to search for
        :param str source_type_name: The name of the source type of the relation type to search for
        :param str target_type_id: The <code>id</code> of the target type of the relation type to search for
        :param str target_type_name: The name of the target type of the relation type to search for
        :return: JsonPagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['co_role', 'limit', 'offset', 'role', 'role_co_role_logical_operator', 'sort_field', 'sort_order', 'source_type_id', 'source_type_name', 'target_type_id', 'target_type_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_relation_type_resource_find_relation_types_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'co_role' in params:
            query_params.append(('coRole', params['co_role']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'role' in params:
            query_params.append(('role', params['role']))  # noqa: E501
        if 'role_co_role_logical_operator' in params:
            query_params.append(('roleCoRoleLogicalOperator', params['role_co_role_logical_operator']))  # noqa: E501
        if 'sort_field' in params:
            query_params.append(('sortField', params['sort_field']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501
        if 'source_type_id' in params:
            query_params.append(('sourceTypeId', params['source_type_id']))  # noqa: E501
        if 'source_type_name' in params:
            query_params.append(('sourceTypeName', params['source_type_name']))  # noqa: E501
        if 'target_type_id' in params:
            query_params.append(('targetTypeId', params['target_type_id']))  # noqa: E501
        if 'target_type_name' in params:
            query_params.append(('targetTypeName', params['target_type_name']))  # noqa: E501

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
            '/relationTypes', 'GET',
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

    def resource_relation_type_resource_get_relation_type_get(self, relation_type_id, **kwargs):  # noqa: E501
        """Returns relation type identified by given id.  # noqa: E501

        Returns relation type identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_type_resource_get_relation_type_get(relation_type_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str relation_type_id: the <code>id</code> of the relation type (required)
        :return: JsonRelationTypeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_relation_type_resource_get_relation_type_get_with_http_info(relation_type_id, **kwargs)  # noqa: E501
        else:
            (data) = self.resource_relation_type_resource_get_relation_type_get_with_http_info(relation_type_id, **kwargs)  # noqa: E501
            return data

    def resource_relation_type_resource_get_relation_type_get_with_http_info(self, relation_type_id, **kwargs):  # noqa: E501
        """Returns relation type identified by given id.  # noqa: E501

        Returns relation type identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_type_resource_get_relation_type_get_with_http_info(relation_type_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str relation_type_id: the <code>id</code> of the relation type (required)
        :return: JsonRelationTypeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['relation_type_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_relation_type_resource_get_relation_type_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'relation_type_id' is set
        if ('relation_type_id' not in params or
                params['relation_type_id'] is None):
            raise ValueError("Missing the required parameter `relation_type_id` when calling `resource_relation_type_resource_get_relation_type_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'relation_type_id' in params:
            path_params['relationTypeId'] = params['relation_type_id']  # noqa: E501

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
            '/relationTypes/{relationTypeId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonRelationTypeImpl',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_relation_type_resource_remove_relation_type_delete(self, relation_type_id, **kwargs):  # noqa: E501
        """Removes relation type identified by given id.  # noqa: E501

        Removes relation type identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_type_resource_remove_relation_type_delete(relation_type_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str relation_type_id: the <code>id</code> of the relation type (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_relation_type_resource_remove_relation_type_delete_with_http_info(relation_type_id, **kwargs)  # noqa: E501
        else:
            (data) = self.resource_relation_type_resource_remove_relation_type_delete_with_http_info(relation_type_id, **kwargs)  # noqa: E501
            return data

    def resource_relation_type_resource_remove_relation_type_delete_with_http_info(self, relation_type_id, **kwargs):  # noqa: E501
        """Removes relation type identified by given id.  # noqa: E501

        Removes relation type identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_type_resource_remove_relation_type_delete_with_http_info(relation_type_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str relation_type_id: the <code>id</code> of the relation type (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['relation_type_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_relation_type_resource_remove_relation_type_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'relation_type_id' is set
        if ('relation_type_id' not in params or
                params['relation_type_id'] is None):
            raise ValueError("Missing the required parameter `relation_type_id` when calling `resource_relation_type_resource_remove_relation_type_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'relation_type_id' in params:
            path_params['relationTypeId'] = params['relation_type_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/relationTypes/{relationTypeId}', 'DELETE',
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

    def resource_relation_type_resource_remove_relation_types_delete(self, **kwargs):  # noqa: E501
        """Removes multiple relation types.  # noqa: E501

        Removes multiple relation types.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_type_resource_remove_relation_types_delete(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] body: the <code>id</code>s of the relation types to be removed, i.e. [\"6f685f90-1036-4d30-983a-a9bbcdd7b8f6\", \"6f685f90-1036-4d30-983a-a9bbcdd7b123\"]
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_relation_type_resource_remove_relation_types_delete_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_relation_type_resource_remove_relation_types_delete_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_relation_type_resource_remove_relation_types_delete_with_http_info(self, **kwargs):  # noqa: E501
        """Removes multiple relation types.  # noqa: E501

        Removes multiple relation types.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_type_resource_remove_relation_types_delete_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] body: the <code>id</code>s of the relation types to be removed, i.e. [\"6f685f90-1036-4d30-983a-a9bbcdd7b8f6\", \"6f685f90-1036-4d30-983a-a9bbcdd7b123\"]
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
                    " to method resource_relation_type_resource_remove_relation_types_delete" % key
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
            '/relationTypes/bulk', 'DELETE',
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
