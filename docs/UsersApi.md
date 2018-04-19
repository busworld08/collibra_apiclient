# swagger_client.UsersApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_user_resource_add_user_groups_for_user_post**](UsersApi.md#resource_user_resource_add_user_groups_for_user_post) | **POST** /users/{userId}/userGroups | Adds user to multiple user groups.
[**resource_user_resource_add_user_post**](UsersApi.md#resource_user_resource_add_user_post) | **POST** /users | Adds new user.
[**resource_user_resource_add_users_post**](UsersApi.md#resource_user_resource_add_users_post) | **POST** /users/bulk | Adds multiple users.
[**resource_user_resource_change_user_avatar_patch**](UsersApi.md#resource_user_resource_change_user_avatar_patch) | **PATCH** /users/{userId}/avatar | Changes the avatar for the user identified by given id.
[**resource_user_resource_change_user_patch**](UsersApi.md#resource_user_resource_change_user_patch) | **PATCH** /users/{userId} | Changes the user with the information that is present in the request.
[**resource_user_resource_find_users_get**](UsersApi.md#resource_user_resource_find_users_get) | **GET** /users | Returns users matching the given search criteria.
[**resource_user_resource_get_avatar_file_get**](UsersApi.md#resource_user_resource_get_avatar_file_get) | **GET** /users/{userId}/avatar | Return the avatar image for the user identified with the requested UUID.
[**resource_user_resource_get_current_user_get**](UsersApi.md#resource_user_resource_get_current_user_get) | **GET** /users/current | Returns current user, if logged in.
[**resource_user_resource_get_user_by_email_address_get**](UsersApi.md#resource_user_resource_get_user_by_email_address_get) | **GET** /users/email/{emailAddress} | Returns user identified by given email address.
[**resource_user_resource_get_user_get**](UsersApi.md#resource_user_resource_get_user_get) | **GET** /users/{userId} | Returns user identified by given id.
[**resource_user_resource_remove_user_from_user_groups_delete**](UsersApi.md#resource_user_resource_remove_user_from_user_groups_delete) | **DELETE** /users/{userId}/userGroups | Removes user from multiple user groups.
[**resource_user_resource_set_user_groups_for_user_put**](UsersApi.md#resource_user_resource_set_user_groups_for_user_put) | **PUT** /users/{userId}/userGroups | Sets user groups for user identified by given id.


# **resource_user_resource_add_user_groups_for_user_post**
> list[JsonUserGroupImpl] resource_user_resource_add_user_groups_for_user_post(user_id, body=body)

Adds user to multiple user groups.

Adds user to multiple user groups.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 'user_id_example' # str | the <code>id</code> of the user
body = swagger_client.JsonAddUserToUserGroupsRequest() # JsonAddUserToUserGroupsRequest | the properties needed to add the user to the user groups (optional)

try:
    # Adds user to multiple user groups.
    api_response = api_instance.resource_user_resource_add_user_groups_for_user_post(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->resource_user_resource_add_user_groups_for_user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the user | 
 **body** | [**JsonAddUserToUserGroupsRequest**](JsonAddUserToUserGroupsRequest.md)| the properties needed to add the user to the user groups | [optional] 

### Return type

[**list[JsonUserGroupImpl]**](JsonUserGroupImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_user_resource_add_user_post**
> JsonUserImpl resource_user_resource_add_user_post(body=body)

Adds new user.

Adds new user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.JsonAddUserRequest() # JsonAddUserRequest | the properties of the user to be added (optional)

try:
    # Adds new user.
    api_response = api_instance.resource_user_resource_add_user_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->resource_user_resource_add_user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAddUserRequest**](JsonAddUserRequest.md)| the properties of the user to be added | [optional] 

### Return type

[**JsonUserImpl**](JsonUserImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_user_resource_add_users_post**
> list[JsonUserImpl] resource_user_resource_add_users_post(body=body)

Adds multiple users.

Adds multiple users.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = [swagger_client.JsonAddUserRequest()] # list[JsonAddUserRequest] | the properties of the users to be added (optional)

try:
    # Adds multiple users.
    api_response = api_instance.resource_user_resource_add_users_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->resource_user_resource_add_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JsonAddUserRequest]**](JsonAddUserRequest.md)| the properties of the users to be added | [optional] 

### Return type

[**list[JsonUserImpl]**](JsonUserImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_user_resource_change_user_avatar_patch**
> JsonUserImpl resource_user_resource_change_user_avatar_patch(user_id, body=body)

Changes the avatar for the user identified by given id.

Changes the avatar for the user identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 'user_id_example' # str | the <code>id</code> of the user to change the avatar for
body = swagger_client.JsonChangeUserAvatarRequest() # JsonChangeUserAvatarRequest | the properties needed to change to avatar for the user (optional)

try:
    # Changes the avatar for the user identified by given id.
    api_response = api_instance.resource_user_resource_change_user_avatar_patch(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->resource_user_resource_change_user_avatar_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the user to change the avatar for | 
 **body** | [**JsonChangeUserAvatarRequest**](JsonChangeUserAvatarRequest.md)| the properties needed to change to avatar for the user | [optional] 

### Return type

[**JsonUserImpl**](JsonUserImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_user_resource_change_user_patch**
> JsonUserImpl resource_user_resource_change_user_patch(user_id, body=body)

Changes the user with the information that is present in the request.

Changes the user with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 'user_id_example' # str | the <code>id</code> of the user to be changed
body = swagger_client.JsonChangeUserRequest() # JsonChangeUserRequest | the properties of the user to be changed (optional)

try:
    # Changes the user with the information that is present in the request.
    api_response = api_instance.resource_user_resource_change_user_patch(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->resource_user_resource_change_user_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the user to be changed | 
 **body** | [**JsonChangeUserRequest**](JsonChangeUserRequest.md)| the properties of the user to be changed | [optional] 

### Return type

[**JsonUserImpl**](JsonUserImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_user_resource_find_users_get**
> JsonUserImpl resource_user_resource_find_users_get(group_id=group_id, include_disabled=include_disabled, limit=limit, name=name, offset=offset, only_logged_in=only_logged_in)

Returns users matching the given search criteria.

Returns users matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned users satisfy all constraints that are specified in this search criteria. By default a result containing 1000 users is returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
group_id = 'group_id_example' # str | The <code>id</code> of the group the searched users should belong to (optional)
include_disabled = true # bool | Whether disabled users should be included in the search results (optional)
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
name = 'name_example' # str | The name of the user. The search will occur in the username, firstname and lastname (and a combination) (optional)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)
only_logged_in = true # bool | Whether only currently logged in users should be returned (optional)

try:
    # Returns users matching the given search criteria.
    api_response = api_instance.resource_user_resource_find_users_get(group_id=group_id, include_disabled=include_disabled, limit=limit, name=name, offset=offset, only_logged_in=only_logged_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->resource_user_resource_find_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the group the searched users should belong to | [optional] 
 **include_disabled** | **bool**| Whether disabled users should be included in the search results | [optional] 
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **name** | **str**| The name of the user. The search will occur in the username, firstname and lastname (and a combination) | [optional] 
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]
 **only_logged_in** | **bool**| Whether only currently logged in users should be returned | [optional] 

### Return type

[**JsonUserImpl**](JsonUserImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_user_resource_get_avatar_file_get**
> file resource_user_resource_get_avatar_file_get(user_id, height=height, width=width)

Return the avatar image for the user identified with the requested UUID.

Return the avatar image for the user identified with the requested UUID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 'user_id_example' # str | the UUID of the user to get the avatar UUID for
height = 56 # int |  (optional)
width = 56 # int |  (optional)

try:
    # Return the avatar image for the user identified with the requested UUID.
    api_response = api_instance.resource_user_resource_get_avatar_file_get(user_id, height=height, width=width)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->resource_user_resource_get_avatar_file_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| the UUID of the user to get the avatar UUID for | 
 **height** | **int**|  | [optional] 
 **width** | **int**|  | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_user_resource_get_current_user_get**
> JsonUserImpl resource_user_resource_get_current_user_get()

Returns current user, if logged in.

Returns current user, if logged in.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()

try:
    # Returns current user, if logged in.
    api_response = api_instance.resource_user_resource_get_current_user_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->resource_user_resource_get_current_user_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonUserImpl**](JsonUserImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_user_resource_get_user_by_email_address_get**
> JsonUserImpl resource_user_resource_get_user_by_email_address_get(email_address)

Returns user identified by given email address.

Returns user identified by given email address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
email_address = 'email_address_example' # str | the email address of the user

try:
    # Returns user identified by given email address.
    api_response = api_instance.resource_user_resource_get_user_by_email_address_get(email_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->resource_user_resource_get_user_by_email_address_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_address** | **str**| the email address of the user | 

### Return type

[**JsonUserImpl**](JsonUserImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_user_resource_get_user_get**
> JsonUserImpl resource_user_resource_get_user_get(user_id)

Returns user identified by given id.

Returns user identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 'user_id_example' # str | the <code>id</code> of the user

try:
    # Returns user identified by given id.
    api_response = api_instance.resource_user_resource_get_user_get(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->resource_user_resource_get_user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the user | 

### Return type

[**JsonUserImpl**](JsonUserImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_user_resource_remove_user_from_user_groups_delete**
> resource_user_resource_remove_user_from_user_groups_delete(user_id, body=body)

Removes user from multiple user groups.

Removes user from multiple user groups.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 'user_id_example' # str | the <code>id</code> of the user
body = swagger_client.JsonRemoveUserFromUserGroupsRequest() # JsonRemoveUserFromUserGroupsRequest | the properties needed to remove the user from user groups (optional)

try:
    # Removes user from multiple user groups.
    api_instance.resource_user_resource_remove_user_from_user_groups_delete(user_id, body=body)
except ApiException as e:
    print("Exception when calling UsersApi->resource_user_resource_remove_user_from_user_groups_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the user | 
 **body** | [**JsonRemoveUserFromUserGroupsRequest**](JsonRemoveUserFromUserGroupsRequest.md)| the properties needed to remove the user from user groups | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_user_resource_set_user_groups_for_user_put**
> JsonUserImpl resource_user_resource_set_user_groups_for_user_put(user_id, body=body)

Sets user groups for user identified by given id.

Sets user groups for user identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 'user_id_example' # str | the <code>id</code> of the user
body = swagger_client.JsonSetUserGroupsForUserRequest() # JsonSetUserGroupsForUserRequest | the properties needed to add the user to user groups (optional)

try:
    # Sets user groups for user identified by given id.
    api_response = api_instance.resource_user_resource_set_user_groups_for_user_put(user_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->resource_user_resource_set_user_groups_for_user_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the user | 
 **body** | [**JsonSetUserGroupsForUserRequest**](JsonSetUserGroupsForUserRequest.md)| the properties needed to add the user to user groups | [optional] 

### Return type

[**JsonUserImpl**](JsonUserImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

