# Address


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Internally referenced id | [optional] 
**bldg_room** | [**AddressBldgRoom**](AddressBldgRoom.md) |  | [optional] 
**number** | [**AddressStreetNumber**](AddressStreetNumber.md) |  | [optional] 
**street** | **str** | May contain the street number when the Street number element is missing. | [optional] 
**address_line** | **List[str]** | Additional address line details | [optional] 
**city** | **str** | City (e.g., Dublin), town, or postal station (i.e., a postal service territory, often used in a military address). | 
**county** | **str** | County or Region Name (e.g., Fairfax). | [optional] 
**state_prov** | [**StateProv**](StateProv.md) |  | [optional] 
**country** | [**Country**](Country.md) |  | [optional] 
**postal_code** | **str** | Post Office Code number. | [optional] 
**addressee** | **str** | The name of the company or person to be addressed | [optional] 
**role** | [**EnumAddressRole**](EnumAddressRole.md) |  | [optional] 

## Example

```python
from openapi_client.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print Address.to_json()

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_form_dict = address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


