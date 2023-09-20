# ThreeDomainSecurityGateway


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**e_ci** | **str** | The eCI value | [optional] 
**merchant_id** | **str** | The merchant ID value | [optional] 
**processor_id** | **str** | The processor ID value | [optional] 
**u_rl** | **str** | Transaction URL. | [optional] 
**authentication_verification** | [**AuthenticationVerification**](AuthenticationVerification.md) |  | [optional] 
**password** | [**Password**](Password.md) |  | [optional] 

## Example

```python
from openapi_client.models.three_domain_security_gateway import ThreeDomainSecurityGateway

# TODO update the JSON string below
json = "{}"
# create an instance of ThreeDomainSecurityGateway from a JSON string
three_domain_security_gateway_instance = ThreeDomainSecurityGateway.from_json(json)
# print the JSON string representation of the object
print ThreeDomainSecurityGateway.to_json()

# convert the object into a dict
three_domain_security_gateway_dict = three_domain_security_gateway_instance.to_dict()
# create an instance of ThreeDomainSecurityGateway from a dict
three_domain_security_gateway_form_dict = three_domain_security_gateway.from_dict(three_domain_security_gateway_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


