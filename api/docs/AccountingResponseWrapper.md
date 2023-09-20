# AccountingResponseWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_response** | [**AccountingResponse**](AccountingResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.accounting_response_wrapper import AccountingResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingResponseWrapper from a JSON string
accounting_response_wrapper_instance = AccountingResponseWrapper.from_json(json)
# print the JSON string representation of the object
print AccountingResponseWrapper.to_json()

# convert the object into a dict
accounting_response_wrapper_dict = accounting_response_wrapper_instance.to_dict()
# create an instance of AccountingResponseWrapper from a dict
accounting_response_wrapper_form_dict = accounting_response_wrapper.from_dict(accounting_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


