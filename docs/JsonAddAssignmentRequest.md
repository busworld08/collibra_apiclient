# JsonAddAssignmentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_type_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the asset type corresponding to the assignment | 
**status_ids** | **list[str]** | The list of &lt;code&gt;id&lt;/code&gt;s of the statuses | 
**characteristic_types** | [**list[JsonCharacteristicTypeAssignmentReference]**](JsonCharacteristicTypeAssignmentReference.md) | The list of the references to characteristic types corresponding to the assignment | [optional] 
**articulation_rules** | [**list[JsonArticulationRuleRequest]**](JsonArticulationRuleRequest.md) | The list of the articulation rules | [optional] 
**validation_rule_ids** | **list[str]** | The list of &lt;code&gt;id&lt;/code&gt;s of the validation rules | [optional] 
**data_quality_rule_ids** | **list[str]** | The list of &lt;code&gt;id&lt;/code&gt;s of the data quality rules | [optional] 
**domain_type_ids** | **list[str]** | The list of &lt;code&gt;id&lt;/code&gt;s of the domain types | [optional] 
**default_status_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the default status for the asset type | 
**scope_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the scope the assignment corresponds to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


