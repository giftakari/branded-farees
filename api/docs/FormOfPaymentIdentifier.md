# FormOfPaymentIdentifier


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**form_of_payment_ref** | **str** |  | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.form_of_payment_identifier import FormOfPaymentIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of FormOfPaymentIdentifier from a JSON string
form_of_payment_identifier_instance = FormOfPaymentIdentifier.from_json(json)
# print the JSON string representation of the object
print FormOfPaymentIdentifier.to_json()

# convert the object into a dict
form_of_payment_identifier_dict = form_of_payment_identifier_instance.to_dict()
# create an instance of FormOfPaymentIdentifier from a dict
form_of_payment_identifier_form_dict = form_of_payment_identifier.from_dict(form_of_payment_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


