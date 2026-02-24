# Interface

A resource describing a network interface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | **List[str]** |  | [optional] 
**hardware_address** | **str** |  | 
**index** | **int** |  | 
**is_broadcast** | **bool** |  | 
**is_loopback** | **bool** |  | 
**is_multicast** | **bool** |  | 
**is_running** | **bool** |  | 
**is_up** | **bool** |  | 
**mtu** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from openziti_edge_client.models.interface import Interface

# TODO update the JSON string below
json = "{}"
# create an instance of Interface from a JSON string
interface_instance = Interface.from_json(json)
# print the JSON string representation of the object
print(Interface.to_json())

# convert the object into a dict
interface_dict = interface_instance.to_dict()
# create an instance of Interface from a dict
interface_from_dict = Interface.from_dict(interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


