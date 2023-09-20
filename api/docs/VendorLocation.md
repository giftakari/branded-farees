# VendorLocation

The vendor's location number for pickup or return

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**rental_location_number** | **str** |  | [optional] 
**vendor_code** | **str** |  | [optional] 
**rental_location_name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**telephone** | [**List[Telephone]**](Telephone.md) |  | [optional] 
**description** | **str** | Detailed location information on where to pick up and return a vehicle | [optional] 
**operation_times** | [**List[OperationTimes]**](OperationTimes.md) |  | [optional] 
**directions** | **str** | Directions for collecting the vehicle | [optional] 
**additional_instructions** | **str** | Additional instructions regarding the vendor location | [optional] 
**shuttle_service** | **str** | Information on shuttle service | [optional] 
**rental_location_code** | [**Code**](Code.md) |  | [optional] 
**counter_location_code** | [**Code**](Code.md) |  | [optional] 

## Example

```python
from openapi_client.models.vendor_location import VendorLocation

# TODO update the JSON string below
json = "{}"
# create an instance of VendorLocation from a JSON string
vendor_location_instance = VendorLocation.from_json(json)
# print the JSON string representation of the object
print VendorLocation.to_json()

# convert the object into a dict
vendor_location_dict = vendor_location_instance.to_dict()
# create an instance of VendorLocation from a dict
vendor_location_form_dict = vendor_location.from_dict(vendor_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


