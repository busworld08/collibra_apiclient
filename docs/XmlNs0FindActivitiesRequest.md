# XmlNs0FindActivitiesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**activity_type** | [**XmlNs0ActivityType**](XmlNs0ActivityType.md) | The type of the activity | [optional] 
**call_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the call | [optional] 
**categories** | [**XmlNs0ActivityFilterCategory**](XmlNs0ActivityFilterCategory.md) | The set of the categories of activities that should be searched. One of [ATTRIBUTE, ATTACHMENT, RELATION, COMMENT, STATUS, WORKFLOW, RESPONSIBILITY, USER, USER_GROUP, ROLE, TAGS, OTHERS] | [optional] 
**context_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the context which the activities should be searched for | [optional] 
**end_date** | **float** | The end date of the searched activities. It is the timestamp (in UTC time standard) | [optional] 
**involved_people_ids** | **str** | The list of &lt;code&gt;id&lt;/code&gt;s of the people that should be involved in searched activities | [optional] 
**involved_role_ids** | **str** | The list of &lt;code&gt;id&lt;/code&gt;s of the roles that should be involved in searched activities | [optional] 
**performed_by_role_ids** | **str** | The list of &lt;code&gt;id&lt;/code&gt;s of the roles assigned to users who performed searched activities | [optional] 
**performed_by_user_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the user who performed searched activities | [optional] 
**resource_types** | [**XmlNs0ResourceType**](XmlNs0ResourceType.md) | The set of the resource types that searched activities refer to, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance] | [optional] 
**start_date** | **float** | The start date of the searched activities. It is the timestamp (in UTC time standard) | [optional] 
**task_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the task which contains the basic find activities request | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


