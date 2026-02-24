# ListControllerSettingEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[str]** |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_controller_setting_envelope import ListControllerSettingEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListControllerSettingEnvelope from a JSON string
list_controller_setting_envelope_instance = ListControllerSettingEnvelope.from_json(json)
# print the JSON string representation of the object
print(ListControllerSettingEnvelope.to_json())

# convert the object into a dict
list_controller_setting_envelope_dict = list_controller_setting_envelope_instance.to_dict()
# create an instance of ListControllerSettingEnvelope from a dict
list_controller_setting_envelope_from_dict = ListControllerSettingEnvelope.from_dict(list_controller_setting_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


