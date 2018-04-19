# JsonAddComplexRelationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complex_relation_type_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the type of the complex relation | 
**legs** | [**list[JsonComplexRelationLegRequest]**](JsonComplexRelationLegRequest.md) | The list of legs that the new complex relation should contain | [optional] 
**relations** | **list[dict(str, JsonRelatedAssetId)]** | The relations that the new complex relation should contain | [optional] 
**attributes** | **list[dict(str, JsonAttributeValue)]** | The attributes that the new complex relation should contain | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


