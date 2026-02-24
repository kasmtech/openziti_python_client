# ListNetworkJWTsEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NetworkJWT]**](NetworkJWT.md) | An array of network JWTs | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.list_network_jwts_envelope import ListNetworkJWTsEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListNetworkJWTsEnvelope from a JSON string
list_network_jwts_envelope_instance = ListNetworkJWTsEnvelope.from_json(json)
# print the JSON string representation of the object
print(ListNetworkJWTsEnvelope.to_json())

# convert the object into a dict
list_network_jwts_envelope_dict = list_network_jwts_envelope_instance.to_dict()
# create an instance of ListNetworkJWTsEnvelope from a dict
list_network_jwts_envelope_from_dict = ListNetworkJWTsEnvelope.from_dict(list_network_jwts_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


