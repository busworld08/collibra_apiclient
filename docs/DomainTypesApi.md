# swagger_client.DomainTypesApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_domain_type_resource_add_domain_type_post**](DomainTypesApi.md#resource_domain_type_resource_add_domain_type_post) | **POST** /domainTypes | Adds new domain type.
[**resource_domain_type_resource_add_domain_types_post**](DomainTypesApi.md#resource_domain_type_resource_add_domain_types_post) | **POST** /domainTypes/bulk | Adds multiple domain types.
[**resource_domain_type_resource_change_domain_type_patch**](DomainTypesApi.md#resource_domain_type_resource_change_domain_type_patch) | **PATCH** /domainTypes/{domainTypeId} | Changes the domain type with the information that is present in the request.
[**resource_domain_type_resource_change_domain_types_patch**](DomainTypesApi.md#resource_domain_type_resource_change_domain_types_patch) | **PATCH** /domainTypes/bulk | Changes multiple domain types.
[**resource_domain_type_resource_find_domain_types_get**](DomainTypesApi.md#resource_domain_type_resource_find_domain_types_get) | **GET** /domainTypes | Returns domain types matching the given search criteria.
[**resource_domain_type_resource_find_sub_asset_types_get**](DomainTypesApi.md#resource_domain_type_resource_find_sub_asset_types_get) | **GET** /domainTypes/{domainTypeId}/subTypes | Finds all the sub types of the domain type as described in the request object.
[**resource_domain_type_resource_get_domain_type_get**](DomainTypesApi.md#resource_domain_type_resource_get_domain_type_get) | **GET** /domainTypes/{domainTypeId} | Returns domain type identified by given id.
[**resource_domain_type_resource_remove_domain_type_delete**](DomainTypesApi.md#resource_domain_type_resource_remove_domain_type_delete) | **DELETE** /domainTypes/{domainTypeId} | Removes domain type identified by given id.
[**resource_domain_type_resource_remove_domain_types_delete**](DomainTypesApi.md#resource_domain_type_resource_remove_domain_types_delete) | **DELETE** /domainTypes/bulk | Removes multiple domain types.


# **resource_domain_type_resource_add_domain_type_post**
> JsonDomainTypeImpl resource_domain_type_resource_add_domain_type_post(body=body)

Adds new domain type.

Adds new domain type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainTypesApi()
body = swagger_client.JsonAddDomainTypeRequest() # JsonAddDomainTypeRequest | the properties of the domain type to be added (optional)

try:
    # Adds new domain type.
    api_response = api_instance.resource_domain_type_resource_add_domain_type_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainTypesApi->resource_domain_type_resource_add_domain_type_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAddDomainTypeRequest**](JsonAddDomainTypeRequest.md)| the properties of the domain type to be added | [optional] 

### Return type

[**JsonDomainTypeImpl**](JsonDomainTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_domain_type_resource_add_domain_types_post**
> list[JsonDomainTypeImpl] resource_domain_type_resource_add_domain_types_post(body=body)

Adds multiple domain types.

Adds multiple domain types.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainTypesApi()
body = [swagger_client.JsonAddDomainTypeRequest()] # list[JsonAddDomainTypeRequest] | the properties of the domain types to be added (optional)

try:
    # Adds multiple domain types.
    api_response = api_instance.resource_domain_type_resource_add_domain_types_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainTypesApi->resource_domain_type_resource_add_domain_types_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonAddDomainTypeRequest]**](JsonAddDomainTypeRequest.md)| the properties of the domain types to be added | [optional] 

### Return type

[**list[JsonDomainTypeImpl]**](JsonDomainTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_domain_type_resource_change_domain_type_patch**
> JsonDomainTypeImpl resource_domain_type_resource_change_domain_type_patch(domain_type_id, body=body)

Changes the domain type with the information that is present in the request.

Changes the domain type with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainTypesApi()
domain_type_id = 'domain_type_id_example' # str | the <code>id</code> of the domain type to be changed
body = swagger_client.JsonChangeDomainTypeRequest() # JsonChangeDomainTypeRequest | the properties of the domain type to be changed (optional)

try:
    # Changes the domain type with the information that is present in the request.
    api_response = api_instance.resource_domain_type_resource_change_domain_type_patch(domain_type_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainTypesApi->resource_domain_type_resource_change_domain_type_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_type_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the domain type to be changed | 
 **body** | [**JsonChangeDomainTypeRequest**](JsonChangeDomainTypeRequest.md)| the properties of the domain type to be changed | [optional] 

### Return type

[**JsonDomainTypeImpl**](JsonDomainTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_domain_type_resource_change_domain_types_patch**
> list[JsonDomainTypeImpl] resource_domain_type_resource_change_domain_types_patch(body=body)

Changes multiple domain types.

Changes multiple domain types.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainTypesApi()
body = [swagger_client.JsonChangeDomainTypeRequest()] # list[JsonChangeDomainTypeRequest] | the properties of the domain types to be changed (optional)

try:
    # Changes multiple domain types.
    api_response = api_instance.resource_domain_type_resource_change_domain_types_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainTypesApi->resource_domain_type_resource_change_domain_types_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonChangeDomainTypeRequest]**](JsonChangeDomainTypeRequest.md)| the properties of the domain types to be changed | [optional] 

### Return type

[**list[JsonDomainTypeImpl]**](JsonDomainTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_domain_type_resource_find_domain_types_get**
> JsonPagedResponse resource_domain_type_resource_find_domain_types_get(exclude_meta=exclude_meta, limit=limit, name=name, name_match_mode=name_match_mode, offset=offset, parent_id=parent_id, top_level=top_level)

Returns domain types matching the given search criteria.

Returns domain types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned domain types satisfy all constraints that are specified in this search criteria. By default a result containing 1000 domain types is returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainTypesApi()
exclude_meta = true # bool | Whether the meta domain types should be excluded from search or not (optional) (default to true)
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
name = 'name_example' # str | The name of the domain type to search for (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code> (optional) (default to ANYWHERE)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)
parent_id = 'parent_id_example' # str | The <code>id</code> of the parent to find the domain types in (optional)
top_level = false # bool | Whether only top level domain types should be searched or not (optional) (default to false)

try:
    # Returns domain types matching the given search criteria.
    api_response = api_instance.resource_domain_type_resource_find_domain_types_get(exclude_meta=exclude_meta, limit=limit, name=name, name_match_mode=name_match_mode, offset=offset, parent_id=parent_id, top_level=top_level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainTypesApi->resource_domain_type_resource_find_domain_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exclude_meta** | **bool**| Whether the meta domain types should be excluded from search or not | [optional] [default to true]
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **name** | **str**| The name of the domain type to search for | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt; | [optional] [default to ANYWHERE]
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]
 **parent_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the parent to find the domain types in | [optional] 
 **top_level** | **bool**| Whether only top level domain types should be searched or not | [optional] [default to false]

### Return type

[**JsonPagedResponse**](JsonPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_domain_type_resource_find_sub_asset_types_get**
> JsonPagedResponse resource_domain_type_resource_find_sub_asset_types_get(domain_type_id, domain_type_id2=domain_type_id2, include_parent=include_parent)

Finds all the sub types of the domain type as described in the request object.

Finds all the sub types of the domain type as described in the request object.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainTypesApi()
domain_type_id = 'domain_type_id_example' # str | 
domain_type_id2 = 'domain_type_id_example' # str | The <code>id</code> of the domain type to search the sub types for (optional)
include_parent = true # bool | Whether parent domain type should be included in the search result (optional)

try:
    # Finds all the sub types of the domain type as described in the request object.
    api_response = api_instance.resource_domain_type_resource_find_sub_asset_types_get(domain_type_id, domain_type_id2=domain_type_id2, include_parent=include_parent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainTypesApi->resource_domain_type_resource_find_sub_asset_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_type_id** | **str**|  | 
 **domain_type_id2** | **str**| The &lt;code&gt;id&lt;/code&gt; of the domain type to search the sub types for | [optional] 
 **include_parent** | **bool**| Whether parent domain type should be included in the search result | [optional] 

### Return type

[**JsonPagedResponse**](JsonPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_domain_type_resource_get_domain_type_get**
> JsonDomainTypeImpl resource_domain_type_resource_get_domain_type_get(domain_type_id)

Returns domain type identified by given id.

Returns domain type identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainTypesApi()
domain_type_id = 'domain_type_id_example' # str | the <code>id</code> of the domain type

try:
    # Returns domain type identified by given id.
    api_response = api_instance.resource_domain_type_resource_get_domain_type_get(domain_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainTypesApi->resource_domain_type_resource_get_domain_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_type_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the domain type | 

### Return type

[**JsonDomainTypeImpl**](JsonDomainTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_domain_type_resource_remove_domain_type_delete**
> resource_domain_type_resource_remove_domain_type_delete(domain_type_id)

Removes domain type identified by given id.

Removes domain type identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainTypesApi()
domain_type_id = 'domain_type_id_example' # str | the <code>id</code> of the domain type

try:
    # Removes domain type identified by given id.
    api_instance.resource_domain_type_resource_remove_domain_type_delete(domain_type_id)
except ApiException as e:
    print("Exception when calling DomainTypesApi->resource_domain_type_resource_remove_domain_type_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_type_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the domain type | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_domain_type_resource_remove_domain_types_delete**
> resource_domain_type_resource_remove_domain_types_delete(body=body)

Removes multiple domain types.

Removes multiple domain types.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainTypesApi()
body = [swagger_client.list[str]()] # list[str] | the <code>id</code>s of the domain types to be removed, i.e. [“6f685f90-1036-4d30-983a-a9bbcdd7b8f6”,\"174b6334-9804-495d-b659-43f53a5de8b8\"] (optional)

try:
    # Removes multiple domain types.
    api_instance.resource_domain_type_resource_remove_domain_types_delete(body=body)
except ApiException as e:
    print("Exception when calling DomainTypesApi->resource_domain_type_resource_remove_domain_types_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**| the &lt;code&gt;id&lt;/code&gt;s of the domain types to be removed, i.e. [“6f685f90-1036-4d30-983a-a9bbcdd7b8f6”,\&quot;174b6334-9804-495d-b659-43f53a5de8b8\&quot;] | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

