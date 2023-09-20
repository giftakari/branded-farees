# openapi_client.FareRulesApi

All URIs are relative to *https://api.pp.travelport.com/11/air*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_rules_from_catalog_offerings**](FareRulesApi.md#get_rules_from_catalog_offerings) | **GET** /farerule/farerules/fromcatalogofferings | Return standalone fare rules with reference to CatalogOfferings
[**get_rules_from_catalog_product_offerings**](FareRulesApi.md#get_rules_from_catalog_product_offerings) | **GET** /farerule/farerules/fromcatalogproductofferings | Return standalone fare rules with reference to CatalogProductOfferings
[**get_rules_from_offer**](FareRulesApi.md#get_rules_from_offer) | **GET** /farerule/farerules/fromoffer | Return standalone fare rules with reference to an Offer
[**get_rules_from_reservation**](FareRulesApi.md#get_rules_from_reservation) | **GET** /farerule/farerules/fromreservation | Return standalone fare rules with reference to a Reservation
[**get_rules_from_reservation_workbench**](FareRulesApi.md#get_rules_from_reservation_workbench) | **GET** /farerule/farerules/fromreservationworkbench | Return standalone fare rules with reference to a Reservation workbench


# **get_rules_from_catalog_offerings**
> FareRuleListResponseWrapper get_rules_from_catalog_offerings(catalog_offerings_identifier, catalog_offering_id, fare_rule_type, product_ids=product_ids, flight_ids=flight_ids, fare_rule_categories=fare_rule_categories, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)

Return standalone fare rules with reference to CatalogOfferings

Fare rules are the conditions and restrictions that apply to any booking based on its fare type. These determine the price of the fare. Generally, less expensive fares have more restrictions and more expensive fares have fewer restrictions. Fare rules can include blackout dates, advanced reservation requirements, minimum and maximum stay requirements, and cancellation and change penalties.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.fare_rule_list_response_wrapper import FareRuleListResponseWrapper
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
    api_instance = openapi_client.FareRulesApi(api_client)
    catalog_offerings_identifier = 'catalog_offerings_identifier_example' # str | 
    catalog_offering_id = 'catalog_offering_id_example' # str | 
    fare_rule_type = 'fare_rule_type_example' # str | The type of fare rule structure required
    product_ids = ['product_ids_example'] # List[str] |  (optional)
    flight_ids = ['flight_ids_example'] # List[str] |  (optional)
    fare_rule_categories = ['fare_rule_categories_example'] # List[str] | Penalties MinimumStay (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)

    try:
        # Return standalone fare rules with reference to CatalogOfferings
        api_response = api_instance.get_rules_from_catalog_offerings(catalog_offerings_identifier, catalog_offering_id, fare_rule_type, product_ids=product_ids, flight_ids=flight_ids, fare_rule_categories=fare_rule_categories, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)
        print("The response of FareRulesApi->get_rules_from_catalog_offerings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FareRulesApi->get_rules_from_catalog_offerings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_offerings_identifier** | **str**|  | 
 **catalog_offering_id** | **str**|  | 
 **fare_rule_type** | **str**| The type of fare rule structure required | 
 **product_ids** | [**List[str]**](str.md)|  | [optional] 
 **flight_ids** | [**List[str]**](str.md)|  | [optional] 
 **fare_rule_categories** | [**List[str]**](str.md)| Penalties MinimumStay | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 

### Return type

[**FareRuleListResponseWrapper**](FareRuleListResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Successful Response - 200 |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rules_from_catalog_product_offerings**
> FareRuleListResponseWrapper get_rules_from_catalog_product_offerings(catalog_product_offerings_identifier, catalog_product_offering_id, fare_rule_type, product_brand_offering_ids=product_brand_offering_ids, product_ids=product_ids, flight_ids=flight_ids, fare_rule_categories=fare_rule_categories, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)

Return standalone fare rules with reference to CatalogProductOfferings

Fare rules are the conditions and restrictions that apply to any booking based on its fare type. These determine the price of the fare. Generally, less expensive fares have more restrictions and more expensive fares have fewer restrictions. Fare rules can include blackout dates, advanced reservation requirements, minimum and maximum stay requirements, and cancellation and change penalties.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.fare_rule_list_response_wrapper import FareRuleListResponseWrapper
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
    api_instance = openapi_client.FareRulesApi(api_client)
    catalog_product_offerings_identifier = 'catalog_product_offerings_identifier_example' # str | 
    catalog_product_offering_id = 'catalog_product_offering_id_example' # str | 
    fare_rule_type = 'fare_rule_type_example' # str | The type of fare rule structure required
    product_brand_offering_ids = ['product_brand_offering_ids_example'] # List[str] |  (optional)
    product_ids = ['product_ids_example'] # List[str] |  (optional)
    flight_ids = ['flight_ids_example'] # List[str] |  (optional)
    fare_rule_categories = ['fare_rule_categories_example'] # List[str] | Space separated list of fare rule categories required (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)

    try:
        # Return standalone fare rules with reference to CatalogProductOfferings
        api_response = api_instance.get_rules_from_catalog_product_offerings(catalog_product_offerings_identifier, catalog_product_offering_id, fare_rule_type, product_brand_offering_ids=product_brand_offering_ids, product_ids=product_ids, flight_ids=flight_ids, fare_rule_categories=fare_rule_categories, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)
        print("The response of FareRulesApi->get_rules_from_catalog_product_offerings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FareRulesApi->get_rules_from_catalog_product_offerings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_product_offerings_identifier** | **str**|  | 
 **catalog_product_offering_id** | **str**|  | 
 **fare_rule_type** | **str**| The type of fare rule structure required | 
 **product_brand_offering_ids** | [**List[str]**](str.md)|  | [optional] 
 **product_ids** | [**List[str]**](str.md)|  | [optional] 
 **flight_ids** | [**List[str]**](str.md)|  | [optional] 
 **fare_rule_categories** | [**List[str]**](str.md)| Space separated list of fare rule categories required | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 

### Return type

[**FareRuleListResponseWrapper**](FareRuleListResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Successful Response - 200 |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rules_from_offer**
> FareRuleListResponseWrapper get_rules_from_offer(offer_identifier, fare_rule_type, product_ids=product_ids, flight_ids=flight_ids, fare_rule_categories=fare_rule_categories, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)

Return standalone fare rules with reference to an Offer

Fare rules are the conditions and restrictions that apply to any booking based on its fare type. These determine the price of the fare. Generally, less expensive fares have more restrictions and more expensive fares have fewer restrictions. Fare rules can include blackout dates, advanced reservation requirements, minimum and maximum stay requirements, and cancellation and change penalties.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.fare_rule_list_response_wrapper import FareRuleListResponseWrapper
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
    api_instance = openapi_client.FareRulesApi(api_client)
    offer_identifier = 'offer_identifier_example' # str | 
    fare_rule_type = 'fare_rule_type_example' # str | The type of fare rule structure required
    product_ids = ['product_ids_example'] # List[str] |  (optional)
    flight_ids = ['flight_ids_example'] # List[str] |  (optional)
    fare_rule_categories = ['fare_rule_categories_example'] # List[str] | Space separated list of fare rule categories required (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)

    try:
        # Return standalone fare rules with reference to an Offer
        api_response = api_instance.get_rules_from_offer(offer_identifier, fare_rule_type, product_ids=product_ids, flight_ids=flight_ids, fare_rule_categories=fare_rule_categories, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)
        print("The response of FareRulesApi->get_rules_from_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FareRulesApi->get_rules_from_offer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_identifier** | **str**|  | 
 **fare_rule_type** | **str**| The type of fare rule structure required | 
 **product_ids** | [**List[str]**](str.md)|  | [optional] 
 **flight_ids** | [**List[str]**](str.md)|  | [optional] 
 **fare_rule_categories** | [**List[str]**](str.md)| Space separated list of fare rule categories required | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 

### Return type

[**FareRuleListResponseWrapper**](FareRuleListResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Successful Response - 200 |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rules_from_reservation**
> FareRuleListResponseWrapper get_rules_from_reservation(reservation_identifier, offer_ids, fare_rule_type, product_ids=product_ids, flight_ids=flight_ids, fare_rule_categories=fare_rule_categories, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)

Return standalone fare rules with reference to a Reservation

Fare rules are the conditions and restrictions that apply to any booking based on its fare type. These determine the price of the fare. Generally, less expensive fares have more restrictions and more expensive fares have fewer restrictions. Fare rules can include blackout dates, advanced reservation requirements, minimum and maximum stay requirements, and cancellation and change penalties.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.fare_rule_list_response_wrapper import FareRuleListResponseWrapper
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
    api_instance = openapi_client.FareRulesApi(api_client)
    reservation_identifier = 'reservation_identifier_example' # str | 
    offer_ids = ['offer_ids_example'] # List[str] | 
    fare_rule_type = 'fare_rule_type_example' # str | The type of fare rule structure required
    product_ids = ['product_ids_example'] # List[str] |  (optional)
    flight_ids = ['flight_ids_example'] # List[str] |  (optional)
    fare_rule_categories = ['fare_rule_categories_example'] # List[str] | Space separated list of fare rule categories required (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)

    try:
        # Return standalone fare rules with reference to a Reservation
        api_response = api_instance.get_rules_from_reservation(reservation_identifier, offer_ids, fare_rule_type, product_ids=product_ids, flight_ids=flight_ids, fare_rule_categories=fare_rule_categories, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)
        print("The response of FareRulesApi->get_rules_from_reservation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FareRulesApi->get_rules_from_reservation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_identifier** | **str**|  | 
 **offer_ids** | [**List[str]**](str.md)|  | 
 **fare_rule_type** | **str**| The type of fare rule structure required | 
 **product_ids** | [**List[str]**](str.md)|  | [optional] 
 **flight_ids** | [**List[str]**](str.md)|  | [optional] 
 **fare_rule_categories** | [**List[str]**](str.md)| Space separated list of fare rule categories required | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 

### Return type

[**FareRuleListResponseWrapper**](FareRuleListResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Succesful Response - 200 |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rules_from_reservation_workbench**
> FareRuleListResponseWrapper get_rules_from_reservation_workbench(reservation_identifier, offer_ids, fare_rule_type, product_ids=product_ids, flight_ids=flight_ids, fare_rule_categories=fare_rule_categories, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)

Return standalone fare rules with reference to a Reservation workbench

Fare rules are the conditions and restrictions that apply to any booking based on its fare type. These determine the price of the fare. Generally, less expensive fares have more restrictions and more expensive fares have fewer restrictions. Fare rules can include blackout dates, advanced reservation requirements, minimum and maximum stay requirements, and cancellation and change penalties.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.fare_rule_list_response_wrapper import FareRuleListResponseWrapper
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
    api_instance = openapi_client.FareRulesApi(api_client)
    reservation_identifier = 'reservation_identifier_example' # str | 
    offer_ids = ['offer_ids_example'] # List[str] | 
    fare_rule_type = 'fare_rule_type_example' # str | The type of fare rule structure required
    product_ids = ['product_ids_example'] # List[str] |  (optional)
    flight_ids = ['flight_ids_example'] # List[str] |  (optional)
    fare_rule_categories = ['fare_rule_categories_example'] # List[str] | Space separated list of fare rule categories required (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)

    try:
        # Return standalone fare rules with reference to a Reservation workbench
        api_response = api_instance.get_rules_from_reservation_workbench(reservation_identifier, offer_ids, fare_rule_type, product_ids=product_ids, flight_ids=flight_ids, fare_rule_categories=fare_rule_categories, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)
        print("The response of FareRulesApi->get_rules_from_reservation_workbench:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FareRulesApi->get_rules_from_reservation_workbench: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_identifier** | **str**|  | 
 **offer_ids** | [**List[str]**](str.md)|  | 
 **fare_rule_type** | **str**| The type of fare rule structure required | 
 **product_ids** | [**List[str]**](str.md)|  | [optional] 
 **flight_ids** | [**List[str]**](str.md)|  | [optional] 
 **fare_rule_categories** | [**List[str]**](str.md)| Space separated list of fare rule categories required | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 

### Return type

[**FareRuleListResponseWrapper**](FareRuleListResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Successful Response - 200 |  -  |
**201** | Created - 201 |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

