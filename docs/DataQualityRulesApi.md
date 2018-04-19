# swagger_client.DataQualityRulesApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_data_quality_rule_resource_add_data_quality_rule_post**](DataQualityRulesApi.md#resource_data_quality_rule_resource_add_data_quality_rule_post) | **POST** /dataQualityRules | Adds new data quality rule.
[**resource_data_quality_rule_resource_change_data_quality_rule_patch**](DataQualityRulesApi.md#resource_data_quality_rule_resource_change_data_quality_rule_patch) | **PATCH** /dataQualityRules/{dataQualityRuleId} | Changes the data quality rule with the information that is present in the request.
[**resource_data_quality_rule_resource_find_data_quality_rules_get**](DataQualityRulesApi.md#resource_data_quality_rule_resource_find_data_quality_rules_get) | **GET** /dataQualityRules | Returns data quality rules matching the given search criteria.
[**resource_data_quality_rule_resource_get_data_quality_rule_get**](DataQualityRulesApi.md#resource_data_quality_rule_resource_get_data_quality_rule_get) | **GET** /dataQualityRules/{dataQualityRuleId} | Returns data quality rule identified by given id.
[**resource_data_quality_rule_resource_remove_data_quality_rule_delete**](DataQualityRulesApi.md#resource_data_quality_rule_resource_remove_data_quality_rule_delete) | **DELETE** /dataQualityRules/{dataQualityRuleId} | Removes data quality rule identified by given id.


# **resource_data_quality_rule_resource_add_data_quality_rule_post**
> JsonDataQualityRuleImpl resource_data_quality_rule_resource_add_data_quality_rule_post(body=body)

Adds new data quality rule.

Adds new data quality rule.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataQualityRulesApi()
body = swagger_client.JsonAddDataQualityRuleRequest() # JsonAddDataQualityRuleRequest | the properties of the data quality rule to be added (optional)

try:
    # Adds new data quality rule.
    api_response = api_instance.resource_data_quality_rule_resource_add_data_quality_rule_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataQualityRulesApi->resource_data_quality_rule_resource_add_data_quality_rule_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAddDataQualityRuleRequest**](JsonAddDataQualityRuleRequest.md)| the properties of the data quality rule to be added | [optional] 

### Return type

[**JsonDataQualityRuleImpl**](JsonDataQualityRuleImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_data_quality_rule_resource_change_data_quality_rule_patch**
> JsonDataQualityRuleImpl resource_data_quality_rule_resource_change_data_quality_rule_patch(data_quality_rule_id, body=body)

Changes the data quality rule with the information that is present in the request.

Changes the data quality rule with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataQualityRulesApi()
data_quality_rule_id = 'data_quality_rule_id_example' # str | the <code>id</code> of the data quality rule to be changed
body = swagger_client.JsonChangeDataQualityRuleRequest() # JsonChangeDataQualityRuleRequest | the properties of the data quality rule to be changed (optional)

try:
    # Changes the data quality rule with the information that is present in the request.
    api_response = api_instance.resource_data_quality_rule_resource_change_data_quality_rule_patch(data_quality_rule_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataQualityRulesApi->resource_data_quality_rule_resource_change_data_quality_rule_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_quality_rule_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the data quality rule to be changed | 
 **body** | [**JsonChangeDataQualityRuleRequest**](JsonChangeDataQualityRuleRequest.md)| the properties of the data quality rule to be changed | [optional] 

### Return type

[**JsonDataQualityRuleImpl**](JsonDataQualityRuleImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_data_quality_rule_resource_find_data_quality_rules_get**
> JsonPagedResponse resource_data_quality_rule_resource_find_data_quality_rules_get(limit=limit, name=name, name_match_mode=name_match_mode, offset=offset, sort_field=sort_field, sort_order=sort_order)

Returns data quality rules matching the given search criteria.

Returns data quality rules matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned data quality rules satisfy all constraints that are specified in this search criteria. By default a result containing 1000 data quality rules is returned.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataQualityRulesApi()
limit = 0 # int | The maximum number of results to retrieve. If not set (value = <tt>0</tt>), the default limit will be used (optional) (default to 0)
name = 'name_example' # str | The name of the dataquality rule to search for (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code> (optional) (default to ANYWHERE)
offset = 0 # int | The first result to retrieve. If not set (value = <tt>0</tt>), results will be retrieved starting from row <tt>0</tt> (optional) (default to 0)
sort_field = 'NAME' # str | The field that should be used as reference for sorting (optional) (default to NAME)
sort_order = 'ASC' # str | The order of sorting (optional) (default to ASC)

try:
    # Returns data quality rules matching the given search criteria.
    api_response = api_instance.resource_data_quality_rule_resource_find_data_quality_rules_get(limit=limit, name=name, name_match_mode=name_match_mode, offset=offset, sort_field=sort_field, sort_order=sort_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataQualityRulesApi->resource_data_quality_rule_resource_find_data_quality_rules_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] [default to 0]
 **name** | **str**| The name of the dataquality rule to search for | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt; | [optional] [default to ANYWHERE]
 **offset** | **int**| The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] [default to 0]
 **sort_field** | **str**| The field that should be used as reference for sorting | [optional] [default to NAME]
 **sort_order** | **str**| The order of sorting | [optional] [default to ASC]

### Return type

[**JsonPagedResponse**](JsonPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_data_quality_rule_resource_get_data_quality_rule_get**
> JsonDataQualityRuleImpl resource_data_quality_rule_resource_get_data_quality_rule_get(data_quality_rule_id)

Returns data quality rule identified by given id.

Returns data quality rule identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataQualityRulesApi()
data_quality_rule_id = 'data_quality_rule_id_example' # str | the <code>id</code> of the data quality rule

try:
    # Returns data quality rule identified by given id.
    api_response = api_instance.resource_data_quality_rule_resource_get_data_quality_rule_get(data_quality_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataQualityRulesApi->resource_data_quality_rule_resource_get_data_quality_rule_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_quality_rule_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the data quality rule | 

### Return type

[**JsonDataQualityRuleImpl**](JsonDataQualityRuleImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_data_quality_rule_resource_remove_data_quality_rule_delete**
> resource_data_quality_rule_resource_remove_data_quality_rule_delete(data_quality_rule_id)

Removes data quality rule identified by given id.

Removes data quality rule identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataQualityRulesApi()
data_quality_rule_id = 'data_quality_rule_id_example' # str | the <code>id</code> of the data quality rule

try:
    # Removes data quality rule identified by given id.
    api_instance.resource_data_quality_rule_resource_remove_data_quality_rule_delete(data_quality_rule_id)
except ApiException as e:
    print("Exception when calling DataQualityRulesApi->resource_data_quality_rule_resource_remove_data_quality_rule_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_quality_rule_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the data quality rule | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

