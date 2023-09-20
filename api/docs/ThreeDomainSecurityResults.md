# ThreeDomainSecurityResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**c_avv** | **str** | The cAVV value | [optional] 
**p_a_res_status** | **str** | The pAResStatus value | [optional] 
**signature_verfication** | **str** | The signature Verification value | [optional] 
**transaction_id** | **str** | The transaction ID | [optional] 
**x_id** | **str** | Merchants must ensure that each Payer Authentication Request (PAReq) contains a unique combination of account ID and XID | [optional] 
**e_ci** | **str** | Electronic Commerce Indicator - 3-D secure data, contact your authenticator for rules and downline processing. | [optional] 
**u_caf_indicator** | **str** | Universal Card Authentication Field™ MasterCard only UCAF is the mechanism that is used to transmit the AAV from the merchant to issuer for authentication purposes during the authorization process | [optional] 

## Example

```python
from openapi_client.models.three_domain_security_results import ThreeDomainSecurityResults

# TODO update the JSON string below
json = "{}"
# create an instance of ThreeDomainSecurityResults from a JSON string
three_domain_security_results_instance = ThreeDomainSecurityResults.from_json(json)
# print the JSON string representation of the object
print ThreeDomainSecurityResults.to_json()

# convert the object into a dict
three_domain_security_results_dict = three_domain_security_results_instance.to_dict()
# create an instance of ThreeDomainSecurityResults from a dict
three_domain_security_results_form_dict = three_domain_security_results.from_dict(three_domain_security_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


