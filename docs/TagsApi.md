# swagger_client.TagsApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_tag_resource_find_tags_get**](TagsApi.md#resource_tag_resource_find_tags_get) | **GET** /tags | Returns tags matching given search criteria.
[**resource_tag_resource_get_tag_get**](TagsApi.md#resource_tag_resource_get_tag_get) | **GET** /tags/{tagId} | Returns a tag identified by given id.
[**resource_tag_resource_get_tags_by_asset_id_get**](TagsApi.md#resource_tag_resource_get_tags_by_asset_id_get) | **GET** /tags/asset/{assetId} | Retrieves all tags of given asset.


# **resource_tag_resource_find_tags_get**
> JsonPagedResponse resource_tag_resource_find_tags_get(limit=limit, name=name, name_match_mode=name_match_mode, offset=offset)

Returns tags matching given search criteria.

Returns tags matching given search criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
name = 'name_example' # str |  (optional)
name_match_mode = 'ANYWHERE' # str |  (optional) (default to ANYWHERE)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)

try:
    # Returns tags matching given search criteria.
    api_response = api_instance.resource_tag_resource_find_tags_get(limit=limit, name=name, name_match_mode=name_match_mode, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->resource_tag_resource_find_tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **name** | **str**|  | [optional] 
 **name_match_mode** | **str**|  | [optional] [default to ANYWHERE]
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]

### Return type

[**JsonPagedResponse**](JsonPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_tag_resource_get_tag_get**
> JsonTagImpl resource_tag_resource_get_tag_get(tag_id)

Returns a tag identified by given id.

Returns a tag identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
tag_id = 'tag_id_example' # str | the <code>id</code> of the tag

try:
    # Returns a tag identified by given id.
    api_response = api_instance.resource_tag_resource_get_tag_get(tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->resource_tag_resource_get_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the tag | 

### Return type

[**JsonTagImpl**](JsonTagImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_tag_resource_get_tags_by_asset_id_get**
> list[JsonTagImpl] resource_tag_resource_get_tags_by_asset_id_get(asset_id)

Retrieves all tags of given asset.

Retrieves all tags of given asset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TagsApi()
asset_id = 'asset_id_example' # str | the <code>id</code> of an asset

try:
    # Retrieves all tags of given asset.
    api_response = api_instance.resource_tag_resource_get_tags_by_asset_id_get(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->resource_tag_resource_get_tags_by_asset_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of an asset | 

### Return type

[**list[JsonTagImpl]**](JsonTagImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

