# NetRemitInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**car_code** | **str** | The CAR code applied to this product for use in net remit | [optional] 
**value_code** | **str** | The Value code applied to this product for use in net remit | [optional] 
**actual_selling_fare** | **float** | The actual selling fare which will override the Offer base fare on the document | [optional] 
**net_base_amount** | [**FiledAmount**](FiledAmount.md) |  | [optional] 

## Example

```python
from openapi_client.models.net_remit_info import NetRemitInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetRemitInfo from a JSON string
net_remit_info_instance = NetRemitInfo.from_json(json)
# print the JSON string representation of the object
print NetRemitInfo.to_json()

# convert the object into a dict
net_remit_info_dict = net_remit_info_instance.to_dict()
# create an instance of NetRemitInfo from a dict
net_remit_info_form_dict = net_remit_info.from_dict(net_remit_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


