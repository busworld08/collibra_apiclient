# swagger_client.WorkflowTasksApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_workflow_task_resource_cancel_workflow_task_post**](WorkflowTasksApi.md#resource_workflow_task_resource_cancel_workflow_task_post) | **POST** /workflowTasks/{workflowTaskId}/canceled | Cancels the workflow task identified by the given id with provided reason.
[**resource_workflow_task_resource_complete_workflow_tasks_post**](WorkflowTasksApi.md#resource_workflow_task_resource_complete_workflow_tasks_post) | **POST** /workflowTasks/completed | Completes and returns the workflow tasks basing on the provided request.
[**resource_workflow_task_resource_find_workflow_tasks_get**](WorkflowTasksApi.md#resource_workflow_task_resource_find_workflow_tasks_get) | **GET** /workflowTasks | Returns the workflow tasks matching given search criteria.
[**resource_workflow_task_resource_get_task_form_data_get**](WorkflowTasksApi.md#resource_workflow_task_resource_get_task_form_data_get) | **GET** /workflowTasks/{workflowTaskId}/taskFormData | Returns the task form data of the workflow task.
[**resource_workflow_task_resource_get_workflow_task_get**](WorkflowTasksApi.md#resource_workflow_task_resource_get_workflow_task_get) | **GET** /workflowTasks/{workflowTaskId} | Returns the workflow task identified by given id.


# **resource_workflow_task_resource_cancel_workflow_task_post**
> file resource_workflow_task_resource_cancel_workflow_task_post(workflow_task_id, body=body)

Cancels the workflow task identified by the given id with provided reason.

Cancels the workflow task identified by the given id with provided reason. If the given workflow is a subprocess, this method makes sure everything is cancelled from the root process instance. If the given task is not found, this method will assume it already was cancelled without throwing any error.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowTasksApi()
workflow_task_id = 'workflow_task_id_example' # str | the <code>id</code> of the workflow task to be cancelled
body = 'body_example' # str | the reason for the cancellation of the workflow instance (optional)

try:
    # Cancels the workflow task identified by the given id with provided reason.
    api_response = api_instance.resource_workflow_task_resource_cancel_workflow_task_post(workflow_task_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowTasksApi->resource_workflow_task_resource_cancel_workflow_task_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_task_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the workflow task to be cancelled | 
 **body** | **str**| the reason for the cancellation of the workflow instance | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_task_resource_complete_workflow_tasks_post**
> list[JsonWorkflowTaskImpl] resource_workflow_task_resource_complete_workflow_tasks_post(body=body)

Completes and returns the workflow tasks basing on the provided request.

Completes and returns the workflow tasks basing on the provided request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowTasksApi()
body = swagger_client.JsonCompleteWorkflowTasksRequest() # JsonCompleteWorkflowTasksRequest | the request describing the parameters for the workflow tasks to complete (optional)

try:
    # Completes and returns the workflow tasks basing on the provided request.
    api_response = api_instance.resource_workflow_task_resource_complete_workflow_tasks_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowTasksApi->resource_workflow_task_resource_complete_workflow_tasks_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonCompleteWorkflowTasksRequest**](JsonCompleteWorkflowTasksRequest.md)| the request describing the parameters for the workflow tasks to complete | [optional] 

### Return type

[**list[JsonWorkflowTaskImpl]**](JsonWorkflowTaskImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_task_resource_find_workflow_tasks_get**
> JsonPagedResponse resource_workflow_task_resource_find_workflow_tasks_get(business_item_id=business_item_id, business_item_name=business_item_name, business_item_type=business_item_type, create_date=create_date, due_date=due_date, limit=limit, offset=offset, sort_field=sort_field, sort_order=sort_order, title=title, type=type, user_id=user_id, workflow_task_user_relation=workflow_task_user_relation)

Returns the workflow tasks matching given search criteria.

Returns the workflow tasks matching given search criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowTasksApi()
business_item_id = 'business_item_id_example' # str | The <code>id</code> of the business item (optional)
business_item_name = 'business_item_name_example' # str | The part of the name of the business item (optional)
business_item_type = 'business_item_type_example' # str | The type of the business item (optional)
create_date = 8.14 # float | The creation date of the task. It is the timestamp (in UTC time standard) (optional)
due_date = 8.14 # float | The due date of the task. It is the timestamp (in UTC time standard) (optional)
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)
sort_field = 'DUE_DATE' # str | The field on which the results are sorted. On due date by default. For possible values see SortField (optional) (default to DUE_DATE)
sort_order = 'DESC' # str | The sorting order (optional) (default to DESC)
title = 'title_example' # str | The title/name of the task (optional)
type = 'type_example' # str | The task type (optional)
user_id = 'user_id_example' # str | The <code>id</code> of the user for which the tasks need to be returned. If empty, the current logged in user will be used (optional)
workflow_task_user_relation = 'ALL' # str | The type of relation between user and searched tasks <p> This could be either set to search for all the tasks the user is permitted to view or just those assigned to the user. (optional) (default to ALL)

try:
    # Returns the workflow tasks matching given search criteria.
    api_response = api_instance.resource_workflow_task_resource_find_workflow_tasks_get(business_item_id=business_item_id, business_item_name=business_item_name, business_item_type=business_item_type, create_date=create_date, due_date=due_date, limit=limit, offset=offset, sort_field=sort_field, sort_order=sort_order, title=title, type=type, user_id=user_id, workflow_task_user_relation=workflow_task_user_relation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowTasksApi->resource_workflow_task_resource_find_workflow_tasks_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_item_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the business item | [optional] 
 **business_item_name** | **str**| The part of the name of the business item | [optional] 
 **business_item_type** | **str**| The type of the business item | [optional] 
 **create_date** | **float**| The creation date of the task. It is the timestamp (in UTC time standard) | [optional] 
 **due_date** | **float**| The due date of the task. It is the timestamp (in UTC time standard) | [optional] 
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]
 **sort_field** | **str**| The field on which the results are sorted. On due date by default. For possible values see SortField | [optional] [default to DUE_DATE]
 **sort_order** | **str**| The sorting order | [optional] [default to DESC]
 **title** | **str**| The title/name of the task | [optional] 
 **type** | **str**| The task type | [optional] 
 **user_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the user for which the tasks need to be returned. If empty, the current logged in user will be used | [optional] 
 **workflow_task_user_relation** | **str**| The type of relation between user and searched tasks &lt;p&gt; This could be either set to search for all the tasks the user is permitted to view or just those assigned to the user. | [optional] [default to ALL]

### Return type

[**JsonPagedResponse**](JsonPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_task_resource_get_task_form_data_get**
> JsonTaskFormDataImpl resource_workflow_task_resource_get_task_form_data_get(workflow_task_id, form_property_type=form_property_type)

Returns the task form data of the workflow task.

Returns the task form data of the workflow task.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowTasksApi()
workflow_task_id = 'workflow_task_id_example' # str | the <code>id</code> of the workflow task that should be used for the form data retrieval
form_property_type = 'form_property_type_example' # str | the form type to be returned (optional)

try:
    # Returns the task form data of the workflow task.
    api_response = api_instance.resource_workflow_task_resource_get_task_form_data_get(workflow_task_id, form_property_type=form_property_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowTasksApi->resource_workflow_task_resource_get_task_form_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_task_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the workflow task that should be used for the form data retrieval | 
 **form_property_type** | **str**| the form type to be returned | [optional] 

### Return type

[**JsonTaskFormDataImpl**](JsonTaskFormDataImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_task_resource_get_workflow_task_get**
> JsonWorkflowTaskImpl resource_workflow_task_resource_get_workflow_task_get(workflow_task_id)

Returns the workflow task identified by given id.

Returns the workflow task identified by given id. A task will only be returned when the user has the correct permission to view it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowTasksApi()
workflow_task_id = 'workflow_task_id_example' # str | the <code>id</code> of the workflow task to return

try:
    # Returns the workflow task identified by given id.
    api_response = api_instance.resource_workflow_task_resource_get_workflow_task_get(workflow_task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowTasksApi->resource_workflow_task_resource_get_workflow_task_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_task_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the workflow task to return | 

### Return type

[**JsonWorkflowTaskImpl**](JsonWorkflowTaskImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

