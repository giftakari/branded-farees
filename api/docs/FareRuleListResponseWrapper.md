# FareRuleListResponseWrapper


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fare_rules_list_response** | [**FareRuleListResponse**](FareRuleListResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.fare_rule_list_response_wrapper import FareRuleListResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FareRuleListResponseWrapper from a JSON string
fare_rule_list_response_wrapper_instance = FareRuleListResponseWrapper.from_json(json)
# print the JSON string representation of the object
print FareRuleListResponseWrapper.to_json()

# convert the object into a dict
fare_rule_list_response_wrapper_dict = fare_rule_list_response_wrapper_instance.to_dict()
# create an instance of FareRuleListResponseWrapper from a dict
fare_rule_list_response_wrapper_form_dict = fare_rule_list_response_wrapper.from_dict(fare_rule_list_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


