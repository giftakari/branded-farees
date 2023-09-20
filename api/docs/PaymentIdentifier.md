# PaymentIdentifier


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**payment_ref** | **str** |  | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_identifier import PaymentIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIdentifier from a JSON string
payment_identifier_instance = PaymentIdentifier.from_json(json)
# print the JSON string representation of the object
print PaymentIdentifier.to_json()

# convert the object into a dict
payment_identifier_dict = payment_identifier_instance.to_dict()
# create an instance of PaymentIdentifier from a dict
payment_identifier_form_dict = payment_identifier.from_dict(payment_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


