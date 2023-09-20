# openapi_client.BrandApi

All URIs are relative to *https://api.pp.travelport.com/11/air*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_brand**](BrandApi.md#create_brand) | **POST** /brandfullinfo/brands/buildcompleteinfofromoffer | Follow-on request for full brand pricing


# **create_brand**
> BrandListResponseWrapper create_brand(brand_query_build_complete_info_from_offer, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

Follow-on request for full brand pricing

The full brand pricing request is a follow-on request to air pricing that returns any additional content for the branded fares returned. All attributes associated with that branded fare are returned along with any additional details available, such as beverages, mileage accrual, etc. If brand details are not available for that market, no additional details are returned.The full brand pricing request can be sent after either an AirPrice reference payload request or an AirPrice full payload request , as long as the request sent returnBrandedFaresInd set to true to return brand attributes.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.brand_list_response_wrapper import BrandListResponseWrapper
from openapi_client.models.brand_query_build_complete_info_from_offer import BrandQueryBuildCompleteInfoFromOffer
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pp.travelport.com/11/air
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pp.travelport.com/11/air"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BrandApi(api_client)
    brand_query_build_complete_info_from_offer = openapi_client.BrandQueryBuildCompleteInfoFromOffer() # BrandQueryBuildCompleteInfoFromOffer | 
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # Follow-on request for full brand pricing
        api_response = api_instance.create_brand(brand_query_build_complete_info_from_offer, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of BrandApi->create_brand:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandApi->create_brand: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_query_build_complete_info_from_offer** | [**BrandQueryBuildCompleteInfoFromOffer**](BrandQueryBuildCompleteInfoFromOffer.md)|  | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**BrandListResponseWrapper**](BrandListResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created - 201 |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

