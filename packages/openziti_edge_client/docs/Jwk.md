# Jwk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** | Algorithm intended for use with the key. | [optional] 
**crv** | **str** | Curve for ECC Public Keys. | [optional] 
**d** | **str** | ECC Private Key or RSA Private Exponent. | [optional] 
**dp** | **str** | First Factor CRT Exponent for RSA. | [optional] 
**dq** | **str** | Second Factor CRT Exponent for RSA. | [optional] 
**e** | **str** | Exponent for RSA Public Key. | [optional] 
**key_ops** | **List[str]** | Intended key operations, e.g., sign, verify. | [optional] 
**kid** | **str** | Key ID. | [optional] 
**kty** | **str** | Key Type. | 
**n** | **str** | Modulus for RSA Public Key. | [optional] 
**oth** | [**List[OtherPrime]**](OtherPrime.md) | Other Primes Info not represented by the first two primes. | [optional] 
**p** | **str** | First Prime Factor for RSA. | [optional] 
**q** | **str** | Second Prime Factor for RSA. | [optional] 
**qi** | **str** | First CRT Coefficient for RSA. | [optional] 
**use** | **str** | Public key use, e.g., sig (signature) or enc (encryption). | [optional] 
**x** | **str** | X Coordinate for ECC Public Keys. | [optional] 
**x5c** | **List[str]** | X.509 Certificate Chain. | [optional] 
**x5t** | **str** | X.509 Certificate SHA-1 Thumbprint. | [optional] 
**x5t_s256** | **str** | X.509 Certificate SHA-256 Thumbprint. | [optional] 
**x5u** | **str** | X.509 URL. | [optional] 
**y** | **str** | Y Coordinate for ECC Public Keys. | [optional] 

## Example

```python
from openziti_edge_client.models.jwk import Jwk

# TODO update the JSON string below
json = "{}"
# create an instance of Jwk from a JSON string
jwk_instance = Jwk.from_json(json)
# print the JSON string representation of the object
print(Jwk.to_json())

# convert the object into a dict
jwk_dict = jwk_instance.to_dict()
# create an instance of Jwk from a dict
jwk_from_dict = Jwk.from_dict(jwk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


