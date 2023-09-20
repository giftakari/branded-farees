# EMD


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person_name** | [**PersonName**](PersonName.md) |  | 
**reservation_locator** | [**List[SupplierLocator]**](SupplierLocator.md) |  | [optional] 
**agency_info** | [**AgencyInfo**](AgencyInfo.md) |  | 
**emd_segment** | [**List[EMDSegment]**](EMDSegment.md) |  | 
**total_amount** | [**TotalAmount**](TotalAmount.md) |  | [optional] 
**form_of_payment** | [**FormOfPayment**](FormOfPayment.md) |  | 
**esac** | **str** | The BSP ESAC code assign for a void or refund transaction\\nThe BSP E | [optional] 
**associated_ticket_number** | [**TicketNumber**](TicketNumber.md) |  | [optional] 
**restrictions** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.emd import EMD

# TODO update the JSON string below
json = "{}"
# create an instance of EMD from a JSON string
emd_instance = EMD.from_json(json)
# print the JSON string representation of the object
print EMD.to_json()

# convert the object into a dict
emd_dict = emd_instance.to_dict()
# create an instance of EMD from a dict
emd_form_dict = emd.from_dict(emd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


