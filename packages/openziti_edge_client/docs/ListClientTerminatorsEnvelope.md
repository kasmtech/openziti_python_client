# ListClientTerminatorsEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TerminatorClientDetail]**](TerminatorClientDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_client.models.list_client_terminators_envelope import ListClientTerminatorsEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListClientTerminatorsEnvelope from a JSON string
list_client_terminators_envelope_instance = ListClientTerminatorsEnvelope.from_json(json)
# print the JSON string representation of the object
print(ListClientTerminatorsEnvelope.to_json())

# convert the object into a dict
list_client_terminators_envelope_dict = list_client_terminators_envelope_instance.to_dict()
# create an instance of ListClientTerminatorsEnvelope from a dict
list_client_terminators_envelope_from_dict = ListClientTerminatorsEnvelope.from_dict(list_client_terminators_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


