# swagger_client.CommentsApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_comment_resource_add_comment_post**](CommentsApi.md#resource_comment_resource_add_comment_post) | **POST** /comments | Adds new comment.
[**resource_comment_resource_change_comment_patch**](CommentsApi.md#resource_comment_resource_change_comment_patch) | **PATCH** /comments/{commentId} | Changes the comment with the information that is present in the request.
[**resource_comment_resource_find_comments_get**](CommentsApi.md#resource_comment_resource_find_comments_get) | **GET** /comments | Returns comments matching the given search criteria.
[**resource_comment_resource_get_comment_get**](CommentsApi.md#resource_comment_resource_get_comment_get) | **GET** /comments/{commentId} | Returns comment identified by given id.
[**resource_comment_resource_remove_comment_delete**](CommentsApi.md#resource_comment_resource_remove_comment_delete) | **DELETE** /comments/{commentId} | Removes comment identified by given id.


# **resource_comment_resource_add_comment_post**
> JsonCommentImpl resource_comment_resource_add_comment_post(body=body)

Adds new comment.

Adds new comment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommentsApi()
body = swagger_client.JsonAddCommentRequest() # JsonAddCommentRequest | the properties of the comment to be added (optional)

try:
    # Adds new comment.
    api_response = api_instance.resource_comment_resource_add_comment_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->resource_comment_resource_add_comment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAddCommentRequest**](JsonAddCommentRequest.md)| the properties of the comment to be added | [optional] 

### Return type

[**JsonCommentImpl**](JsonCommentImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_comment_resource_change_comment_patch**
> JsonCommentImpl resource_comment_resource_change_comment_patch(comment_id, body=body)

Changes the comment with the information that is present in the request.

Changes the comment with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommentsApi()
comment_id = 'comment_id_example' # str | the <code>id</code> of the comment to be changed
body = swagger_client.JsonChangeCommentRequest() # JsonChangeCommentRequest | the properties of the comment to be changed (optional)

try:
    # Changes the comment with the information that is present in the request.
    api_response = api_instance.resource_comment_resource_change_comment_patch(comment_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->resource_comment_resource_change_comment_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the comment to be changed | 
 **body** | [**JsonChangeCommentRequest**](JsonChangeCommentRequest.md)| the properties of the comment to be changed | [optional] 

### Return type

[**JsonCommentImpl**](JsonCommentImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_comment_resource_find_comments_get**
> JsonCommentImpl resource_comment_resource_find_comments_get(base_resource_id=base_resource_id, limit=limit, offset=offset, parent_id=parent_id, root_comment=root_comment, sort_order=sort_order, user_id=user_id)

Returns comments matching the given search criteria.

Returns comments matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned comments satisfy all constraints that are specified in this search criteria. By default a result containing 1000 comments is returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommentsApi()
base_resource_id = 'base_resource_id_example' # str | The <code>id</code> of the resource which the searched comments refer to (optional)
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)
parent_id = 'parent_id_example' # str | The <code>id</code> of the comment which the reply comments should be searched for (optional)
root_comment = true # bool | Whether the searched comments should be root comments (not reply comments) (optional)
sort_order = 'DESC' # str | The order of sorting on the date the comment was created (optional) (default to DESC)
user_id = 'user_id_example' # str | The <code>id</code> of the user who created the comment (optional)

try:
    # Returns comments matching the given search criteria.
    api_response = api_instance.resource_comment_resource_find_comments_get(base_resource_id=base_resource_id, limit=limit, offset=offset, parent_id=parent_id, root_comment=root_comment, sort_order=sort_order, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->resource_comment_resource_find_comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_resource_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the resource which the searched comments refer to | [optional] 
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]
 **parent_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the comment which the reply comments should be searched for | [optional] 
 **root_comment** | **bool**| Whether the searched comments should be root comments (not reply comments) | [optional] 
 **sort_order** | **str**| The order of sorting on the date the comment was created | [optional] [default to DESC]
 **user_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the user who created the comment | [optional] 

### Return type

[**JsonCommentImpl**](JsonCommentImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_comment_resource_get_comment_get**
> JsonCommentImpl resource_comment_resource_get_comment_get(comment_id)

Returns comment identified by given id.

Returns comment identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommentsApi()
comment_id = 'comment_id_example' # str | the <code>id</code> of the comment

try:
    # Returns comment identified by given id.
    api_response = api_instance.resource_comment_resource_get_comment_get(comment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->resource_comment_resource_get_comment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the comment | 

### Return type

[**JsonCommentImpl**](JsonCommentImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_comment_resource_remove_comment_delete**
> resource_comment_resource_remove_comment_delete(comment_id)

Removes comment identified by given id.

Removes comment identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommentsApi()
comment_id = 'comment_id_example' # str | the <code>id</code> of the comment to remove

try:
    # Removes comment identified by given id.
    api_instance.resource_comment_resource_remove_comment_delete(comment_id)
except ApiException as e:
    print("Exception when calling CommentsApi->resource_comment_resource_remove_comment_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the comment to remove | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

