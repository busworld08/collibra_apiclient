# JsonFindActivitiesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** | The first result to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), results will be retrieved starting from row &lt;tt&gt;0&lt;/tt&gt; | [optional] 
**limit** | **float** | The maximum number of results to retrieve. If not set (value &#x3D; &lt;tt&gt;0&lt;/tt&gt;), the default limit will be used | [optional] 
**task_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the task which contains the basic find activities request | [optional] 
**context_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the context which the activities should be searched for | [optional] 
**involved_people_ids** | **list[str]** | The list of &lt;code&gt;id&lt;/code&gt;s of the people that should be involved in searched activities | [optional] 
**involved_role_ids** | **list[str]** | The list of &lt;code&gt;id&lt;/code&gt;s of the roles that should be involved in searched activities | [optional] 
**performed_by_user_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the user who performed searched activities | [optional] 
**performed_by_role_ids** | **list[str]** | The list of &lt;code&gt;id&lt;/code&gt;s of the roles assigned to users who performed searched activities | [optional] 
**activity_type** | [**JsonActivityType**](JsonActivityType.md) | The type of the activity | [optional] 
**call_id** | **str** | The &lt;code&gt;id&lt;/code&gt; of the call | [optional] 
**categories** | [**list[JsonActivityFilterCategory]**](JsonActivityFilterCategory.md) | The set of the categories of activities that should be searched. One of [ATTRIBUTE, ATTACHMENT, RELATION, COMMENT, STATUS, WORKFLOW, RESPONSIBILITY, USER, USER_GROUP, ROLE, TAGS, OTHERS] | [optional] 
**resource_types** | [**list[JsonResourceType]**](JsonResourceType.md) | The set of the resource types that searched activities refer to, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance] | [optional] 
**start_date** | **float** | The start date of the searched activities. It is the timestamp (in UTC time standard) | [optional] 
**end_date** | **float** | The end date of the searched activities. It is the timestamp (in UTC time standard) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


