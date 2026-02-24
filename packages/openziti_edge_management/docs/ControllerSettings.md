# ControllerSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oidc** | [**ControllerSettingsOidc**](ControllerSettingsOidc.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.controller_settings import ControllerSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ControllerSettings from a JSON string
controller_settings_instance = ControllerSettings.from_json(json)
# print the JSON string representation of the object
print(ControllerSettings.to_json())

# convert the object into a dict
controller_settings_dict = controller_settings_instance.to_dict()
# create an instance of ControllerSettings from a dict
controller_settings_from_dict = ControllerSettings.from_dict(controller_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


