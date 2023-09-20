# FulfillmentMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**product_refs** | **List[str]** | The product(s) the Fulfillment Method applies to. If blank applies to all products in the Offer | [optional] 
**segment_sequence_list** | **List[int]** | List of segment sequence | [optional] 
**refund_method** | [**RefundMethodEnum**](RefundMethodEnum.md) |  | [optional] 
**change_fee_collection_method** | [**ChangeFeeCollectionMethod**](ChangeFeeCollectionMethod.md) |  | [optional] 

## Example

```python
from openapi_client.models.fulfillment_method import FulfillmentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of FulfillmentMethod from a JSON string
fulfillment_method_instance = FulfillmentMethod.from_json(json)
# print the JSON string representation of the object
print FulfillmentMethod.to_json()

# convert the object into a dict
fulfillment_method_dict = fulfillment_method_instance.to_dict()
# create an instance of FulfillmentMethod from a dict
fulfillment_method_form_dict = fulfillment_method.from_dict(fulfillment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


