# FormOfPaymentID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | [optional] 
**form_of_payment_ref** | **str** |  | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.form_of_payment_id import FormOfPaymentID

# TODO update the JSON string below
json = "{}"
# create an instance of FormOfPaymentID from a JSON string
form_of_payment_id_instance = FormOfPaymentID.from_json(json)
# print the JSON string representation of the object
print FormOfPaymentID.to_json()

# convert the object into a dict
form_of_payment_id_dict = form_of_payment_id_instance.to_dict()
# create an instance of FormOfPaymentID from a dict
form_of_payment_id_form_dict = form_of_payment_id.from_dict(form_of_payment_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


