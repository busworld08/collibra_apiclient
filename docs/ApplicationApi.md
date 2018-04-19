# swagger_client.ApplicationApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_application_resource_get_info_get**](ApplicationApi.md#resource_application_resource_get_info_get) | **GET** /application/info | Returns the basic information about the application.


# **resource_application_resource_get_info_get**
> JsonApplicationInfoImpl resource_application_resource_get_info_get()

Returns the basic information about the application.

Returns the basic information about the application.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationApi()

try:
    # Returns the basic information about the application.
    api_response = api_instance.resource_application_resource_get_info_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationApi->resource_application_resource_get_info_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonApplicationInfoImpl**](JsonApplicationInfoImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

