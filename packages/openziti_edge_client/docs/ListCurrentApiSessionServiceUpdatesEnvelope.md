# ListCurrentApiSessionServiceUpdatesEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CurrentApiSessionServiceUpdateList**](CurrentApiSessionServiceUpdateList.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_client.models.list_current_api_session_service_updates_envelope import ListCurrentApiSessionServiceUpdatesEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListCurrentApiSessionServiceUpdatesEnvelope from a JSON string
list_current_api_session_service_updates_envelope_instance = ListCurrentApiSessionServiceUpdatesEnvelope.from_json(json)
# print the JSON string representation of the object
print(ListCurrentApiSessionServiceUpdatesEnvelope.to_json())

# convert the object into a dict
list_current_api_session_service_updates_envelope_dict = list_current_api_session_service_updates_envelope_instance.to_dict()
# create an instance of ListCurrentApiSessionServiceUpdatesEnvelope from a dict
list_current_api_session_service_updates_envelope_from_dict = ListCurrentApiSessionServiceUpdatesEnvelope.from_dict(list_current_api_session_service_updates_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


