# CurrentIdentityEdgeRouterDetail

A detail edge router resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**app_data** | [**Tags**](Tags.md) |  | [optional] 
**cost** | **int** |  | 
**disabled** | **bool** |  | 
**hostname** | **str** |  | 
**is_online** | **bool** |  | 
**name** | **str** |  | 
**no_traversal** | **bool** |  | 
**supported_protocols** | **Dict[str, str]** |  | 
**sync_status** | **str** |  | 

## Example

```python
from openziti_edge_client.models.current_identity_edge_router_detail import CurrentIdentityEdgeRouterDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentIdentityEdgeRouterDetail from a JSON string
current_identity_edge_router_detail_instance = CurrentIdentityEdgeRouterDetail.from_json(json)
# print the JSON string representation of the object
print(CurrentIdentityEdgeRouterDetail.to_json())

# convert the object into a dict
current_identity_edge_router_detail_dict = current_identity_edge_router_detail_instance.to_dict()
# create an instance of CurrentIdentityEdgeRouterDetail from a dict
current_identity_edge_router_detail_from_dict = CurrentIdentityEdgeRouterDetail.from_dict(current_identity_edge_router_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


