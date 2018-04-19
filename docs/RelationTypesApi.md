# swagger_client.RelationTypesApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_relation_type_resource_add_relation_type_post**](RelationTypesApi.md#resource_relation_type_resource_add_relation_type_post) | **POST** /relationTypes | Adds new relation type.
[**resource_relation_type_resource_add_relation_types_post**](RelationTypesApi.md#resource_relation_type_resource_add_relation_types_post) | **POST** /relationTypes/bulk | Adds multiple relation types.
[**resource_relation_type_resource_change_relation_type_patch**](RelationTypesApi.md#resource_relation_type_resource_change_relation_type_patch) | **PATCH** /relationTypes/{relationTypeId} | Changes the relation type with the information that is present in the request.
[**resource_relation_type_resource_change_relation_types_patch**](RelationTypesApi.md#resource_relation_type_resource_change_relation_types_patch) | **PATCH** /relationTypes/bulk | Changes multiple relation types.
[**resource_relation_type_resource_find_relation_types_get**](RelationTypesApi.md#resource_relation_type_resource_find_relation_types_get) | **GET** /relationTypes | Returns relation types matching the given search criteria.
[**resource_relation_type_resource_get_relation_type_get**](RelationTypesApi.md#resource_relation_type_resource_get_relation_type_get) | **GET** /relationTypes/{relationTypeId} | Returns relation type identified by given id.
[**resource_relation_type_resource_remove_relation_type_delete**](RelationTypesApi.md#resource_relation_type_resource_remove_relation_type_delete) | **DELETE** /relationTypes/{relationTypeId} | Removes relation type identified by given id.
[**resource_relation_type_resource_remove_relation_types_delete**](RelationTypesApi.md#resource_relation_type_resource_remove_relation_types_delete) | **DELETE** /relationTypes/bulk | Removes multiple relation types.


# **resource_relation_type_resource_add_relation_type_post**
> JsonRelationTypeImpl resource_relation_type_resource_add_relation_type_post(body=body)

Adds new relation type.

Adds new relation type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationTypesApi()
body = swagger_client.JsonAddRelationTypeRequest() # JsonAddRelationTypeRequest | the properties of the relation type to be added (optional)

try:
    # Adds new relation type.
    api_response = api_instance.resource_relation_type_resource_add_relation_type_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationTypesApi->resource_relation_type_resource_add_relation_type_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAddRelationTypeRequest**](JsonAddRelationTypeRequest.md)| the properties of the relation type to be added | [optional] 

### Return type

[**JsonRelationTypeImpl**](JsonRelationTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_relation_type_resource_add_relation_types_post**
> list[JsonRelationTypeImpl] resource_relation_type_resource_add_relation_types_post(body=body)

Adds multiple relation types.

Adds multiple relation types.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationTypesApi()
body = [swagger_client.JsonAddRelationTypeRequest()] # list[JsonAddRelationTypeRequest] | the properties of the relation types to be added (optional)

try:
    # Adds multiple relation types.
    api_response = api_instance.resource_relation_type_resource_add_relation_types_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationTypesApi->resource_relation_type_resource_add_relation_types_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonAddRelationTypeRequest]**](JsonAddRelationTypeRequest.md)| the properties of the relation types to be added | [optional] 

### Return type

[**list[JsonRelationTypeImpl]**](JsonRelationTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_relation_type_resource_change_relation_type_patch**
> JsonRelationTypeImpl resource_relation_type_resource_change_relation_type_patch(relation_type_id, body=body)

Changes the relation type with the information that is present in the request.

Changes the relation type with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationTypesApi()
relation_type_id = 'relation_type_id_example' # str | the <code>id</code> of the relation type to be changed
body = swagger_client.JsonChangeRelationTypeRequest() # JsonChangeRelationTypeRequest | the properties of the relation type to be changed (optional)

try:
    # Changes the relation type with the information that is present in the request.
    api_response = api_instance.resource_relation_type_resource_change_relation_type_patch(relation_type_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationTypesApi->resource_relation_type_resource_change_relation_type_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_type_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the relation type to be changed | 
 **body** | [**JsonChangeRelationTypeRequest**](JsonChangeRelationTypeRequest.md)| the properties of the relation type to be changed | [optional] 

### Return type

[**JsonRelationTypeImpl**](JsonRelationTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_relation_type_resource_change_relation_types_patch**
> list[JsonRelationTypeImpl] resource_relation_type_resource_change_relation_types_patch(body=body)

Changes multiple relation types.

Changes multiple relation types.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationTypesApi()
body = [swagger_client.JsonChangeRelationTypeRequest()] # list[JsonChangeRelationTypeRequest] | the properties of the relation types to be changed (optional)

try:
    # Changes multiple relation types.
    api_response = api_instance.resource_relation_type_resource_change_relation_types_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationTypesApi->resource_relation_type_resource_change_relation_types_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonChangeRelationTypeRequest]**](JsonChangeRelationTypeRequest.md)| the properties of the relation types to be changed | [optional] 

### Return type

[**list[JsonRelationTypeImpl]**](JsonRelationTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_relation_type_resource_find_relation_types_get**
> JsonPagedResponse resource_relation_type_resource_find_relation_types_get(co_role=co_role, limit=limit, offset=offset, role=role, role_co_role_logical_operator=role_co_role_logical_operator, sort_field=sort_field, sort_order=sort_order, source_type_id=source_type_id, source_type_name=source_type_name, target_type_id=target_type_id, target_type_name=target_type_name)

Returns relation types matching the given search criteria.

Returns relation types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned relation types satisfy all constraints that are specified in this search criteria. By default a result containing 1000 relation types is returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationTypesApi()
co_role = 'co_role_example' # str | The name of the role that the target plays to search for (optional)
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)
role = 'role_example' # str | The name of the role that the source plays to search for (optional)
role_co_role_logical_operator = 'AND' # str | The logical operator determining how to combine the role and coRole criteria: AND or OR (optional) (default to AND)
sort_field = 'ROLE' # str | The field that should be used as reference for sorting (optional) (default to ROLE)
sort_order = 'ASC' # str | The order of sorting (optional) (default to ASC)
source_type_id = 'source_type_id_example' # str | The <code>id</code> of the source type of the relation type to search for (optional)
source_type_name = 'source_type_name_example' # str | The name of the source type of the relation type to search for (optional)
target_type_id = 'target_type_id_example' # str | The <code>id</code> of the target type of the relation type to search for (optional)
target_type_name = 'target_type_name_example' # str | The name of the target type of the relation type to search for (optional)

try:
    # Returns relation types matching the given search criteria.
    api_response = api_instance.resource_relation_type_resource_find_relation_types_get(co_role=co_role, limit=limit, offset=offset, role=role, role_co_role_logical_operator=role_co_role_logical_operator, sort_field=sort_field, sort_order=sort_order, source_type_id=source_type_id, source_type_name=source_type_name, target_type_id=target_type_id, target_type_name=target_type_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationTypesApi->resource_relation_type_resource_find_relation_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **co_role** | **str**| The name of the role that the target plays to search for | [optional] 
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]
 **role** | **str**| The name of the role that the source plays to search for | [optional] 
 **role_co_role_logical_operator** | **str**| The logical operator determining how to combine the role and coRole criteria: AND or OR | [optional] [default to AND]
 **sort_field** | **str**| The field that should be used as reference for sorting | [optional] [default to ROLE]
 **sort_order** | **str**| The order of sorting | [optional] [default to ASC]
 **source_type_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the source type of the relation type to search for | [optional] 
 **source_type_name** | **str**| The name of the source type of the relation type to search for | [optional] 
 **target_type_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the target type of the relation type to search for | [optional] 
 **target_type_name** | **str**| The name of the target type of the relation type to search for | [optional] 

### Return type

[**JsonPagedResponse**](JsonPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_relation_type_resource_get_relation_type_get**
> JsonRelationTypeImpl resource_relation_type_resource_get_relation_type_get(relation_type_id)

Returns relation type identified by given id.

Returns relation type identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationTypesApi()
relation_type_id = 'relation_type_id_example' # str | the <code>id</code> of the relation type

try:
    # Returns relation type identified by given id.
    api_response = api_instance.resource_relation_type_resource_get_relation_type_get(relation_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationTypesApi->resource_relation_type_resource_get_relation_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_type_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the relation type | 

### Return type

[**JsonRelationTypeImpl**](JsonRelationTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_relation_type_resource_remove_relation_type_delete**
> resource_relation_type_resource_remove_relation_type_delete(relation_type_id)

Removes relation type identified by given id.

Removes relation type identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationTypesApi()
relation_type_id = 'relation_type_id_example' # str | the <code>id</code> of the relation type

try:
    # Removes relation type identified by given id.
    api_instance.resource_relation_type_resource_remove_relation_type_delete(relation_type_id)
except ApiException as e:
    print("Exception when calling RelationTypesApi->resource_relation_type_resource_remove_relation_type_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_type_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the relation type | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_relation_type_resource_remove_relation_types_delete**
> resource_relation_type_resource_remove_relation_types_delete(body=body)

Removes multiple relation types.

Removes multiple relation types.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationTypesApi()
body = [swagger_client.list[str]()] # list[str] | the <code>id</code>s of the relation types to be removed, i.e. [\"6f685f90-1036-4d30-983a-a9bbcdd7b8f6\", \"6f685f90-1036-4d30-983a-a9bbcdd7b123\"] (optional)

try:
    # Removes multiple relation types.
    api_instance.resource_relation_type_resource_remove_relation_types_delete(body=body)
except ApiException as e:
    print("Exception when calling RelationTypesApi->resource_relation_type_resource_remove_relation_types_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**| the &lt;code&gt;id&lt;/code&gt;s of the relation types to be removed, i.e. [\&quot;6f685f90-1036-4d30-983a-a9bbcdd7b8f6\&quot;, \&quot;6f685f90-1036-4d30-983a-a9bbcdd7b123\&quot;] | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

