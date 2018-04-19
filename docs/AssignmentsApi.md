# swagger_client.AssignmentsApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_assignment_resource_get_assignments_for_asset_get**](AssignmentsApi.md#resource_assignment_resource_get_assignments_for_asset_get) | **GET** /assignments/asset/{assetId} | Returns assignment for given asset id.
[**resource_assignment_resource_get_assignments_for_asset_type_get**](AssignmentsApi.md#resource_assignment_resource_get_assignments_for_asset_type_get) | **GET** /assignments/assetType/{assetTypeId} | Returns assignments for given asset type id.
[**resource_assignment_resource_get_available_asset_types_for_domain_get**](AssignmentsApi.md#resource_assignment_resource_get_available_asset_types_for_domain_get) | **GET** /assignments/domain/{domainId}/assetTypes | Returns available asset types for domain identified by given id.
[**resource_assignment_resource_get_available_attribute_types_for_asset_get**](AssignmentsApi.md#resource_assignment_resource_get_available_attribute_types_for_asset_get) | **GET** /assignments/asset/{assetId}/attributeTypes | Returns available attribute types for asset identified by given id.
[**resource_assignment_resource_get_available_complex_relation_types_for_asset_get**](AssignmentsApi.md#resource_assignment_resource_get_available_complex_relation_types_for_asset_get) | **GET** /assignments/asset/{assetId}/complexRelationTypes | Returns available complex relation types for asset identified by given id.
[**resource_assignment_resource_get_available_relation_types_for_asset_get**](AssignmentsApi.md#resource_assignment_resource_get_available_relation_types_for_asset_get) | **GET** /assignments/asset/{assetId}/relationTypes | Returns available relation types for asset identified by given id.


# **resource_assignment_resource_get_assignments_for_asset_get**
> JsonAssignmentImpl resource_assignment_resource_get_assignments_for_asset_get(asset_id)

Returns assignment for given asset id.

Returns assignment for given asset id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssignmentsApi()
asset_id = 'asset_id_example' # str | the <code>id</code> of the asset

try:
    # Returns assignment for given asset id.
    api_response = api_instance.resource_assignment_resource_get_assignments_for_asset_get(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->resource_assignment_resource_get_assignments_for_asset_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the asset | 

### Return type

[**JsonAssignmentImpl**](JsonAssignmentImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_assignment_resource_get_assignments_for_asset_type_get**
> list[JsonAssignmentImpl] resource_assignment_resource_get_assignments_for_asset_type_get(asset_type_id)

Returns assignments for given asset type id.

Returns assignments for given asset type id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssignmentsApi()
asset_type_id = 'asset_type_id_example' # str | the <code>id</code> of the asset type

try:
    # Returns assignments for given asset type id.
    api_response = api_instance.resource_assignment_resource_get_assignments_for_asset_type_get(asset_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->resource_assignment_resource_get_assignments_for_asset_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the asset type | 

### Return type

[**list[JsonAssignmentImpl]**](JsonAssignmentImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_assignment_resource_get_available_asset_types_for_domain_get**
> list[JsonAssetTypeImpl] resource_assignment_resource_get_available_asset_types_for_domain_get(domain_id)

Returns available asset types for domain identified by given id.

Returns available asset types for domain identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssignmentsApi()
domain_id = 'domain_id_example' # str | the <code>id</code> of the domain

try:
    # Returns available asset types for domain identified by given id.
    api_response = api_instance.resource_assignment_resource_get_available_asset_types_for_domain_get(domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->resource_assignment_resource_get_available_asset_types_for_domain_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the domain | 

### Return type

[**list[JsonAssetTypeImpl]**](JsonAssetTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_assignment_resource_get_available_attribute_types_for_asset_get**
> list[JsonAttributeTypeImpl] resource_assignment_resource_get_available_attribute_types_for_asset_get(asset_id)

Returns available attribute types for asset identified by given id.

Returns available attribute types for asset identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssignmentsApi()
asset_id = 'asset_id_example' # str | the <code>id</code> of the asset

try:
    # Returns available attribute types for asset identified by given id.
    api_response = api_instance.resource_assignment_resource_get_available_attribute_types_for_asset_get(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->resource_assignment_resource_get_available_attribute_types_for_asset_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the asset | 

### Return type

[**list[JsonAttributeTypeImpl]**](JsonAttributeTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_assignment_resource_get_available_complex_relation_types_for_asset_get**
> list[JsonComplexRelationTypeImpl] resource_assignment_resource_get_available_complex_relation_types_for_asset_get(asset_id)

Returns available complex relation types for asset identified by given id.

Returns available complex relation types for asset identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssignmentsApi()
asset_id = 'asset_id_example' # str | the <code>id</code> of the asset

try:
    # Returns available complex relation types for asset identified by given id.
    api_response = api_instance.resource_assignment_resource_get_available_complex_relation_types_for_asset_get(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->resource_assignment_resource_get_available_complex_relation_types_for_asset_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the asset | 

### Return type

[**list[JsonComplexRelationTypeImpl]**](JsonComplexRelationTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_assignment_resource_get_available_relation_types_for_asset_get**
> list[JsonRelationTypeImpl] resource_assignment_resource_get_available_relation_types_for_asset_get(asset_id)

Returns available relation types for asset identified by given id.

Returns available relation types for asset identified by given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssignmentsApi()
asset_id = 'asset_id_example' # str | the <code>id</code> of the asset

try:
    # Returns available relation types for asset identified by given id.
    api_response = api_instance.resource_assignment_resource_get_available_relation_types_for_asset_get(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssignmentsApi->resource_assignment_resource_get_available_relation_types_for_asset_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of the asset | 

### Return type

[**list[JsonRelationTypeImpl]**](JsonRelationTypeImpl.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

