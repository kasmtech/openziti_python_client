# SessionCreateEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SessionDetail**](SessionDetail.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openziti_edge_client.models.session_create_envelope import SessionCreateEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of SessionCreateEnvelope from a JSON string
session_create_envelope_instance = SessionCreateEnvelope.from_json(json)
# print the JSON string representation of the object
print(SessionCreateEnvelope.to_json())

# convert the object into a dict
session_create_envelope_dict = session_create_envelope_instance.to_dict()
# create an instance of SessionCreateEnvelope from a dict
session_create_envelope_from_dict = SessionCreateEnvelope.from_dict(session_create_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


