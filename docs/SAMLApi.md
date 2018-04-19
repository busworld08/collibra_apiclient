# swagger_client.SAMLApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_saml_resource_get_sp_metadata_as_string_get**](SAMLApi.md#resource_saml_resource_get_sp_metadata_as_string_get) | **GET** /security/saml | Returns the SAML Service Provider metadata for a this instance.


# **resource_saml_resource_get_sp_metadata_as_string_get**
> str resource_saml_resource_get_sp_metadata_as_string_get(complete=complete)

Returns the SAML Service Provider metadata for a this instance.

Returns the SAML Service Provider metadata for a this instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SAMLApi()
complete = true # bool | whether or not the meta data generated should include the non-required attributes (completeMetadata = true means all the non-essential attributes too) (optional)

try:
    # Returns the SAML Service Provider metadata for a this instance.
    api_response = api_instance.resource_saml_resource_get_sp_metadata_as_string_get(complete=complete)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SAMLApi->resource_saml_resource_get_sp_metadata_as_string_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complete** | **bool**| whether or not the meta data generated should include the non-required attributes (completeMetadata &#x3D; true means all the non-essential attributes too) | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

