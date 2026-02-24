# EnrollmentCerts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca** | **str** | A PEM encoded set of CA certificates to trust | [optional] 
**cert** | **str** | A PEM encoded set of certificates to use as the client chain | [optional] 
**server_cert** | **str** | A PEM encoded set of certificates to use as the servers chain | [optional] 

## Example

```python
from openziti_edge_client.models.enrollment_certs import EnrollmentCerts

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentCerts from a JSON string
enrollment_certs_instance = EnrollmentCerts.from_json(json)
# print the JSON string representation of the object
print(EnrollmentCerts.to_json())

# convert the object into a dict
enrollment_certs_dict = enrollment_certs_instance.to_dict()
# create an instance of EnrollmentCerts from a dict
enrollment_certs_from_dict = EnrollmentCerts.from_dict(enrollment_certs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


