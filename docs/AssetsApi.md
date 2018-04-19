# swagger_client.AssetsApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_asset_resource_add_asset_post**](AssetsApi.md#resource_asset_resource_add_asset_post) | **POST** /assets | Adds a new asset into a domain.
[**resource_asset_resource_add_assets_post**](AssetsApi.md#resource_asset_resource_add_assets_post) | **POST** /assets/bulk | Adds multiple assets.
[**resource_asset_resource_add_tags_to_asset_post**](AssetsApi.md#resource_asset_resource_add_tags_to_asset_post) | **POST** /assets/{assetId}/tags | Adds tags to given asset.
[**resource_asset_resource_change_asset_patch**](AssetsApi.md#resource_asset_resource_change_asset_patch) | **PATCH** /assets/{assetId} | Change the asset with the information that is present in the request.
[**resource_asset_resource_change_assets_patch**](AssetsApi.md#resource_asset_resource_change_assets_patch) | **PATCH** /assets/bulk | Changes multiple assets.
[**resource_asset_resource_find_assets_get**](AssetsApi.md#resource_asset_resource_find_assets_get) | **GET** /assets | Returns assets matching the given search criteria.
[**resource_asset_resource_get_asset_get**](AssetsApi.md#resource_asset_resource_get_asset_get) | **GET** /assets/{assetId} | Returns an asset identified by given id.
[**resource_asset_resource_get_asset_tags_get**](AssetsApi.md#resource_asset_resource_get_asset_tags_get) | **GET** /assets/{assetId}/tags | Returns all tags of given asset.
[**resource_asset_resource_remove_asset_delete**](AssetsApi.md#resource_asset_resource_remove_asset_delete) | **DELETE** /assets/{assetId} | Removes an asset identified by given id.
[**resource_asset_resource_remove_assets_delete**](AssetsApi.md#resource_asset_resource_remove_assets_delete) | **DELETE** /assets/bulk | Removes multiple assets.
[**resource_asset_resource_remove_tags_from_asset_delete**](AssetsApi.md#resource_asset_resource_remove_tags_from_asset_delete) | **DELETE** /assets/{assetId}/tags | Remove tags from given asset.
[**resource_asset_resource_set_asset_attributes_put**](AssetsApi.md#resource_asset_resource_set_asset_attributes_put) | **PUT** /assets/{assetId}/attributes | Replaces all the attributes of the asset (of given attribute type) with the attributes from the request, except matching attributes, these are retained.
[**resource_asset_resource_set_asset_relations_put**](AssetsApi.md#resource_asset_resource_set_asset_relations_put) | **PUT** /assets/{assetId}/relations | Sets relations for given asset.
[**resource_asset_resource_set_asset_responsibilities_put**](AssetsApi.md#resource_asset_resource_set_asset_responsibilities_put) | **PUT** /assets/{assetId}/responsibilities | Sets responsibilities for given asset.
[**resource_asset_resource_set_tags_for_asset_put**](AssetsApi.md#resource_asset_resource_set_tags_for_asset_put) | **PUT** /assets/{assetId}/tags | Sets tags for given asset.


# **resource_asset_resource_add_asset_post**
> JsonAssetImpl resource_asset_resource_add_asset_post(body=body)

Adds a new asset into a domain.

Adds a new asset into a domain.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
body = swagger_client.JsonAddAssetRequest() # JsonAddAssetRequest | the properties of the asset to be added (optional)

try:
    # Adds a new asset into a domain.
    api_response = api_instance.resource_asset_resource_add_asset_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->resource_asset_resource_add_asset_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAddAssetRequest**](JsonAddAssetRequest.md)| the properties of the asset to be added | [optional] 

### Return type

[**JsonAssetImpl**](JsonAssetImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_resource_add_assets_post**
> list[JsonAssetImpl] resource_asset_resource_add_assets_post(body=body)

Adds multiple assets.

Adds multiple assets.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
body = [swagger_client.JsonAddAssetRequest()] # list[JsonAddAssetRequest] | the properties of the assets to be added (optional)

try:
    # Adds multiple assets.
    api_response = api_instance.resource_asset_resource_add_assets_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->resource_asset_resource_add_assets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonAddAssetRequest]**](JsonAddAssetRequest.md)| the properties of the assets to be added | [optional] 

### Return type

[**list[JsonAssetImpl]**](JsonAssetImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_resource_add_tags_to_asset_post**
> list[JsonTagImpl] resource_asset_resource_add_tags_to_asset_post(asset_id, body=body)

Adds tags to given asset.

Adds tags to given asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
asset_id = 'asset_id_example' # str | the <code>id</code> of the asset
body = swagger_client.JsonAddAssetTagsRequest() # JsonAddAssetTagsRequest | the tags to be added to given asset (optional)

try:
    # Adds tags to given asset.
    api_response = api_instance.resource_asset_resource_add_tags_to_asset_post(asset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->resource_asset_resource_add_tags_to_asset_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the asset | 
 **body** | [**JsonAddAssetTagsRequest**](JsonAddAssetTagsRequest.md)| the tags to be added to given asset | [optional] 

### Return type

[**list[JsonTagImpl]**](JsonTagImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_resource_change_asset_patch**
> JsonAssetImpl resource_asset_resource_change_asset_patch(asset_id, body=body)

Change the asset with the information that is present in the request.

Change the asset with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
asset_id = 'asset_id_example' # str | the <code>id</code> of the asset to be changed.
body = swagger_client.JsonChangeAssetRequest() # JsonChangeAssetRequest | the properties of the asset to be changed (optional)

try:
    # Change the asset with the information that is present in the request.
    api_response = api_instance.resource_asset_resource_change_asset_patch(asset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->resource_asset_resource_change_asset_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the asset to be changed. | 
 **body** | [**JsonChangeAssetRequest**](JsonChangeAssetRequest.md)| the properties of the asset to be changed | [optional] 

### Return type

[**JsonAssetImpl**](JsonAssetImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_resource_change_assets_patch**
> list[JsonAssetImpl] resource_asset_resource_change_assets_patch(body=body)

Changes multiple assets.

Changes multiple assets.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
body = [swagger_client.JsonChangeAssetRequest()] # list[JsonChangeAssetRequest] | the properties of the assets to be changed (optional)

try:
    # Changes multiple assets.
    api_response = api_instance.resource_asset_resource_change_assets_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->resource_asset_resource_change_assets_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonChangeAssetRequest]**](JsonChangeAssetRequest.md)| the properties of the assets to be changed | [optional] 

### Return type

[**list[JsonAssetImpl]**](JsonAssetImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_resource_find_assets_get**
> JsonPagedResponse resource_asset_resource_find_assets_get(community_id=community_id, domain_id=domain_id, exclude_meta=exclude_meta, limit=limit, name=name, name_match_mode=name_match_mode, offset=offset, status_id=status_id, tag_names=tag_names, type_id=type_id, type_inheritance=type_inheritance)

Returns assets matching the given search criteria.

Returns assets matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned assets satisfy all constraints that are specified in this search criteria. By default a result containing 1000 assets is returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
community_id = 'community_id_example' # str | The <code>id</code> of the community to find the assets in (optional)
domain_id = 'domain_id_example' # str | The <code>id</code> of the domain to find the assets in (optional)
exclude_meta = true # bool | The exclude meta flag. If this is set to true then the assets from meta domains will not be returned (meta domains are the domains which were not created by the user manually) (optional) (default to true)
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
name = 'name_example' # str | The name of the asset to search for (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code> (optional) (default to ANYWHERE)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)
status_id = ['status_id_example'] # list[str] | The list of <code>ids</code> of the statuses. The returned assets have one of statuses specified by this parameter (optional)
tag_names = ['tag_names_example'] # list[str] | The list of names of tags. The returned assets have one of tags with names specified by this parameter (optional)
type_id = ['type_id_example'] # list[str] | The list of <code>ids</code> of the asset types. The returned assets are of one of types specified by this parameter (optional)
type_inheritance = true # bool | Whether the type inheritance for the asset type filtering should be applied or not (optional) (default to true)

try:
    # Returns assets matching the given search criteria.
    api_response = api_instance.resource_asset_resource_find_assets_get(community_id=community_id, domain_id=domain_id, exclude_meta=exclude_meta, limit=limit, name=name, name_match_mode=name_match_mode, offset=offset, status_id=status_id, tag_names=tag_names, type_id=type_id, type_inheritance=type_inheritance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->resource_asset_resource_find_assets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **community_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the community to find the assets in | [optional] 
 **domain_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the domain to find the assets in | [optional] 
 **exclude_meta** | **bool**| The exclude meta flag. If this is set to true then the assets from meta domains will not be returned (meta domains are the domains which were not created by the user manually) | [optional] [default to true]
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **name** | **str**| The name of the asset to search for | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt; | [optional] [default to ANYWHERE]
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]
 **status_id** | [**list[str]**](str.md)| The list of &lt;code&gt;ids&lt;/code&gt; of the statuses. The returned assets have one of statuses specified by this parameter | [optional] 
 **tag_names** | [**list[str]**](str.md)| The list of names of tags. The returned assets have one of tags with names specified by this parameter | [optional] 
 **type_id** | [**list[str]**](str.md)| The list of &lt;code&gt;ids&lt;/code&gt; of the asset types. The returned assets are of one of types specified by this parameter | [optional] 
 **type_inheritance** | **bool**| Whether the type inheritance for the asset type filtering should be applied or not | [optional] [default to true]

### Return type

[**JsonPagedResponse**](JsonPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_resource_get_asset_get**
> JsonAssetImpl resource_asset_resource_get_asset_get(asset_id)

Returns an asset identified by given id.

Returns an asset identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
asset_id = 'asset_id_example' # str | the <code>id</code> of the asset

try:
    # Returns an asset identified by given id.
    api_response = api_instance.resource_asset_resource_get_asset_get(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->resource_asset_resource_get_asset_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the asset | 

### Return type

[**JsonAssetImpl**](JsonAssetImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_resource_get_asset_tags_get**
> list[JsonTagImpl] resource_asset_resource_get_asset_tags_get(asset_id)

Returns all tags of given asset.

Returns all tags of given asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
asset_id = 'asset_id_example' # str | the <code>id</code> of the asset

try:
    # Returns all tags of given asset.
    api_response = api_instance.resource_asset_resource_get_asset_tags_get(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->resource_asset_resource_get_asset_tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the asset | 

### Return type

[**list[JsonTagImpl]**](JsonTagImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_resource_remove_asset_delete**
> resource_asset_resource_remove_asset_delete(asset_id)

Removes an asset identified by given id.

Removes an asset identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
asset_id = 'asset_id_example' # str | the <code>id</code> of the asset to remove

try:
    # Removes an asset identified by given id.
    api_instance.resource_asset_resource_remove_asset_delete(asset_id)
except ApiException as e:
    print("Exception when calling AssetsApi->resource_asset_resource_remove_asset_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the asset to remove | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_resource_remove_assets_delete**
> resource_asset_resource_remove_assets_delete(body=body)

Removes multiple assets.

Removes multiple assets.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
body = [swagger_client.list[str]()] # list[str] | the <code>id</code>s of the assets to be removed, i.e. [“6f685f90-1036-4d30-983a-a9bbcdd7b8f6”,\"174b6334-9804-495d-b659-43f53a5de8b8\"] (optional)

try:
    # Removes multiple assets.
    api_instance.resource_asset_resource_remove_assets_delete(body=body)
except ApiException as e:
    print("Exception when calling AssetsApi->resource_asset_resource_remove_assets_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**| the &lt;code&gt;id&lt;/code&gt;s of the assets to be removed, i.e. [“6f685f90-1036-4d30-983a-a9bbcdd7b8f6”,\&quot;174b6334-9804-495d-b659-43f53a5de8b8\&quot;] | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_resource_remove_tags_from_asset_delete**
> resource_asset_resource_remove_tags_from_asset_delete(asset_id, body=body)

Remove tags from given asset.

Remove tags from given asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
asset_id = 'asset_id_example' # str | the <code>id</code> of the asset
body = swagger_client.JsonRemoveAssetTagsRequest() # JsonRemoveAssetTagsRequest | the tags to be removed from given asset (optional)

try:
    # Remove tags from given asset.
    api_instance.resource_asset_resource_remove_tags_from_asset_delete(asset_id, body=body)
except ApiException as e:
    print("Exception when calling AssetsApi->resource_asset_resource_remove_tags_from_asset_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the asset | 
 **body** | [**JsonRemoveAssetTagsRequest**](JsonRemoveAssetTagsRequest.md)| the tags to be removed from given asset | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_resource_set_asset_attributes_put**
> list[JsonAttributeImpl] resource_asset_resource_set_asset_attributes_put(asset_id, body=body)

Replaces all the attributes of the asset (of given attribute type) with the attributes from the request, except matching attributes, these are retained.

Replaces all the attributes of the asset (of given attribute type) with the attributes from the request, except matching attributes, these are retained.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
asset_id = 'asset_id_example' # str | 
body = swagger_client.JsonSetAssetAttributesRequest() # JsonSetAssetAttributesRequest | the attributes to be set on given asset (optional)

try:
    # Replaces all the attributes of the asset (of given attribute type) with the attributes from the request, except matching attributes, these are retained.
    api_response = api_instance.resource_asset_resource_set_asset_attributes_put(asset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->resource_asset_resource_set_asset_attributes_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 
 **body** | [**JsonSetAssetAttributesRequest**](JsonSetAssetAttributesRequest.md)| the attributes to be set on given asset | [optional] 

### Return type

[**list[JsonAttributeImpl]**](JsonAttributeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_resource_set_asset_relations_put**
> list[JsonRelationImpl] resource_asset_resource_set_asset_relations_put(asset_id, body=body)

Sets relations for given asset.

Sets relations for given asset. All the relations described by this request will replace the existing ones (identified with asset as one end, relation type and direction of the relation).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
asset_id = 'asset_id_example' # str | 
body = swagger_client.JsonSetAssetRelationsRequest() # JsonSetAssetRelationsRequest | the relations to be set on given asset (optional)

try:
    # Sets relations for given asset.
    api_response = api_instance.resource_asset_resource_set_asset_relations_put(asset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->resource_asset_resource_set_asset_relations_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 
 **body** | [**JsonSetAssetRelationsRequest**](JsonSetAssetRelationsRequest.md)| the relations to be set on given asset | [optional] 

### Return type

[**list[JsonRelationImpl]**](JsonRelationImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_resource_set_asset_responsibilities_put**
> list[JsonResponsibilityImpl] resource_asset_resource_set_asset_responsibilities_put(asset_id, body=body)

Sets responsibilities for given asset.

Sets responsibilities for given asset. All the relations described by this request will replace the existing ones (identified with asset as one end, relation type and direction of the relation).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
asset_id = 'asset_id_example' # str | 
body = swagger_client.JsonSetAssetResponsibilitiesRequest() # JsonSetAssetResponsibilitiesRequest | the relations to be set on given asset (optional)

try:
    # Sets responsibilities for given asset.
    api_response = api_instance.resource_asset_resource_set_asset_responsibilities_put(asset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->resource_asset_resource_set_asset_responsibilities_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 
 **body** | [**JsonSetAssetResponsibilitiesRequest**](JsonSetAssetResponsibilitiesRequest.md)| the relations to be set on given asset | [optional] 

### Return type

[**list[JsonResponsibilityImpl]**](JsonResponsibilityImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_asset_resource_set_tags_for_asset_put**
> list[JsonTagImpl] resource_asset_resource_set_tags_for_asset_put(asset_id, body=body)

Sets tags for given asset.

Sets tags for given asset. Given asset will contain only tags that are present in this request after the request is performed.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
asset_id = 'asset_id_example' # str | the <code>id</code> of the asset
body = swagger_client.JsonSetAssetTagsRequest() # JsonSetAssetTagsRequest | the tags to be set on given asset (optional)

try:
    # Sets tags for given asset.
    api_response = api_instance.resource_asset_resource_set_tags_for_asset_put(asset_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->resource_asset_resource_set_tags_for_asset_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the asset | 
 **body** | [**JsonSetAssetTagsRequest**](JsonSetAssetTagsRequest.md)| the tags to be set on given asset | [optional] 

### Return type

[**list[JsonTagImpl]**](JsonTagImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

