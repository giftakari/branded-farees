# GuestCount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**age** | **int** | The age of the guest | [optional] 
**count** | **int** | The number of guests in one AgeQualifyingCode or Count. | [optional] 
**age_qualifying_code** | **str** | Enter 10 for an adult or 08 for a child | [optional] 

## Example

```python
from openapi_client.models.guest_count import GuestCount

# TODO update the JSON string below
json = "{}"
# create an instance of GuestCount from a JSON string
guest_count_instance = GuestCount.from_json(json)
# print the JSON string representation of the object
print GuestCount.to_json()

# convert the object into a dict
guest_count_dict = guest_count_instance.to_dict()
# create an instance of GuestCount from a dict
guest_count_form_dict = guest_count.from_dict(guest_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


