# swagger_client.RolesApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_role_resource_add_role_post**](RolesApi.md#resource_role_resource_add_role_post) | **POST** /roles | Adds new role.
[**resource_role_resource_change_role_patch**](RolesApi.md#resource_role_resource_change_role_patch) | **PATCH** /roles/{roleId} | Changes the role with the information that is present in the request.
[**resource_role_resource_find_roles_get**](RolesApi.md#resource_role_resource_find_roles_get) | **GET** /roles | Returns roles matching the given search criteria.
[**resource_role_resource_get_role_get**](RolesApi.md#resource_role_resource_get_role_get) | **GET** /roles/{roleId} | Returns role identified by given id.
[**resource_role_resource_remove_role_delete**](RolesApi.md#resource_role_resource_remove_role_delete) | **DELETE** /roles/{roleId} | Removes role identified by given id.


# **resource_role_resource_add_role_post**
> JsonRoleImpl resource_role_resource_add_role_post(body=body)

Adds new role.

Adds new role.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
body = swagger_client.JsonAddRoleRequest() # JsonAddRoleRequest | the properties of the role to be added (optional)

try:
    # Adds new role.
    api_response = api_instance.resource_role_resource_add_role_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->resource_role_resource_add_role_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAddRoleRequest**](JsonAddRoleRequest.md)| the properties of the role to be added | [optional] 

### Return type

[**JsonRoleImpl**](JsonRoleImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_role_resource_change_role_patch**
> JsonRoleImpl resource_role_resource_change_role_patch(role_id, body=body)

Changes the role with the information that is present in the request.

Changes the role with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
role_id = 'role_id_example' # str | the <code>id</code> of the role to be changed
body = swagger_client.JsonChangeRoleRequest() # JsonChangeRoleRequest | the properties of the role to be changed (optional)

try:
    # Changes the role with the information that is present in the request.
    api_response = api_instance.resource_role_resource_change_role_patch(role_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->resource_role_resource_change_role_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the role to be changed | 
 **body** | [**JsonChangeRoleRequest**](JsonChangeRoleRequest.md)| the properties of the role to be changed | [optional] 

### Return type

[**JsonRoleImpl**](JsonRoleImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_role_resource_find_roles_get**
> JsonPagedResponse resource_role_resource_find_roles_get(description=description, _global=_global, limit=limit, name=name, offset=offset)

Returns roles matching the given search criteria.

Returns roles matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned roles satisfy all constraints that are specified in this search criteria. By default a result containing 1000 roles is returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
description = 'description_example' # str | The description of the role to search for (optional)
_global = true # bool | Whether global roles should be searched for (optional)
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
name = 'name_example' # str | The name of the role to search for (optional)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)

try:
    # Returns roles matching the given search criteria.
    api_response = api_instance.resource_role_resource_find_roles_get(description=description, _global=_global, limit=limit, name=name, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->resource_role_resource_find_roles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| The description of the role to search for | [optional] 
 **_global** | **bool**| Whether global roles should be searched for | [optional] 
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **name** | **str**| The name of the role to search for | [optional] 
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]

### Return type

[**JsonPagedResponse**](JsonPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_role_resource_get_role_get**
> JsonRoleImpl resource_role_resource_get_role_get(role_id)

Returns role identified by given id.

Returns role identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
role_id = 'role_id_example' # str | the <code>id</code> of the role

try:
    # Returns role identified by given id.
    api_response = api_instance.resource_role_resource_get_role_get(role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->resource_role_resource_get_role_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the role | 

### Return type

[**JsonRoleImpl**](JsonRoleImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_role_resource_remove_role_delete**
> resource_role_resource_remove_role_delete(role_id)

Removes role identified by given id.

Removes role identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()
role_id = 'role_id_example' # str | the <code>id</code> of the role

try:
    # Removes role identified by given id.
    api_instance.resource_role_resource_remove_role_delete(role_id)
except ApiException as e:
    print("Exception when calling RolesApi->resource_role_resource_remove_role_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the role | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

