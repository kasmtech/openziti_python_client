# DetailControllerSettingEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ControllerSettingDetail**](ControllerSettingDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_controller_setting_envelope import DetailControllerSettingEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailControllerSettingEnvelope from a JSON string
detail_controller_setting_envelope_instance = DetailControllerSettingEnvelope.from_json(json)
# print the JSON string representation of the object
print(DetailControllerSettingEnvelope.to_json())

# convert the object into a dict
detail_controller_setting_envelope_dict = detail_controller_setting_envelope_instance.to_dict()
# create an instance of DetailControllerSettingEnvelope from a dict
detail_controller_setting_envelope_from_dict = DetailControllerSettingEnvelope.from_dict(detail_controller_setting_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


