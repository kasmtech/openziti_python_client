# ControllerSettingsOidc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_logout_uris** | **List[str]** |  | [optional] 
**redirect_uris** | **List[str]** |  | [optional] 

## Example

```python
from openziti_edge_management.models.controller_settings_oidc import ControllerSettingsOidc

# TODO update the JSON string below
json = "{}"
# create an instance of ControllerSettingsOidc from a JSON string
controller_settings_oidc_instance = ControllerSettingsOidc.from_json(json)
# print the JSON string representation of the object
print(ControllerSettingsOidc.to_json())

# convert the object into a dict
controller_settings_oidc_dict = controller_settings_oidc_instance.to_dict()
# create an instance of ControllerSettingsOidc from a dict
controller_settings_oidc_from_dict = ControllerSettingsOidc.from_dict(controller_settings_oidc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


