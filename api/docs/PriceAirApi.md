# openapi_client.PriceAirApi

All URIs are relative to *https://api.pp.travelport.com/11/air*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offer_build_from_catalog_offerings**](PriceAirApi.md#offer_build_from_catalog_offerings) | **POST** /price/offers/buildfromcatalogofferings | Price by reference to a low fare search response
[**offer_build_from_catalog_product_offerings**](PriceAirApi.md#offer_build_from_catalog_product_offerings) | **POST** /price/offers/buildfromcatalogproductofferings | Price request with reference payload
[**offer_build_from_products**](PriceAirApi.md#offer_build_from_products) | **POST** /price/offers/buildfromproducts | Price request with full payload


# **offer_build_from_catalog_offerings**
> OfferListResponseWrapper offer_build_from_catalog_offerings(offer_query_build_from_catalog_offerings, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)

Price by reference to a low fare search response

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.offer_list_response_wrapper import OfferListResponseWrapper
from openapi_client.models.offer_query_build_from_catalog_offerings import OfferQueryBuildFromCatalogOfferings
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
    api_instance = openapi_client.PriceAirApi(api_client)
    offer_query_build_from_catalog_offerings = openapi_client.OfferQueryBuildFromCatalogOfferings() # OfferQueryBuildFromCatalogOfferings | 
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)

    try:
        # Price by reference to a low fare search response
        api_response = api_instance.offer_build_from_catalog_offerings(offer_query_build_from_catalog_offerings, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)
        print("The response of PriceAirApi->offer_build_from_catalog_offerings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceAirApi->offer_build_from_catalog_offerings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_query_build_from_catalog_offerings** | [**OfferQueryBuildFromCatalogOfferings**](OfferQueryBuildFromCatalogOfferings.md)|  | 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 

### Return type

[**OfferListResponseWrapper**](OfferListResponseWrapper.md)

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

# **offer_build_from_catalog_product_offerings**
> OfferListResponseWrapper offer_build_from_catalog_product_offerings(offer_query_build_from_catalog_product_offerings, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)

Price request with reference payload

The AirPrice API confirms pricing on air search results. While air pricing is generally an optional but recommended step, it is required for low cost carriers and some NDC carriers.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.offer_list_response_wrapper import OfferListResponseWrapper
from openapi_client.models.offer_query_build_from_catalog_product_offerings import OfferQueryBuildFromCatalogProductOfferings
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
    api_instance = openapi_client.PriceAirApi(api_client)
    offer_query_build_from_catalog_product_offerings = openapi_client.OfferQueryBuildFromCatalogProductOfferings() # OfferQueryBuildFromCatalogProductOfferings | 
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)

    try:
        # Price request with reference payload
        api_response = api_instance.offer_build_from_catalog_product_offerings(offer_query_build_from_catalog_product_offerings, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)
        print("The response of PriceAirApi->offer_build_from_catalog_product_offerings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceAirApi->offer_build_from_catalog_product_offerings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_query_build_from_catalog_product_offerings** | [**OfferQueryBuildFromCatalogProductOfferings**](OfferQueryBuildFromCatalogProductOfferings.md)|  | 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 

### Return type

[**OfferListResponseWrapper**](OfferListResponseWrapper.md)

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

# **offer_build_from_products**
> OfferListResponseWrapper offer_build_from_products(offer_query_build_from_products, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)

Price request with full payload

The AirPrice API confirms pricing on air search results. While air pricing is generally an optional but recommended step, it is required for low cost carriers and some NDC carriers.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.offer_list_response_wrapper import OfferListResponseWrapper
from openapi_client.models.offer_query_build_from_products import OfferQueryBuildFromProducts
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
    api_instance = openapi_client.PriceAirApi(api_client)
    offer_query_build_from_products = openapi_client.OfferQueryBuildFromProducts() # OfferQueryBuildFromProducts | 
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)

    try:
        # Price request with full payload
        api_response = api_instance.offer_build_from_products(offer_query_build_from_products, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)
        print("The response of PriceAirApi->offer_build_from_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceAirApi->offer_build_from_products: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_query_build_from_products** | [**OfferQueryBuildFromProducts**](OfferQueryBuildFromProducts.md)|  | 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 

### Return type

[**OfferListResponseWrapper**](OfferListResponseWrapper.md)

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

