# swagger_client.UserGroupsApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_user_group_resource_add_user_group_post**](UserGroupsApi.md#resource_user_group_resource_add_user_group_post) | **POST** /userGroups | Adds new user group.
[**resource_user_group_resource_add_user_to_user_group_post**](UserGroupsApi.md#resource_user_group_resource_add_user_to_user_group_post) | **POST** /userGroups/{userGroupId}/users | Adds users to existing user group.
[**resource_user_group_resource_change_user_group_patch**](UserGroupsApi.md#resource_user_group_resource_change_user_group_patch) | **PATCH** /userGroups/{userGroupId} | Changes the user group with the information that is present in the request.
[**resource_user_group_resource_find_user_groups_get**](UserGroupsApi.md#resource_user_group_resource_find_user_groups_get) | **GET** /userGroups | Returns user groups matching the given search criteria.
[**resource_user_group_resource_get_user_group_get**](UserGroupsApi.md#resource_user_group_resource_get_user_group_get) | **GET** /userGroups/{userGroupId} | Returns user group identified by given id.
[**resource_user_group_resource_remove_user_group_delete**](UserGroupsApi.md#resource_user_group_resource_remove_user_group_delete) | **DELETE** /userGroups/{userGroupId} | Removes user group identified by given id.
[**resource_user_group_resource_remove_users_from_user_group_delete**](UserGroupsApi.md#resource_user_group_resource_remove_users_from_user_group_delete) | **DELETE** /userGroups/{userGroupId}/users | Removes users from the user group identified by given id.


# **resource_user_group_resource_add_user_group_post**
> JsonUserGroupImpl resource_user_group_resource_add_user_group_post(body=body)

Adds new user group.

Adds new user group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupsApi()
body = swagger_client.JsonAddUserGroupRequest() # JsonAddUserGroupRequest | the properties of the user group to be added (optional)

try:
    # Adds new user group.
    api_response = api_instance.resource_user_group_resource_add_user_group_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupsApi->resource_user_group_resource_add_user_group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAddUserGroupRequest**](JsonAddUserGroupRequest.md)| the properties of the user group to be added | [optional] 

### Return type

[**JsonUserGroupImpl**](JsonUserGroupImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_user_group_resource_add_user_to_user_group_post**
> list[JsonUserImpl] resource_user_group_resource_add_user_to_user_group_post(user_group_id, body=body)

Adds users to existing user group.

Adds users to existing user group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupsApi()
user_group_id = 'user_group_id_example' # str | 
body = swagger_client.JsonAddUsersToUserGroupRequest() # JsonAddUsersToUserGroupRequest | the properties needed to add users to given user group (optional)

try:
    # Adds users to existing user group.
    api_response = api_instance.resource_user_group_resource_add_user_to_user_group_post(user_group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupsApi->resource_user_group_resource_add_user_to_user_group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**|  | 
 **body** | [**JsonAddUsersToUserGroupRequest**](JsonAddUsersToUserGroupRequest.md)| the properties needed to add users to given user group | [optional] 

### Return type

[**list[JsonUserImpl]**](JsonUserImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_user_group_resource_change_user_group_patch**
> JsonUserGroupImpl resource_user_group_resource_change_user_group_patch(user_group_id, body=body)

Changes the user group with the information that is present in the request.

Changes the user group with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupsApi()
user_group_id = 'user_group_id_example' # str | the <code>id</code> of the user group to be changed
body = swagger_client.JsonChangeUserGroupRequest() # JsonChangeUserGroupRequest | the properties of the user group to be changed (optional)

try:
    # Changes the user group with the information that is present in the request.
    api_response = api_instance.resource_user_group_resource_change_user_group_patch(user_group_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupsApi->resource_user_group_resource_change_user_group_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the user group to be changed | 
 **body** | [**JsonChangeUserGroupRequest**](JsonChangeUserGroupRequest.md)| the properties of the user group to be changed | [optional] 

### Return type

[**JsonUserGroupImpl**](JsonUserGroupImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_user_group_resource_find_user_groups_get**
> JsonUserGroupImpl resource_user_group_resource_find_user_groups_get(include_everyone=include_everyone, limit=limit, name=name, name_match_mode=name_match_mode, offset=offset, user_id=user_id)

Returns user groups matching the given search criteria.

Returns user groups matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned user groups satisfy all constraints that are specified in this search criteria. By default a result containing 1000 user groups is returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupsApi()
include_everyone = true # bool |  (optional)
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
name = 'name_example' # str | The name of the user group (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code>. (optional) (default to ANYWHERE)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)
user_id = 'user_id_example' # str | The <code>id</code> of the user who should belong to searched user groups (optional)

try:
    # Returns user groups matching the given search criteria.
    api_response = api_instance.resource_user_group_resource_find_user_groups_get(include_everyone=include_everyone, limit=limit, name=name, name_match_mode=name_match_mode, offset=offset, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupsApi->resource_user_group_resource_find_user_groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_everyone** | **bool**|  | [optional] 
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **name** | **str**| The name of the user group | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. | [optional] [default to ANYWHERE]
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]
 **user_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the user who should belong to searched user groups | [optional] 

### Return type

[**JsonUserGroupImpl**](JsonUserGroupImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_user_group_resource_get_user_group_get**
> JsonUserGroupImpl resource_user_group_resource_get_user_group_get(user_group_id)

Returns user group identified by given id.

Returns user group identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupsApi()
user_group_id = 'user_group_id_example' # str | the <code>id</code> of the user group

try:
    # Returns user group identified by given id.
    api_response = api_instance.resource_user_group_resource_get_user_group_get(user_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupsApi->resource_user_group_resource_get_user_group_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the user group | 

### Return type

[**JsonUserGroupImpl**](JsonUserGroupImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_user_group_resource_remove_user_group_delete**
> resource_user_group_resource_remove_user_group_delete(user_group_id)

Removes user group identified by given id.

Removes user group identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupsApi()
user_group_id = 'user_group_id_example' # str | the <code>id</code> of the user group to remove

try:
    # Removes user group identified by given id.
    api_instance.resource_user_group_resource_remove_user_group_delete(user_group_id)
except ApiException as e:
    print("Exception when calling UserGroupsApi->resource_user_group_resource_remove_user_group_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the user group to remove | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_user_group_resource_remove_users_from_user_group_delete**
> resource_user_group_resource_remove_users_from_user_group_delete(user_group_id, body=body)

Removes users from the user group identified by given id.

Removes users from the user group identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserGroupsApi()
user_group_id = 'user_group_id_example' # str | the <code>id</code> of the user group
body = swagger_client.JsonRemoveUsersFromUserGroupRequest() # JsonRemoveUsersFromUserGroupRequest | the properties needed to remove the users from given user group (optional)

try:
    # Removes users from the user group identified by given id.
    api_instance.resource_user_group_resource_remove_users_from_user_group_delete(user_group_id, body=body)
except ApiException as e:
    print("Exception when calling UserGroupsApi->resource_user_group_resource_remove_users_from_user_group_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the user group | 
 **body** | [**JsonRemoveUsersFromUserGroupRequest**](JsonRemoveUsersFromUserGroupRequest.md)| the properties needed to remove the users from given user group | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

