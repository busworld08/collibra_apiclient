# swagger_client.CommunitiesApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_community_resource_add_communities_post**](CommunitiesApi.md#resource_community_resource_add_communities_post) | **POST** /communities/bulk | Adds multiple communities.
[**resource_community_resource_add_community_post**](CommunitiesApi.md#resource_community_resource_add_community_post) | **POST** /communities | Adds new community.
[**resource_community_resource_change_communities_patch**](CommunitiesApi.md#resource_community_resource_change_communities_patch) | **PATCH** /communities/bulk | Changes multiple communities.
[**resource_community_resource_change_community_patch**](CommunitiesApi.md#resource_community_resource_change_community_patch) | **PATCH** /communities/{communityId} | Changes the community with the information that is present in the request.
[**resource_community_resource_find_communities_get**](CommunitiesApi.md#resource_community_resource_find_communities_get) | **GET** /communities | Returns communities matching the given search criteria.
[**resource_community_resource_get_community_get**](CommunitiesApi.md#resource_community_resource_get_community_get) | **GET** /communities/{communityId} | Returns community identified by given id.
[**resource_community_resource_remove_communities_delete**](CommunitiesApi.md#resource_community_resource_remove_communities_delete) | **DELETE** /communities/bulk | Removes multiple communities.
[**resource_community_resource_remove_communities_in_job_post**](CommunitiesApi.md#resource_community_resource_remove_communities_in_job_post) | **POST** /communities/removalJobs | Removes multiple communities in job.
[**resource_community_resource_remove_community_delete**](CommunitiesApi.md#resource_community_resource_remove_community_delete) | **DELETE** /communities/{communityId} | Removes community identified by given id.


# **resource_community_resource_add_communities_post**
> list[JsonCommunityImpl] resource_community_resource_add_communities_post(body=body)

Adds multiple communities.

Adds multiple communities.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommunitiesApi()
body = [swagger_client.JsonAddCommunityRequest()] # list[JsonAddCommunityRequest] | the properties of the communities to be added (optional)

try:
    # Adds multiple communities.
    api_response = api_instance.resource_community_resource_add_communities_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunitiesApi->resource_community_resource_add_communities_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonAddCommunityRequest]**](JsonAddCommunityRequest.md)| the properties of the communities to be added | [optional] 

### Return type

[**list[JsonCommunityImpl]**](JsonCommunityImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_community_resource_add_community_post**
> JsonCommunityImpl resource_community_resource_add_community_post(body=body)

Adds new community.

Adds new community.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommunitiesApi()
body = swagger_client.JsonAddCommunityRequest() # JsonAddCommunityRequest | the properties of the community to be added (optional)

try:
    # Adds new community.
    api_response = api_instance.resource_community_resource_add_community_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunitiesApi->resource_community_resource_add_community_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAddCommunityRequest**](JsonAddCommunityRequest.md)| the properties of the community to be added | [optional] 

### Return type

[**JsonCommunityImpl**](JsonCommunityImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_community_resource_change_communities_patch**
> list[JsonCommunityImpl] resource_community_resource_change_communities_patch(body=body)

Changes multiple communities.

Changes multiple communities.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommunitiesApi()
body = [swagger_client.JsonChangeCommunityRequest()] # list[JsonChangeCommunityRequest] | the properties of the communities to be changed (optional)

try:
    # Changes multiple communities.
    api_response = api_instance.resource_community_resource_change_communities_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunitiesApi->resource_community_resource_change_communities_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonChangeCommunityRequest]**](JsonChangeCommunityRequest.md)| the properties of the communities to be changed | [optional] 

### Return type

[**list[JsonCommunityImpl]**](JsonCommunityImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_community_resource_change_community_patch**
> JsonCommunityImpl resource_community_resource_change_community_patch(community_id, body=body)

Changes the community with the information that is present in the request.

Changes the community with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommunitiesApi()
community_id = 'community_id_example' # str | the <code>id</code> of the community to be changed
body = swagger_client.JsonChangeCommunityRequest() # JsonChangeCommunityRequest | the properties of the community to be changed (optional)

try:
    # Changes the community with the information that is present in the request.
    api_response = api_instance.resource_community_resource_change_community_patch(community_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunitiesApi->resource_community_resource_change_community_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **community_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the community to be changed | 
 **body** | [**JsonChangeCommunityRequest**](JsonChangeCommunityRequest.md)| the properties of the community to be changed | [optional] 

### Return type

[**JsonCommunityImpl**](JsonCommunityImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_community_resource_find_communities_get**
> JsonPagedResponse resource_community_resource_find_communities_get(exclude_meta=exclude_meta, limit=limit, name=name, name_match_mode=name_match_mode, offset=offset, parent_id=parent_id, sort_field=sort_field, sort_order=sort_order)

Returns communities matching the given search criteria.

Returns communities matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned communities satisfy all constraints that are specified in this search criteria. By default a result containing 1000 communities is returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommunitiesApi()
exclude_meta = true # bool | The exclude meta flag. If this is set to true then the meta communities will not be returned (meta communities are i.e. communities not created manually by the user) (optional) (default to true)
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
name = 'name_example' # str | The name of the community to search for (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code> (optional) (default to ANYWHERE)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)
parent_id = 'parent_id_example' # str | The <code>id</code> of the parent community to find the communities in (optional)
sort_field = 'NAME' # str | The field on which the results are sorted (optional) (default to NAME)
sort_order = 'ASC' # str | The sorting order (optional) (default to ASC)

try:
    # Returns communities matching the given search criteria.
    api_response = api_instance.resource_community_resource_find_communities_get(exclude_meta=exclude_meta, limit=limit, name=name, name_match_mode=name_match_mode, offset=offset, parent_id=parent_id, sort_field=sort_field, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunitiesApi->resource_community_resource_find_communities_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exclude_meta** | **bool**| The exclude meta flag. If this is set to true then the meta communities will not be returned (meta communities are i.e. communities not created manually by the user) | [optional] [default to true]
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **name** | **str**| The name of the community to search for | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt; | [optional] [default to ANYWHERE]
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]
 **parent_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the parent community to find the communities in | [optional] 
 **sort_field** | **str**| The field on which the results are sorted | [optional] [default to NAME]
 **sort_order** | **str**| The sorting order | [optional] [default to ASC]

### Return type

[**JsonPagedResponse**](JsonPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_community_resource_get_community_get**
> JsonCommunityImpl resource_community_resource_get_community_get(community_id)

Returns community identified by given id.

Returns community identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommunitiesApi()
community_id = 'community_id_example' # str | the <code>id</code> of the community

try:
    # Returns community identified by given id.
    api_response = api_instance.resource_community_resource_get_community_get(community_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunitiesApi->resource_community_resource_get_community_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **community_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the community | 

### Return type

[**JsonCommunityImpl**](JsonCommunityImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_community_resource_remove_communities_delete**
> resource_community_resource_remove_communities_delete(body=body)

Removes multiple communities.

Removes multiple communities.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommunitiesApi()
body = [swagger_client.list[str]()] # list[str] | the <code>id</code>s of the communities to be removed, i.e. [\"6f685f90-1036-4d30-983a-a9bbcdd7b8f6\", \"6f685f90-1036-4d30-983a-a9bbcdd7b123\"] (optional)

try:
    # Removes multiple communities.
    api_instance.resource_community_resource_remove_communities_delete(body=body)
except ApiException as e:
    print("Exception when calling CommunitiesApi->resource_community_resource_remove_communities_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**| the &lt;code&gt;id&lt;/code&gt;s of the communities to be removed, i.e. [\&quot;6f685f90-1036-4d30-983a-a9bbcdd7b8f6\&quot;, \&quot;6f685f90-1036-4d30-983a-a9bbcdd7b123\&quot;] | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_community_resource_remove_communities_in_job_post**
> JsonJobImpl resource_community_resource_remove_communities_in_job_post(body=body)

Removes multiple communities in job.

Removes multiple communities in job.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommunitiesApi()
body = [swagger_client.list[str]()] # list[str] | the <code>id</code>s of the communities to be removed, i.e. [\"6f685f90-1036-4d30-983a-a9bbcdd7b8f6\", \"6f685f90-1036-4d30-983a-a9bbcdd7b123\"] (optional)

try:
    # Removes multiple communities in job.
    api_response = api_instance.resource_community_resource_remove_communities_in_job_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunitiesApi->resource_community_resource_remove_communities_in_job_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**| the &lt;code&gt;id&lt;/code&gt;s of the communities to be removed, i.e. [\&quot;6f685f90-1036-4d30-983a-a9bbcdd7b8f6\&quot;, \&quot;6f685f90-1036-4d30-983a-a9bbcdd7b123\&quot;] | [optional] 

### Return type

[**JsonJobImpl**](JsonJobImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_community_resource_remove_community_delete**
> resource_community_resource_remove_community_delete(community_id)

Removes community identified by given id.

Removes community identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommunitiesApi()
community_id = 'community_id_example' # str | the <code>id</code> of the community

try:
    # Removes community identified by given id.
    api_instance.resource_community_resource_remove_community_delete(community_id)
except ApiException as e:
    print("Exception when calling CommunitiesApi->resource_community_resource_remove_community_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **community_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the community | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

