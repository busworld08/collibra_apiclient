# swagger_client.IssuesApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_issue_resource_add_issue_post**](IssuesApi.md#resource_issue_resource_add_issue_post) | **POST** /issues | Add a new issue with the given parameters.
[**resource_issue_resource_find_issues_get**](IssuesApi.md#resource_issue_resource_find_issues_get) | **GET** /issues | Returns issues matching the given search criteria.


# **resource_issue_resource_add_issue_post**
> JsonAssetImpl resource_issue_resource_add_issue_post(body=body)

Add a new issue with the given parameters.

Add a new issue with the given parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssuesApi()
body = swagger_client.JsonAddIssueRequest() # JsonAddIssueRequest | the properties of the issue to be added (optional)

try:
    # Add a new issue with the given parameters.
    api_response = api_instance.resource_issue_resource_add_issue_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->resource_issue_resource_add_issue_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAddIssueRequest**](JsonAddIssueRequest.md)| the properties of the issue to be added | [optional] 

### Return type

[**JsonAssetImpl**](JsonAssetImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_issue_resource_find_issues_get**
> JsonAssetImpl resource_issue_resource_find_issues_get(limit=limit, offset=offset, only_open_issues=only_open_issues, sort_field=sort_field, sort_order=sort_order, user_relation=user_relation)

Returns issues matching the given search criteria.

Returns issues matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned issues satisfy all constraints that are specified in this search criteria. By default a result containing 1000 issues is returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IssuesApi()
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)
only_open_issues = true # bool | Whether only open issues should be returned (optional) (default to true)
sort_field = 'NAME' # str | The field on which the results are sorted. Default is NAME (optional) (default to NAME)
sort_order = 'ASC' # str | The sorting order of the results (optional) (default to ASC)
user_relation = 'ALL' # str | The relation of the user with the issues to be returned. By default all issues for the current user will be returned. (optional) (default to ALL)

try:
    # Returns issues matching the given search criteria.
    api_response = api_instance.resource_issue_resource_find_issues_get(limit=limit, offset=offset, only_open_issues=only_open_issues, sort_field=sort_field, sort_order=sort_order, user_relation=user_relation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->resource_issue_resource_find_issues_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]
 **only_open_issues** | **bool**| Whether only open issues should be returned | [optional] [default to true]
 **sort_field** | **str**| The field on which the results are sorted. Default is NAME | [optional] [default to NAME]
 **sort_order** | **str**| The sorting order of the results | [optional] [default to ASC]
 **user_relation** | **str**| The relation of the user with the issues to be returned. By default all issues for the current user will be returned. | [optional] [default to ALL]

### Return type

[**JsonAssetImpl**](JsonAssetImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

