# swagger_client.FilesApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_file_resource_add_files_post**](FilesApi.md#resource_file_resource_add_files_post) | **POST** /files | Uploads files.
[**resource_file_resource_get_file_get**](FilesApi.md#resource_file_resource_get_file_get) | **GET** /files/{fileId} | Downloads file identified by given id.
[**resource_file_resource_get_file_info_get**](FilesApi.md#resource_file_resource_get_file_info_get) | **GET** /files/{fileId}/info | Returns information about the file identified by given id.


# **resource_file_resource_add_files_post**
> list[JsonFileInfoImpl] resource_file_resource_add_files_post(body=body)

Uploads files.

Uploads files.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FilesApi()
body = swagger_client.null() #  | the properties of the files to be uploaded (optional)

try:
    # Uploads files.
    api_response = api_instance.resource_file_resource_add_files_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->resource_file_resource_add_files_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [****](.md)| the properties of the files to be uploaded | [optional] 

### Return type

[**list[JsonFileInfoImpl]**](JsonFileInfoImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_file_resource_get_file_get**
> file resource_file_resource_get_file_get(file_id)

Downloads file identified by given id.

Downloads file identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FilesApi()
file_id = 'file_id_example' # str | the UUID of the file

try:
    # Downloads file identified by given id.
    api_response = api_instance.resource_file_resource_get_file_get(file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->resource_file_resource_get_file_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| the UUID of the file | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_file_resource_get_file_info_get**
> JsonFileInfoImpl resource_file_resource_get_file_info_get(file_id)

Returns information about the file identified by given id.

Returns information about the file identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FilesApi()
file_id = 'file_id_example' # str | the UUID of the file

try:
    # Returns information about the file identified by given id.
    api_response = api_instance.resource_file_resource_get_file_info_get(file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->resource_file_resource_get_file_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| the UUID of the file | 

### Return type

[**JsonFileInfoImpl**](JsonFileInfoImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

