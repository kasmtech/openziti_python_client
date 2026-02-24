# DetailSessionEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SessionDetail**](SessionDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_client.models.detail_session_envelope import DetailSessionEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailSessionEnvelope from a JSON string
detail_session_envelope_instance = DetailSessionEnvelope.from_json(json)
# print the JSON string representation of the object
print(DetailSessionEnvelope.to_json())

# convert the object into a dict
detail_session_envelope_dict = detail_session_envelope_instance.to_dict()
# create an instance of DetailSessionEnvelope from a dict
detail_session_envelope_from_dict = DetailSessionEnvelope.from_dict(detail_session_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


