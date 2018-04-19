# swagger_client.ScopesApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_scope_resource_add_scope_post**](ScopesApi.md#resource_scope_resource_add_scope_post) | **POST** /scopes | Adds new scope.
[**resource_scope_resource_change_scope_patch**](ScopesApi.md#resource_scope_resource_change_scope_patch) | **PATCH** /scopes/{scopeId} | Changes the scope with the information that is present in the request.
[**resource_scope_resource_get_all_scopes_get**](ScopesApi.md#resource_scope_resource_get_all_scopes_get) | **GET** /scopes | Returns all scopes.
[**resource_scope_resource_get_scope_get**](ScopesApi.md#resource_scope_resource_get_scope_get) | **GET** /scopes/{scopeId} | Returns scope identified by given id.
[**resource_scope_resource_remove_scope_delete**](ScopesApi.md#resource_scope_resource_remove_scope_delete) | **DELETE** /scopes/{scopeId} | Removes scope identified by given id.


# **resource_scope_resource_add_scope_post**
> JsonScopeImpl resource_scope_resource_add_scope_post(body=body)

Adds new scope.

Adds new scope.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScopesApi()
body = swagger_client.JsonAddScopeRequest() # JsonAddScopeRequest | the properties of the scope to be added (optional)

try:
    # Adds new scope.
    api_response = api_instance.resource_scope_resource_add_scope_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopesApi->resource_scope_resource_add_scope_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAddScopeRequest**](JsonAddScopeRequest.md)| the properties of the scope to be added | [optional] 

### Return type

[**JsonScopeImpl**](JsonScopeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_scope_resource_change_scope_patch**
> JsonScopeImpl resource_scope_resource_change_scope_patch(scope_id, body=body)

Changes the scope with the information that is present in the request.

Changes the scope with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScopesApi()
scope_id = 'scope_id_example' # str | the <code>id</code> of the scope to be changed
body = swagger_client.JsonChangeScopeRequest() # JsonChangeScopeRequest | the properties of the scope to be changed (optional)

try:
    # Changes the scope with the information that is present in the request.
    api_response = api_instance.resource_scope_resource_change_scope_patch(scope_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopesApi->resource_scope_resource_change_scope_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the scope to be changed | 
 **body** | [**JsonChangeScopeRequest**](JsonChangeScopeRequest.md)| the properties of the scope to be changed | [optional] 

### Return type

[**JsonScopeImpl**](JsonScopeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_scope_resource_get_all_scopes_get**
> JsonPagedResponse resource_scope_resource_get_all_scopes_get()

Returns all scopes.

Returns all scopes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScopesApi()

try:
    # Returns all scopes.
    api_response = api_instance.resource_scope_resource_get_all_scopes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopesApi->resource_scope_resource_get_all_scopes_get: %s\n" % e)
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

# **resource_scope_resource_get_scope_get**
> JsonScopeImpl resource_scope_resource_get_scope_get(scope_id)

Returns scope identified by given id.

Returns scope identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScopesApi()
scope_id = 'scope_id_example' # str | the <code>id</code> of the scope

try:
    # Returns scope identified by given id.
    api_response = api_instance.resource_scope_resource_get_scope_get(scope_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScopesApi->resource_scope_resource_get_scope_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the scope | 

### Return type

[**JsonScopeImpl**](JsonScopeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_scope_resource_remove_scope_delete**
> resource_scope_resource_remove_scope_delete(scope_id)

Removes scope identified by given id.

Removes scope identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ScopesApi()
scope_id = 'scope_id_example' # str | the <code>id</code> of the scope

try:
    # Removes scope identified by given id.
    api_instance.resource_scope_resource_remove_scope_delete(scope_id)
except ApiException as e:
    print("Exception when calling ScopesApi->resource_scope_resource_remove_scope_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the scope | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

