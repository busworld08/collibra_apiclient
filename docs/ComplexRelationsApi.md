# swagger_client.ComplexRelationsApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_complex_relation_resource_add_complex_relation_post**](ComplexRelationsApi.md#resource_complex_relation_resource_add_complex_relation_post) | **POST** /complexRelations | Adds new complex relation.
[**resource_complex_relation_resource_change_complex_relation_patch**](ComplexRelationsApi.md#resource_complex_relation_resource_change_complex_relation_patch) | **PATCH** /complexRelations/{complexRelationId} | Change the complex relation with the information that is present in the request.
[**resource_complex_relation_resource_find_complex_relations_get**](ComplexRelationsApi.md#resource_complex_relation_resource_find_complex_relations_get) | **GET** /complexRelations | Returns complex relations matching the given search criteria.
[**resource_complex_relation_resource_get_complex_relation_get**](ComplexRelationsApi.md#resource_complex_relation_resource_get_complex_relation_get) | **GET** /complexRelations/{complexRelationId} | Returns complex relation identified by given id.
[**resource_complex_relation_resource_remove_complex_relation_delete**](ComplexRelationsApi.md#resource_complex_relation_resource_remove_complex_relation_delete) | **DELETE** /complexRelations/{complexRelationId} | Removes complex relation identified by given id.


# **resource_complex_relation_resource_add_complex_relation_post**
> JsonComplexRelationImpl resource_complex_relation_resource_add_complex_relation_post(body=body)

Adds new complex relation.

Adds new complex relation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComplexRelationsApi()
body = swagger_client.JsonAddComplexRelationRequest() # JsonAddComplexRelationRequest | the properties of the complex relation to be added (optional)

try:
    # Adds new complex relation.
    api_response = api_instance.resource_complex_relation_resource_add_complex_relation_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplexRelationsApi->resource_complex_relation_resource_add_complex_relation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAddComplexRelationRequest**](JsonAddComplexRelationRequest.md)| the properties of the complex relation to be added | [optional] 

### Return type

[**JsonComplexRelationImpl**](JsonComplexRelationImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_complex_relation_resource_change_complex_relation_patch**
> JsonComplexRelationImpl resource_complex_relation_resource_change_complex_relation_patch(complex_relation_id, body=body)

Change the complex relation with the information that is present in the request.

Change the complex relation with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComplexRelationsApi()
complex_relation_id = 'complex_relation_id_example' # str | the <code>id</code> of the complex relation to be changed.
body = swagger_client.JsonChangeComplexRelationRequest() # JsonChangeComplexRelationRequest | the properties of the complex relation to be changed (optional)

try:
    # Change the complex relation with the information that is present in the request.
    api_response = api_instance.resource_complex_relation_resource_change_complex_relation_patch(complex_relation_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplexRelationsApi->resource_complex_relation_resource_change_complex_relation_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complex_relation_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the complex relation to be changed. | 
 **body** | [**JsonChangeComplexRelationRequest**](JsonChangeComplexRelationRequest.md)| the properties of the complex relation to be changed | [optional] 

### Return type

[**JsonComplexRelationImpl**](JsonComplexRelationImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_complex_relation_resource_find_complex_relations_get**
> JsonComplexRelationImpl resource_complex_relation_resource_find_complex_relations_get(asset_id=asset_id, limit=limit, offset=offset, type_id=type_id)

Returns complex relations matching the given search criteria.

Returns complex relations matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned complex relations satisfy all constraints that are specified in this search criteria. By default a result containing 1000 complex relations is returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComplexRelationsApi()
asset_id = 'asset_id_example' # str | The <code>id</code> of the asset for which complex relations should be found (optional)
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)
type_id = 'type_id_example' # str | The <code>id</code> of the type of complex relations to search for (optional)

try:
    # Returns complex relations matching the given search criteria.
    api_response = api_instance.resource_complex_relation_resource_find_complex_relations_get(asset_id=asset_id, limit=limit, offset=offset, type_id=type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplexRelationsApi->resource_complex_relation_resource_find_complex_relations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the asset for which complex relations should be found | [optional] 
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]
 **type_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the type of complex relations to search for | [optional] 

### Return type

[**JsonComplexRelationImpl**](JsonComplexRelationImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_complex_relation_resource_get_complex_relation_get**
> JsonComplexRelationImpl resource_complex_relation_resource_get_complex_relation_get(complex_relation_id)

Returns complex relation identified by given id.

Returns complex relation identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComplexRelationsApi()
complex_relation_id = 'complex_relation_id_example' # str | the <code>id</code> of the complex relation

try:
    # Returns complex relation identified by given id.
    api_response = api_instance.resource_complex_relation_resource_get_complex_relation_get(complex_relation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplexRelationsApi->resource_complex_relation_resource_get_complex_relation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complex_relation_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the complex relation | 

### Return type

[**JsonComplexRelationImpl**](JsonComplexRelationImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_complex_relation_resource_remove_complex_relation_delete**
> resource_complex_relation_resource_remove_complex_relation_delete(complex_relation_id)

Removes complex relation identified by given id.

Removes complex relation identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComplexRelationsApi()
complex_relation_id = 'complex_relation_id_example' # str | the <code>id</code> of the complex relation to remove

try:
    # Removes complex relation identified by given id.
    api_instance.resource_complex_relation_resource_remove_complex_relation_delete(complex_relation_id)
except ApiException as e:
    print("Exception when calling ComplexRelationsApi->resource_complex_relation_resource_remove_complex_relation_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complex_relation_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the complex relation to remove | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

