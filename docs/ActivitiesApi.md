# swagger_client.ActivitiesApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_activity_stream_resource_get_activities_get**](ActivitiesApi.md#resource_activity_stream_resource_get_activities_get) | **GET** /activities | Returns activities matching the given search criteria.


# **resource_activity_stream_resource_get_activities_get**
> JsonActivityImpl resource_activity_stream_resource_get_activities_get(activity_type=activity_type, call_id=call_id, categories=categories, context_id=context_id, end_date=end_date, involved_people_ids=involved_people_ids, involved_role_ids=involved_role_ids, limit=limit, offset=offset, performed_by_role_ids=performed_by_role_ids, performed_by_user_id=performed_by_user_id, resource_types=resource_types, start_date=start_date, task_id=task_id)

Returns activities matching the given search criteria.

Returns activities matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned activities satisfy all constraints that are specified in this search criteria. By default a result containing 1000 activities is returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivitiesApi()
activity_type = 'activity_type_example' # str | The type of the activity (optional)
call_id = 'call_id_example' # str | The <code>id</code> of the call (optional)
categories = ['categories_example'] # list[str] | The set of the categories of activities that should be searched. One of [ATTRIBUTE, ATTACHMENT, RELATION, COMMENT, STATUS, WORKFLOW, RESPONSIBILITY, USER, USER_GROUP, ROLE, TAGS, OTHERS] (optional)
context_id = 'context_id_example' # str | The <code>id</code> of the context which the activities should be searched for (optional)
end_date = 8.14 # float | The end date of the searched activities. It is the timestamp (in UTC time standard) (optional)
involved_people_ids = ['involved_people_ids_example'] # list[str] | The list of <code>id</code>s of the people that should be involved in searched activities (optional)
involved_role_ids = ['involved_role_ids_example'] # list[str] | The list of <code>id</code>s of the roles that should be involved in searched activities (optional)
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)
performed_by_role_ids = ['performed_by_role_ids_example'] # list[str] | The list of <code>id</code>s of the roles assigned to users who performed searched activities (optional)
performed_by_user_id = 'performed_by_user_id_example' # str | The <code>id</code> of the user who performed searched activities (optional)
resource_types = ['resource_types_example'] # list[str] | The set of the resource types that searched activities refer to, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance] (optional)
start_date = 8.14 # float | The start date of the searched activities. It is the timestamp (in UTC time standard) (optional)
task_id = 'task_id_example' # str | The <code>id</code> of the task which contains the basic find activities request (optional)

try:
    # Returns activities matching the given search criteria.
    api_response = api_instance.resource_activity_stream_resource_get_activities_get(activity_type=activity_type, call_id=call_id, categories=categories, context_id=context_id, end_date=end_date, involved_people_ids=involved_people_ids, involved_role_ids=involved_role_ids, limit=limit, offset=offset, performed_by_role_ids=performed_by_role_ids, performed_by_user_id=performed_by_user_id, resource_types=resource_types, start_date=start_date, task_id=task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->resource_activity_stream_resource_get_activities_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_type** | **str**| The type of the activity | [optional] 
 **call_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the call | [optional] 
 **categories** | [**list[str]**](str.md)| The set of the categories of activities that should be searched. One of [ATTRIBUTE, ATTACHMENT, RELATION, COMMENT, STATUS, WORKFLOW, RESPONSIBILITY, USER, USER_GROUP, ROLE, TAGS, OTHERS] | [optional] 
 **context_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the context which the activities should be searched for | [optional] 
 **end_date** | **float**| The end date of the searched activities. It is the timestamp (in UTC time standard) | [optional] 
 **involved_people_ids** | [**list[str]**](str.md)| The list of &lt;code&gt;id&lt;/code&gt;s of the people that should be involved in searched activities | [optional] 
 **involved_role_ids** | [**list[str]**](str.md)| The list of &lt;code&gt;id&lt;/code&gt;s of the roles that should be involved in searched activities | [optional] 
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]
 **performed_by_role_ids** | [**list[str]**](str.md)| The list of &lt;code&gt;id&lt;/code&gt;s of the roles assigned to users who performed searched activities | [optional] 
 **performed_by_user_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the user who performed searched activities | [optional] 
 **resource_types** | [**list[str]**](str.md)| The set of the resource types that searched activities refer to, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance] | [optional] 
 **start_date** | **float**| The start date of the searched activities. It is the timestamp (in UTC time standard) | [optional] 
 **task_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the task which contains the basic find activities request | [optional] 

### Return type

[**JsonActivityImpl**](JsonActivityImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

