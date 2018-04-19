# swagger_client.AuthenticationSessionsApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_session_resource_is_logged_in_get**](AuthenticationSessionsApi.md#resource_session_resource_is_logged_in_get) | **GET** /auth/sessions/current | Gets current session (checks if user is logged in).
[**resource_session_resource_login_post**](AuthenticationSessionsApi.md#resource_session_resource_login_post) | **POST** /auth/sessions | Login.
[**resource_session_resource_logout_delete**](AuthenticationSessionsApi.md#resource_session_resource_logout_delete) | **DELETE** /auth/sessions/current | Logout.


# **resource_session_resource_is_logged_in_get**
> file resource_session_resource_is_logged_in_get()

Gets current session (checks if user is logged in).

Gets current session (checks if user is logged in). Returns <code>401</code> if the user is not authenticated and session does not exist.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationSessionsApi()

try:
    # Gets current session (checks if user is logged in).
    api_response = api_instance.resource_session_resource_is_logged_in_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSessionsApi->resource_session_resource_is_logged_in_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_session_resource_login_post**
> file resource_session_resource_login_post(body=body)

Login.

Login. Authenticates a user and creates a new session on the server. Once the user is authenticated then the returned session id can be used to access DGC REST Api in subsequent requests. The method additionally returns the JSESSIONID cookie in a <code>Set-Cookie</code> header. If user already has an open session then this session will be terminated.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationSessionsApi()
body = swagger_client.JsonLoginRequest() # JsonLoginRequest |  (optional)

try:
    # Login.
    api_response = api_instance.resource_session_resource_login_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationSessionsApi->resource_session_resource_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonLoginRequest**](JsonLoginRequest.md)|  | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_session_resource_logout_delete**
> resource_session_resource_logout_delete()

Logout.

Logout. Logs current user out and destroys the active session. Returns <code>401</code> if user is not authenticated.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationSessionsApi()

try:
    # Logout.
    api_instance.resource_session_resource_logout_delete()
except ApiException as e:
    print("Exception when calling AuthenticationSessionsApi->resource_session_resource_logout_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

