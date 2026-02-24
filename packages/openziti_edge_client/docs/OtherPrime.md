# OtherPrime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**d** | **str** | Factor CRT exponent. | [optional] 
**r** | **str** | Prime factor. | [optional] 
**t** | **str** | Factor CRT coefficient. | [optional] 

## Example

```python
from openziti_edge_client.models.other_prime import OtherPrime

# TODO update the JSON string below
json = "{}"
# create an instance of OtherPrime from a JSON string
other_prime_instance = OtherPrime.from_json(json)
# print the JSON string representation of the object
print(OtherPrime.to_json())

# convert the object into a dict
other_prime_dict = other_prime_instance.to_dict()
# create an instance of OtherPrime from a dict
other_prime_from_dict = OtherPrime.from_dict(other_prime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


