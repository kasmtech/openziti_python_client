# ListEnumeratedCapabilitiesEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Capabilities]**](Capabilities.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_client.models.list_enumerated_capabilities_envelope import ListEnumeratedCapabilitiesEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListEnumeratedCapabilitiesEnvelope from a JSON string
list_enumerated_capabilities_envelope_instance = ListEnumeratedCapabilitiesEnvelope.from_json(json)
# print the JSON string representation of the object
print(ListEnumeratedCapabilitiesEnvelope.to_json())

# convert the object into a dict
list_enumerated_capabilities_envelope_dict = list_enumerated_capabilities_envelope_instance.to_dict()
# create an instance of ListEnumeratedCapabilitiesEnvelope from a dict
list_enumerated_capabilities_envelope_from_dict = ListEnumeratedCapabilitiesEnvelope.from_dict(list_enumerated_capabilities_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


