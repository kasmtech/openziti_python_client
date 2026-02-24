# ListCurrentApiSessionCertificatesEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CurrentApiSessionCertificateDetail]**](CurrentApiSessionCertificateDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_client.models.list_current_api_session_certificates_envelope import ListCurrentApiSessionCertificatesEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListCurrentApiSessionCertificatesEnvelope from a JSON string
list_current_api_session_certificates_envelope_instance = ListCurrentApiSessionCertificatesEnvelope.from_json(json)
# print the JSON string representation of the object
print(ListCurrentApiSessionCertificatesEnvelope.to_json())

# convert the object into a dict
list_current_api_session_certificates_envelope_dict = list_current_api_session_certificates_envelope_instance.to_dict()
# create an instance of ListCurrentApiSessionCertificatesEnvelope from a dict
list_current_api_session_certificates_envelope_from_dict = ListCurrentApiSessionCertificatesEnvelope.from_dict(list_current_api_session_certificates_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


