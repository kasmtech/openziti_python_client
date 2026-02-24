# ListServiceEdgeRoutersEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ServiceEdgeRouters**](ServiceEdgeRouters.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_client.models.list_service_edge_routers_envelope import ListServiceEdgeRoutersEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListServiceEdgeRoutersEnvelope from a JSON string
list_service_edge_routers_envelope_instance = ListServiceEdgeRoutersEnvelope.from_json(json)
# print the JSON string representation of the object
print(ListServiceEdgeRoutersEnvelope.to_json())

# convert the object into a dict
list_service_edge_routers_envelope_dict = list_service_edge_routers_envelope_instance.to_dict()
# create an instance of ListServiceEdgeRoutersEnvelope from a dict
list_service_edge_routers_envelope_from_dict = ListServiceEdgeRoutersEnvelope.from_dict(list_service_edge_routers_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


