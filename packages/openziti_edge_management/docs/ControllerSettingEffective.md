# ControllerSettingEffective


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**effective** | [**ControllerSettings**](ControllerSettings.md) |  | [optional] 
**instance** | [**ControllerSettings**](ControllerSettings.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.controller_setting_effective import ControllerSettingEffective

# TODO update the JSON string below
json = "{}"
# create an instance of ControllerSettingEffective from a JSON string
controller_setting_effective_instance = ControllerSettingEffective.from_json(json)
# print the JSON string representation of the object
print(ControllerSettingEffective.to_json())

# convert the object into a dict
controller_setting_effective_dict = controller_setting_effective_instance.to_dict()
# create an instance of ControllerSettingEffective from a dict
controller_setting_effective_from_dict = ControllerSettingEffective.from_dict(controller_setting_effective_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


