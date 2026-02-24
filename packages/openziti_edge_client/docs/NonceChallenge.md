# NonceChallenge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** |  | 
**nonce** | **UUID** |  | 

## Example

```python
from openziti_edge_client.models.nonce_challenge import NonceChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of NonceChallenge from a JSON string
nonce_challenge_instance = NonceChallenge.from_json(json)
# print the JSON string representation of the object
print(NonceChallenge.to_json())

# convert the object into a dict
nonce_challenge_dict = nonce_challenge_instance.to_dict()
# create an instance of NonceChallenge from a dict
nonce_challenge_from_dict = NonceChallenge.from_dict(nonce_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


