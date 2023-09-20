# DocumentValidDateRange


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**product_ref** | [**List[ProductIdentifier]**](ProductIdentifier.md) |  | [optional] 
**segment_sequence_list** | **List[int]** | The segmentSequence within the product the action is being requested for. Used when multiple flights exist within a product. Only one product may be selected with this option. | [optional] 
**valid_date_range** | [**DateRange**](DateRange.md) |  | [optional] 

## Example

```python
from openapi_client.models.document_valid_date_range import DocumentValidDateRange

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentValidDateRange from a JSON string
document_valid_date_range_instance = DocumentValidDateRange.from_json(json)
# print the JSON string representation of the object
print DocumentValidDateRange.to_json()

# convert the object into a dict
document_valid_date_range_dict = document_valid_date_range_instance.to_dict()
# create an instance of DocumentValidDateRange from a dict
document_valid_date_range_form_dict = document_valid_date_range.from_dict(document_valid_date_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


