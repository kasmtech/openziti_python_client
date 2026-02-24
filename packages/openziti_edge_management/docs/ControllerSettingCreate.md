# ControllerSettingCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oidc** | [**ControllerSettingsOidc**](ControllerSettingsOidc.md) |  | [optional] 
**controller_id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.controller_setting_create import ControllerSettingCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ControllerSettingCreate from a JSON string
controller_setting_create_instance = ControllerSettingCreate.from_json(json)
# print the JSON string representation of the object
print(ControllerSettingCreate.to_json())

# convert the object into a dict
controller_setting_create_dict = controller_setting_create_instance.to_dict()
# create an instance of ControllerSettingCreate from a dict
controller_setting_create_from_dict = ControllerSettingCreate.from_dict(controller_setting_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


