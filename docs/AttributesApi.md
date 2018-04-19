# swagger_client.AttributesApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_attribute_resource_add_attribute_post**](AttributesApi.md#resource_attribute_resource_add_attribute_post) | **POST** /attributes | Adds a new attribute to an asset.
[**resource_attribute_resource_add_attributes_post**](AttributesApi.md#resource_attribute_resource_add_attributes_post) | **POST** /attributes/bulk | Adds multiple attributes.
[**resource_attribute_resource_change_attribute_patch**](AttributesApi.md#resource_attribute_resource_change_attribute_patch) | **PATCH** /attributes/{attributeId} | Changes the attribute with the information that is present in the request.
[**resource_attribute_resource_change_attributes_patch**](AttributesApi.md#resource_attribute_resource_change_attributes_patch) | **PATCH** /attributes/bulk | Changes multiple attributes with the information that is present in the request.
[**resource_attribute_resource_find_attributes_get**](AttributesApi.md#resource_attribute_resource_find_attributes_get) | **GET** /attributes | Returns attributes matching the given search criteria.
[**resource_attribute_resource_get_attribute_get**](AttributesApi.md#resource_attribute_resource_get_attribute_get) | **GET** /attributes/{attributeId} | Returns the attribute identified by given id.
[**resource_attribute_resource_remove_attribute_delete**](AttributesApi.md#resource_attribute_resource_remove_attribute_delete) | **DELETE** /attributes/{attributeId} | Removes the attribute identified by given id.
[**resource_attribute_resource_remove_attributes_delete**](AttributesApi.md#resource_attribute_resource_remove_attributes_delete) | **DELETE** /attributes/bulk | Removes the attributes identified by given ids.


# **resource_attribute_resource_add_attribute_post**
> JsonAttributeImpl resource_attribute_resource_add_attribute_post(body=body)

Adds a new attribute to an asset.

Adds a new attribute to an asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributesApi()
body = swagger_client.JsonAddAttributeRequest() # JsonAddAttributeRequest | the properties of the attribute to be added (optional)

try:
    # Adds a new attribute to an asset.
    api_response = api_instance.resource_attribute_resource_add_attribute_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->resource_attribute_resource_add_attribute_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAddAttributeRequest**](JsonAddAttributeRequest.md)| the properties of the attribute to be added | [optional] 

### Return type

[**JsonAttributeImpl**](JsonAttributeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_attribute_resource_add_attributes_post**
> list[JsonAttributeImpl] resource_attribute_resource_add_attributes_post(body=body)

Adds multiple attributes.

Adds multiple attributes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributesApi()
body = [swagger_client.JsonAddAttributeRequest()] # list[JsonAddAttributeRequest] | the list of the properties of the attributes to be added (optional)

try:
    # Adds multiple attributes.
    api_response = api_instance.resource_attribute_resource_add_attributes_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->resource_attribute_resource_add_attributes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonAddAttributeRequest]**](JsonAddAttributeRequest.md)| the list of the properties of the attributes to be added | [optional] 

### Return type

[**list[JsonAttributeImpl]**](JsonAttributeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_attribute_resource_change_attribute_patch**
> JsonAttributeImpl resource_attribute_resource_change_attribute_patch(attribute_id, body=body)

Changes the attribute with the information that is present in the request.

Changes the attribute with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributesApi()
attribute_id = 'attribute_id_example' # str | the <code>id</code> of the attribute to be changed
body = swagger_client.JsonChangeAttributeRequestAttribute() # JsonChangeAttributeRequestAttribute | the properties of the attribute to be changed (optional)

try:
    # Changes the attribute with the information that is present in the request.
    api_response = api_instance.resource_attribute_resource_change_attribute_patch(attribute_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->resource_attribute_resource_change_attribute_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the attribute to be changed | 
 **body** | [**JsonChangeAttributeRequestAttribute**](JsonChangeAttributeRequestAttribute.md)| the properties of the attribute to be changed | [optional] 

### Return type

[**JsonAttributeImpl**](JsonAttributeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_attribute_resource_change_attributes_patch**
> list[JsonAttributeImpl] resource_attribute_resource_change_attributes_patch(body=body)

Changes multiple attributes with the information that is present in the request.

Changes multiple attributes with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributesApi()
body = [swagger_client.JsonChangeAttributeRequestAttribute()] # list[JsonChangeAttributeRequestAttribute] | the list of properties of the attributes to be changed (optional)

try:
    # Changes multiple attributes with the information that is present in the request.
    api_response = api_instance.resource_attribute_resource_change_attributes_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->resource_attribute_resource_change_attributes_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonChangeAttributeRequestAttribute]**](JsonChangeAttributeRequestAttribute.md)| the list of properties of the attributes to be changed | [optional] 

### Return type

[**list[JsonAttributeImpl]**](JsonAttributeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_attribute_resource_find_attributes_get**
> JsonPagedResponse resource_attribute_resource_find_attributes_get(asset_id=asset_id, limit=limit, offset=offset, sort_field=sort_field, sort_order=sort_order, type_ids=type_ids)

Returns attributes matching the given search criteria.

Returns attributes matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned attributes satisfy all constraints that are specified in this search criteria. By default a result containing 1000 attributes is returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributesApi()
asset_id = 'asset_id_example' # str | The <code>id</code> of the asset to find the attributes in (optional)
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)
sort_field = 'LAST_MODIFIED' # str | The field on which the results are sorted (optional) (default to LAST_MODIFIED)
sort_order = 'DESC' # str | The sorting order (optional) (default to DESC)
type_ids = ['type_ids_example'] # list[str] | The list of <code>id</code>s of the attribute types the found attributes should have (optional)

try:
    # Returns attributes matching the given search criteria.
    api_response = api_instance.resource_attribute_resource_find_attributes_get(asset_id=asset_id, limit=limit, offset=offset, sort_field=sort_field, sort_order=sort_order, type_ids=type_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->resource_attribute_resource_find_attributes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the asset to find the attributes in | [optional] 
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]
 **sort_field** | **str**| The field on which the results are sorted | [optional] [default to LAST_MODIFIED]
 **sort_order** | **str**| The sorting order | [optional] [default to DESC]
 **type_ids** | [**list[str]**](str.md)| The list of &lt;code&gt;id&lt;/code&gt;s of the attribute types the found attributes should have | [optional] 

### Return type

[**JsonPagedResponse**](JsonPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_attribute_resource_get_attribute_get**
> JsonAttributeImpl resource_attribute_resource_get_attribute_get(attribute_id)

Returns the attribute identified by given id.

Returns the attribute identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributesApi()
attribute_id = 'attribute_id_example' # str | the <code>id</code> of the attribute

try:
    # Returns the attribute identified by given id.
    api_response = api_instance.resource_attribute_resource_get_attribute_get(attribute_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->resource_attribute_resource_get_attribute_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the attribute | 

### Return type

[**JsonAttributeImpl**](JsonAttributeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_attribute_resource_remove_attribute_delete**
> resource_attribute_resource_remove_attribute_delete(attribute_id)

Removes the attribute identified by given id.

Removes the attribute identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributesApi()
attribute_id = 'attribute_id_example' # str | the <code>id</code> of the attribute to remove

try:
    # Removes the attribute identified by given id.
    api_instance.resource_attribute_resource_remove_attribute_delete(attribute_id)
except ApiException as e:
    print("Exception when calling AttributesApi->resource_attribute_resource_remove_attribute_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the attribute to remove | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_attribute_resource_remove_attributes_delete**
> resource_attribute_resource_remove_attributes_delete(body=body)

Removes the attributes identified by given ids.

Removes the attributes identified by given ids.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttributesApi()
body = [swagger_client.list[str]()] # list[str] | the <code>id</code>s of the attributes to remove (optional)

try:
    # Removes the attributes identified by given ids.
    api_instance.resource_attribute_resource_remove_attributes_delete(body=body)
except ApiException as e:
    print("Exception when calling AttributesApi->resource_attribute_resource_remove_attributes_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**| the &lt;code&gt;id&lt;/code&gt;s of the attributes to remove | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

