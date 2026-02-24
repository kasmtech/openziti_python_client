# NetworkJWT

A network JWT

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**token** | **str** |  | 

## Example

```python
from openziti_edge_management.models.network_jwt import NetworkJWT

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkJWT from a JSON string
network_jwt_instance = NetworkJWT.from_json(json)
# print the JSON string representation of the object
print(NetworkJWT.to_json())

# convert the object into a dict
network_jwt_dict = network_jwt_instance.to_dict()
# create an instance of NetworkJWT from a dict
network_jwt_from_dict = NetworkJWT.from_dict(network_jwt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


