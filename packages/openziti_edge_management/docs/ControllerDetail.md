# ControllerDetail

A controller resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**api_addresses** | **Dict[str, List[ApiAddress]]** |  | [optional] 
**cert_pem** | **str** |  | 
**ctrl_address** | **str** |  | [optional] 
**fingerprint** | **str** |  | 
**is_online** | **bool** |  | 
**last_joined_at** | **datetime** |  | 
**name** | **str** |  | 

## Example

```python
from openziti_edge_management.models.controller_detail import ControllerDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ControllerDetail from a JSON string
controller_detail_instance = ControllerDetail.from_json(json)
# print the JSON string representation of the object
print(ControllerDetail.to_json())

# convert the object into a dict
controller_detail_dict = controller_detail_instance.to_dict()
# create an instance of ControllerDetail from a dict
controller_detail_from_dict = ControllerDetail.from_dict(controller_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


