# ListCurrentIdentityEdgeRoutersEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CurrentIdentityEdgeRouterDetail]**](CurrentIdentityEdgeRouterDetail.md) | A list of edge router resources | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_client.models.list_current_identity_edge_routers_envelope import ListCurrentIdentityEdgeRoutersEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListCurrentIdentityEdgeRoutersEnvelope from a JSON string
list_current_identity_edge_routers_envelope_instance = ListCurrentIdentityEdgeRoutersEnvelope.from_json(json)
# print the JSON string representation of the object
print(ListCurrentIdentityEdgeRoutersEnvelope.to_json())

# convert the object into a dict
list_current_identity_edge_routers_envelope_dict = list_current_identity_edge_routers_envelope_instance.to_dict()
# create an instance of ListCurrentIdentityEdgeRoutersEnvelope from a dict
list_current_identity_edge_routers_envelope_from_dict = ListCurrentIdentityEdgeRoutersEnvelope.from_dict(list_current_identity_edge_routers_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


