# PostureResponseEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PostureResponse**](PostureResponse.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_client.models.posture_response_envelope import PostureResponseEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PostureResponseEnvelope from a JSON string
posture_response_envelope_instance = PostureResponseEnvelope.from_json(json)
# print the JSON string representation of the object
print(PostureResponseEnvelope.to_json())

# convert the object into a dict
posture_response_envelope_dict = posture_response_envelope_instance.to_dict()
# create an instance of PostureResponseEnvelope from a dict
posture_response_envelope_from_dict = PostureResponseEnvelope.from_dict(posture_response_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


