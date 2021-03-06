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


class DomainsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def resource_domain_resource_add_domain_post(self, **kwargs):  # noqa: E501
        """Adds a new domain into a community.  # noqa: E501

        Adds a new domain into a community.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_domain_resource_add_domain_post(async=True)
        >>> result = thread.get()

        :param async bool
        :param JsonAddDomainRequest body: the properties of the domain to be added
        :return: JsonDomainImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_domain_resource_add_domain_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_domain_resource_add_domain_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_domain_resource_add_domain_post_with_http_info(self, **kwargs):  # noqa: E501
        """Adds a new domain into a community.  # noqa: E501

        Adds a new domain into a community.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_domain_resource_add_domain_post_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param JsonAddDomainRequest body: the properties of the domain to be added
        :return: JsonDomainImpl
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
                    " to method resource_domain_resource_add_domain_post" % key
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
            '/domains', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonDomainImpl',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_domain_resource_add_domains_post(self, **kwargs):  # noqa: E501
        """Adds multiple domains.  # noqa: E501

        Adds multiple domains.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_domain_resource_add_domains_post(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[JsonAddDomainRequest] body: the properties of the domains to be added
        :return: list[JsonDomainImpl]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_domain_resource_add_domains_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_domain_resource_add_domains_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_domain_resource_add_domains_post_with_http_info(self, **kwargs):  # noqa: E501
        """Adds multiple domains.  # noqa: E501

        Adds multiple domains.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_domain_resource_add_domains_post_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[JsonAddDomainRequest] body: the properties of the domains to be added
        :return: list[JsonDomainImpl]
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
                    " to method resource_domain_resource_add_domains_post" % key
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
            '/domains/bulk', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[JsonDomainImpl]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_domain_resource_change_domain_patch(self, domain_id, **kwargs):  # noqa: E501
        """Changes the domain with the information that is present in the request.  # noqa: E501

        Changes the domain with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_domain_resource_change_domain_patch(domain_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str domain_id: the <code>id</code> of the domain to be changed. (required)
        :param JsonChangeDomainRequest body: the properties of the domain to be changed
        :return: JsonDomainImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_domain_resource_change_domain_patch_with_http_info(domain_id, **kwargs)  # noqa: E501
        else:
            (data) = self.resource_domain_resource_change_domain_patch_with_http_info(domain_id, **kwargs)  # noqa: E501
            return data

    def resource_domain_resource_change_domain_patch_with_http_info(self, domain_id, **kwargs):  # noqa: E501
        """Changes the domain with the information that is present in the request.  # noqa: E501

        Changes the domain with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_domain_resource_change_domain_patch_with_http_info(domain_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str domain_id: the <code>id</code> of the domain to be changed. (required)
        :param JsonChangeDomainRequest body: the properties of the domain to be changed
        :return: JsonDomainImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_domain_resource_change_domain_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params or
                params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `resource_domain_resource_change_domain_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']  # noqa: E501

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
            '/domains/{domainId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonDomainImpl',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_domain_resource_change_domains_patch(self, **kwargs):  # noqa: E501
        """Changes multiple domains.  # noqa: E501

        Changes multiple domains.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_domain_resource_change_domains_patch(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[JsonChangeDomainRequest] body: the properties of the domains to be changed
        :return: list[file]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_domain_resource_change_domains_patch_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_domain_resource_change_domains_patch_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_domain_resource_change_domains_patch_with_http_info(self, **kwargs):  # noqa: E501
        """Changes multiple domains.  # noqa: E501

        Changes multiple domains.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_domain_resource_change_domains_patch_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[JsonChangeDomainRequest] body: the properties of the domains to be changed
        :return: list[file]
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
                    " to method resource_domain_resource_change_domains_patch" % key
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
            '/domains/bulk', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[file]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_domain_resource_find_domains_get(self, **kwargs):  # noqa: E501
        """Returns domains matching the given search criteria.  # noqa: E501

        Returns domains matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned domains satisfy all constraints that are specified in this search criteria. By default a result containing 1000 domains is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_domain_resource_find_domains_get(async=True)
        >>> result = thread.get()

        :param async bool
        :param str community_id: The <code>id</code> of the community to find the domains in
        :param bool exclude_meta: The exclude meta flag. If this is set to true then the meta domains will not be returned (meta domains are i.e. domains not created manually by the user)
        :param int limit: The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used
        :param str name: The name of the domain to search for
        :param str name_match_mode: The match mode used to compare <code>name</code>
        :param int offset: The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>
        :param str type_id: The <code>id</code> of the domain type to search for. Returned domains are of this type
        :return: JsonPagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_domain_resource_find_domains_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_domain_resource_find_domains_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_domain_resource_find_domains_get_with_http_info(self, **kwargs):  # noqa: E501
        """Returns domains matching the given search criteria.  # noqa: E501

        Returns domains matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned domains satisfy all constraints that are specified in this search criteria. By default a result containing 1000 domains is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_domain_resource_find_domains_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str community_id: The <code>id</code> of the community to find the domains in
        :param bool exclude_meta: The exclude meta flag. If this is set to true then the meta domains will not be returned (meta domains are i.e. domains not created manually by the user)
        :param int limit: The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used
        :param str name: The name of the domain to search for
        :param str name_match_mode: The match mode used to compare <code>name</code>
        :param int offset: The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt>
        :param str type_id: The <code>id</code> of the domain type to search for. Returned domains are of this type
        :return: JsonPagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['community_id', 'exclude_meta', 'limit', 'name', 'name_match_mode', 'offset', 'type_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_domain_resource_find_domains_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'community_id' in params:
            query_params.append(('communityId', params['community_id']))  # noqa: E501
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
        if 'type_id' in params:
            query_params.append(('typeId', params['type_id']))  # noqa: E501

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
            '/domains', 'GET',
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

    def resource_domain_resource_get_domain_get(self, domain_id, **kwargs):  # noqa: E501
        """Returns a domain identified by given id.  # noqa: E501

        Returns a domain identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_domain_resource_get_domain_get(domain_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str domain_id: the <code>id</code> of the domain (required)
        :return: JsonDomainImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_domain_resource_get_domain_get_with_http_info(domain_id, **kwargs)  # noqa: E501
        else:
            (data) = self.resource_domain_resource_get_domain_get_with_http_info(domain_id, **kwargs)  # noqa: E501
            return data

    def resource_domain_resource_get_domain_get_with_http_info(self, domain_id, **kwargs):  # noqa: E501
        """Returns a domain identified by given id.  # noqa: E501

        Returns a domain identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_domain_resource_get_domain_get_with_http_info(domain_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str domain_id: the <code>id</code> of the domain (required)
        :return: JsonDomainImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_domain_resource_get_domain_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params or
                params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `resource_domain_resource_get_domain_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']  # noqa: E501

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
            '/domains/{domainId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonDomainImpl',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resource_domain_resource_remove_domain_delete(self, domain_id, **kwargs):  # noqa: E501
        """Removes a domain identified by given id.  # noqa: E501

        Removes a domain identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_domain_resource_remove_domain_delete(domain_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str domain_id: the <code>id</code> of the domain to remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_domain_resource_remove_domain_delete_with_http_info(domain_id, **kwargs)  # noqa: E501
        else:
            (data) = self.resource_domain_resource_remove_domain_delete_with_http_info(domain_id, **kwargs)  # noqa: E501
            return data

    def resource_domain_resource_remove_domain_delete_with_http_info(self, domain_id, **kwargs):  # noqa: E501
        """Removes a domain identified by given id.  # noqa: E501

        Removes a domain identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_domain_resource_remove_domain_delete_with_http_info(domain_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str domain_id: the <code>id</code> of the domain to remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resource_domain_resource_remove_domain_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain_id' is set
        if ('domain_id' not in params or
                params['domain_id'] is None):
            raise ValueError("Missing the required parameter `domain_id` when calling `resource_domain_resource_remove_domain_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'domain_id' in params:
            path_params['domainId'] = params['domain_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/domains/{domainId}', 'DELETE',
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

    def resource_domain_resource_remove_domains_delete(self, **kwargs):  # noqa: E501
        """Removes multiple domains.  # noqa: E501

        Removes multiple domains.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_domain_resource_remove_domains_delete(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] body: the <code>id</code>s of the domains to be removed, i.e. [\"6f685f90-1036-4d30-983a-a9bbcdd7b8f6\", \"6f685f90-1036-4d30-983a-a9bbcdd7b123\"]
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_domain_resource_remove_domains_delete_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_domain_resource_remove_domains_delete_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_domain_resource_remove_domains_delete_with_http_info(self, **kwargs):  # noqa: E501
        """Removes multiple domains.  # noqa: E501

        Removes multiple domains.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_domain_resource_remove_domains_delete_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] body: the <code>id</code>s of the domains to be removed, i.e. [\"6f685f90-1036-4d30-983a-a9bbcdd7b8f6\", \"6f685f90-1036-4d30-983a-a9bbcdd7b123\"]
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
                    " to method resource_domain_resource_remove_domains_delete" % key
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
            '/domains/bulk', 'DELETE',
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

    def resource_domain_resource_remove_domains_in_job_post(self, **kwargs):  # noqa: E501
        """Removes multiple domains in job.  # noqa: E501

        Removes multiple domains in job.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_domain_resource_remove_domains_in_job_post(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] body: the <code>id</code>s of the domains to be removed, i.e. [\"6f685f90-1036-4d30-983a-a9bbcdd7b8f6\", \"6f685f90-1036-4d30-983a-a9bbcdd7b123\"]
        :return: JsonJobImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.resource_domain_resource_remove_domains_in_job_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.resource_domain_resource_remove_domains_in_job_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def resource_domain_resource_remove_domains_in_job_post_with_http_info(self, **kwargs):  # noqa: E501
        """Removes multiple domains in job.  # noqa: E501

        Removes multiple domains in job.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.resource_domain_resource_remove_domains_in_job_post_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param list[str] body: the <code>id</code>s of the domains to be removed, i.e. [\"6f685f90-1036-4d30-983a-a9bbcdd7b8f6\", \"6f685f90-1036-4d30-983a-a9bbcdd7b123\"]
        :return: JsonJobImpl
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
                    " to method resource_domain_resource_remove_domains_in_job_post" % key
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
            '/domains/removalJobs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonJobImpl',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
