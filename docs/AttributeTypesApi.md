# swagger_client.AttributeTypesApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_attribute_type_resource_add_attribute_type_post**](AttributeTypesApi.md#resource_attribute_type_resource_add_attribute_type_post) | **POST** /attributeTypes | Adds new attribute type.
[**resource_attribute_type_resource_add_attribute_types_post**](AttributeTypesApi.md#resource_attribute_type_resource_add_attribute_types_post) | **POST** /attributeTypes/bulk | Adds multiple attribute types.
[**resource_attribute_type_resource_change_attribute_type_patch**](AttributeTypesApi.md#resource_attribute_type_resource_change_attribute_type_patch) | **PATCH** /attributeTypes/{attributeTypeId} | Changes the attribute type with the information that is present in the request.
[**resource_attribute_type_resource_change_attribute_types_patch**](AttributeTypesApi.md#resource_attribute_type_resource_change_attribute_types_patch) | **PATCH** /attributeTypes/bulk | Changes multiple attribute types.
[**resource_attribute_type_resource_find_attribute_types_get**](AttributeTypesApi.md#resource_attribute_type_resource_find_attribute_types_get) | **GET** /attributeTypes | Returns attribute types matching the given search criteria.
[**resource_attribute_type_resource_get_attribute_type_by_name_get**](AttributeTypesApi.md#resource_attribute_type_resource_get_attribute_type_by_name_get) | **GET** /attributeTypes/name/{attributeTypeName} | Returns attribute type identified by given name.
[**resource_attribute_type_resource_get_attribute_type_get**](AttributeTypesApi.md#resource_attribute_type_resource_get_attribute_type_get) | **GET** /attributeTypes/{attributeTypeId} | Returns attribute type identified by given id.
[**resource_attribute_type_resource_remove_attribute_type_delete**](AttributeTypesApi.md#resource_attribute_type_resource_remove_attribute_type_delete) | **DELETE** /attributeTypes/{attributeTypeId} | Removes attribute type identified by given id.
[**resource_attribute_type_resource_remove_attribute_types_delete**](AttributeTypesApi.md#resource_attribute_type_resource_remove_attribute_types_delete) | **DELETE** /attributeTypes/bulk | Removes multiple attribute types.


# **resource_attribute_type_resource_add_attribute_type_post**
> JsonAttributeTypeImpl resource_attribute_type_resource_add_attribute_type_post(body=body)

Adds new attribute type.

Adds new attribute type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeTypesApi()
body = swagger_client.JsonAddAttributeTypeRequest() # JsonAddAttributeTypeRequest | the properties of the attribute type to be added (optional)

try:
    # Adds new attribute type.
    api_response = api_instance.resource_attribute_type_resource_add_attribute_type_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTypesApi->resource_attribute_type_resource_add_attribute_type_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAddAttributeTypeRequest**](JsonAddAttributeTypeRequest.md)| the properties of the attribute type to be added | [optional] 

### Return type

[**JsonAttributeTypeImpl**](JsonAttributeTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_attribute_type_resource_add_attribute_types_post**
> list[JsonAttributeTypeImpl] resource_attribute_type_resource_add_attribute_types_post(body=body)

Adds multiple attribute types.

Adds multiple attribute types.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeTypesApi()
body = [swagger_client.JsonAddAttributeTypeRequest()] # list[JsonAddAttributeTypeRequest] | the properties of the attribute types to be added (optional)

try:
    # Adds multiple attribute types.
    api_response = api_instance.resource_attribute_type_resource_add_attribute_types_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTypesApi->resource_attribute_type_resource_add_attribute_types_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonAddAttributeTypeRequest]**](JsonAddAttributeTypeRequest.md)| the properties of the attribute types to be added | [optional] 

### Return type

[**list[JsonAttributeTypeImpl]**](JsonAttributeTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_attribute_type_resource_change_attribute_type_patch**
> JsonAttributeTypeImpl resource_attribute_type_resource_change_attribute_type_patch(attribute_type_id, body=body)

Changes the attribute type with the information that is present in the request.

Changes the attribute type with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeTypesApi()
attribute_type_id = 'attribute_type_id_example' # str | the <code>id</code> of the attribute type to be changed
body = swagger_client.JsonChangeAttributeTypeRequest() # JsonChangeAttributeTypeRequest | the properties of the attribute type to be changed (optional)

try:
    # Changes the attribute type with the information that is present in the request.
    api_response = api_instance.resource_attribute_type_resource_change_attribute_type_patch(attribute_type_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTypesApi->resource_attribute_type_resource_change_attribute_type_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_type_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the attribute type to be changed | 
 **body** | [**JsonChangeAttributeTypeRequest**](JsonChangeAttributeTypeRequest.md)| the properties of the attribute type to be changed | [optional] 

### Return type

[**JsonAttributeTypeImpl**](JsonAttributeTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_attribute_type_resource_change_attribute_types_patch**
> list[JsonAttributeTypeImpl] resource_attribute_type_resource_change_attribute_types_patch(body=body)

Changes multiple attribute types.

Changes multiple attribute types.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeTypesApi()
body = [swagger_client.JsonChangeAttributeTypeRequest()] # list[JsonChangeAttributeTypeRequest] | the properties of the attribute types to be changed (optional)

try:
    # Changes multiple attribute types.
    api_response = api_instance.resource_attribute_type_resource_change_attribute_types_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTypesApi->resource_attribute_type_resource_change_attribute_types_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonChangeAttributeTypeRequest]**](JsonChangeAttributeTypeRequest.md)| the properties of the attribute types to be changed | [optional] 

### Return type

[**list[JsonAttributeTypeImpl]**](JsonAttributeTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_attribute_type_resource_find_attribute_types_get**
> JsonPagedResponse resource_attribute_type_resource_find_attribute_types_get(is_integer=is_integer, kind=kind, language=language, limit=limit, name=name, name_match_mode=name_match_mode, offset=offset, sort_field=sort_field, sort_order=sort_order, statistics_enabled=statistics_enabled)

Returns attribute types matching the given search criteria.

Returns attribute types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned attribute types satisfy all constraints that are specified in this search criteria. By default a result containing 1000 attribute types is returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeTypesApi()
is_integer = true # bool | Whether only integer-type attribute types should be searched or not (optional)
kind = 'kind_example' # str | The kind of the attribute type to search for (optional)
language = 'language_example' # str | The language of the attribute type to search for (optional)
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
name = 'name_example' # str | The name of the attribute type to search for (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code>. (optional) (default to ANYWHERE)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)
sort_field = 'NAME' # str | The field that should be used as reference for sorting (optional) (default to NAME)
sort_order = 'ASC' # str | The order of sorting (optional) (default to ASC)
statistics_enabled = true # bool | Whether the attribute types should be searched with statistics enabled or not (optional)

try:
    # Returns attribute types matching the given search criteria.
    api_response = api_instance.resource_attribute_type_resource_find_attribute_types_get(is_integer=is_integer, kind=kind, language=language, limit=limit, name=name, name_match_mode=name_match_mode, offset=offset, sort_field=sort_field, sort_order=sort_order, statistics_enabled=statistics_enabled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTypesApi->resource_attribute_type_resource_find_attribute_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_integer** | **bool**| Whether only integer-type attribute types should be searched or not | [optional] 
 **kind** | **str**| The kind of the attribute type to search for | [optional] 
 **language** | **str**| The language of the attribute type to search for | [optional] 
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **name** | **str**| The name of the attribute type to search for | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. | [optional] [default to ANYWHERE]
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]
 **sort_field** | **str**| The field that should be used as reference for sorting | [optional] [default to NAME]
 **sort_order** | **str**| The order of sorting | [optional] [default to ASC]
 **statistics_enabled** | **bool**| Whether the attribute types should be searched with statistics enabled or not | [optional] 

### Return type

[**JsonPagedResponse**](JsonPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_attribute_type_resource_get_attribute_type_by_name_get**
> JsonAttributeTypeImpl resource_attribute_type_resource_get_attribute_type_by_name_get(attribute_type_name)

Returns attribute type identified by given name.

Returns attribute type identified by given name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeTypesApi()
attribute_type_name = 'attribute_type_name_example' # str | the name of the attribute type

try:
    # Returns attribute type identified by given name.
    api_response = api_instance.resource_attribute_type_resource_get_attribute_type_by_name_get(attribute_type_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTypesApi->resource_attribute_type_resource_get_attribute_type_by_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_type_name** | **str**| the name of the attribute type | 

### Return type

[**JsonAttributeTypeImpl**](JsonAttributeTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_attribute_type_resource_get_attribute_type_get**
> JsonAttributeTypeImpl resource_attribute_type_resource_get_attribute_type_get(attribute_type_id)

Returns attribute type identified by given id.

Returns attribute type identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeTypesApi()
attribute_type_id = 'attribute_type_id_example' # str | the <code>id</code> of the attribute type

try:
    # Returns attribute type identified by given id.
    api_response = api_instance.resource_attribute_type_resource_get_attribute_type_get(attribute_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeTypesApi->resource_attribute_type_resource_get_attribute_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_type_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the attribute type | 

### Return type

[**JsonAttributeTypeImpl**](JsonAttributeTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_attribute_type_resource_remove_attribute_type_delete**
> resource_attribute_type_resource_remove_attribute_type_delete(attribute_type_id)

Removes attribute type identified by given id.

Removes attribute type identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeTypesApi()
attribute_type_id = 'attribute_type_id_example' # str | the <code>id</code> of the attribute type

try:
    # Removes attribute type identified by given id.
    api_instance.resource_attribute_type_resource_remove_attribute_type_delete(attribute_type_id)
except ApiException as e:
    print("Exception when calling AttributeTypesApi->resource_attribute_type_resource_remove_attribute_type_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_type_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the attribute type | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_attribute_type_resource_remove_attribute_types_delete**
> resource_attribute_type_resource_remove_attribute_types_delete(body=body)

Removes multiple attribute types.

Removes multiple attribute types.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributeTypesApi()
body = [swagger_client.list[str]()] # list[str] | the <code>id</code>s of the attribute types to be removed, i.e. [“6f685f90-1036-4d30-983a-a9bbcdd7b8f6”,\"174b6334-9804-495d-b659-43f53a5de8b8\"] (optional)

try:
    # Removes multiple attribute types.
    api_instance.resource_attribute_type_resource_remove_attribute_types_delete(body=body)
except ApiException as e:
    print("Exception when calling AttributeTypesApi->resource_attribute_type_resource_remove_attribute_types_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**| the &lt;code&gt;id&lt;/code&gt;s of the attribute types to be removed, i.e. [“6f685f90-1036-4d30-983a-a9bbcdd7b8f6”,\&quot;174b6334-9804-495d-b659-43f53a5de8b8\&quot;] | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

