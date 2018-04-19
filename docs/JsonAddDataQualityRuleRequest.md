# JsonAddDataQualityRuleRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the new data quality rule. Should be unique within all data quality rules | 
**description** | **str** | The description of the new data quality rule | [optional] 
**categorization_relation_type_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the categorization relation type | 
**data_quality_metrics** | [**list[JsonDataQualityMetricRequest]**](JsonDataQualityMetricRequest.md) | The Data Quality Metrics that should be assigned to the rule that is going to be created | [optional] 
**relation_trace_entries** | [**list[JsonRelationTraceEntryRequest]**](JsonRelationTraceEntryRequest.md) | The list of entries that describes relations along which the data quality result is calculated | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


