# swagger_client.ResponsibilitiesApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_responsibility_resource_add_responsibilities_post**](ResponsibilitiesApi.md#resource_responsibility_resource_add_responsibilities_post) | **POST** /responsibilities/bulk | Adds new responsibilities in one go.
[**resource_responsibility_resource_add_responsibility_post**](ResponsibilitiesApi.md#resource_responsibility_resource_add_responsibility_post) | **POST** /responsibilities | Adds new responsibility.
[**resource_responsibility_resource_find_responsibilities_get**](ResponsibilitiesApi.md#resource_responsibility_resource_find_responsibilities_get) | **GET** /responsibilities | Returns responsibilities matching the given search criteria.
[**resource_responsibility_resource_get_responsibility_get**](ResponsibilitiesApi.md#resource_responsibility_resource_get_responsibility_get) | **GET** /responsibilities/{responsibilityId} | Returns responsibility identified by given id.
[**resource_responsibility_resource_remove_responsibilities_delete**](ResponsibilitiesApi.md#resource_responsibility_resource_remove_responsibilities_delete) | **DELETE** /responsibilities/bulk | Removes responsibilities identified by given ids.
[**resource_responsibility_resource_remove_responsibility_delete**](ResponsibilitiesApi.md#resource_responsibility_resource_remove_responsibility_delete) | **DELETE** /responsibilities/{responsibilityId} | Removes responsibility identified by given id.


# **resource_responsibility_resource_add_responsibilities_post**
> list[JsonResponsibilityImpl] resource_responsibility_resource_add_responsibilities_post(body=body)

Adds new responsibilities in one go.

Adds new responsibilities in one go. Assigns given users to resources with given roles.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResponsibilitiesApi()
body = [swagger_client.JsonAddResponsibilityRequest()] # list[JsonAddResponsibilityRequest] | the list of properties of the reponsibilities to be added (optional)

try:
    # Adds new responsibilities in one go.
    api_response = api_instance.resource_responsibility_resource_add_responsibilities_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponsibilitiesApi->resource_responsibility_resource_add_responsibilities_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonAddResponsibilityRequest]**](JsonAddResponsibilityRequest.md)| the list of properties of the reponsibilities to be added | [optional] 

### Return type

[**list[JsonResponsibilityImpl]**](JsonResponsibilityImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_responsibility_resource_add_responsibility_post**
> JsonResponsibilityImpl resource_responsibility_resource_add_responsibility_post(body=body)

Adds new responsibility.

Adds new responsibility. Assigns given user to resource with given role.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResponsibilitiesApi()
body = swagger_client.JsonAddResponsibilityRequest() # JsonAddResponsibilityRequest | the properties of the reponsibility to be added (optional)

try:
    # Adds new responsibility.
    api_response = api_instance.resource_responsibility_resource_add_responsibility_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponsibilitiesApi->resource_responsibility_resource_add_responsibility_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAddResponsibilityRequest**](JsonAddResponsibilityRequest.md)| the properties of the reponsibility to be added | [optional] 

### Return type

[**JsonResponsibilityImpl**](JsonResponsibilityImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_responsibility_resource_find_responsibilities_get**
> JsonPagedResponse resource_responsibility_resource_find_responsibilities_get(global_only=global_only, include_inherited=include_inherited, limit=limit, offset=offset, owner_ids=owner_ids, resource_ids=resource_ids, role_ids=role_ids, sort_field=sort_field, sort_order=sort_order)

Returns responsibilities matching the given search criteria.

Returns responsibilities matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned responsibilities satisfy all constraints that are specified in this search criteria. By default a result containing 1000 responsibilities is returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResponsibilitiesApi()
global_only = true # bool | Whether only global responsibilities should be searched (optional)
include_inherited = true # bool | Whether inherited responsibilities should be included in the search results (optional) (default to true)
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)
owner_ids = ['owner_ids_example'] # list[str] | The list of <code>id</code>s of the owners for which the responsibilities should be found (optional)
resource_ids = ['resource_ids_example'] # list[str] | The list of <code>id</code>s of the resources for which the responsibilities should be found (optional)
role_ids = ['role_ids_example'] # list[str] | The list of <code>id</code>s of the roles for which the responsibilities should be found (optional)
sort_field = 'LAST_MODIFIED' # str | The field that should be used as reference for sorting (optional) (default to LAST_MODIFIED)
sort_order = 'DESC' # str | The order of sorting (optional) (default to DESC)

try:
    # Returns responsibilities matching the given search criteria.
    api_response = api_instance.resource_responsibility_resource_find_responsibilities_get(global_only=global_only, include_inherited=include_inherited, limit=limit, offset=offset, owner_ids=owner_ids, resource_ids=resource_ids, role_ids=role_ids, sort_field=sort_field, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponsibilitiesApi->resource_responsibility_resource_find_responsibilities_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **global_only** | **bool**| Whether only global responsibilities should be searched | [optional] 
 **include_inherited** | **bool**| Whether inherited responsibilities should be included in the search results | [optional] [default to true]
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]
 **owner_ids** | [**list[str]**](str.md)| The list of &lt;code&gt;id&lt;/code&gt;s of the owners for which the responsibilities should be found | [optional] 
 **resource_ids** | [**list[str]**](str.md)| The list of &lt;code&gt;id&lt;/code&gt;s of the resources for which the responsibilities should be found | [optional] 
 **role_ids** | [**list[str]**](str.md)| The list of &lt;code&gt;id&lt;/code&gt;s of the roles for which the responsibilities should be found | [optional] 
 **sort_field** | **str**| The field that should be used as reference for sorting | [optional] [default to LAST_MODIFIED]
 **sort_order** | **str**| The order of sorting | [optional] [default to DESC]

### Return type

[**JsonPagedResponse**](JsonPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_responsibility_resource_get_responsibility_get**
> JsonResponsibilityImpl resource_responsibility_resource_get_responsibility_get(responsibility_id)

Returns responsibility identified by given id.

Returns responsibility identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResponsibilitiesApi()
responsibility_id = 'responsibility_id_example' # str | the <code>id</code> of the responsibility

try:
    # Returns responsibility identified by given id.
    api_response = api_instance.resource_responsibility_resource_get_responsibility_get(responsibility_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResponsibilitiesApi->resource_responsibility_resource_get_responsibility_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **responsibility_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the responsibility | 

### Return type

[**JsonResponsibilityImpl**](JsonResponsibilityImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_responsibility_resource_remove_responsibilities_delete**
> resource_responsibility_resource_remove_responsibilities_delete(body=body)

Removes responsibilities identified by given ids.

Removes responsibilities identified by given ids.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResponsibilitiesApi()
body = [swagger_client.list[str]()] # list[str] | the <code>id</code>s of the responsibilities to remove (optional)

try:
    # Removes responsibilities identified by given ids.
    api_instance.resource_responsibility_resource_remove_responsibilities_delete(body=body)
except ApiException as e:
    print("Exception when calling ResponsibilitiesApi->resource_responsibility_resource_remove_responsibilities_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**| the &lt;code&gt;id&lt;/code&gt;s of the responsibilities to remove | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_responsibility_resource_remove_responsibility_delete**
> resource_responsibility_resource_remove_responsibility_delete(responsibility_id)

Removes responsibility identified by given id.

Removes responsibility identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResponsibilitiesApi()
responsibility_id = 'responsibility_id_example' # str | the <code>id</code> of the responsibility

try:
    # Removes responsibility identified by given id.
    api_instance.resource_responsibility_resource_remove_responsibility_delete(responsibility_id)
except ApiException as e:
    print("Exception when calling ResponsibilitiesApi->resource_responsibility_resource_remove_responsibility_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **responsibility_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the responsibility | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

