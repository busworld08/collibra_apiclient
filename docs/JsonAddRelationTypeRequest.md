# JsonAddRelationTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the new domain type. Should be unique within all domain types. It should have a format of universally unique identifier (UUID) and should not start with &lt;code&gt;00000000-0000-0000-&lt;/code&gt; which is a reserved prefix | [optional] 
**source_type_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the source type for new relation type | 
**role** | **str** | The name of the role that the source plays | 
**target_type_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the source type for new relation type | 
**co_role** | **str** | The name of the role that the target plays | 
**description** | **str** | The description of the relation type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


