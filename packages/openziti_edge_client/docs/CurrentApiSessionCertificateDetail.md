# CurrentApiSessionCertificateDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**certificate** | **str** |  | 
**fingerprint** | **str** |  | 
**subject** | **str** |  | 
**valid_from** | **datetime** |  | 
**valid_to** | **datetime** |  | 

## Example

```python
from openziti_edge_client.models.current_api_session_certificate_detail import CurrentApiSessionCertificateDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentApiSessionCertificateDetail from a JSON string
current_api_session_certificate_detail_instance = CurrentApiSessionCertificateDetail.from_json(json)
# print the JSON string representation of the object
print(CurrentApiSessionCertificateDetail.to_json())

# convert the object into a dict
current_api_session_certificate_detail_dict = current_api_session_certificate_detail_instance.to_dict()
# create an instance of CurrentApiSessionCertificateDetail from a dict
current_api_session_certificate_detail_from_dict = CurrentApiSessionCertificateDetail.from_dict(current_api_session_certificate_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


