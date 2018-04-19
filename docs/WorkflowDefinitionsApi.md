# swagger_client.WorkflowDefinitionsApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_workflow_definition_resource_add_asset_type_assignment_rule_post**](WorkflowDefinitionsApi.md#resource_workflow_definition_resource_add_asset_type_assignment_rule_post) | **POST** /workflowDefinitions/{workflowDefinitionId}/assetTypeAssignmentRules | Adds an asset type assignment rule to the workflow definition specified in the request.
[**resource_workflow_definition_resource_add_domain_type_assignment_rule_post**](WorkflowDefinitionsApi.md#resource_workflow_definition_resource_add_domain_type_assignment_rule_post) | **POST** /workflowDefinitions/{workflowDefinitionId}/domainTypeAssignmentRules | Adds an domain type assignment rule to the workflow definition specified in the request.
[**resource_workflow_definition_resource_change_asset_type_assignment_rule_patch**](WorkflowDefinitionsApi.md#resource_workflow_definition_resource_change_asset_type_assignment_rule_patch) | **PATCH** /workflowDefinitions/{workflowDefinitionId}/assetTypeAssignmentRules/{ruleId} | Changes asset type assignment rule with the information that is present in the request.
[**resource_workflow_definition_resource_change_domain_type_assignment_rule_patch**](WorkflowDefinitionsApi.md#resource_workflow_definition_resource_change_domain_type_assignment_rule_patch) | **PATCH** /workflowDefinitions/{workflowDefinitionId}/domainTypeAssignmentRules/{ruleId} | Changes domain type assignment rule with the information that is present in the request.
[**resource_workflow_definition_resource_change_workflow_definition_patch**](WorkflowDefinitionsApi.md#resource_workflow_definition_resource_change_workflow_definition_patch) | **PATCH** /workflowDefinitions/{workflowDefinitionId} | Changes the workflow definition with the information that is present in the request.
[**resource_workflow_definition_resource_deploy_workflow_definition_post**](WorkflowDefinitionsApi.md#resource_workflow_definition_resource_deploy_workflow_definition_post) | **POST** /workflowDefinitions | Deploys workflow definition (the business process and resources) using the specified request.
[**resource_workflow_definition_resource_find_workflow_definitions_get**](WorkflowDefinitionsApi.md#resource_workflow_definition_resource_find_workflow_definitions_get) | **GET** /workflowDefinitions | Finds the workflow definitions matching the criteria described in the request object.
[**resource_workflow_definition_resource_get_configuration_start_form_data_get**](WorkflowDefinitionsApi.md#resource_workflow_definition_resource_get_configuration_start_form_data_get) | **GET** /workflowDefinitions/workflowDefinition/{workflowDefinitionId}/configurationStartFormData | Returns the configuration start form data of the workflow task.
[**resource_workflow_definition_resource_get_start_form_data_get**](WorkflowDefinitionsApi.md#resource_workflow_definition_resource_get_start_form_data_get) | **GET** /workflowDefinitions/workflowDefinition/{workflowDefinitionId}/startFormData | Returns the start form data of the workflow task.
[**resource_workflow_definition_resource_get_workflow_definition_diagram_get**](WorkflowDefinitionsApi.md#resource_workflow_definition_resource_get_workflow_definition_diagram_get) | **GET** /workflowDefinitions/{workflowDefinitionId}/diagram | Returns the diagram of the process with workflow definition identified by the given id.
[**resource_workflow_definition_resource_get_workflow_definition_get**](WorkflowDefinitionsApi.md#resource_workflow_definition_resource_get_workflow_definition_get) | **GET** /workflowDefinitions/process/{processId} | Returns the workflow definition identified by given process id.
[**resource_workflow_definition_resource_get_workflow_definition_xmlget**](WorkflowDefinitionsApi.md#resource_workflow_definition_resource_get_workflow_definition_xmlget) | **GET** /workflowDefinitions/{workflowDefinitionId}/xml | Returns the XML source of the workflow definition identified by the given id.
[**resource_workflow_definition_resource_remove_assignment_rule_delete**](WorkflowDefinitionsApi.md#resource_workflow_definition_resource_remove_assignment_rule_delete) | **DELETE** /workflowDefinitions/{workflowDefinitionId}/assignmentRules/{ruleId} | Removes an assignment rule identified by the given id of the assignment rule and the id of the workflow definition.
[**resource_workflow_definition_resource_remove_workflow_definition_delete**](WorkflowDefinitionsApi.md#resource_workflow_definition_resource_remove_workflow_definition_delete) | **DELETE** /workflowDefinitions/{workflowDefinitionId} | Removes the workflow definition identified by given id.
[**resource_workflow_definition_resource_remove_workflow_definition_post**](WorkflowDefinitionsApi.md#resource_workflow_definition_resource_remove_workflow_definition_post) | **POST** /workflowDefinitions/removalJobs | Removes multiple workflow definitions asynchronously.


# **resource_workflow_definition_resource_add_asset_type_assignment_rule_post**
> JsonAssetAssignmentRuleImpl resource_workflow_definition_resource_add_asset_type_assignment_rule_post(workflow_definition_id, body=body)

Adds an asset type assignment rule to the workflow definition specified in the request.

Adds an asset type assignment rule to the workflow definition specified in the request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowDefinitionsApi()
workflow_definition_id = 'workflow_definition_id_example' # str | the <code>id</code> of the workflow definition
body = swagger_client.JsonAddAssetTypeAssignmentRuleRequest() # JsonAddAssetTypeAssignmentRuleRequest | the request describing assignment rule to be added (optional)

try:
    # Adds an asset type assignment rule to the workflow definition specified in the request.
    api_response = api_instance.resource_workflow_definition_resource_add_asset_type_assignment_rule_post(workflow_definition_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->resource_workflow_definition_resource_add_asset_type_assignment_rule_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the workflow definition | 
 **body** | [**JsonAddAssetTypeAssignmentRuleRequest**](JsonAddAssetTypeAssignmentRuleRequest.md)| the request describing assignment rule to be added | [optional] 

### Return type

[**JsonAssetAssignmentRuleImpl**](JsonAssetAssignmentRuleImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_definition_resource_add_domain_type_assignment_rule_post**
> JsonDomainAssignmentRuleImpl resource_workflow_definition_resource_add_domain_type_assignment_rule_post(workflow_definition_id, body=body)

Adds an domain type assignment rule to the workflow definition specified in the request.

Adds an domain type assignment rule to the workflow definition specified in the request.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowDefinitionsApi()
workflow_definition_id = 'workflow_definition_id_example' # str | the <code>id</code> of the workflow definition
body = swagger_client.JsonAddDomainTypeAssignmentRuleRequest() # JsonAddDomainTypeAssignmentRuleRequest | the request describing assignment rule to be added (optional)

try:
    # Adds an domain type assignment rule to the workflow definition specified in the request.
    api_response = api_instance.resource_workflow_definition_resource_add_domain_type_assignment_rule_post(workflow_definition_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->resource_workflow_definition_resource_add_domain_type_assignment_rule_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the workflow definition | 
 **body** | [**JsonAddDomainTypeAssignmentRuleRequest**](JsonAddDomainTypeAssignmentRuleRequest.md)| the request describing assignment rule to be added | [optional] 

### Return type

[**JsonDomainAssignmentRuleImpl**](JsonDomainAssignmentRuleImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_definition_resource_change_asset_type_assignment_rule_patch**
> JsonAssetAssignmentRuleImpl resource_workflow_definition_resource_change_asset_type_assignment_rule_patch(rule_id, workflow_definition_id, body=body)

Changes asset type assignment rule with the information that is present in the request.

Changes asset type assignment rule with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowDefinitionsApi()
rule_id = 'rule_id_example' # str | the <code>id</code> of the assignment rule to be changed
workflow_definition_id = 'workflow_definition_id_example' # str | the <code>id</code> of the workflow definition
body = swagger_client.JsonChangeAssetTypeAssignmentRuleRequest() # JsonChangeAssetTypeAssignmentRuleRequest | changes that are to be performed on the asset type assignment rule (optional)

try:
    # Changes asset type assignment rule with the information that is present in the request.
    api_response = api_instance.resource_workflow_definition_resource_change_asset_type_assignment_rule_patch(rule_id, workflow_definition_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->resource_workflow_definition_resource_change_asset_type_assignment_rule_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the assignment rule to be changed | 
 **workflow_definition_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the workflow definition | 
 **body** | [**JsonChangeAssetTypeAssignmentRuleRequest**](JsonChangeAssetTypeAssignmentRuleRequest.md)| changes that are to be performed on the asset type assignment rule | [optional] 

### Return type

[**JsonAssetAssignmentRuleImpl**](JsonAssetAssignmentRuleImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_definition_resource_change_domain_type_assignment_rule_patch**
> JsonDomainAssignmentRuleImpl resource_workflow_definition_resource_change_domain_type_assignment_rule_patch(rule_id, workflow_definition_id, body=body)

Changes domain type assignment rule with the information that is present in the request.

Changes domain type assignment rule with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowDefinitionsApi()
rule_id = 'rule_id_example' # str | the <code>id</code> of the assignment rule to be changed
workflow_definition_id = 'workflow_definition_id_example' # str | the <code>id</code> of the workflow definition
body = swagger_client.JsonChangeDomainTypeAssignmentRuleRequest() # JsonChangeDomainTypeAssignmentRuleRequest | changes that are to be performed on the domain type assignment rule (optional)

try:
    # Changes domain type assignment rule with the information that is present in the request.
    api_response = api_instance.resource_workflow_definition_resource_change_domain_type_assignment_rule_patch(rule_id, workflow_definition_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->resource_workflow_definition_resource_change_domain_type_assignment_rule_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the assignment rule to be changed | 
 **workflow_definition_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the workflow definition | 
 **body** | [**JsonChangeDomainTypeAssignmentRuleRequest**](JsonChangeDomainTypeAssignmentRuleRequest.md)| changes that are to be performed on the domain type assignment rule | [optional] 

### Return type

[**JsonDomainAssignmentRuleImpl**](JsonDomainAssignmentRuleImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_definition_resource_change_workflow_definition_patch**
> JsonWorkflowDefinitionImpl resource_workflow_definition_resource_change_workflow_definition_patch(workflow_definition_id, body=body)

Changes the workflow definition with the information that is present in the request.

Changes the workflow definition with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowDefinitionsApi()
workflow_definition_id = 'workflow_definition_id_example' # str | the <code>id</code> of the workflow definition
body = swagger_client.JsonChangeWorkflowDefinitionRequest() # JsonChangeWorkflowDefinitionRequest | changes that are to be performed on the workflow definition (optional)

try:
    # Changes the workflow definition with the information that is present in the request.
    api_response = api_instance.resource_workflow_definition_resource_change_workflow_definition_patch(workflow_definition_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->resource_workflow_definition_resource_change_workflow_definition_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the workflow definition | 
 **body** | [**JsonChangeWorkflowDefinitionRequest**](JsonChangeWorkflowDefinitionRequest.md)| changes that are to be performed on the workflow definition | [optional] 

### Return type

[**JsonWorkflowDefinitionImpl**](JsonWorkflowDefinitionImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_definition_resource_deploy_workflow_definition_post**
> JsonWorkflowDefinitionImpl resource_workflow_definition_resource_deploy_workflow_definition_post(file=file, file_name=file_name, body=body)

Deploys workflow definition (the business process and resources) using the specified request.

Deploys workflow definition (the business process and resources) using the specified request. <p> The input stream can represent a single file(e.g: .bpmn20.xml or .bpmn) or an archive file (e.g: .zip or .bar). It is not allowed to deploy a resource containing more than one process definition.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowDefinitionsApi()
file = '/path/to/file.txt' # file | the file with described workflow definition (optional)
file_name = 'file_name_example' # str | the name of the file (optional)
body = swagger_client.null() #  |  (optional)

try:
    # Deploys workflow definition (the business process and resources) using the specified request.
    api_response = api_instance.resource_workflow_definition_resource_deploy_workflow_definition_post(file=file, file_name=file_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->resource_workflow_definition_resource_deploy_workflow_definition_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| the file with described workflow definition | [optional] 
 **file_name** | **str**| the name of the file | [optional] 
 **body** | [****](.md)|  | [optional] 

### Return type

[**JsonWorkflowDefinitionImpl**](JsonWorkflowDefinitionImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_definition_resource_find_workflow_definitions_get**
> JsonPagedResponse resource_workflow_definition_resource_find_workflow_definitions_get(asset_id=asset_id, community_id=community_id, domain_id=domain_id, enabled=enabled, _global=_global, limit=limit, name=name, offset=offset)

Finds the workflow definitions matching the criteria described in the request object.

Finds the workflow definitions matching the criteria described in the request object.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowDefinitionsApi()
asset_id = ['asset_id_example'] # list[str] | The list of the <code>id</code>s of business items (assets) for which the workflow definitions should be found (optional)
community_id = ['community_id_example'] # list[str] | The list of the <code>id</code>s of business items (communities) for which the workflow definitions should be found (optional)
domain_id = ['domain_id_example'] # list[str] | The list of the <code>id</code>s of business items (domains) for which the workflow definitions should be found (optional)
enabled = true # bool | Whether the found workflow definitions should be enabled (optional) (default to true)
_global = true # bool | Whether the found workflow definitions should be global (optional)
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
name = 'name_example' # str | The name (could be partial) of the workflow definition to search for (optional)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)

try:
    # Finds the workflow definitions matching the criteria described in the request object.
    api_response = api_instance.resource_workflow_definition_resource_find_workflow_definitions_get(asset_id=asset_id, community_id=community_id, domain_id=domain_id, enabled=enabled, _global=_global, limit=limit, name=name, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->resource_workflow_definition_resource_find_workflow_definitions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | [**list[str]**](str.md)| The list of the &lt;code&gt;id&lt;/code&gt;s of business items (assets) for which the workflow definitions should be found | [optional] 
 **community_id** | [**list[str]**](str.md)| The list of the &lt;code&gt;id&lt;/code&gt;s of business items (communities) for which the workflow definitions should be found | [optional] 
 **domain_id** | [**list[str]**](str.md)| The list of the &lt;code&gt;id&lt;/code&gt;s of business items (domains) for which the workflow definitions should be found | [optional] 
 **enabled** | **bool**| Whether the found workflow definitions should be enabled | [optional] [default to true]
 **_global** | **bool**| Whether the found workflow definitions should be global | [optional] 
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **name** | **str**| The name (could be partial) of the workflow definition to search for | [optional] 
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]

### Return type

[**JsonPagedResponse**](JsonPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_definition_resource_get_configuration_start_form_data_get**
> JsonStartFormDataImpl resource_workflow_definition_resource_get_configuration_start_form_data_get(workflow_definition_id, form_property_type=form_property_type)

Returns the configuration start form data of the workflow task.

Returns the configuration start form data of the workflow task.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowDefinitionsApi()
workflow_definition_id = 'workflow_definition_id_example' # str | the <code>id</code> of the workflow definition that should be used for the form data retrieval
form_property_type = 'form_property_type_example' # str | the form type to be returned (optional)

try:
    # Returns the configuration start form data of the workflow task.
    api_response = api_instance.resource_workflow_definition_resource_get_configuration_start_form_data_get(workflow_definition_id, form_property_type=form_property_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->resource_workflow_definition_resource_get_configuration_start_form_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the workflow definition that should be used for the form data retrieval | 
 **form_property_type** | **str**| the form type to be returned | [optional] 

### Return type

[**JsonStartFormDataImpl**](JsonStartFormDataImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_definition_resource_get_start_form_data_get**
> JsonStartFormDataImpl resource_workflow_definition_resource_get_start_form_data_get(workflow_definition_id, form_property_type=form_property_type)

Returns the start form data of the workflow task.

Returns the start form data of the workflow task.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowDefinitionsApi()
workflow_definition_id = 'workflow_definition_id_example' # str | the <code>id</code> of the workflow definition that should be used for the form data retrieval
form_property_type = 'form_property_type_example' # str | the form type to be returned (optional)

try:
    # Returns the start form data of the workflow task.
    api_response = api_instance.resource_workflow_definition_resource_get_start_form_data_get(workflow_definition_id, form_property_type=form_property_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->resource_workflow_definition_resource_get_start_form_data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the workflow definition that should be used for the form data retrieval | 
 **form_property_type** | **str**| the form type to be returned | [optional] 

### Return type

[**JsonStartFormDataImpl**](JsonStartFormDataImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_definition_resource_get_workflow_definition_diagram_get**
> resource_workflow_definition_resource_get_workflow_definition_diagram_get(workflow_definition_id)

Returns the diagram of the process with workflow definition identified by the given id.

Returns the diagram of the process with workflow definition identified by the given id. The diagram input stream returned can be null as deployed workflow definitions without graphical notation included do not have a diagram.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowDefinitionsApi()
workflow_definition_id = 'workflow_definition_id_example' # str | the <code>id</code> of the workflow definition

try:
    # Returns the diagram of the process with workflow definition identified by the given id.
    api_instance.resource_workflow_definition_resource_get_workflow_definition_diagram_get(workflow_definition_id)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->resource_workflow_definition_resource_get_workflow_definition_diagram_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the workflow definition | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_definition_resource_get_workflow_definition_get**
> JsonWorkflowDefinitionImpl resource_workflow_definition_resource_get_workflow_definition_get(process_id)

Returns the workflow definition identified by given process id.

Returns the workflow definition identified by given process id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowDefinitionsApi()
process_id = 'process_id_example' # str | the process id of the workflow definition

try:
    # Returns the workflow definition identified by given process id.
    api_response = api_instance.resource_workflow_definition_resource_get_workflow_definition_get(process_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->resource_workflow_definition_resource_get_workflow_definition_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_id** | **str**| the process id of the workflow definition | 

### Return type

[**JsonWorkflowDefinitionImpl**](JsonWorkflowDefinitionImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_definition_resource_get_workflow_definition_xmlget**
> str resource_workflow_definition_resource_get_workflow_definition_xmlget(workflow_definition_id)

Returns the XML source of the workflow definition identified by the given id.

Returns the XML source of the workflow definition identified by the given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowDefinitionsApi()
workflow_definition_id = 'workflow_definition_id_example' # str | the <code>id</code> of the workflow definition

try:
    # Returns the XML source of the workflow definition identified by the given id.
    api_response = api_instance.resource_workflow_definition_resource_get_workflow_definition_xmlget(workflow_definition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->resource_workflow_definition_resource_get_workflow_definition_xmlget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the workflow definition | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_definition_resource_remove_assignment_rule_delete**
> resource_workflow_definition_resource_remove_assignment_rule_delete(rule_id, workflow_definition_id)

Removes an assignment rule identified by the given id of the assignment rule and the id of the workflow definition.

Removes an assignment rule identified by the given id of the assignment rule and the id of the workflow definition.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowDefinitionsApi()
rule_id = 'rule_id_example' # str | the <code>id</code> of the assignment rule
workflow_definition_id = 'workflow_definition_id_example' # str | the <code>id</code> of the workflow definition

try:
    # Removes an assignment rule identified by the given id of the assignment rule and the id of the workflow definition.
    api_instance.resource_workflow_definition_resource_remove_assignment_rule_delete(rule_id, workflow_definition_id)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->resource_workflow_definition_resource_remove_assignment_rule_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the assignment rule | 
 **workflow_definition_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the workflow definition | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_definition_resource_remove_workflow_definition_delete**
> resource_workflow_definition_resource_remove_workflow_definition_delete(workflow_definition_id)

Removes the workflow definition identified by given id.

Removes the workflow definition identified by given id. The WorkflowDefinition will be completely removed from the application, including any history.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowDefinitionsApi()
workflow_definition_id = 'workflow_definition_id_example' # str | the <code>id</code> of the workflow definition

try:
    # Removes the workflow definition identified by given id.
    api_instance.resource_workflow_definition_resource_remove_workflow_definition_delete(workflow_definition_id)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->resource_workflow_definition_resource_remove_workflow_definition_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_definition_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the workflow definition | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_workflow_definition_resource_remove_workflow_definition_post**
> JsonJobImpl resource_workflow_definition_resource_remove_workflow_definition_post(body=body)

Removes multiple workflow definitions asynchronously.

Removes multiple workflow definitions asynchronously. The WorkflowDefinitions will be completely removed from the application, including any history.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowDefinitionsApi()
body = [swagger_client.list[str]()] # list[str] | the list of <code>id</code>s of the workflow definitions to remove, i.e. [\"6f685f90-1036-4d30-983a-a9bbcdd7b8f6\", \"6f685f90-1036-4d30-983a-a9bbcdd7b123\"] (optional)

try:
    # Removes multiple workflow definitions asynchronously.
    api_response = api_instance.resource_workflow_definition_resource_remove_workflow_definition_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkflowDefinitionsApi->resource_workflow_definition_resource_remove_workflow_definition_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[str]**| the list of &lt;code&gt;id&lt;/code&gt;s of the workflow definitions to remove, i.e. [\&quot;6f685f90-1036-4d30-983a-a9bbcdd7b8f6\&quot;, \&quot;6f685f90-1036-4d30-983a-a9bbcdd7b123\&quot;] | [optional] 

### Return type

[**JsonJobImpl**](JsonJobImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

