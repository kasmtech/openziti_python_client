# ControllerSettingPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oidc** | [**ControllerSettingsOidc**](ControllerSettingsOidc.md) |  | [optional] 
**tags** | [**Tags**](Tags.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.controller_setting_patch import ControllerSettingPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ControllerSettingPatch from a JSON string
controller_setting_patch_instance = ControllerSettingPatch.from_json(json)
# print the JSON string representation of the object
print(ControllerSettingPatch.to_json())

# convert the object into a dict
controller_setting_patch_dict = controller_setting_patch_instance.to_dict()
# create an instance of ControllerSettingPatch from a dict
controller_setting_patch_from_dict = ControllerSettingPatch.from_dict(controller_setting_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


