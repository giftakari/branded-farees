# PaymentID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** |  | [optional] 
**payment_ref** | **str** |  | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.payment_id import PaymentID

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentID from a JSON string
payment_id_instance = PaymentID.from_json(json)
# print the JSON string representation of the object
print PaymentID.to_json()

# convert the object into a dict
payment_id_dict = payment_id_instance.to_dict()
# create an instance of PaymentID from a dict
payment_id_form_dict = payment_id.from_dict(payment_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


