# PaymentListRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment** | [**List[Payment]**](Payment.md) |  | 

## Example

```python
from openapi_client.models.payment_list_request import PaymentListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentListRequest from a JSON string
payment_list_request_instance = PaymentListRequest.from_json(json)
# print the JSON string representation of the object
print PaymentListRequest.to_json()

# convert the object into a dict
payment_list_request_dict = payment_list_request_instance.to_dict()
# create an instance of PaymentListRequest from a dict
payment_list_request_form_dict = payment_list_request.from_dict(payment_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


