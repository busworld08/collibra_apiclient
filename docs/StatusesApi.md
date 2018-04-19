# swagger_client.StatusesApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_status_resource_add_status_post**](StatusesApi.md#resource_status_resource_add_status_post) | **POST** /statuses | Adds new status.
[**resource_status_resource_add_statuses_post**](StatusesApi.md#resource_status_resource_add_statuses_post) | **POST** /statuses/bulk | Adds multiple statuses.
[**resource_status_resource_change_status_patch**](StatusesApi.md#resource_status_resource_change_status_patch) | **PATCH** /statuses/{statusId} | Changes the status with the information that is present in the request.
[**resource_status_resource_change_statuses_patch**](StatusesApi.md#resource_status_resource_change_statuses_patch) | **PATCH** /statuses/bulk | Changes multiple statuses.
[**resource_status_resource_find_statuses_get**](StatusesApi.md#resource_status_resource_find_statuses_get) | **GET** /statuses | Returns statuses matching the given search criteria.
[**resource_status_resource_get_status_by_name_get**](StatusesApi.md#resource_status_resource_get_status_by_name_get) | **GET** /statuses/name/{statusName} | Returns status identified by given name.
[**resource_status_resource_get_status_get**](StatusesApi.md#resource_status_resource_get_status_get) | **GET** /statuses/{statusId} | Returns status identified by given id.
[**resource_status_resource_remove_status_delete**](StatusesApi.md#resource_status_resource_remove_status_delete) | **DELETE** /statuses/{statusId} | Removes status identified by given id.
[**resource_status_resource_remove_statuses_delete**](StatusesApi.md#resource_status_resource_remove_statuses_delete) | **DELETE** /statuses/bulk | Removes multiple statuses.


# **resource_status_resource_add_status_post**
> JsonStatusImpl resource_status_resource_add_status_post(body=body)

Adds new status.

Adds new status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusesApi()
body = swagger_client.JsonAddStatusRequest() # JsonAddStatusRequest | the properties of the status to be added (optional)

try:
    # Adds new status.
    api_response = api_instance.resource_status_resource_add_status_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusesApi->resource_status_resource_add_status_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAddStatusRequest**](JsonAddStatusRequest.md)| the properties of the status to be added | [optional] 

### Return type

[**JsonStatusImpl**](JsonStatusImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_status_resource_add_statuses_post**
> list[JsonStatusImpl] resource_status_resource_add_statuses_post(body=body)

Adds multiple statuses.

Adds multiple statuses.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusesApi()
body = [swagger_client.JsonAddStatusRequest()] # list[JsonAddStatusRequest] | the properties of the statuses to be added (optional)

try:
    # Adds multiple statuses.
    api_response = api_instance.resource_status_resource_add_statuses_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusesApi->resource_status_resource_add_statuses_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonAddStatusRequest]**](JsonAddStatusRequest.md)| the properties of the statuses to be added | [optional] 

### Return type

[**list[JsonStatusImpl]**](JsonStatusImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_status_resource_change_status_patch**
> JsonStatusImpl resource_status_resource_change_status_patch(status_id, body=body)

Changes the status with the information that is present in the request.

Changes the status with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusesApi()
status_id = 'status_id_example' # str | the UUID of the status to be changed
body = swagger_client.JsonChangeStatusRequest() # JsonChangeStatusRequest | the properties of the status to be changed (optional)

try:
    # Changes the status with the information that is present in the request.
    api_response = api_instance.resource_status_resource_change_status_patch(status_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusesApi->resource_status_resource_change_status_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_id** | **str**| the UUID of the status to be changed | 
 **body** | [**JsonChangeStatusRequest**](JsonChangeStatusRequest.md)| the properties of the status to be changed | [optional] 

### Return type

[**JsonStatusImpl**](JsonStatusImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_status_resource_change_statuses_patch**
> list[JsonStatusImpl] resource_status_resource_change_statuses_patch(body=body)

Changes multiple statuses.

Changes multiple statuses.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusesApi()
body = [swagger_client.JsonChangeStatusRequest()] # list[JsonChangeStatusRequest] | the properties of the statuses to be changed (optional)

try:
    # Changes multiple statuses.
    api_response = api_instance.resource_status_resource_change_statuses_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusesApi->resource_status_resource_change_statuses_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonChangeStatusRequest]**](JsonChangeStatusRequest.md)| the properties of the statuses to be changed | [optional] 

### Return type

[**list[JsonStatusImpl]**](JsonStatusImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_status_resource_find_statuses_get**
> JsonPagedResponse resource_status_resource_find_statuses_get(description=description, limit=limit, name=name, offset=offset)

Returns statuses matching the given search criteria.

Returns statuses matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned statuses satisfy all constraints that are specified in this search criteria. By default a result containing 1000 statuses is returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusesApi()
description = 'description_example' # str | The description of the status to search for (optional)
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
name = 'name_example' # str | The name of the status to search for (optional)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)

try:
    # Returns statuses matching the given search criteria.
    api_response = api_instance.resource_status_resource_find_statuses_get(description=description, limit=limit, name=name, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusesApi->resource_status_resource_find_statuses_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| The description of the status to search for | [optional] 
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **name** | **str**| The name of the status to search for | [optional] 
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]

### Return type

[**JsonPagedResponse**](JsonPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_status_resource_get_status_by_name_get**
> JsonStatusImpl resource_status_resource_get_status_by_name_get(status_name)

Returns status identified by given name.

Returns status identified by given name.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusesApi()
status_name = 'status_name_example' # str | the name of the status

try:
    # Returns status identified by given name.
    api_response = api_instance.resource_status_resource_get_status_by_name_get(status_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusesApi->resource_status_resource_get_status_by_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_name** | **str**| the name of the status | 

### Return type

[**JsonStatusImpl**](JsonStatusImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_status_resource_get_status_get**
> JsonStatusImpl resource_status_resource_get_status_get(status_id)

Returns status identified by given id.

Returns status identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusesApi()
status_id = 'status_id_example' # str | the <code>id</code> of the status

try:
    # Returns status identified by given id.
    api_response = api_instance.resource_status_resource_get_status_get(status_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusesApi->resource_status_resource_get_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the status | 

### Return type

[**JsonStatusImpl**](JsonStatusImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_status_resource_remove_status_delete**
> resource_status_resource_remove_status_delete(status_id)

Removes status identified by given id.

Removes status identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusesApi()
status_id = 'status_id_example' # str | the <code>id</code> of the status

try:
    # Removes status identified by given id.
    api_instance.resource_status_resource_remove_status_delete(status_id)
except ApiException as e:
    print("Exception when calling StatusesApi->resource_status_resource_remove_status_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the status | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_status_resource_remove_statuses_delete**
> resource_status_resource_remove_statuses_delete(body=body)

Removes multiple statuses.

Removes multiple statuses.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusesApi()
body = [swagger_client.list[str]()] # list[str] | the <code>id</code>s of the statuses to be removed (optional)

try:
    # Removes multiple statuses.
    api_instance.resource_status_resource_remove_statuses_delete(body=body)
except ApiException as e:
    print("Exception when calling StatusesApi->resource_status_resource_remove_statuses_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**| the &lt;code&gt;id&lt;/code&gt;s of the statuses to be removed | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

