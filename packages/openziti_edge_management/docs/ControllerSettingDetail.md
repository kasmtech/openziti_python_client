# ControllerSettingDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**oidc** | [**ControllerSettingsOidc**](ControllerSettingsOidc.md) |  | [optional] 

## Example

```python
from openziti_edge_management.models.controller_setting_detail import ControllerSettingDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ControllerSettingDetail from a JSON string
controller_setting_detail_instance = ControllerSettingDetail.from_json(json)
# print the JSON string representation of the object
print(ControllerSettingDetail.to_json())

# convert the object into a dict
controller_setting_detail_dict = controller_setting_detail_instance.to_dict()
# create an instance of ControllerSettingDetail from a dict
controller_setting_detail_from_dict = ControllerSettingDetail.from_dict(controller_setting_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


