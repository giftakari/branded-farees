# openapi_client.WorkbenchTravelerUpdatableItemsApi

All URIs are relative to *https://api.pp.travelport.com/11/air*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_from_traveler**](WorkbenchTravelerUpdatableItemsApi.md#build_from_traveler) | **POST** /book/updateableitem/reservationworkbench/{ReservationResource_Identifier}/travelerupdatableitems/buildfromtraveler | Retrieve updatable items by traveler


# **build_from_traveler**
> TravelerUpdatableItemsListResponseWrapper build_from_traveler(reservation_resource_identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, traveler_updatable_items_query_build_from_traveler=traveler_updatable_items_query_build_from_traveler)

Retrieve updatable items by traveler

The Updatable Items request retrieves by traveler ID a list of objects that are updatable for that traveler, and returns for each an indicator for whether that item can be added, modified, or deleted.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.traveler_updatable_items_list_response_wrapper import TravelerUpdatableItemsListResponseWrapper
from openapi_client.models.traveler_updatable_items_query_build_from_traveler import TravelerUpdatableItemsQueryBuildFromTraveler
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
    api_instance = openapi_client.WorkbenchTravelerUpdatableItemsApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    traveler_updatable_items_query_build_from_traveler = openapi_client.TravelerUpdatableItemsQueryBuildFromTraveler() # TravelerUpdatableItemsQueryBuildFromTraveler |  (optional)

    try:
        # Retrieve updatable items by traveler
        api_response = api_instance.build_from_traveler(reservation_resource_identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id, traveler_updatable_items_query_build_from_traveler=traveler_updatable_items_query_build_from_traveler)
        print("The response of WorkbenchTravelerUpdatableItemsApi->build_from_traveler:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkbenchTravelerUpdatableItemsApi->build_from_traveler: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **traveler_updatable_items_query_build_from_traveler** | [**TravelerUpdatableItemsQueryBuildFromTraveler**](TravelerUpdatableItemsQueryBuildFromTraveler.md)|  | [optional] 

### Return type

[**TravelerUpdatableItemsListResponseWrapper**](TravelerUpdatableItemsListResponseWrapper.md)

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

