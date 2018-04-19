# swagger_client.JobsApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_job_resource_cancel_job_post**](JobsApi.md#resource_job_resource_cancel_job_post) | **POST** /jobs/{jobId}/canceled | Cancels given job.
[**resource_job_resource_get_job_get**](JobsApi.md#resource_job_resource_get_job_get) | **GET** /jobs/{jobId} | Returns the job identified by given UUID.


# **resource_job_resource_cancel_job_post**
> file resource_job_resource_cancel_job_post(job_id, body=body)

Cancels given job.

Cancels given job. This method will return immediately and not wait until the job is actually stopped.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
job_id = 'job_id_example' # str | 
body = swagger_client.JsonCancelJobRequest() # JsonCancelJobRequest | the properties of this cancel request. (optional)

try:
    # Cancels given job.
    api_response = api_instance.resource_job_resource_cancel_job_post(job_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->resource_job_resource_cancel_job_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 
 **body** | [**JsonCancelJobRequest**](JsonCancelJobRequest.md)| the properties of this cancel request. | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_job_resource_get_job_get**
> JsonJobImpl resource_job_resource_get_job_get(job_id)

Returns the job identified by given UUID.

Returns the job identified by given UUID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JobsApi()
job_id = 'job_id_example' # str | the UUID of the asset

try:
    # Returns the job identified by given UUID.
    api_response = api_instance.resource_job_resource_get_job_get(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->resource_job_resource_get_job_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| the UUID of the asset | 

### Return type

[**JsonJobImpl**](JsonJobImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

