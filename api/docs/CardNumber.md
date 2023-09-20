# CardNumber


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**encryption_key** | **str** | Note: This contains a key required to retrieve the full payment instrument details compliant with PCI DSS standards. | [optional] 
**encryption_key_method** | **str** | Developer: This contains a reference to the key generation method being used - this is NOT the key value. | [optional] 
**encryption_method** | **str** | OpenTravel Best Practice: Encryption Method: When using the OpenTravel Encryption element, it is RECOMMENDED that all trading partners be informed of all encryption methods being used in advance of implementation to ensure message processing compatibility. | [optional] 
**encrypted_value** | **str** | Encrypted value | [optional] 
**mask** | **str** | Masked Value | [optional] 
**token** | **str** | Token value | [optional] 
**token_provider_id** | **str** | Developer: This contains a provider ID if multiple providers are used for secure information exchange. | [optional] 
**authentication_method** | [**EncryptionTokenTypeAuthEnum**](EncryptionTokenTypeAuthEnum.md) |  | [optional] 
**plain_text** | **str** | Don&#39;t use this unless it is REALLY ok to not use encryption. Non-secure (plain text) value. | [optional] 
**error_warning** | [**ErrorWarning**](ErrorWarning.md) |  | [optional] 

## Example

```python
from openapi_client.models.card_number import CardNumber

# TODO update the JSON string below
json = "{}"
# create an instance of CardNumber from a JSON string
card_number_instance = CardNumber.from_json(json)
# print the JSON string representation of the object
print CardNumber.to_json()

# convert the object into a dict
card_number_dict = card_number_instance.to_dict()
# create an instance of CardNumber from a dict
card_number_form_dict = card_number.from_dict(card_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


