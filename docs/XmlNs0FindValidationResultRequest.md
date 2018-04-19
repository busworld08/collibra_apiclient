# XmlNs0FindValidationResultRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**asset_id** | **str** | The unique identifier of the asset for which we are searching validation results | [optional] 
**job_id** | **str** | The unique identifier of the job for which we are searching validation results | [optional] 
**most_recent_job** | **bool** | Check the validationResults of only the most recent job according to the other criteria | [optional] 
**result** | **bool** | Filter on the result of validation results | [optional] 
**validation_rule_id** | **str** | The unique identifier of the validation rule for which we are searching validation results | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


