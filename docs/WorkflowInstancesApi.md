# swagger_client.WorkflowInstancesApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_workflow_instance_resource_cancel_workflow_instances_post**](WorkflowInstancesApi.md#resource_workflow_instance_resource_cancel_workflow_instances_post) | **POST** /workflowInstances/{workflowInstanceId}/canceled | Cancels the workflow instance identified by the given.
[**resource_workflow_instance_resource_find_workflow_instances_get**](WorkflowInstancesApi.md#resource_workflow_instance_resource_find_workflow_instances_get) | **GET** /workflowInstances | Returns workflow instances matching given search criteria.
[**resource_workflow_instance_resource_get_workflow_instance_diagram_get**](WorkflowInstancesApi.md#resource_workflow_instance_resource_get_workflow_instance_diagram_get) | **GET** /workflowInstances/{workflowInstanceId}/diagram | Returns the file representing the diagram of workflow instance identified by the given id.
[**resource_workflow_instance_resource_message_event_received_post**](WorkflowInstancesApi.md#resource_workflow_instance_resource_message_event_received_post) | **POST** /workflowInstances/{processInstanceId}/messageEvents/{messageName} | Passes the message event to the workflow engine.
[**resource_workflow_instance_resource_start_workflow_instances_in_job_post**](WorkflowInstancesApi.md#resource_workflow_instance_resource_start_workflow_instances_in_job_post) | **POST** /workflowInstances/startJobs | Starts workflow instances in job basing on the provided request.
[**resource_workflow_instance_resource_start_workflow_instances_post**](WorkflowInstancesApi.md#resource_workflow_instance_resource_start_workflow_instances_post) | **POST** /workflowInstances | Starts multiple workflow instances basing on the provided request.


# **resource_workflow_instance_resource_cancel_workflow_instances_post**
> file resource_workflow_instance_resource_cancel_workflow_instances_post(workflow_instance_id, body=body)

Cancels the workflow instance identified by the given.

Cancels the workflow instance identified by the given <code>id</code> with provided reason. Please be aware that cancelling a workflow, leaves possible parent workflow instances running, if you want them also to be cleaned up, you will have to cancel them explicitly.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowInstancesApi()
workflow_instance_id = 'workflow_instance_id_example' # str | the <code>id</code> of the workflow instance to be cancelled
body = 'body_example' # str | the reason for the cancellation of the workflow instance (optional)

try:
    # Cancels the workflow instance identified by the given.
    api_response = api_instance.resource_workflow_instance_resource_cancel_workflow_instances_post(workflow_instance_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowInstancesApi->resource_workflow_instance_resource_cancel_workflow_instances_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_instance_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the workflow instance to be cancelled | 
 **body** | **str**| the reason for the cancellation of the workflow instance | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_instance_resource_find_workflow_instances_get**
> JsonPagedResponse resource_workflow_instance_resource_find_workflow_instances_get(business_item_name=business_item_name, limit=limit, offset=offset, sort_field=sort_field, sort_order=sort_order, workflow_definition_id=workflow_definition_id)

Returns workflow instances matching given search criteria.

Returns workflow instances matching given search criteria.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowInstancesApi()
business_item_name = 'business_item_name_example' # str | The name of the business item that should be contained by the searched workflows (optional)
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)
sort_field = 'START_DATE' # str | The field on which the results are sorted (optional) (default to START_DATE)
sort_order = 'DESC' # str | The sorting order (optional) (default to DESC)
workflow_definition_id = 'workflow_definition_id_example' # str | The <code>id</code> of the workflow definition (optional)

try:
    # Returns workflow instances matching given search criteria.
    api_response = api_instance.resource_workflow_instance_resource_find_workflow_instances_get(business_item_name=business_item_name, limit=limit, offset=offset, sort_field=sort_field, sort_order=sort_order, workflow_definition_id=workflow_definition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowInstancesApi->resource_workflow_instance_resource_find_workflow_instances_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_item_name** | **str**| The name of the business item that should be contained by the searched workflows | [optional] 
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]
 **sort_field** | **str**| The field on which the results are sorted | [optional] [default to START_DATE]
 **sort_order** | **str**| The sorting order | [optional] [default to DESC]
 **workflow_definition_id** | **str**| The &lt;code&gt;id&lt;/code&gt; of the workflow definition | [optional] 

### Return type

[**JsonPagedResponse**](JsonPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_instance_resource_get_workflow_instance_diagram_get**
> resource_workflow_instance_resource_get_workflow_instance_diagram_get(workflow_instance_id)

Returns the file representing the diagram of workflow instance identified by the given id.

Returns the file representing the diagram of workflow instance identified by the given id. The diagram input stream returned can be null as deployed workflow defintions without graphical notation included don't have a diagram.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowInstancesApi()
workflow_instance_id = 'workflow_instance_id_example' # str | the <code>id</code> of the workflow instance to return the diagram for

try:
    # Returns the file representing the diagram of workflow instance identified by the given id.
    api_instance.resource_workflow_instance_resource_get_workflow_instance_diagram_get(workflow_instance_id)
except ApiException as e:
    print("Exception when calling WorkflowInstancesApi->resource_workflow_instance_resource_get_workflow_instance_diagram_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_instance_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the workflow instance to return the diagram for | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_instance_resource_message_event_received_post**
> file resource_workflow_instance_resource_message_event_received_post(message_name, process_instance_id, body=body)

Passes the message event to the workflow engine.

Passes the message event to the workflow engine. It will pass on this specific event to the engine with the given name, process instance and variables.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowInstancesApi()
message_name = 'message_name_example' # str | the name of the message to trigger
process_instance_id = 'process_instance_id_example' # str | the id of an instance of a process. Given process instance should have only one execution running at the time. Otherwise this method will fail.
body = swagger_client.JsonMessageEventReceivedRequest() # JsonMessageEventReceivedRequest | the properties of the message event (optional)

try:
    # Passes the message event to the workflow engine.
    api_response = api_instance.resource_workflow_instance_resource_message_event_received_post(message_name, process_instance_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowInstancesApi->resource_workflow_instance_resource_message_event_received_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_name** | **str**| the name of the message to trigger | 
 **process_instance_id** | **str**| the id of an instance of a process. Given process instance should have only one execution running at the time. Otherwise this method will fail. | 
 **body** | [**JsonMessageEventReceivedRequest**](JsonMessageEventReceivedRequest.md)| the properties of the message event | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_instance_resource_start_workflow_instances_in_job_post**
> JsonJobImplImpl resource_workflow_instance_resource_start_workflow_instances_in_job_post(body=body)

Starts workflow instances in job basing on the provided request.

Starts workflow instances in job basing on the provided request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowInstancesApi()
body = swagger_client.JsonStartWorkflowInstancesRequest() # JsonStartWorkflowInstancesRequest | the properties of the workflows to be started (optional)

try:
    # Starts workflow instances in job basing on the provided request.
    api_response = api_instance.resource_workflow_instance_resource_start_workflow_instances_in_job_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowInstancesApi->resource_workflow_instance_resource_start_workflow_instances_in_job_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonStartWorkflowInstancesRequest**](JsonStartWorkflowInstancesRequest.md)| the properties of the workflows to be started | [optional] 

### Return type

[**JsonJobImplImpl**](JsonJobImplImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_instance_resource_start_workflow_instances_post**
> list[JsonWorkflowInstanceImpl] resource_workflow_instance_resource_start_workflow_instances_post(body=body)

Starts multiple workflow instances basing on the provided request.

Starts multiple workflow instances basing on the provided request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowInstancesApi()
body = swagger_client.JsonStartWorkflowInstancesRequest() # JsonStartWorkflowInstancesRequest | the properties of the workflows to be started (optional)

try:
    # Starts multiple workflow instances basing on the provided request.
    api_response = api_instance.resource_workflow_instance_resource_start_workflow_instances_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowInstancesApi->resource_workflow_instance_resource_start_workflow_instances_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonStartWorkflowInstancesRequest**](JsonStartWorkflowInstancesRequest.md)| the properties of the workflows to be started | [optional] 

### Return type

[**list[JsonWorkflowInstanceImpl]**](JsonWorkflowInstanceImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

