# ControllerSettingUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oidc** | [**ControllerSettingsOidc**](ControllerSettingsOidc.md) |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.controller_setting_update import ControllerSettingUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ControllerSettingUpdate from a JSON string
controller_setting_update_instance = ControllerSettingUpdate.from_json(json)
# print the JSON string representation of the object
print(ControllerSettingUpdate.to_json())

# convert the object into a dict
controller_setting_update_dict = controller_setting_update_instance.to_dict()
# create an instance of ControllerSettingUpdate from a dict
controller_setting_update_from_dict = ControllerSettingUpdate.from_dict(controller_setting_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


