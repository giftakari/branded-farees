# CatalogOfferingsRequestHospitality


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**search_control_console_channel_id** | [**SearchControlConsoleChannelID**](SearchControlConsoleChannelID.md) |  | [optional] 
**requested_currency** | **str** | You can use requested currency to request conversion rate information. The response will return the currencyRateConversion object which will contain conversion rate of the requested currency. | [optional] 
**max_response_wait_time** | **int** | Maximum time (in milliseconds) to wait for provider responses before returning a response to the consumer of this service | [optional] 
**stay_dates** | [**DateOrDateWindows**](DateOrDateWindows.md) |  | 
**hotel_search_criterion** | [**HotelSearchCriterion**](HotelSearchCriterion.md) |  | [optional] 
**minimum_amount** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 
**maximum_amount** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 
**verbose_response_ind** | **bool** | Used to specify that a verbose response is to be returned.  Verbose responses repeat the Property information in each Product and do not return the reference list. | [optional] 

## Example

```python
from openapi_client.models.catalog_offerings_request_hospitality import CatalogOfferingsRequestHospitality

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogOfferingsRequestHospitality from a JSON string
catalog_offerings_request_hospitality_instance = CatalogOfferingsRequestHospitality.from_json(json)
# print the JSON string representation of the object
print CatalogOfferingsRequestHospitality.to_json()

# convert the object into a dict
catalog_offerings_request_hospitality_dict = catalog_offerings_request_hospitality_instance.to_dict()
# create an instance of CatalogOfferingsRequestHospitality from a dict
catalog_offerings_request_hospitality_form_dict = catalog_offerings_request_hospitality.from_dict(catalog_offerings_request_hospitality_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


