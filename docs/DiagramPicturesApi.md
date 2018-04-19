# swagger_client.DiagramPicturesApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_diagram_picture_resource_add_asset_type_post**](DiagramPicturesApi.md#resource_diagram_picture_resource_add_asset_type_post) | **POST** /diagramPictures | Take a diagram picture for a given asset and diagram view.


# **resource_diagram_picture_resource_add_asset_type_post**
> str resource_diagram_picture_resource_add_asset_type_post(body=body)

Take a diagram picture for a given asset and diagram view.

Take a diagram picture for a given asset and diagram view. A diagram picture is a copy of traceability diagram (result diagram) at a given time (for more information on traceability diagram check DGC User Guide).  The motivation behind diagram picture is to be able to reopen them at a later point in time and be able to see them them exactly as they were created. This feature is not possible for result diagram which are always showing the current situation.  The picture inherits it's sharing rule from the view passed as parameter.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DiagramPicturesApi()
body = swagger_client.JsonAddDiagramPictureRequest() # JsonAddDiagramPictureRequest | the parameters for creating the picture (optional)

try:
    # Take a diagram picture for a given asset and diagram view.
    api_response = api_instance.resource_diagram_picture_resource_add_asset_type_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DiagramPicturesApi->resource_diagram_picture_resource_add_asset_type_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JsonAddDiagramPictureRequest**](JsonAddDiagramPictureRequest.md)| the parameters for creating the picture | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

