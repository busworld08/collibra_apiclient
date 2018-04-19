# swagger_client.DomainsApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_domain_resource_add_domain_post**](DomainsApi.md#resource_domain_resource_add_domain_post) | **POST** /domains | Adds a new domain into a community.
[**resource_domain_resource_add_domains_post**](DomainsApi.md#resource_domain_resource_add_domains_post) | **POST** /domains/bulk | Adds multiple domains.
[**resource_domain_resource_change_domain_patch**](DomainsApi.md#resource_domain_resource_change_domain_patch) | **PATCH** /domains/{domainId} | Changes the domain with the information that is present in the request.
[**resource_domain_resource_change_domains_patch**](DomainsApi.md#resource_domain_resource_change_domains_patch) | **PATCH** /domains/bulk | Changes multiple domains.
[**resource_domain_resource_find_domains_get**](DomainsApi.md#resource_domain_resource_find_domains_get) | **GET** /domains | Returns domains matching the given search criteria.
[**resource_domain_resource_get_domain_get**](DomainsApi.md#resource_domain_resource_get_domain_get) | **GET** /domains/{domainId} | Returns a domain identified by given id.
[**resource_domain_resource_remove_domain_delete**](DomainsApi.md#resource_domain_resource_remove_domain_delete) | **DELETE** /domains/{domainId} | Removes a domain identified by given id.
[**resource_domain_resource_remove_domains_delete**](DomainsApi.md#resource_domain_resource_remove_domains_delete) | **DELETE** /domains/bulk | Removes multiple domains.
[**resource_domain_resource_remove_domains_in_job_post**](DomainsApi.md#resource_domain_resource_remove_domains_in_job_post) | **POST** /domains/removalJobs | Removes multiple domains in job.


# **resource_domain_resource_add_domain_post**
> JsonDomainImpl resource_domain_resource_add_domain_post(body=body)

Adds a new domain into a community.

Adds a new domain into a community.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
body = swagger_client.JsonAddDomainRequest() # JsonAddDomainRequest | the properties of the domain to be added (optional)

try:
    # Adds a new domain into a community.
    api_response = api_instance.resource_domain_resource_add_domain_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->resource_domain_resource_add_domain_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAddDomainRequest**](JsonAddDomainRequest.md)| the properties of the domain to be added | [optional] 

### Return type

[**JsonDomainImpl**](JsonDomainImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_domain_resource_add_domains_post**
> list[JsonDomainImpl] resource_domain_resource_add_domains_post(body=body)

Adds multiple domains.

Adds multiple domains.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
body = [swagger_client.JsonAddDomainRequest()] # list[JsonAddDomainRequest] | the properties of the domains to be added (optional)

try:
    # Adds multiple domains.
    api_response = api_instance.resource_domain_resource_add_domains_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->resource_domain_resource_add_domains_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonAddDomainRequest]**](JsonAddDomainRequest.md)| the properties of the domains to be added | [optional] 

### Return type

[**list[JsonDomainImpl]**](JsonDomainImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_domain_resource_change_domain_patch**
> JsonDomainImpl resource_domain_resource_change_domain_patch(domain_id, body=body)

Changes the domain with the information that is present in the request.

Changes the domain with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
domain_id = 'domain_id_example' # str | the <code>id</code> of the domain to be changed.
body = swagger_client.JsonChangeDomainRequest() # JsonChangeDomainRequest | the properties of the domain to be changed (optional)

try:
    # Changes the domain with the information that is present in the request.
    api_response = api_instance.resource_domain_resource_change_domain_patch(domain_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->resource_domain_resource_change_domain_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the domain to be changed. | 
 **body** | [**JsonChangeDomainRequest**](JsonChangeDomainRequest.md)| the properties of the domain to be changed | [optional] 

### Return type

[**JsonDomainImpl**](JsonDomainImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_domain_resource_change_domains_patch**
> list[file] resource_domain_resource_change_domains_patch(body=body)

Changes multiple domains.

Changes multiple domains.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
body = [swagger_client.JsonChangeDomainRequest()] # list[JsonChangeDomainRequest] | the properties of the domains to be changed (optional)

try:
    # Changes multiple domains.
    api_response = api_instance.resource_domain_resource_change_domains_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->resource_domain_resource_change_domains_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonChangeDomainRequest]**](JsonChangeDomainRequest.md)| the properties of the domains to be changed | [optional] 

### Return type

[**list[file]**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_domain_resource_find_domains_get**
> JsonPagedResponse resource_domain_resource_find_domains_get(community_id=community_id, exclude_meta=exclude_meta, limit=limit, name=name, name_match_mode=name_match_mode, offset=offset, type_id=type_id)

Returns domains matching the given search criteria.

Returns domains matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned domains satisfy all constraints that are specified in this search criteria. By default a result containing 1000 domains is returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
community_id = 'community_id_example' # str | The <code>id</code> of the community to find the domains in (optional)
exclude_meta = true # bool | The exclude meta flag. If this is set to true then the meta domains will not be returned (meta domains are i.e. domains not created manually by the user) (optional) (default to true)
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
name = 'name_example' # str | The name of the domain to search for (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code> (optional) (default to ANYWHERE)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)
type_id = 'type_id_example' # str | The <code>id</code> of the domain type to search for. Returned domains are of this type (optional)

try:
    # Returns domains matching the given search criteria.
    api_response = api_instance.resource_domain_resource_find_domains_get(community_id=community_id, exclude_meta=exclude_meta, limit=limit, name=name, name_match_mode=name_match_mode, offset=offset, type_id=type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->resource_domain_resource_find_domains_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **community_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the community to find the domains in | [optional] 
 **exclude_meta** | **bool**| The exclude meta flag. If this is set to true then the meta domains will not be returned (meta domains are i.e. domains not created manually by the user) | [optional] [default to true]
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **name** | **str**| The name of the domain to search for | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt; | [optional] [default to ANYWHERE]
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]
 **type_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the domain type to search for. Returned domains are of this type | [optional] 

### Return type

[**JsonPagedResponse**](JsonPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_domain_resource_get_domain_get**
> JsonDomainImpl resource_domain_resource_get_domain_get(domain_id)

Returns a domain identified by given id.

Returns a domain identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
domain_id = 'domain_id_example' # str | the <code>id</code> of the domain

try:
    # Returns a domain identified by given id.
    api_response = api_instance.resource_domain_resource_get_domain_get(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->resource_domain_resource_get_domain_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the domain | 

### Return type

[**JsonDomainImpl**](JsonDomainImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_domain_resource_remove_domain_delete**
> resource_domain_resource_remove_domain_delete(domain_id)

Removes a domain identified by given id.

Removes a domain identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
domain_id = 'domain_id_example' # str | the <code>id</code> of the domain to remove

try:
    # Removes a domain identified by given id.
    api_instance.resource_domain_resource_remove_domain_delete(domain_id)
except ApiException as e:
    print("Exception when calling DomainsApi->resource_domain_resource_remove_domain_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the domain to remove | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_domain_resource_remove_domains_delete**
> resource_domain_resource_remove_domains_delete(body=body)

Removes multiple domains.

Removes multiple domains.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
body = [swagger_client.list[str]()] # list[str] | the <code>id</code>s of the domains to be removed, i.e. [\"6f685f90-1036-4d30-983a-a9bbcdd7b8f6\", \"6f685f90-1036-4d30-983a-a9bbcdd7b123\"] (optional)

try:
    # Removes multiple domains.
    api_instance.resource_domain_resource_remove_domains_delete(body=body)
except ApiException as e:
    print("Exception when calling DomainsApi->resource_domain_resource_remove_domains_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**| the &lt;code&gt;id&lt;/code&gt;s of the domains to be removed, i.e. [\&quot;6f685f90-1036-4d30-983a-a9bbcdd7b8f6\&quot;, \&quot;6f685f90-1036-4d30-983a-a9bbcdd7b123\&quot;] | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_domain_resource_remove_domains_in_job_post**
> JsonJobImpl resource_domain_resource_remove_domains_in_job_post(body=body)

Removes multiple domains in job.

Removes multiple domains in job.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
body = [swagger_client.list[str]()] # list[str] | the <code>id</code>s of the domains to be removed, i.e. [\"6f685f90-1036-4d30-983a-a9bbcdd7b8f6\", \"6f685f90-1036-4d30-983a-a9bbcdd7b123\"] (optional)

try:
    # Removes multiple domains in job.
    api_response = api_instance.resource_domain_resource_remove_domains_in_job_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->resource_domain_resource_remove_domains_in_job_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**| the &lt;code&gt;id&lt;/code&gt;s of the domains to be removed, i.e. [\&quot;6f685f90-1036-4d30-983a-a9bbcdd7b8f6\&quot;, \&quot;6f685f90-1036-4d30-983a-a9bbcdd7b123\&quot;] | [optional] 

### Return type

[**JsonJobImpl**](JsonJobImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

