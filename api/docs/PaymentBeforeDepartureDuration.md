# PaymentBeforeDepartureDuration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | The advance duration the Offer can be reserved. | 

## Example

```python
from openapi_client.models.payment_before_departure_duration import PaymentBeforeDepartureDuration

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentBeforeDepartureDuration from a JSON string
payment_before_departure_duration_instance = PaymentBeforeDepartureDuration.from_json(json)
# print the JSON string representation of the object
print PaymentBeforeDepartureDuration.to_json()

# convert the object into a dict
payment_before_departure_duration_dict = payment_before_departure_duration_instance.to_dict()
# create an instance of PaymentBeforeDepartureDuration from a dict
payment_before_departure_duration_form_dict = payment_before_departure_duration.from_dict(payment_before_departure_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


