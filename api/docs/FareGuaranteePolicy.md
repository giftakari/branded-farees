# FareGuaranteePolicy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**passenger_type_codes** | **List[str]** | The list of passenger type codes | [optional] 
**eligiblefor_adm_review** | [**YesNoUnknownEnum**](YesNoUnknownEnum.md) |  | 
**code** | [**Code**](Code.md) |  | [optional] 

## Example

```python
from openapi_client.models.fare_guarantee_policy import FareGuaranteePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of FareGuaranteePolicy from a JSON string
fare_guarantee_policy_instance = FareGuaranteePolicy.from_json(json)
# print the JSON string representation of the object
print FareGuaranteePolicy.to_json()

# convert the object into a dict
fare_guarantee_policy_dict = fare_guarantee_policy_instance.to_dict()
# create an instance of FareGuaranteePolicy from a dict
fare_guarantee_policy_form_dict = fare_guarantee_policy.from_dict(fare_guarantee_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


