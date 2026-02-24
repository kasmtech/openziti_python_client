# TerminatorClientDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**identity** | **str** |  | 
**router_id** | **str** |  | 
**service** | [**EntityRef**](EntityRef.md) |  | 
**service_id** | **str** |  | 

## Example

```python
from openziti_edge_client.models.terminator_client_detail import TerminatorClientDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TerminatorClientDetail from a JSON string
terminator_client_detail_instance = TerminatorClientDetail.from_json(json)
# print the JSON string representation of the object
print(TerminatorClientDetail.to_json())

# convert the object into a dict
terminator_client_detail_dict = terminator_client_detail_instance.to_dict()
# create an instance of TerminatorClientDetail from a dict
terminator_client_detail_from_dict = TerminatorClientDetail.from_dict(terminator_client_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


