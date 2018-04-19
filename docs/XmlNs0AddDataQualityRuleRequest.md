# XmlNs0AddDataQualityRuleRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categorization_relation_type_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the categorization relation type | [optional] 
**data_quality_metrics** | [**XmlNs0DataQualityMetricRequest**](XmlNs0DataQualityMetricRequest.md) | The Data Quality Metrics that should be assigned to the rule that is going to be created | [optional] 
**description** | **str** | The description of the new data quality rule | [optional] 
**name** | **str** | The name of the new data quality rule. Should be unique within all data quality rules | [optional] 
**relation_trace_entries** | [**XmlNs0RelationTraceEntryRequest**](XmlNs0RelationTraceEntryRequest.md) | The list of entries that describes relations along which the data quality result is calculated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


