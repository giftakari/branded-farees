# PaymentBeforeDeparture


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**time_of_day** | **str** | The time of day indicates the earliest time the Offer can be reserved. Used in conjunction with DayOfWeek or Duration | [optional] 

## Example

```python
from openapi_client.models.payment_before_departure import PaymentBeforeDeparture

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentBeforeDeparture from a JSON string
payment_before_departure_instance = PaymentBeforeDeparture.from_json(json)
# print the JSON string representation of the object
print PaymentBeforeDeparture.to_json()

# convert the object into a dict
payment_before_departure_dict = payment_before_departure_instance.to_dict()
# create an instance of PaymentBeforeDeparture from a dict
payment_before_departure_form_dict = payment_before_departure.from_dict(payment_before_departure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


