# swagger_client.AssetTypesApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_asset_type_resource_add_asset_type_post**](AssetTypesApi.md#resource_asset_type_resource_add_asset_type_post) | **POST** /assetTypes | Adds new asset type.
[**resource_asset_type_resource_add_asset_types_post**](AssetTypesApi.md#resource_asset_type_resource_add_asset_types_post) | **POST** /assetTypes/bulk | Adds multiple asset types.
[**resource_asset_type_resource_change_asset_type_patch**](AssetTypesApi.md#resource_asset_type_resource_change_asset_type_patch) | **PATCH** /assetTypes/{assetTypeId} | Changes the asset type with the information that is present in the request.
[**resource_asset_type_resource_change_asset_types_patch**](AssetTypesApi.md#resource_asset_type_resource_change_asset_types_patch) | **PATCH** /assetTypes/bulk | Changes multiple asset types.
[**resource_asset_type_resource_find_asset_types_get**](AssetTypesApi.md#resource_asset_type_resource_find_asset_types_get) | **GET** /assetTypes | Returns asset types matching the given search criteria.
[**resource_asset_type_resource_find_sub_asset_types_get**](AssetTypesApi.md#resource_asset_type_resource_find_sub_asset_types_get) | **GET** /assetTypes/{assetTypeId}/subTypes | Finds all the sub types of the asset type as described in the request object.
[**resource_asset_type_resource_get_asset_type_get**](AssetTypesApi.md#resource_asset_type_resource_get_asset_type_get) | **GET** /assetTypes/{assetTypeId} | Returns asset type identified by given UUID.
[**resource_asset_type_resource_remove_asset_type_delete**](AssetTypesApi.md#resource_asset_type_resource_remove_asset_type_delete) | **DELETE** /assetTypes/{assetTypeId} | Removes asset type identified by given UUID.
[**resource_asset_type_resource_remove_asset_types_delete**](AssetTypesApi.md#resource_asset_type_resource_remove_asset_types_delete) | **DELETE** /assetTypes/bulk | Removes multiple asset types.


# **resource_asset_type_resource_add_asset_type_post**
> JsonAssetTypeImpl resource_asset_type_resource_add_asset_type_post(body=body)

Adds new asset type.

Adds new asset type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetTypesApi()
body = swagger_client.JsonAddAssetTypeRequest() # JsonAddAssetTypeRequest | the properties of the asset type to be added (optional)

try:
    # Adds new asset type.
    api_response = api_instance.resource_asset_type_resource_add_asset_type_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetTypesApi->resource_asset_type_resource_add_asset_type_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAddAssetTypeRequest**](JsonAddAssetTypeRequest.md)| the properties of the asset type to be added | [optional] 

### Return type

[**JsonAssetTypeImpl**](JsonAssetTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_type_resource_add_asset_types_post**
> list[JsonAssetTypeImpl] resource_asset_type_resource_add_asset_types_post(body=body)

Adds multiple asset types.

Adds multiple asset types.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetTypesApi()
body = [swagger_client.JsonAddAssetTypeRequest()] # list[JsonAddAssetTypeRequest] | the properties of the asset types to be added (optional)

try:
    # Adds multiple asset types.
    api_response = api_instance.resource_asset_type_resource_add_asset_types_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetTypesApi->resource_asset_type_resource_add_asset_types_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonAddAssetTypeRequest]**](JsonAddAssetTypeRequest.md)| the properties of the asset types to be added | [optional] 

### Return type

[**list[JsonAssetTypeImpl]**](JsonAssetTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_type_resource_change_asset_type_patch**
> JsonAssetTypeImpl resource_asset_type_resource_change_asset_type_patch(asset_type_id, body=body)

Changes the asset type with the information that is present in the request.

Changes the asset type with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetTypesApi()
asset_type_id = 'asset_type_id_example' # str | the UUID of the asset type to be changed
body = swagger_client.JsonChangeAssetTypeRequest() # JsonChangeAssetTypeRequest | the properties of the asset type to be changed (optional)

try:
    # Changes the asset type with the information that is present in the request.
    api_response = api_instance.resource_asset_type_resource_change_asset_type_patch(asset_type_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetTypesApi->resource_asset_type_resource_change_asset_type_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_id** | **str**| the UUID of the asset type to be changed | 
 **body** | [**JsonChangeAssetTypeRequest**](JsonChangeAssetTypeRequest.md)| the properties of the asset type to be changed | [optional] 

### Return type

[**JsonAssetTypeImpl**](JsonAssetTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_type_resource_change_asset_types_patch**
> list[JsonAssetTypeImpl] resource_asset_type_resource_change_asset_types_patch(body=body)

Changes multiple asset types.

Changes multiple asset types.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetTypesApi()
body = [swagger_client.JsonChangeAssetTypeRequest()] # list[JsonChangeAssetTypeRequest] | the properties of the asset types to be changed (optional)

try:
    # Changes multiple asset types.
    api_response = api_instance.resource_asset_type_resource_change_asset_types_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetTypesApi->resource_asset_type_resource_change_asset_types_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonChangeAssetTypeRequest]**](JsonChangeAssetTypeRequest.md)| the properties of the asset types to be changed | [optional] 

### Return type

[**list[JsonAssetTypeImpl]**](JsonAssetTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_type_resource_find_asset_types_get**
> JsonPagedResponse resource_asset_type_resource_find_asset_types_get(exclude_meta=exclude_meta, limit=limit, name=name, name_match_mode=name_match_mode, offset=offset, parent_id=parent_id, top_level=top_level)

Returns asset types matching the given search criteria.

Returns asset types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned asset types satisfy all constraints that are specified in this search criteria. By default a result containing 1000 asset types is returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetTypesApi()
exclude_meta = true # bool | Whether the meta asset types should be excluded from search or not (optional) (default to true)
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
name = 'name_example' # str | The name of the asset type to search for (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code> (optional) (default to ANYWHERE)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)
parent_id = 'parent_id_example' # str | The <code>id</code> of the parent to find the asset types in (optional)
top_level = false # bool | Whether only top level asset types should be searched or not (optional) (default to false)

try:
    # Returns asset types matching the given search criteria.
    api_response = api_instance.resource_asset_type_resource_find_asset_types_get(exclude_meta=exclude_meta, limit=limit, name=name, name_match_mode=name_match_mode, offset=offset, parent_id=parent_id, top_level=top_level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetTypesApi->resource_asset_type_resource_find_asset_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exclude_meta** | **bool**| Whether the meta asset types should be excluded from search or not | [optional] [default to true]
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **name** | **str**| The name of the asset type to search for | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt; | [optional] [default to ANYWHERE]
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]
 **parent_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the parent to find the asset types in | [optional] 
 **top_level** | **bool**| Whether only top level asset types should be searched or not | [optional] [default to false]

### Return type

[**JsonPagedResponse**](JsonPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_type_resource_find_sub_asset_types_get**
> JsonPagedResponse resource_asset_type_resource_find_sub_asset_types_get(asset_type_id, include_parent=include_parent)

Finds all the sub types of the asset type as described in the request object.

Finds all the sub types of the asset type as described in the request object.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetTypesApi()
asset_type_id = 'asset_type_id_example' # str | 
include_parent = true # bool | Whether parent asset type should be included in the search result (optional)

try:
    # Finds all the sub types of the asset type as described in the request object.
    api_response = api_instance.resource_asset_type_resource_find_sub_asset_types_get(asset_type_id, include_parent=include_parent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetTypesApi->resource_asset_type_resource_find_sub_asset_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_id** | **str**|  | 
 **include_parent** | **bool**| Whether parent asset type should be included in the search result | [optional] 

### Return type

[**JsonPagedResponse**](JsonPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_type_resource_get_asset_type_get**
> JsonAssetTypeImpl resource_asset_type_resource_get_asset_type_get(asset_type_id)

Returns asset type identified by given UUID.

Returns asset type identified by given UUID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetTypesApi()
asset_type_id = 'asset_type_id_example' # str | the UUID of the asset type

try:
    # Returns asset type identified by given UUID.
    api_response = api_instance.resource_asset_type_resource_get_asset_type_get(asset_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetTypesApi->resource_asset_type_resource_get_asset_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_id** | **str**| the UUID of the asset type | 

### Return type

[**JsonAssetTypeImpl**](JsonAssetTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_type_resource_remove_asset_type_delete**
> resource_asset_type_resource_remove_asset_type_delete(asset_type_id)

Removes asset type identified by given UUID.

Removes asset type identified by given UUID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetTypesApi()
asset_type_id = 'asset_type_id_example' # str | the UUID of the asset type

try:
    # Removes asset type identified by given UUID.
    api_instance.resource_asset_type_resource_remove_asset_type_delete(asset_type_id)
except ApiException as e:
    print("Exception when calling AssetTypesApi->resource_asset_type_resource_remove_asset_type_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_id** | **str**| the UUID of the asset type | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_type_resource_remove_asset_types_delete**
> resource_asset_type_resource_remove_asset_types_delete(body=body)

Removes multiple asset types.

Removes multiple asset types.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetTypesApi()
body = [swagger_client.list[str]()] # list[str] | the UUIDs of the asset types to be removed, i.e. [“6f685f90-1036-4d30-983a-a9bbcdd7b8f6”,\"174b6334-9804-495d-b659-43f53a5de8b8\"] (optional)

try:
    # Removes multiple asset types.
    api_instance.resource_asset_type_resource_remove_asset_types_delete(body=body)
except ApiException as e:
    print("Exception when calling AssetTypesApi->resource_asset_type_resource_remove_asset_types_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**| the UUIDs of the asset types to be removed, i.e. [“6f685f90-1036-4d30-983a-a9bbcdd7b8f6”,\&quot;174b6334-9804-495d-b659-43f53a5de8b8\&quot;] | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

