# Restriction

Restriction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**segment_sequence_list** | **List[int]** | Segment sequence list | [optional] 
**product_ref** | **List[str]** | The productRef which the restriction applies to | [optional] 

## Example

```python
from openapi_client.models.restriction import Restriction

# TODO update the JSON string below
json = "{}"
# create an instance of Restriction from a JSON string
restriction_instance = Restriction.from_json(json)
# print the JSON string representation of the object
print Restriction.to_json()

# convert the object into a dict
restriction_dict = restriction_instance.to_dict()
# create an instance of Restriction from a dict
restriction_form_dict = restriction.from_dict(restriction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


