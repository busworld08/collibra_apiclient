# swagger_client.ComplexRelationTypesApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_complex_relation_type_resource_add_complex_relation_type_post**](ComplexRelationTypesApi.md#resource_complex_relation_type_resource_add_complex_relation_type_post) | **POST** /complexRelationTypes | Adds new complex relation type.
[**resource_complex_relation_type_resource_change_relation_type_patch**](ComplexRelationTypesApi.md#resource_complex_relation_type_resource_change_relation_type_patch) | **PATCH** /complexRelationTypes/{complexRelationTypeId} | Changes the complex relation type with the information that is present in the request.
[**resource_complex_relation_type_resource_get_all_complex_relation_types_get**](ComplexRelationTypesApi.md#resource_complex_relation_type_resource_get_all_complex_relation_types_get) | **GET** /complexRelationTypes | Returns all complex relation types.
[**resource_complex_relation_type_resource_get_complex_relation_type_get**](ComplexRelationTypesApi.md#resource_complex_relation_type_resource_get_complex_relation_type_get) | **GET** /complexRelationTypes/{complexRelationTypeId} | Returns complex relation type identified by given id.
[**resource_complex_relation_type_resource_remove_complex_relation_type_delete**](ComplexRelationTypesApi.md#resource_complex_relation_type_resource_remove_complex_relation_type_delete) | **DELETE** /complexRelationTypes/{complexRelationTypeId} | Removes complex relation type identified by given id.


# **resource_complex_relation_type_resource_add_complex_relation_type_post**
> JsonComplexRelationTypeImpl resource_complex_relation_type_resource_add_complex_relation_type_post(body=body)

Adds new complex relation type.

Adds new complex relation type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComplexRelationTypesApi()
body = swagger_client.JsonAddComplexRelationTypeRequest() # JsonAddComplexRelationTypeRequest | the properties of the complex relation type to be added (optional)

try:
    # Adds new complex relation type.
    api_response = api_instance.resource_complex_relation_type_resource_add_complex_relation_type_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplexRelationTypesApi->resource_complex_relation_type_resource_add_complex_relation_type_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAddComplexRelationTypeRequest**](JsonAddComplexRelationTypeRequest.md)| the properties of the complex relation type to be added | [optional] 

### Return type

[**JsonComplexRelationTypeImpl**](JsonComplexRelationTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_complex_relation_type_resource_change_relation_type_patch**
> JsonComplexRelationTypeImpl resource_complex_relation_type_resource_change_relation_type_patch(complex_relation_type_id, body=body)

Changes the complex relation type with the information that is present in the request.

Changes the complex relation type with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComplexRelationTypesApi()
complex_relation_type_id = 'complex_relation_type_id_example' # str | the <code>id</code> of the complex relation type to be changed
body = swagger_client.JsonChangeComplexRelationTypeRequest() # JsonChangeComplexRelationTypeRequest | the properties of the complex relation type to be changed (optional)

try:
    # Changes the complex relation type with the information that is present in the request.
    api_response = api_instance.resource_complex_relation_type_resource_change_relation_type_patch(complex_relation_type_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplexRelationTypesApi->resource_complex_relation_type_resource_change_relation_type_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complex_relation_type_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the complex relation type to be changed | 
 **body** | [**JsonChangeComplexRelationTypeRequest**](JsonChangeComplexRelationTypeRequest.md)| the properties of the complex relation type to be changed | [optional] 

### Return type

[**JsonComplexRelationTypeImpl**](JsonComplexRelationTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_complex_relation_type_resource_get_all_complex_relation_types_get**
> JsonPagedResponse resource_complex_relation_type_resource_get_all_complex_relation_types_get()

Returns all complex relation types.

Returns all complex relation types.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComplexRelationTypesApi()

try:
    # Returns all complex relation types.
    api_response = api_instance.resource_complex_relation_type_resource_get_all_complex_relation_types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplexRelationTypesApi->resource_complex_relation_type_resource_get_all_complex_relation_types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonPagedResponse**](JsonPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_complex_relation_type_resource_get_complex_relation_type_get**
> JsonComplexRelationTypeImpl resource_complex_relation_type_resource_get_complex_relation_type_get(complex_relation_type_id)

Returns complex relation type identified by given id.

Returns complex relation type identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComplexRelationTypesApi()
complex_relation_type_id = 'complex_relation_type_id_example' # str | the <code>id</code> of the complex relation type

try:
    # Returns complex relation type identified by given id.
    api_response = api_instance.resource_complex_relation_type_resource_get_complex_relation_type_get(complex_relation_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComplexRelationTypesApi->resource_complex_relation_type_resource_get_complex_relation_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complex_relation_type_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the complex relation type | 

### Return type

[**JsonComplexRelationTypeImpl**](JsonComplexRelationTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_complex_relation_type_resource_remove_complex_relation_type_delete**
> resource_complex_relation_type_resource_remove_complex_relation_type_delete(complex_relation_type_id)

Removes complex relation type identified by given id.

Removes complex relation type identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComplexRelationTypesApi()
complex_relation_type_id = 'complex_relation_type_id_example' # str | the <code>id</code> of the complex relation type

try:
    # Removes complex relation type identified by given id.
    api_instance.resource_complex_relation_type_resource_remove_complex_relation_type_delete(complex_relation_type_id)
except ApiException as e:
    print("Exception when calling ComplexRelationTypesApi->resource_complex_relation_type_resource_remove_complex_relation_type_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complex_relation_type_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the complex relation type | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

