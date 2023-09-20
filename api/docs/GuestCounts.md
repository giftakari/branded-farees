# GuestCounts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**guest_count** | [**List[GuestCount]**](GuestCount.md) |  | 

## Example

```python
from openapi_client.models.guest_counts import GuestCounts

# TODO update the JSON string below
json = "{}"
# create an instance of GuestCounts from a JSON string
guest_counts_instance = GuestCounts.from_json(json)
# print the JSON string representation of the object
print GuestCounts.to_json()

# convert the object into a dict
guest_counts_dict = guest_counts_instance.to_dict()
# create an instance of GuestCounts from a dict
guest_counts_form_dict = guest_counts.from_dict(guest_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


