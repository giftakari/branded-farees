# CustomerLoyalty

Specifies the ID for the membership program.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**id** | **str** | Customer Loyality Id | [optional] 
**priority** | **int** | Numeric Priority Code | [optional] 
**program_id** | **str** | Specifies an identifier to indicate the company owner of the loyalty program | [optional] 
**program_name** | **str** | Supplier&#39;s loyalty program name such as Frontier-EarlyReturns | [optional] 
**supplier_type** | **str** | The kind of supplier of a loyalty program | [optional] 
**supplier** | **str** | Supplier of a loyalty program | [optional] 
**tier** | **str** | Customer Loyalty tier level | [optional] 
**share_with_supplier** | **List[str]** | The list of suppliers that the CustomerLoyalty number is shared. | [optional] 
**card_holder_name** | **str** | The card holder name | [optional] 
**validated_ind** | **bool** | Customer loyalty number has been validated by the supplier | [optional] 

## Example

```python
from openapi_client.models.customer_loyalty import CustomerLoyalty

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerLoyalty from a JSON string
customer_loyalty_instance = CustomerLoyalty.from_json(json)
# print the JSON string representation of the object
print CustomerLoyalty.to_json()

# convert the object into a dict
customer_loyalty_dict = customer_loyalty_instance.to_dict()
# create an instance of CustomerLoyalty from a dict
customer_loyalty_form_dict = customer_loyalty.from_dict(customer_loyalty_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


