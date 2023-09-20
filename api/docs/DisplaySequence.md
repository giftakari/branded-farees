# DisplaySequence


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**display_sequence** | **str** | The sequence the products are to be displayed for sequential date ordering | 
**offer_ref** | **str** | Offer reference | 
**product_ref** | **str** | Product reference. If blank, display sequence applies to all products within the Offer. | [optional] 
**sequence** | **int** | Segment sequence, if blank, display sequence applies to all segments within the product | [optional] 

## Example

```python
from openapi_client.models.display_sequence import DisplaySequence

# TODO update the JSON string below
json = "{}"
# create an instance of DisplaySequence from a JSON string
display_sequence_instance = DisplaySequence.from_json(json)
# print the JSON string representation of the object
print DisplaySequence.to_json()

# convert the object into a dict
display_sequence_dict = display_sequence_instance.to_dict()
# create an instance of DisplaySequence from a dict
display_sequence_form_dict = display_sequence.from_dict(display_sequence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


