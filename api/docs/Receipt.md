# Receipt


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_time** | **datetime** | Receipt date time | [optional] 
**offer_ref** | **List[str]** | List of offers which links with the receipt | [optional] 
**product_ref** | **str** | Reference of product | [optional] 

## Example

```python
from openapi_client.models.receipt import Receipt

# TODO update the JSON string below
json = "{}"
# create an instance of Receipt from a JSON string
receipt_instance = Receipt.from_json(json)
# print the JSON string representation of the object
print Receipt.to_json()

# convert the object into a dict
receipt_dict = receipt_instance.to_dict()
# create an instance of Receipt from a dict
receipt_form_dict = receipt.from_dict(receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


