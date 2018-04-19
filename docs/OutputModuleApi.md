# swagger_client.OutputModuleApi

All URIs are relative to *https://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource_output_module_resource_export_csv_in_job_post**](OutputModuleApi.md#resource_output_module_resource_export_csv_in_job_post) | **POST** /outputModule/export/csv-job | Starts a job that performs an Output Module query and stores the results in a file in CSV format.
[**resource_output_module_resource_export_csv_to_file_post**](OutputModuleApi.md#resource_output_module_resource_export_csv_to_file_post) | **POST** /outputModule/export/csv-file | Performs an Output Module query and stores the query results in a file in CSV format.
[**resource_output_module_resource_export_csvpost**](OutputModuleApi.md#resource_output_module_resource_export_csvpost) | **POST** /outputModule/export/csv | Performs an Output Module query and exports the returns results immediately in CSV format.
[**resource_output_module_resource_export_excel_in_job_post**](OutputModuleApi.md#resource_output_module_resource_export_excel_in_job_post) | **POST** /outputModule/export/excel-job | Starts a job that performs an Output Module query and stores the results in a file in Excel format.
[**resource_output_module_resource_export_excel_to_file_post**](OutputModuleApi.md#resource_output_module_resource_export_excel_to_file_post) | **POST** /outputModule/export/excel-file | Performs an Output Module query and stores the query results in a file in Excel format.
[**resource_output_module_resource_export_json_in_job_post**](OutputModuleApi.md#resource_output_module_resource_export_json_in_job_post) | **POST** /outputModule/export/json-job | Starts a job that performs an Output Module query and stores the results in a file in JSON format.
[**resource_output_module_resource_export_json_to_file_post**](OutputModuleApi.md#resource_output_module_resource_export_json_to_file_post) | **POST** /outputModule/export/json-file | Performs an Output Module query and stores the query results in a file in JSON format.
[**resource_output_module_resource_export_jsonpost**](OutputModuleApi.md#resource_output_module_resource_export_jsonpost) | **POST** /outputModule/export/json | Performs an Output Module query and exports the returns results immediately in JSON format.
[**resource_output_module_resource_export_xml_in_job_post**](OutputModuleApi.md#resource_output_module_resource_export_xml_in_job_post) | **POST** /outputModule/export/xml-job | Starts a job that performs an Output Module query and stores the results in a file in XML format.
[**resource_output_module_resource_export_xml_to_file_post**](OutputModuleApi.md#resource_output_module_resource_export_xml_to_file_post) | **POST** /outputModule/export/xml-file | Performs an Output Module query and stores the query results in a file in XML format.
[**resource_output_module_resource_export_xmlpost**](OutputModuleApi.md#resource_output_module_resource_export_xmlpost) | **POST** /outputModule/export/xml | Performs an Output Module query and exports the returns results immediately in XML format.
[**resource_output_module_resource_get_table_view_config_by_view_id_get**](OutputModuleApi.md#resource_output_module_resource_get_table_view_config_by_view_id_get) | **GET** /outputModule/tableViewConfigs/viewId/{viewId} | .


# **resource_output_module_resource_export_csv_in_job_post**
> file resource_output_module_resource_export_csv_in_job_post(escape=escape, file_name=file_name, header_row=header_row, quote=quote, send_notification=send_notification, separator=separator, body=body)

Starts a job that performs an Output Module query and stores the results in a file in CSV format.

Starts a job that performs an Output Module query and stores the results in a file in CSV format. Id of the file can be retrieved from the <code>message.id</code> property of the job once the job is finished.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutputModuleApi()
escape = 'escape_example' # str | The delimiter character used to escape separator or quote character. Default value is '\\\\' (optional)
file_name = 'file_name_example' # str | The name of the file. By default the file name will be generated (optional)
header_row = true # bool | Whether a response should include a header (true) or not (false). Default value is true (optional) (default to true)
quote = 'quote_example' # str | The delimiter character used for quoted entries. Default value  is '\"' (optional)
send_notification = false # bool | Whether an e-mail must be sent on completion of the job (optional) (default to false)
separator = 'separator_example' # str | The delimiter character used to separate entries. Default value is ';' (optional)
body = 'body_example' # str | the JSON representation of Table View Config that describes the query to be performed. Refer to Output Module documentation for more details (optional)

try:
    # Starts a job that performs an Output Module query and stores the results in a file in CSV format.
    api_response = api_instance.resource_output_module_resource_export_csv_in_job_post(escape=escape, file_name=file_name, header_row=header_row, quote=quote, send_notification=send_notification, separator=separator, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutputModuleApi->resource_output_module_resource_export_csv_in_job_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **escape** | **str**| The delimiter character used to escape separator or quote character. Default value is &#39;\\\\&#39; | [optional] 
 **file_name** | **str**| The name of the file. By default the file name will be generated | [optional] 
 **header_row** | **bool**| Whether a response should include a header (true) or not (false). Default value is true | [optional] [default to true]
 **quote** | **str**| The delimiter character used for quoted entries. Default value  is &#39;\&quot;&#39; | [optional] 
 **send_notification** | **bool**| Whether an e-mail must be sent on completion of the job | [optional] [default to false]
 **separator** | **str**| The delimiter character used to separate entries. Default value is &#39;;&#39; | [optional] 
 **body** | **str**| the JSON representation of Table View Config that describes the query to be performed. Refer to Output Module documentation for more details | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_output_module_resource_export_csv_to_file_post**
> file resource_output_module_resource_export_csv_to_file_post(escape=escape, file_name=file_name, header_row=header_row, quote=quote, separator=separator, body=body)

Performs an Output Module query and stores the query results in a file in CSV format.

Performs an Output Module query and stores the query results in a file in CSV format. The id of the file is returned in the response.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutputModuleApi()
escape = 'escape_example' # str | The delimiter character used to escape separator or quote character. Default value is '\\\\' (optional)
file_name = 'file_name_example' # str | The name of the file. By default the file name will be generated (optional)
header_row = true # bool | Whether a response should include a header (true) or not (false). Default value is true (optional) (default to true)
quote = 'quote_example' # str | The delimiter character used for quoted entries. Default value  is '\"' (optional)
separator = 'separator_example' # str | The delimiter character used to separate entries. Default value is ';' (optional)
body = 'body_example' # str | the JSON representation of Table View Config that describes the query to be performed. Refer to Output Module documentation for more details (optional)

try:
    # Performs an Output Module query and stores the query results in a file in CSV format.
    api_response = api_instance.resource_output_module_resource_export_csv_to_file_post(escape=escape, file_name=file_name, header_row=header_row, quote=quote, separator=separator, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutputModuleApi->resource_output_module_resource_export_csv_to_file_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **escape** | **str**| The delimiter character used to escape separator or quote character. Default value is &#39;\\\\&#39; | [optional] 
 **file_name** | **str**| The name of the file. By default the file name will be generated | [optional] 
 **header_row** | **bool**| Whether a response should include a header (true) or not (false). Default value is true | [optional] [default to true]
 **quote** | **str**| The delimiter character used for quoted entries. Default value  is &#39;\&quot;&#39; | [optional] 
 **separator** | **str**| The delimiter character used to separate entries. Default value is &#39;;&#39; | [optional] 
 **body** | **str**| the JSON representation of Table View Config that describes the query to be performed. Refer to Output Module documentation for more details | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_output_module_resource_export_csvpost**
> str resource_output_module_resource_export_csvpost(escape=escape, header_row=header_row, quote=quote, separator=separator, body=body)

Performs an Output Module query and exports the returns results immediately in CSV format.

Performs an Output Module query and exports the returns results immediately in CSV format.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutputModuleApi()
escape = 'escape_example' # str | The delimiter character used to escape separator or quote character. Default value is '\\\\' (optional)
header_row = true # bool | Whether a response should include a header (true) or not (false). Default value is true (optional) (default to true)
quote = 'quote_example' # str | The delimiter character used for quoted entries. Default value  is '\"' (optional)
separator = 'separator_example' # str | The delimiter character used to separate entries. Default value is ';' (optional)
body = 'body_example' # str | the JSON representation of Table View Config that describes the query to be performed. Refer to Output Module documentation for more details (optional)

try:
    # Performs an Output Module query and exports the returns results immediately in CSV format.
    api_response = api_instance.resource_output_module_resource_export_csvpost(escape=escape, header_row=header_row, quote=quote, separator=separator, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutputModuleApi->resource_output_module_resource_export_csvpost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **escape** | **str**| The delimiter character used to escape separator or quote character. Default value is &#39;\\\\&#39; | [optional] 
 **header_row** | **bool**| Whether a response should include a header (true) or not (false). Default value is true | [optional] [default to true]
 **quote** | **str**| The delimiter character used for quoted entries. Default value  is &#39;\&quot;&#39; | [optional] 
 **separator** | **str**| The delimiter character used to separate entries. Default value is &#39;;&#39; | [optional] 
 **body** | **str**| the JSON representation of Table View Config that describes the query to be performed. Refer to Output Module documentation for more details | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_output_module_resource_export_excel_in_job_post**
> file resource_output_module_resource_export_excel_in_job_post(file_name=file_name, header_row=header_row, send_notification=send_notification, sheet_name=sheet_name, use_xlsx=use_xlsx, body=body)

Starts a job that performs an Output Module query and stores the results in a file in Excel format.

Starts a job that performs an Output Module query and stores the results in a file in Excel format. Id of the file can be retrieved from the <code>message.id</code> property of the job once the job is finished.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutputModuleApi()
file_name = 'file_name_example' # str | The name of the file. By default the file name will be generated (optional)
header_row = true # bool | Whether a response should include a header (true) or not (false). Default value is true (optional) (default to true)
send_notification = false # bool | Whether an e-mail must be sent on completion of the job (optional) (default to false)
sheet_name = 'sheet_name_example' # str | The name of the sheet. By default no sheet name is set (optional)
use_xlsx = true # bool | Whether the Excel file to export will be '.xlsx' file (true) or a '.xls' file (false. Default value is true (optional) (default to true)
body = 'body_example' # str | the JSON representation of Table View Config that describes the query to be performed. Refer to Output Module documentation for more details (optional)

try:
    # Starts a job that performs an Output Module query and stores the results in a file in Excel format.
    api_response = api_instance.resource_output_module_resource_export_excel_in_job_post(file_name=file_name, header_row=header_row, send_notification=send_notification, sheet_name=sheet_name, use_xlsx=use_xlsx, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutputModuleApi->resource_output_module_resource_export_excel_in_job_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| The name of the file. By default the file name will be generated | [optional] 
 **header_row** | **bool**| Whether a response should include a header (true) or not (false). Default value is true | [optional] [default to true]
 **send_notification** | **bool**| Whether an e-mail must be sent on completion of the job | [optional] [default to false]
 **sheet_name** | **str**| The name of the sheet. By default no sheet name is set | [optional] 
 **use_xlsx** | **bool**| Whether the Excel file to export will be &#39;.xlsx&#39; file (true) or a &#39;.xls&#39; file (false. Default value is true | [optional] [default to true]
 **body** | **str**| the JSON representation of Table View Config that describes the query to be performed. Refer to Output Module documentation for more details | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_output_module_resource_export_excel_to_file_post**
> file resource_output_module_resource_export_excel_to_file_post(file_name=file_name, header_row=header_row, sheet_name=sheet_name, use_xlsx=use_xlsx, body=body)

Performs an Output Module query and stores the query results in a file in Excel format.

Performs an Output Module query and stores the query results in a file in Excel format. The id of the file is returned in the response.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutputModuleApi()
file_name = 'file_name_example' # str | The name of the file. By default the file name will be generated (optional)
header_row = true # bool | Whether a response should include a header (true) or not (false). Default value is true (optional) (default to true)
sheet_name = 'sheet_name_example' # str | The name of the sheet. By default no sheet name is set (optional)
use_xlsx = true # bool | Whether the Excel file to export will be '.xlsx' file (true) or a '.xls' file (false. Default value is true (optional) (default to true)
body = 'body_example' # str | the JSON representation of Table View Config that describes the query to be performed. Refer to Output Module documentation for more details (optional)

try:
    # Performs an Output Module query and stores the query results in a file in Excel format.
    api_response = api_instance.resource_output_module_resource_export_excel_to_file_post(file_name=file_name, header_row=header_row, sheet_name=sheet_name, use_xlsx=use_xlsx, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutputModuleApi->resource_output_module_resource_export_excel_to_file_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| The name of the file. By default the file name will be generated | [optional] 
 **header_row** | **bool**| Whether a response should include a header (true) or not (false). Default value is true | [optional] [default to true]
 **sheet_name** | **str**| The name of the sheet. By default no sheet name is set | [optional] 
 **use_xlsx** | **bool**| Whether the Excel file to export will be &#39;.xlsx&#39; file (true) or a &#39;.xls&#39; file (false. Default value is true | [optional] [default to true]
 **body** | **str**| the JSON representation of Table View Config that describes the query to be performed. Refer to Output Module documentation for more details | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_output_module_resource_export_json_in_job_post**
> file resource_output_module_resource_export_json_in_job_post(file_name=file_name, send_notification=send_notification, body=body)

Starts a job that performs an Output Module query and stores the results in a file in JSON format.

Starts a job that performs an Output Module query and stores the results in a file in JSON format. Id of the file can be retrieved from the <code>message.id</code> property of the job once the job is finished.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutputModuleApi()
file_name = 'file_name_example' # str | The name of the file. By default the file name will be generated (optional)
send_notification = false # bool | Whether an e-mail must be sent on completion of the job (optional) (default to false)
body = 'body_example' # str | the JSON representation of View Config that describes the query to be performed. Refer to Output Module documentation for more details (optional)

try:
    # Starts a job that performs an Output Module query and stores the results in a file in JSON format.
    api_response = api_instance.resource_output_module_resource_export_json_in_job_post(file_name=file_name, send_notification=send_notification, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutputModuleApi->resource_output_module_resource_export_json_in_job_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| The name of the file. By default the file name will be generated | [optional] 
 **send_notification** | **bool**| Whether an e-mail must be sent on completion of the job | [optional] [default to false]
 **body** | **str**| the JSON representation of View Config that describes the query to be performed. Refer to Output Module documentation for more details | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_output_module_resource_export_json_to_file_post**
> file resource_output_module_resource_export_json_to_file_post(file_name=file_name, body=body)

Performs an Output Module query and stores the query results in a file in JSON format.

Performs an Output Module query and stores the query results in a file in JSON format. The id of the file is returned in the response.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutputModuleApi()
file_name = 'file_name_example' # str | The name of the file. By default the file name will be generated (optional)
body = 'body_example' # str | the JSON representation of View Config that describes the query to be performed. Refer to Output Module documentation for more details (optional)

try:
    # Performs an Output Module query and stores the query results in a file in JSON format.
    api_response = api_instance.resource_output_module_resource_export_json_to_file_post(file_name=file_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutputModuleApi->resource_output_module_resource_export_json_to_file_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| The name of the file. By default the file name will be generated | [optional] 
 **body** | **str**| the JSON representation of View Config that describes the query to be performed. Refer to Output Module documentation for more details | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_output_module_resource_export_jsonpost**
> str resource_output_module_resource_export_jsonpost(body=body)

Performs an Output Module query and exports the returns results immediately in JSON format.

Performs an Output Module query and exports the returns results immediately in JSON format.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutputModuleApi()
body = 'body_example' # str | the JSON representation of View Config that describes the query to be performed. Refer to Output Module documentation for more details (optional)

try:
    # Performs an Output Module query and exports the returns results immediately in JSON format.
    api_response = api_instance.resource_output_module_resource_export_jsonpost(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutputModuleApi->resource_output_module_resource_export_jsonpost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| the JSON representation of View Config that describes the query to be performed. Refer to Output Module documentation for more details | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_output_module_resource_export_xml_in_job_post**
> file resource_output_module_resource_export_xml_in_job_post(file_name=file_name, body=body)

Starts a job that performs an Output Module query and stores the results in a file in XML format.

Starts a job that performs an Output Module query and stores the results in a file in XML format. Id of the file can be retrieved from the <code>message.id</code> property of the job once the job is finished.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutputModuleApi()
file_name = 'file_name_example' # str | The name of the file. By default the file name will be generated (optional)
body = 'body_example' # str | the XML representation of View Config that describes the query to be performed. Refer to Output Module documentation for more details (optional)

try:
    # Starts a job that performs an Output Module query and stores the results in a file in XML format.
    api_response = api_instance.resource_output_module_resource_export_xml_in_job_post(file_name=file_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutputModuleApi->resource_output_module_resource_export_xml_in_job_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| The name of the file. By default the file name will be generated | [optional] 
 **body** | **str**| the XML representation of View Config that describes the query to be performed. Refer to Output Module documentation for more details | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_output_module_resource_export_xml_to_file_post**
> file resource_output_module_resource_export_xml_to_file_post(file_name=file_name, body=body)

Performs an Output Module query and stores the query results in a file in XML format.

Performs an Output Module query and stores the query results in a file in XML format. The id of the file is returned in the response.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutputModuleApi()
file_name = 'file_name_example' # str | The name of the file. By default the file name will be generated (optional)
body = 'body_example' # str | the JSON representation of View Config that describes the query to be performed. Refer to Output Module documentation for more details (optional)

try:
    # Performs an Output Module query and stores the query results in a file in XML format.
    api_response = api_instance.resource_output_module_resource_export_xml_to_file_post(file_name=file_name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutputModuleApi->resource_output_module_resource_export_xml_to_file_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| The name of the file. By default the file name will be generated | [optional] 
 **body** | **str**| the JSON representation of View Config that describes the query to be performed. Refer to Output Module documentation for more details | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_output_module_resource_export_xmlpost**
> str resource_output_module_resource_export_xmlpost(body=body)

Performs an Output Module query and exports the returns results immediately in XML format.

Performs an Output Module query and exports the returns results immediately in XML format.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutputModuleApi()
body = 'body_example' # str | the JSON representation of View Config that describes the query to be performed. Refer to Output Module documentation for more details (optional)

try:
    # Performs an Output Module query and exports the returns results immediately in XML format.
    api_response = api_instance.resource_output_module_resource_export_xmlpost(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutputModuleApi->resource_output_module_resource_export_xmlpost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| the JSON representation of View Config that describes the query to be performed. Refer to Output Module documentation for more details | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_output_module_resource_get_table_view_config_by_view_id_get**
> str resource_output_module_resource_get_table_view_config_by_view_id_get(view_id, view_location=view_location)

.

<b>EXPERIMENTAL</b> Returns Table View Config based on id of given View and its Location. This Table View Config can be used by Output Module to export the same data as visible in Collibra Data Governance Center User Interface. Example: given page under url https://dgc.collibra.com/glossary?view=133f7f30-033c-4e38-acc2-2c1ac599d19e the view <code>id</code> is <code>133f7f30-033c-4e38-acc2-2c1ac599d19e</code>. The Location represents a location of given View in Collibra Data Governance Center.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OutputModuleApi()
view_id = 'view_id_example' # str | the <code>id</code> of given View. Can be obtained from Collibra Data Governance Center User Interface
view_location = 'view_location_example' # str | The Location of the view. Views in Collibra Data Governance Center are available under specific locations. Setting appropriate View Location will produce Table View Config that returns identical data as seen under desired location and given View. Each location is associated with set of filters that are automatically applied to given view. If this field is not defined then returned Table View Config corresponds to a generic View which where no additional filters are applied. Because of that the data returned when generic Table View Config is used may differ from the data seen in given View in Collibra Data Governance Center User Interface. (optional)

try:
    # .
    api_response = api_instance.resource_output_module_resource_get_table_view_config_by_view_id_get(view_id, view_location=view_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OutputModuleApi->resource_output_module_resource_get_table_view_config_by_view_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| the &lt;code&gt;id&lt;/code&gt; of given View. Can be obtained from Collibra Data Governance Center User Interface | 
 **view_location** | **str**| The Location of the view. Views in Collibra Data Governance Center are available under specific locations. Setting appropriate View Location will produce Table View Config that returns identical data as seen under desired location and given View. Each location is associated with set of filters that are automatically applied to given view. If this field is not defined then returned Table View Config corresponds to a generic View which where no additional filters are applied. Because of that the data returned when generic Table View Config is used may differ from the data seen in given View in Collibra Data Governance Center User Interface. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

