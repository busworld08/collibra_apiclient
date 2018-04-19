# JsonExportCSVInJobRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**table_view_config** | **str** | The JSON representation of Table View Config that describes the query to be performed | 
**file_name** | **str** | The name of the file. By default the file name will be generated | [optional] 
**separator** | **str** | The delimiter character used to separate entries. Default value is &#39;;&#39; | [optional] 
**quote** | **str** | The delimiter character used for quoted entries. Default value  is &#39;\&quot;&#39; | [optional] 
**escape** | **str** | The delimiter character used to escape separator or quote character. Default value is &#39;\\\\&#39; | [optional] 
**header_row** | **bool** | Whether a response should include a header (true) or not (false). Default value is true | [optional] 
**send_notification** | **bool** | Whether an e-mail must be sent on completion of the job | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


