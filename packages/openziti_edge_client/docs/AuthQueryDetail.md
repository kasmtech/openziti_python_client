# AuthQueryDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**format** | [**MfaFormats**](MfaFormats.md) |  | [optional] 
**http_method** | **str** |  | [optional] 
**http_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_totp_enrolled** | **bool** |  | [optional] 
**max_length** | **int** |  | [optional] 
**min_length** | **int** |  | [optional] 
**provider** | [**MfaProviders**](MfaProviders.md) |  | 
**scopes** | **List[str]** |  | [optional] 
**type_id** | [**AuthQueryType**](AuthQueryType.md) |  | [optional] 

## Example

```python
from openziti_edge_client.models.auth_query_detail import AuthQueryDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AuthQueryDetail from a JSON string
auth_query_detail_instance = AuthQueryDetail.from_json(json)
# print the JSON string representation of the object
print(AuthQueryDetail.to_json())

# convert the object into a dict
auth_query_detail_dict = auth_query_detail_instance.to_dict()
# create an instance of AuthQueryDetail from a dict
auth_query_detail_from_dict = AuthQueryDetail.from_dict(auth_query_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


