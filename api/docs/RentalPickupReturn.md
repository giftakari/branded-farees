# RentalPickupReturn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**var_date** | **date** | The local date of the pickup or return | 
**time** | **str** | The local time of the pickup or return | [optional] 
**vendor_location** | [**VendorLocation**](VendorLocation.md) |  | [optional] 

## Example

```python
from openapi_client.models.rental_pickup_return import RentalPickupReturn

# TODO update the JSON string below
json = "{}"
# create an instance of RentalPickupReturn from a JSON string
rental_pickup_return_instance = RentalPickupReturn.from_json(json)
# print the JSON string representation of the object
print RentalPickupReturn.to_json()

# convert the object into a dict
rental_pickup_return_dict = rental_pickup_return_instance.to_dict()
# create an instance of RentalPickupReturn from a dict
rental_pickup_return_form_dict = rental_pickup_return.from_dict(rental_pickup_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


