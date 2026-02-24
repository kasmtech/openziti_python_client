# ListProtocolsEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Dict[str, Protocol]**](Protocol.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_client.models.list_protocols_envelope import ListProtocolsEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListProtocolsEnvelope from a JSON string
list_protocols_envelope_instance = ListProtocolsEnvelope.from_json(json)
# print the JSON string representation of the object
print(ListProtocolsEnvelope.to_json())

# convert the object into a dict
list_protocols_envelope_dict = list_protocols_envelope_instance.to_dict()
# create an instance of ListProtocolsEnvelope from a dict
list_protocols_envelope_from_dict = ListProtocolsEnvelope.from_dict(list_protocols_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


