# BaggageAllowance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**passenger_type_codes** | **List[str]** | List of passenger type codes | [optional] 
**baggage_type** | [**BaggageTypeEnum**](BaggageTypeEnum.md) |  | [optional] 
**product_ref** | **List[str]** | A product is any product, service or package of products and services  that can be priced and purchased by a specific supplier. | [optional] 
**baggage_item** | [**List[BaggageItem]**](BaggageItem.md) |  | [optional] 
**segment_sequence_list** | **List[int]** | Segment sequence is only to be used when the baggage allowance differs between segments within a product. If so, then the ProducRef must be specified. | [optional] 
**text** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.baggage_allowance import BaggageAllowance

# TODO update the JSON string below
json = "{}"
# create an instance of BaggageAllowance from a JSON string
baggage_allowance_instance = BaggageAllowance.from_json(json)
# print the JSON string representation of the object
print BaggageAllowance.to_json()

# convert the object into a dict
baggage_allowance_dict = baggage_allowance_instance.to_dict()
# create an instance of BaggageAllowance from a dict
baggage_allowance_form_dict = baggage_allowance.from_dict(baggage_allowance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


