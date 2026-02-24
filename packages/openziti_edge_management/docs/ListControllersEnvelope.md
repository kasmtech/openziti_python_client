# ListControllersEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ControllerDetail]**](ControllerDetail.md) | An array of controller resources | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_controllers_envelope import ListControllersEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListControllersEnvelope from a JSON string
list_controllers_envelope_instance = ListControllersEnvelope.from_json(json)
# print the JSON string representation of the object
print(ListControllersEnvelope.to_json())

# convert the object into a dict
list_controllers_envelope_dict = list_controllers_envelope_instance.to_dict()
# create an instance of ListControllersEnvelope from a dict
list_controllers_envelope_from_dict = ListControllersEnvelope.from_dict(list_controllers_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


