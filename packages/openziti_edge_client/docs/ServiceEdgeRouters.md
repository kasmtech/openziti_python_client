# ServiceEdgeRouters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edge_routers** | [**List[CommonEdgeRouterProperties]**](CommonEdgeRouterProperties.md) |  | [optional] 

## Example

```python
from openziti_edge_client.models.service_edge_routers import ServiceEdgeRouters

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceEdgeRouters from a JSON string
service_edge_routers_instance = ServiceEdgeRouters.from_json(json)
# print the JSON string representation of the object
print(ServiceEdgeRouters.to_json())

# convert the object into a dict
service_edge_routers_dict = service_edge_routers_instance.to_dict()
# create an instance of ServiceEdgeRouters from a dict
service_edge_routers_from_dict = ServiceEdgeRouters.from_dict(service_edge_routers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


