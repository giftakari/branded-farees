# ThreeDomainSecurity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**three_domain_security_gateway** | [**ThreeDomainSecurityGateway**](ThreeDomainSecurityGateway.md) |  | 
**three_domain_security_results** | [**ThreeDomainSecurityResults**](ThreeDomainSecurityResults.md) |  | 

## Example

```python
from openapi_client.models.three_domain_security import ThreeDomainSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of ThreeDomainSecurity from a JSON string
three_domain_security_instance = ThreeDomainSecurity.from_json(json)
# print the JSON string representation of the object
print ThreeDomainSecurity.to_json()

# convert the object into a dict
three_domain_security_dict = three_domain_security_instance.to_dict()
# create an instance of ThreeDomainSecurity from a dict
three_domain_security_form_dict = three_domain_security.from_dict(three_domain_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


