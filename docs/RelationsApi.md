# swagger_client.RelationsApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_relation_resource_add_relation_post**](RelationsApi.md#resource_relation_resource_add_relation_post) | **POST** /relations | Adds a new relation.
[**resource_relation_resource_add_relations_post**](RelationsApi.md#resource_relation_resource_add_relations_post) | **POST** /relations/bulk | Adds multiple relations in one go.
[**resource_relation_resource_change_relation_patch**](RelationsApi.md#resource_relation_resource_change_relation_patch) | **PATCH** /relations/{relationId} | Change the relation with the information that is present in the request.
[**resource_relation_resource_change_relations_patch**](RelationsApi.md#resource_relation_resource_change_relations_patch) | **PATCH** /relations/bulk | Changes multiple relations with the information that is present in the request.
[**resource_relation_resource_find_relations_get**](RelationsApi.md#resource_relation_resource_find_relations_get) | **GET** /relations | Returns relations matching the given search criteria.
[**resource_relation_resource_get_relation_get**](RelationsApi.md#resource_relation_resource_get_relation_get) | **GET** /relations/{relationId} | Returns an relation identified by given id.
[**resource_relation_resource_remove_relation_delete**](RelationsApi.md#resource_relation_resource_remove_relation_delete) | **DELETE** /relations/bulk | Removes relations identified by given ids.
[**resource_relation_resource_remove_relation_delete_0**](RelationsApi.md#resource_relation_resource_remove_relation_delete_0) | **DELETE** /relations/{relationId} | Removes an relation identified by given id.


# **resource_relation_resource_add_relation_post**
> JsonRelationImpl resource_relation_resource_add_relation_post(body=body)

Adds a new relation.

Adds a new relation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationsApi()
body = swagger_client.JsonAddRelationRequest() # JsonAddRelationRequest | the properties of the relation to be added (optional)

try:
    # Adds a new relation.
    api_response = api_instance.resource_relation_resource_add_relation_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationsApi->resource_relation_resource_add_relation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAddRelationRequest**](JsonAddRelationRequest.md)| the properties of the relation to be added | [optional] 

### Return type

[**JsonRelationImpl**](JsonRelationImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_relation_resource_add_relations_post**
> JsonRelationImpl resource_relation_resource_add_relations_post(body=body)

Adds multiple relations in one go.

Adds multiple relations in one go.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationsApi()
body = [swagger_client.JsonAddRelationRequest()] # list[JsonAddRelationRequest] | the list of properties of the relations to be added (optional)

try:
    # Adds multiple relations in one go.
    api_response = api_instance.resource_relation_resource_add_relations_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationsApi->resource_relation_resource_add_relations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonAddRelationRequest]**](JsonAddRelationRequest.md)| the list of properties of the relations to be added | [optional] 

### Return type

[**JsonRelationImpl**](JsonRelationImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_relation_resource_change_relation_patch**
> JsonRelationImpl resource_relation_resource_change_relation_patch(relation_id, body=body)

Change the relation with the information that is present in the request.

Change the relation with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationsApi()
relation_id = 'relation_id_example' # str | the <code>id</code> of the relation to be changed.
body = swagger_client.JsonChangeRelationRequest() # JsonChangeRelationRequest | the properties of the relation to be changed (optional)

try:
    # Change the relation with the information that is present in the request.
    api_response = api_instance.resource_relation_resource_change_relation_patch(relation_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationsApi->resource_relation_resource_change_relation_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the relation to be changed. | 
 **body** | [**JsonChangeRelationRequest**](JsonChangeRelationRequest.md)| the properties of the relation to be changed | [optional] 

### Return type

[**JsonRelationImpl**](JsonRelationImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_relation_resource_change_relations_patch**
> list[JsonRelationImpl] resource_relation_resource_change_relations_patch(body=body)

Changes multiple relations with the information that is present in the request.

Changes multiple relations with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationsApi()
body = [swagger_client.JsonChangeRelationRequest()] # list[JsonChangeRelationRequest] | the list of properties of the relations to be changed (optional)

try:
    # Changes multiple relations with the information that is present in the request.
    api_response = api_instance.resource_relation_resource_change_relations_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationsApi->resource_relation_resource_change_relations_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonChangeRelationRequest]**](JsonChangeRelationRequest.md)| the list of properties of the relations to be changed | [optional] 

### Return type

[**list[JsonRelationImpl]**](JsonRelationImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_relation_resource_find_relations_get**
> JsonPagedResponse resource_relation_resource_find_relations_get(limit=limit, offset=offset, relation_type_id=relation_type_id, source_id=source_id, source_target_logical_operator=source_target_logical_operator, target_id=target_id)

Returns relations matching the given search criteria.

Returns relations matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned relations satisfy all constraints that are specified in this search criteria. By default a result containing 1000 relations is returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationsApi()
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)
relation_type_id = 'relation_type_id_example' # str | The <code>id</code> of the type of relations to search for (optional)
source_id = 'source_id_example' # str | The <code>id</code> of the source of relations to search for (optional)
source_target_logical_operator = 'AND' # str | The logical operator determining how to combine the source and target criteria: AND or OR (optional) (default to AND)
target_id = 'target_id_example' # str | The <code>id</code> of the target of relations to search for (optional)

try:
    # Returns relations matching the given search criteria.
    api_response = api_instance.resource_relation_resource_find_relations_get(limit=limit, offset=offset, relation_type_id=relation_type_id, source_id=source_id, source_target_logical_operator=source_target_logical_operator, target_id=target_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationsApi->resource_relation_resource_find_relations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]
 **relation_type_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the type of relations to search for | [optional] 
 **source_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the source of relations to search for | [optional] 
 **source_target_logical_operator** | **str**| The logical operator determining how to combine the source and target criteria: AND or OR | [optional] [default to AND]
 **target_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the target of relations to search for | [optional] 

### Return type

[**JsonPagedResponse**](JsonPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_relation_resource_get_relation_get**
> JsonRelationImpl resource_relation_resource_get_relation_get(relation_id)

Returns an relation identified by given id.

Returns an relation identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationsApi()
relation_id = 'relation_id_example' # str | the <code>id</code> of the relation

try:
    # Returns an relation identified by given id.
    api_response = api_instance.resource_relation_resource_get_relation_get(relation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationsApi->resource_relation_resource_get_relation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the relation | 

### Return type

[**JsonRelationImpl**](JsonRelationImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_relation_resource_remove_relation_delete**
> resource_relation_resource_remove_relation_delete(body=body)

Removes relations identified by given ids.

Removes relations identified by given ids.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationsApi()
body = [swagger_client.list[str]()] # list[str] | the list of <code>id</code>s of the relations to remove (optional)

try:
    # Removes relations identified by given ids.
    api_instance.resource_relation_resource_remove_relation_delete(body=body)
except ApiException as e:
    print("Exception when calling RelationsApi->resource_relation_resource_remove_relation_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**| the list of &lt;code&gt;id&lt;/code&gt;s of the relations to remove | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_relation_resource_remove_relation_delete_0**
> resource_relation_resource_remove_relation_delete_0(relation_id)

Removes an relation identified by given id.

Removes an relation identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationsApi()
relation_id = 'relation_id_example' # str | the <code>id</code> of the relation to remove

try:
    # Removes an relation identified by given id.
    api_instance.resource_relation_resource_remove_relation_delete_0(relation_id)
except ApiException as e:
    print("Exception when calling RelationsApi->resource_relation_resource_remove_relation_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the relation to remove | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

