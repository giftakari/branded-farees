# ChangeFeeCollectionMethod


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**ChangeFeeMethodEnum**](ChangeFeeMethodEnum.md) |  | [optional] 
**code** | **str** | The code value | 
**sub_code** | **str** | The subcode value | [optional] 
**description** | **str** | The description value | [optional] 
**change_fee_issued_separately_ind** | **bool** | if true, the change fee will be issued as a separate transaction to the residual amount | [optional] 
**tax_included_in_base_amount_ind** | **bool** | If true, the tax  on the fee will be included in the base fee amount and sent as a single value to the supplier for fulfilment | [optional] 

## Example

```python
from openapi_client.models.change_fee_collection_method import ChangeFeeCollectionMethod

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeFeeCollectionMethod from a JSON string
change_fee_collection_method_instance = ChangeFeeCollectionMethod.from_json(json)
# print the JSON string representation of the object
print ChangeFeeCollectionMethod.to_json()

# convert the object into a dict
change_fee_collection_method_dict = change_fee_collection_method_instance.to_dict()
# create an instance of ChangeFeeCollectionMethod from a dict
change_fee_collection_method_form_dict = change_fee_collection_method.from_dict(change_fee_collection_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


