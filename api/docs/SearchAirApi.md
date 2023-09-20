# openapi_client.SearchAirApi

All URIs are relative to *https://api.pp.travelport.com/11/air*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_next_air_search**](SearchAirApi.md#build_next_air_search) | **POST** /catalog/search/catalogproductofferings/buildnext | Search for flights on next leg
[**build_options_air_search**](SearchAirApi.md#build_options_air_search) | **POST** /catalog/search/catalogproductofferings/buildoptions | Return all upsells on a specific flight
[**create_air_search**](SearchAirApi.md#create_air_search) | **POST** /catalog/search/catalogproductofferings | Initial flight search
[**get_page_air_search**](SearchAirApi.md#get_page_air_search) | **GET** /catalog/search/catalogproductofferings | Return additional search results (pagination)


# **build_next_air_search**
> CatalogProductOfferingsResponseWrapper build_next_air_search(catalog_product_offerings_query_build_next, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

Search for flights on next leg

Use the Next Leg Search API to return offers for the remaining leg/s of an itinerary after a leg-based Search. A leg-based Search response returns offers for only the outbound leg of your itinerary, and you must send Next Leg Search to return offers for the remaining leg or legs of the trip. If pagination was requested in the initial Search request it is applied to the Next Leg Search response as well.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.catalog_product_offerings_query_build_next import CatalogProductOfferingsQueryBuildNext
from openapi_client.models.catalog_product_offerings_response_wrapper import CatalogProductOfferingsResponseWrapper
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
    api_instance = openapi_client.SearchAirApi(api_client)
    catalog_product_offerings_query_build_next = openapi_client.CatalogProductOfferingsQueryBuildNext() # CatalogProductOfferingsQueryBuildNext | 
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # Search for flights on next leg
        api_response = api_instance.build_next_air_search(catalog_product_offerings_query_build_next, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of SearchAirApi->build_next_air_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchAirApi->build_next_air_search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_product_offerings_query_build_next** | [**CatalogProductOfferingsQueryBuildNext**](CatalogProductOfferingsQueryBuildNext.md)|  | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**CatalogProductOfferingsResponseWrapper**](CatalogProductOfferingsResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **build_options_air_search**
> CatalogProductOfferingsResponseWrapper build_options_air_search(catalog_product_offerings_query_build_options, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

Return all upsells on a specific flight

Use the Flight Specific Search API reference payload request to return additional upsells (you can set up to 99) for any product or products returned by a Search or Next Leg Search. The reference payload sends an identifier referencing a previous response and is supported for both GDS and NDC. Full payload is not supported for NDC; use the reference payload instead. For GDS, you can send either a reference payload or a full payload.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.catalog_product_offerings_query_build_options import CatalogProductOfferingsQueryBuildOptions
from openapi_client.models.catalog_product_offerings_response_wrapper import CatalogProductOfferingsResponseWrapper
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
    api_instance = openapi_client.SearchAirApi(api_client)
    catalog_product_offerings_query_build_options = openapi_client.CatalogProductOfferingsQueryBuildOptions() # CatalogProductOfferingsQueryBuildOptions | 
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # Return all upsells on a specific flight
        api_response = api_instance.build_options_air_search(catalog_product_offerings_query_build_options, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of SearchAirApi->build_options_air_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchAirApi->build_options_air_search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_product_offerings_query_build_options** | [**CatalogProductOfferingsQueryBuildOptions**](CatalogProductOfferingsQueryBuildOptions.md)|  | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**CatalogProductOfferingsResponseWrapper**](CatalogProductOfferingsResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_air_search**
> CatalogProductOfferingsResponseWrapper create_air_search(catalog_product_offerings_query_request_wrapper, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

Initial flight search

The Search API is the first step in the travel booking workflow. Send a Search request to return offers for flights between the selected cities

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.catalog_product_offerings_query_request_wrapper import CatalogProductOfferingsQueryRequestWrapper
from openapi_client.models.catalog_product_offerings_response_wrapper import CatalogProductOfferingsResponseWrapper
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
    api_instance = openapi_client.SearchAirApi(api_client)
    catalog_product_offerings_query_request_wrapper = openapi_client.CatalogProductOfferingsQueryRequestWrapper() # CatalogProductOfferingsQueryRequestWrapper | 
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # Initial flight search
        api_response = api_instance.create_air_search(catalog_product_offerings_query_request_wrapper, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of SearchAirApi->create_air_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchAirApi->create_air_search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_product_offerings_query_request_wrapper** | [**CatalogProductOfferingsQueryRequestWrapper**](CatalogProductOfferingsQueryRequestWrapper.md)|  | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**CatalogProductOfferingsResponseWrapper**](CatalogProductOfferingsResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_page_air_search**
> CatalogProductOfferingsResponseWrapper get_page_air_search(identifier=identifier, page_number=page_number, view=view, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

Return additional search results (pagination)

The optional pagination feature is supported for Search and Next Leg Search. Pagination allows you to control the number of offers returned in the initial response, which can affect response time. To request pagination, send offersPerPage in the initial Search request payload. All offers are cached on the server, but only the number sent in offersPerPage is returned in the initial response. For example, if offersPerPage is set to 5, only the first 5 offers are returned in the initial response. (An offer is a set of products that are each available at the same unique price point and same terms and conditions.) To retrieve the second and subsequent pages of search results, send the POST request above to the endpoint used for the initial Search or Next Leg Search request with the transaction identifier from that response.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.catalog_product_offerings_response_wrapper import CatalogProductOfferingsResponseWrapper
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
    api_instance = openapi_client.SearchAirApi(api_client)
    identifier = 'A0656EFF-FAF4-456F-B061-0161008D7C4E' # str | The Identifier of the Offerings from which a page is to be returned (optional)
    page_number = '2' # str | The page number to be returned (optional)
    view = 'detail' # str | The view.  Either detail or summary. (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # Return additional search results (pagination)
        api_response = api_instance.get_page_air_search(identifier=identifier, page_number=page_number, view=view, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of SearchAirApi->get_page_air_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchAirApi->get_page_air_search: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The Identifier of the Offerings from which a page is to be returned | [optional] 
 **page_number** | **str**| The page number to be returned | [optional] 
 **view** | **str**| The view.  Either detail or summary. | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**CatalogProductOfferingsResponseWrapper**](CatalogProductOfferingsResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK Successful Response |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

