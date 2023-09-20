# Change


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**product_refs** | **List[str]** | The productRefs this change or cancel applies to | [optional] 
**segment_sequence** | **List[int]** | The SegmentSequence of the product this change or cancel applies to | [optional] 

## Example

```python
from openapi_client.models.change import Change

# TODO update the JSON string below
json = "{}"
# create an instance of Change from a JSON string
change_instance = Change.from_json(json)
# print the JSON string representation of the object
print Change.to_json()

# convert the object into a dict
change_dict = change_instance.to_dict()
# create an instance of Change from a dict
change_form_dict = change.from_dict(change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


