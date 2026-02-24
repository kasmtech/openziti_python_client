# TotpToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issued_at** | **datetime** |  | 
**token** | **str** |  | 

## Example

```python
from openziti_edge_client.models.totp_token import TotpToken

# TODO update the JSON string below
json = "{}"
# create an instance of TotpToken from a JSON string
totp_token_instance = TotpToken.from_json(json)
# print the JSON string representation of the object
print(TotpToken.to_json())

# convert the object into a dict
totp_token_dict = totp_token_instance.to_dict()
# create an instance of TotpToken from a dict
totp_token_from_dict = TotpToken.from_dict(totp_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


