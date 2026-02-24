# ListSessionsEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SessionDetail]**](SessionDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_client.models.list_sessions_envelope import ListSessionsEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListSessionsEnvelope from a JSON string
list_sessions_envelope_instance = ListSessionsEnvelope.from_json(json)
# print the JSON string representation of the object
print(ListSessionsEnvelope.to_json())

# convert the object into a dict
list_sessions_envelope_dict = list_sessions_envelope_instance.to_dict()
# create an instance of ListSessionsEnvelope from a dict
list_sessions_envelope_from_dict = ListSessionsEnvelope.from_dict(list_sessions_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


