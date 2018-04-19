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


class RelationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def resource_relation_resource_add_relation_post(self, **kwargs):  # noqa: E501
        """Adds a new relation.  # noqa: E501

        Adds a new relation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_resource_add_relation_post(async=True)
        >>> result = thread.get()

        :param async bool
        :param JsonAddRelationRequest body: the properties of the relation to be added
        :return: JsonRelationImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_relation_resource_add_relation_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_relation_resource_add_relation_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_relation_resource_add_relation_post_with_http_info(self, **kwargs):  # noqa: E501
        """Adds a new relation.  # noqa: E501

        Adds a new relation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_resource_add_relation_post_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param JsonAddRelationRequest body: the properties of the relation to be added
        :return: JsonRelationImpl
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
                    " to method resource_relation_resource_add_relation_post" % key
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
            '/relations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonRelationImpl',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_relation_resource_add_relations_post(self, **kwargs):  # noqa: E501
        """Adds multiple relations in one go.  # noqa: E501

        Adds multiple relations in one go.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_resource_add_relations_post(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[JsonAddRelationRequest] body: the list of properties of the relations to be added
        :return: JsonRelationImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_relation_resource_add_relations_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_relation_resource_add_relations_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_relation_resource_add_relations_post_with_http_info(self, **kwargs):  # noqa: E501
        """Adds multiple relations in one go.  # noqa: E501

        Adds multiple relations in one go.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_resource_add_relations_post_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[JsonAddRelationRequest] body: the list of properties of the relations to be added
        :return: JsonRelationImpl
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
                    " to method resource_relation_resource_add_relations_post" % key
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
            '/relations/bulk', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonRelationImpl',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_relation_resource_change_relation_patch(self, relation_id, **kwargs):  # noqa: E501
        """Change the relation with the information that is present in the request.  # noqa: E501

        Change the relation with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_resource_change_relation_patch(relation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str relation_id: the <code>id</code> of the relation to be changed. (required)
        :param JsonChangeRelationRequest body: the properties of the relation to be changed
        :return: JsonRelationImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_relation_resource_change_relation_patch_with_http_info(relation_id, **kwargs)  # noqa: E501
        else:
            (data) = self.resource_relation_resource_change_relation_patch_with_http_info(relation_id, **kwargs)  # noqa: E501
            return data

    def resource_relation_resource_change_relation_patch_with_http_info(self, relation_id, **kwargs):  # noqa: E501
        """Change the relation with the information that is present in the request.  # noqa: E501

        Change the relation with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_resource_change_relation_patch_with_http_info(relation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str relation_id: the <code>id</code> of the relation to be changed. (required)
        :param JsonChangeRelationRequest body: the properties of the relation to be changed
        :return: JsonRelationImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['relation_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_relation_resource_change_relation_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'relation_id' is set
        if ('relation_id' not in params or
                params['relation_id'] is None):
            raise ValueError("Missing the required parameter `relation_id` when calling `resource_relation_resource_change_relation_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'relation_id' in params:
            path_params['relationId'] = params['relation_id']  # noqa: E501

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
            '/relations/{relationId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonRelationImpl',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_relation_resource_change_relations_patch(self, **kwargs):  # noqa: E501
        """Changes multiple relations with the information that is present in the request.  # noqa: E501

        Changes multiple relations with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_resource_change_relations_patch(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[JsonChangeRelationRequest] body: the list of properties of the relations to be changed
        :return: list[JsonRelationImpl]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_relation_resource_change_relations_patch_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_relation_resource_change_relations_patch_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_relation_resource_change_relations_patch_with_http_info(self, **kwargs):  # noqa: E501
        """Changes multiple relations with the information that is present in the request.  # noqa: E501

        Changes multiple relations with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_resource_change_relations_patch_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[JsonChangeRelationRequest] body: the list of properties of the relations to be changed
        :return: list[JsonRelationImpl]
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
                    " to method resource_relation_resource_change_relations_patch" % key
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
            '/relations/bulk', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[JsonRelationImpl]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_relation_resource_find_relations_get(self, **kwargs):  # noqa: E501
        """Returns relations matching the given search criteria.  # noqa: E501

        Returns relations matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned relations satisfy all constraints that are specified in this search criteria. By default a result containing 1000 relations is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_resource_find_relations_get(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used
        :param int offset: The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>
        :param str relation_type_id: The <code>id</code> of the type of relations to search for
        :param str source_id: The <code>id</code> of the source of relations to search for
        :param str source_target_logical_operator: The logical operator determining how to combine the source and target criteria: AND or OR
        :param str target_id: The <code>id</code> of the target of relations to search for
        :return: JsonPagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_relation_resource_find_relations_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_relation_resource_find_relations_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_relation_resource_find_relations_get_with_http_info(self, **kwargs):  # noqa: E501
        """Returns relations matching the given search criteria.  # noqa: E501

        Returns relations matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned relations satisfy all constraints that are specified in this search criteria. By default a result containing 1000 relations is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_resource_find_relations_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int limit: The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used
        :param int offset: The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>
        :param str relation_type_id: The <code>id</code> of the type of relations to search for
        :param str source_id: The <code>id</code> of the source of relations to search for
        :param str source_target_logical_operator: The logical operator determining how to combine the source and target criteria: AND or OR
        :param str target_id: The <code>id</code> of the target of relations to search for
        :return: JsonPagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'relation_type_id', 'source_id', 'source_target_logical_operator', 'target_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_relation_resource_find_relations_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'relation_type_id' in params:
            query_params.append(('relationTypeId', params['relation_type_id']))  # noqa: E501
        if 'source_id' in params:
            query_params.append(('sourceId', params['source_id']))  # noqa: E501
        if 'source_target_logical_operator' in params:
            query_params.append(('sourceTargetLogicalOperator', params['source_target_logical_operator']))  # noqa: E501
        if 'target_id' in params:
            query_params.append(('targetId', params['target_id']))  # noqa: E501

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
            '/relations', 'GET',
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

    def resource_relation_resource_get_relation_get(self, relation_id, **kwargs):  # noqa: E501
        """Returns an relation identified by given id.  # noqa: E501

        Returns an relation identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_resource_get_relation_get(relation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str relation_id: the <code>id</code> of the relation (required)
        :return: JsonRelationImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_relation_resource_get_relation_get_with_http_info(relation_id, **kwargs)  # noqa: E501
        else:
            (data) = self.resource_relation_resource_get_relation_get_with_http_info(relation_id, **kwargs)  # noqa: E501
            return data

    def resource_relation_resource_get_relation_get_with_http_info(self, relation_id, **kwargs):  # noqa: E501
        """Returns an relation identified by given id.  # noqa: E501

        Returns an relation identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_resource_get_relation_get_with_http_info(relation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str relation_id: the <code>id</code> of the relation (required)
        :return: JsonRelationImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['relation_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_relation_resource_get_relation_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'relation_id' is set
        if ('relation_id' not in params or
                params['relation_id'] is None):
            raise ValueError("Missing the required parameter `relation_id` when calling `resource_relation_resource_get_relation_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'relation_id' in params:
            path_params['relationId'] = params['relation_id']  # noqa: E501

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
            '/relations/{relationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonRelationImpl',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_relation_resource_remove_relation_delete(self, **kwargs):  # noqa: E501
        """Removes relations identified by given ids.  # noqa: E501

        Removes relations identified by given ids.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_resource_remove_relation_delete(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] body: the list of <code>id</code>s of the relations to remove
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_relation_resource_remove_relation_delete_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_relation_resource_remove_relation_delete_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_relation_resource_remove_relation_delete_with_http_info(self, **kwargs):  # noqa: E501
        """Removes relations identified by given ids.  # noqa: E501

        Removes relations identified by given ids.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_resource_remove_relation_delete_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] body: the list of <code>id</code>s of the relations to remove
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
                    " to method resource_relation_resource_remove_relation_delete" % key
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
            '/relations/bulk', 'DELETE',
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

    def resource_relation_resource_remove_relation_delete_0(self, relation_id, **kwargs):  # noqa: E501
        """Removes an relation identified by given id.  # noqa: E501

        Removes an relation identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_resource_remove_relation_delete_0(relation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str relation_id: the <code>id</code> of the relation to remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_relation_resource_remove_relation_delete_0_with_http_info(relation_id, **kwargs)  # noqa: E501
        else:
            (data) = self.resource_relation_resource_remove_relation_delete_0_with_http_info(relation_id, **kwargs)  # noqa: E501
            return data

    def resource_relation_resource_remove_relation_delete_0_with_http_info(self, relation_id, **kwargs):  # noqa: E501
        """Removes an relation identified by given id.  # noqa: E501

        Removes an relation identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_relation_resource_remove_relation_delete_0_with_http_info(relation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str relation_id: the <code>id</code> of the relation to remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['relation_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_relation_resource_remove_relation_delete_0" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'relation_id' is set
        if ('relation_id' not in params or
                params['relation_id'] is None):
            raise ValueError("Missing the required parameter `relation_id` when calling `resource_relation_resource_remove_relation_delete_0`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'relation_id' in params:
            path_params['relationId'] = params['relation_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/relations/{relationId}', 'DELETE',
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