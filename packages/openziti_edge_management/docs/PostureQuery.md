# PostureQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**is_passing** | **bool** |  | 
**process** | [**PostureQueryProcess**](PostureQueryProcess.md) |  | [optional] 
**processes** | [**List[PostureQueryProcess]**](PostureQueryProcess.md) |  | [optional] 
**prompt_grace_period_seconds** | **int** |  | [optional] 
**prompt_on_unlock** | **bool** |  | [optional] 
**prompt_on_wake** | **bool** |  | [optional] 
**query_type** | [**PostureCheckType**](PostureCheckType.md) |  | 
**timeout** | **int** |  | 
**timeout_at** | **datetime** |  | [optional] 
**timeout_remaining** | **int** |  | 

## Example

```python
from openziti_edge_management.models.posture_query import PostureQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PostureQuery from a JSON string
posture_query_instance = PostureQuery.from_json(json)
# print the JSON string representation of the object
print(PostureQuery.to_json())

# convert the object into a dict
posture_query_dict = posture_query_instance.to_dict()
# create an instance of PostureQuery from a dict
posture_query_from_dict = PostureQuery.from_dict(posture_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


