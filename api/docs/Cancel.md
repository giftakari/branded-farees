# Cancel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**product_refs** | **List[str]** | The productRefs this change or cancel applies to | [optional] 
**segment_sequence** | **List[int]** | The SegmentSequence of the product this change or cancel applies to | [optional] 

## Example

```python
from openapi_client.models.cancel import Cancel

# TODO update the JSON string below
json = "{}"
# create an instance of Cancel from a JSON string
cancel_instance = Cancel.from_json(json)
# print the JSON string representation of the object
print Cancel.to_json()

# convert the object into a dict
cancel_dict = cancel_instance.to_dict()
# create an instance of Cancel from a dict
cancel_form_dict = cancel.from_dict(cancel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


