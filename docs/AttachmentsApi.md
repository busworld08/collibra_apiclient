# swagger_client.AttachmentsApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_attachment_resource_add_attachment_post**](AttachmentsApi.md#resource_attachment_resource_add_attachment_post) | **POST** /attachments | Adds new attachment.
[**resource_attachment_resource_find_attachments_get**](AttachmentsApi.md#resource_attachment_resource_find_attachments_get) | **GET** /attachments | Returns attachments matching the given search criteria.
[**resource_attachment_resource_get_attachment_content_get**](AttachmentsApi.md#resource_attachment_resource_get_attachment_content_get) | **GET** /attachments/{attachmentId}/file | Returns content of the attachment identified by given id.
[**resource_attachment_resource_get_attachment_get**](AttachmentsApi.md#resource_attachment_resource_get_attachment_get) | **GET** /attachments/{attachmentId} | Returns information about the attachment identified by id.
[**resource_attachment_resource_remove_attachment_delete**](AttachmentsApi.md#resource_attachment_resource_remove_attachment_delete) | **DELETE** /attachments/{attachmentId} | Removes attachment identified by given id.


# **resource_attachment_resource_add_attachment_post**
> JsonAttachmentImpl resource_attachment_resource_add_attachment_post(file=file, file_name=file_name, resource_id=resource_id, resource_type=resource_type, body=body)

Adds new attachment.

Adds new attachment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttachmentsApi()
file = '/path/to/file.txt' # file | the file - attachment content (optional)
file_name = 'file_name_example' # str | the display name of the file of this attachment (optional)
resource_id = 'resource_id_example' # str | the id of the resource the attachment should refer to (optional)
resource_type = 'resource_type_example' # str | the type of the resource the attachment should refer to (optional)
body = swagger_client.null() #  |  (optional)

try:
    # Adds new attachment.
    api_response = api_instance.resource_attachment_resource_add_attachment_post(file=file, file_name=file_name, resource_id=resource_id, resource_type=resource_type, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->resource_attachment_resource_add_attachment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| the file - attachment content | [optional] 
 **file_name** | **str**| the display name of the file of this attachment | [optional] 
 **resource_id** | **str**| the id of the resource the attachment should refer to | [optional] 
 **resource_type** | **str**| the type of the resource the attachment should refer to | [optional] 
 **body** | [****](.md)|  | [optional] 

### Return type

[**JsonAttachmentImpl**](JsonAttachmentImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_attachment_resource_find_attachments_get**
> JsonAttachmentImpl resource_attachment_resource_find_attachments_get(base_resource_id=base_resource_id, file_content_type=file_content_type, file_name=file_name, limit=limit, offset=offset, sort_field=sort_field, sort_order=sort_order, upload_date=upload_date, user_id=user_id)

Returns attachments matching the given search criteria.

Returns attachments matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned attachments satisfy all constraints that are specified in this search criteria. By default a result containing 1000 attachments is returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttachmentsApi()
base_resource_id = 'base_resource_id_example' # str | The <code>id</code> of the resource the attachment refers to (optional)
file_content_type = 'file_content_type_example' # str | The type of the content of the file representing searched attachment (optional)
file_name = 'file_name_example' # str | The name of the file representing searched attachment (optional)
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)
sort_field = 'LAST_MODIFIED' # str | The field that should be used as reference for sorting (optional) (default to LAST_MODIFIED)
sort_order = 'DESC' # str | The order of sorting (optional) (default to DESC)
upload_date = 8.14 # float | The date of attachment upload. It is the timestamp (in UTC time standard) (optional)
user_id = 'user_id_example' # str | The <code>id</code> of the user who uploaded the attachment (optional)

try:
    # Returns attachments matching the given search criteria.
    api_response = api_instance.resource_attachment_resource_find_attachments_get(base_resource_id=base_resource_id, file_content_type=file_content_type, file_name=file_name, limit=limit, offset=offset, sort_field=sort_field, sort_order=sort_order, upload_date=upload_date, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->resource_attachment_resource_find_attachments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_resource_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the resource the attachment refers to | [optional] 
 **file_content_type** | **str**| The type of the content of the file representing searched attachment | [optional] 
 **file_name** | **str**| The name of the file representing searched attachment | [optional] 
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]
 **sort_field** | **str**| The field that should be used as reference for sorting | [optional] [default to LAST_MODIFIED]
 **sort_order** | **str**| The order of sorting | [optional] [default to DESC]
 **upload_date** | **float**| The date of attachment upload. It is the timestamp (in UTC time standard) | [optional] 
 **user_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the user who uploaded the attachment | [optional] 

### Return type

[**JsonAttachmentImpl**](JsonAttachmentImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_attachment_resource_get_attachment_content_get**
> file resource_attachment_resource_get_attachment_content_get(attachment_id)

Returns content of the attachment identified by given id.

Returns content of the attachment identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttachmentsApi()
attachment_id = 'attachment_id_example' # str | the <code>id</code> of the attachment

try:
    # Returns content of the attachment identified by given id.
    api_response = api_instance.resource_attachment_resource_get_attachment_content_get(attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->resource_attachment_resource_get_attachment_content_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the attachment | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_attachment_resource_get_attachment_get**
> JsonAttachmentImpl resource_attachment_resource_get_attachment_get(attachment_id)

Returns information about the attachment identified by id.

Returns information about the attachment identified by id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttachmentsApi()
attachment_id = 'attachment_id_example' # str | the <code>id</code> of the attachment

try:
    # Returns information about the attachment identified by id.
    api_response = api_instance.resource_attachment_resource_get_attachment_get(attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->resource_attachment_resource_get_attachment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the attachment | 

### Return type

[**JsonAttachmentImpl**](JsonAttachmentImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_attachment_resource_remove_attachment_delete**
> resource_attachment_resource_remove_attachment_delete(attachment_id)

Removes attachment identified by given id.

Removes attachment identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttachmentsApi()
attachment_id = 'attachment_id_example' # str | the <code>id</code> of the attachment to remove

try:
    # Removes attachment identified by given id.
    api_instance.resource_attachment_resource_remove_attachment_delete(attachment_id)
except ApiException as e:
    print("Exception when calling AttachmentsApi->resource_attachment_resource_remove_attachment_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the attachment to remove | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

