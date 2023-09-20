# AddressStreetNumber

The street number alone is the numerical number that precedes the street name in the address

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**street_nmbr_suffix** | **str** | Street Number Suffix | [optional] 
**street_direction** | **str** | Dircetion of the Street | [optional] 
**rural_route_nmbr** | **str** | RuralRoute Number | [optional] 
**po_box** | **str** | PO Box Number | [optional] 

## Example

```python
from openapi_client.models.address_street_number import AddressStreetNumber

# TODO update the JSON string below
json = "{}"
# create an instance of AddressStreetNumber from a JSON string
address_street_number_instance = AddressStreetNumber.from_json(json)
# print the JSON string representation of the object
print AddressStreetNumber.to_json()

# convert the object into a dict
address_street_number_dict = address_street_number_instance.to_dict()
# create an instance of AddressStreetNumber from a dict
address_street_number_form_dict = address_street_number.from_dict(address_street_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


