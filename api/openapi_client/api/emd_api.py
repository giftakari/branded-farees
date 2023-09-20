# coding: utf-8

"""
    Akaris Travels Air

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 11.10.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from datetime import date

from pydantic import Field, StrictStr, constr, validator

from typing import Optional

from openapi_client.models.emd_list_response_wrapper import EMDListResponseWrapper
from openapi_client.models.emd_query_update_emd import EMDQueryUpdateEMD

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class EMDApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def e_md_get_by_locator(self, locator : constr(strict=True, max_length=16), locator_type : Annotated[Optional[constr(strict=True, max_length=32)], Field(description="Specifies the type of reservation ID (e.g. reservation or cancellation).")] = None, source : Annotated[Optional[constr(strict=True, max_length=128)], Field(description="Specifies a unique identifier to indicate the source system which generated the resId.")] = None, source_context : Annotated[Optional[constr(strict=True, max_length=128)], Field(description="Specifies the context of the source.")] = None, ota_type : Annotated[Optional[constr(strict=True)], Field(description="Used for codes in the OpenTravel Code tables. Possible values of this pattern are 1, 101, 101.EQP, or 101.EQP.X.")] = None, creation_date : Annotated[Optional[date], Field(description="PNR creation Date")] = None, trace_id : Annotated[Optional[StrictStr], Field(description="Identifier used to correlate API invocations across long-running or multi-call business flows.")] = None, xauth_travelport_accessgroup : Annotated[Optional[StrictStr], Field(description="Identifies the Travelport access group with which the caller is associated")] = None, travelport_plus_session_id : Annotated[Optional[StrictStr], Field(description="Travelport Plus Session ID used to maintain an established agency session")] = None, **kwargs) -> EMDListResponseWrapper:  # noqa: E501
        """Retrieve EMD by locator  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.e_md_get_by_locator(locator, locator_type, source, source_context, ota_type, creation_date, trace_id, xauth_travelport_accessgroup, travelport_plus_session_id, async_req=True)
        >>> result = thread.get()

        :param locator: (required)
        :type locator: str
        :param locator_type: Specifies the type of reservation ID (e.g. reservation or cancellation).
        :type locator_type: str
        :param source: Specifies a unique identifier to indicate the source system which generated the resId.
        :type source: str
        :param source_context: Specifies the context of the source.
        :type source_context: str
        :param ota_type: Used for codes in the OpenTravel Code tables. Possible values of this pattern are 1, 101, 101.EQP, or 101.EQP.X.
        :type ota_type: str
        :param creation_date: PNR creation Date
        :type creation_date: date
        :param trace_id: Identifier used to correlate API invocations across long-running or multi-call business flows.
        :type trace_id: str
        :param xauth_travelport_accessgroup: Identifies the Travelport access group with which the caller is associated
        :type xauth_travelport_accessgroup: str
        :param travelport_plus_session_id: Travelport Plus Session ID used to maintain an established agency session
        :type travelport_plus_session_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: EMDListResponseWrapper
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the e_md_get_by_locator_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.e_md_get_by_locator_with_http_info(locator, locator_type, source, source_context, ota_type, creation_date, trace_id, xauth_travelport_accessgroup, travelport_plus_session_id, **kwargs)  # noqa: E501

    @validate_arguments
    def e_md_get_by_locator_with_http_info(self, locator : constr(strict=True, max_length=16), locator_type : Annotated[Optional[constr(strict=True, max_length=32)], Field(description="Specifies the type of reservation ID (e.g. reservation or cancellation).")] = None, source : Annotated[Optional[constr(strict=True, max_length=128)], Field(description="Specifies a unique identifier to indicate the source system which generated the resId.")] = None, source_context : Annotated[Optional[constr(strict=True, max_length=128)], Field(description="Specifies the context of the source.")] = None, ota_type : Annotated[Optional[constr(strict=True)], Field(description="Used for codes in the OpenTravel Code tables. Possible values of this pattern are 1, 101, 101.EQP, or 101.EQP.X.")] = None, creation_date : Annotated[Optional[date], Field(description="PNR creation Date")] = None, trace_id : Annotated[Optional[StrictStr], Field(description="Identifier used to correlate API invocations across long-running or multi-call business flows.")] = None, xauth_travelport_accessgroup : Annotated[Optional[StrictStr], Field(description="Identifies the Travelport access group with which the caller is associated")] = None, travelport_plus_session_id : Annotated[Optional[StrictStr], Field(description="Travelport Plus Session ID used to maintain an established agency session")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve EMD by locator  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.e_md_get_by_locator_with_http_info(locator, locator_type, source, source_context, ota_type, creation_date, trace_id, xauth_travelport_accessgroup, travelport_plus_session_id, async_req=True)
        >>> result = thread.get()

        :param locator: (required)
        :type locator: str
        :param locator_type: Specifies the type of reservation ID (e.g. reservation or cancellation).
        :type locator_type: str
        :param source: Specifies a unique identifier to indicate the source system which generated the resId.
        :type source: str
        :param source_context: Specifies the context of the source.
        :type source_context: str
        :param ota_type: Used for codes in the OpenTravel Code tables. Possible values of this pattern are 1, 101, 101.EQP, or 101.EQP.X.
        :type ota_type: str
        :param creation_date: PNR creation Date
        :type creation_date: date
        :param trace_id: Identifier used to correlate API invocations across long-running or multi-call business flows.
        :type trace_id: str
        :param xauth_travelport_accessgroup: Identifies the Travelport access group with which the caller is associated
        :type xauth_travelport_accessgroup: str
        :param travelport_plus_session_id: Travelport Plus Session ID used to maintain an established agency session
        :type travelport_plus_session_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(EMDListResponseWrapper, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'locator',
            'locator_type',
            'source',
            'source_context',
            'ota_type',
            'creation_date',
            'trace_id',
            'xauth_travelport_accessgroup',
            'travelport_plus_session_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method e_md_get_by_locator" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('locator') is not None:  # noqa: E501
            _query_params.append(('Locator', _params['locator']))

        if _params.get('locator_type') is not None:  # noqa: E501
            _query_params.append(('locatorType', _params['locator_type']))

        if _params.get('source') is not None:  # noqa: E501
            _query_params.append(('source', _params['source']))

        if _params.get('source_context') is not None:  # noqa: E501
            _query_params.append(('sourceContext', _params['source_context']))

        if _params.get('ota_type') is not None:  # noqa: E501
            _query_params.append(('otaType', _params['ota_type']))

        if _params.get('creation_date') is not None:  # noqa: E501
            if isinstance(_params['creation_date'], date):
                _query_params.append(('creationDate', _params['creation_date'].strftime(self.api_client.configuration.date_format)))
            else:
                _query_params.append(('creationDate', _params['creation_date']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['trace_id']:
            _header_params['TraceId'] = _params['trace_id']

        if _params['xauth_travelport_accessgroup']:
            _header_params['XAUTH_TRAVELPORT_ACCESSGROUP'] = _params['xauth_travelport_accessgroup']

        if _params['travelport_plus_session_id']:
            _header_params['TravelportPlusSessionID'] = _params['travelport_plus_session_id']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {
            '200': "EMDListResponseWrapper",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '402': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
        }

        return self.api_client.call_api(
            '/emds/getbylocator', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_emd(self, identifier : constr(strict=True, max_length=128), trace_id : Annotated[Optional[StrictStr], Field(description="Identifier used to correlate API invocations across long-running or multi-call business flows.")] = None, xauth_travelport_accessgroup : Annotated[Optional[StrictStr], Field(description="Identifies the Travelport access group with which the caller is associated")] = None, travelport_plus_session_id : Annotated[Optional[StrictStr], Field(description="Travelport Plus Session ID used to maintain an established agency session")] = None, **kwargs) -> EMDListResponseWrapper:  # noqa: E501
        """Retrieve an EMD  # noqa: E501

        Display an EMD to retrieve EMD details such as the amount paid and agency ticketing information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_emd(identifier, trace_id, xauth_travelport_accessgroup, travelport_plus_session_id, async_req=True)
        >>> result = thread.get()

        :param identifier: (required)
        :type identifier: str
        :param trace_id: Identifier used to correlate API invocations across long-running or multi-call business flows.
        :type trace_id: str
        :param xauth_travelport_accessgroup: Identifies the Travelport access group with which the caller is associated
        :type xauth_travelport_accessgroup: str
        :param travelport_plus_session_id: Travelport Plus Session ID used to maintain an established agency session
        :type travelport_plus_session_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: EMDListResponseWrapper
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_emd_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_emd_with_http_info(identifier, trace_id, xauth_travelport_accessgroup, travelport_plus_session_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_emd_with_http_info(self, identifier : constr(strict=True, max_length=128), trace_id : Annotated[Optional[StrictStr], Field(description="Identifier used to correlate API invocations across long-running or multi-call business flows.")] = None, xauth_travelport_accessgroup : Annotated[Optional[StrictStr], Field(description="Identifies the Travelport access group with which the caller is associated")] = None, travelport_plus_session_id : Annotated[Optional[StrictStr], Field(description="Travelport Plus Session ID used to maintain an established agency session")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Retrieve an EMD  # noqa: E501

        Display an EMD to retrieve EMD details such as the amount paid and agency ticketing information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_emd_with_http_info(identifier, trace_id, xauth_travelport_accessgroup, travelport_plus_session_id, async_req=True)
        >>> result = thread.get()

        :param identifier: (required)
        :type identifier: str
        :param trace_id: Identifier used to correlate API invocations across long-running or multi-call business flows.
        :type trace_id: str
        :param xauth_travelport_accessgroup: Identifies the Travelport access group with which the caller is associated
        :type xauth_travelport_accessgroup: str
        :param travelport_plus_session_id: Travelport Plus Session ID used to maintain an established agency session
        :type travelport_plus_session_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(EMDListResponseWrapper, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'identifier',
            'trace_id',
            'xauth_travelport_accessgroup',
            'travelport_plus_session_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_emd" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['identifier']:
            _path_params['Identifier'] = _params['identifier']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['trace_id']:
            _header_params['TraceId'] = _params['trace_id']

        if _params['xauth_travelport_accessgroup']:
            _header_params['XAUTH_TRAVELPORT_ACCESSGROUP'] = _params['xauth_travelport_accessgroup']

        if _params['travelport_plus_session_id']:
            _header_params['TravelportPlusSessionID'] = _params['travelport_plus_session_id']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {
            '200': "EMDListResponseWrapper",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '402': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
        }

        return self.api_client.call_api(
            '/emds/{Identifier}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def update_emd(self, identifier : constr(strict=True, max_length=128), emd_query_update_emd : EMDQueryUpdateEMD, trace_id : Annotated[Optional[StrictStr], Field(description="Identifier used to correlate API invocations across long-running or multi-call business flows.")] = None, xauth_travelport_accessgroup : Annotated[Optional[StrictStr], Field(description="Identifies the Travelport access group with which the caller is associated")] = None, travelport_plus_session_id : Annotated[Optional[StrictStr], Field(description="Travelport Plus Session ID used to maintain an established agency session")] = None, **kwargs) -> EMDListResponseWrapper:  # noqa: E501
        """Void an EMD  # noqa: E501

        Void an EMD to cancel it. You can also use EMD void with GDS Exchange Ticketing API to refund an EMD back to the FOP.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_emd(identifier, emd_query_update_emd, trace_id, xauth_travelport_accessgroup, travelport_plus_session_id, async_req=True)
        >>> result = thread.get()

        :param identifier: (required)
        :type identifier: str
        :param emd_query_update_emd: (required)
        :type emd_query_update_emd: EMDQueryUpdateEMD
        :param trace_id: Identifier used to correlate API invocations across long-running or multi-call business flows.
        :type trace_id: str
        :param xauth_travelport_accessgroup: Identifies the Travelport access group with which the caller is associated
        :type xauth_travelport_accessgroup: str
        :param travelport_plus_session_id: Travelport Plus Session ID used to maintain an established agency session
        :type travelport_plus_session_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: EMDListResponseWrapper
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_emd_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_emd_with_http_info(identifier, emd_query_update_emd, trace_id, xauth_travelport_accessgroup, travelport_plus_session_id, **kwargs)  # noqa: E501

    @validate_arguments
    def update_emd_with_http_info(self, identifier : constr(strict=True, max_length=128), emd_query_update_emd : EMDQueryUpdateEMD, trace_id : Annotated[Optional[StrictStr], Field(description="Identifier used to correlate API invocations across long-running or multi-call business flows.")] = None, xauth_travelport_accessgroup : Annotated[Optional[StrictStr], Field(description="Identifies the Travelport access group with which the caller is associated")] = None, travelport_plus_session_id : Annotated[Optional[StrictStr], Field(description="Travelport Plus Session ID used to maintain an established agency session")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Void an EMD  # noqa: E501

        Void an EMD to cancel it. You can also use EMD void with GDS Exchange Ticketing API to refund an EMD back to the FOP.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_emd_with_http_info(identifier, emd_query_update_emd, trace_id, xauth_travelport_accessgroup, travelport_plus_session_id, async_req=True)
        >>> result = thread.get()

        :param identifier: (required)
        :type identifier: str
        :param emd_query_update_emd: (required)
        :type emd_query_update_emd: EMDQueryUpdateEMD
        :param trace_id: Identifier used to correlate API invocations across long-running or multi-call business flows.
        :type trace_id: str
        :param xauth_travelport_accessgroup: Identifies the Travelport access group with which the caller is associated
        :type xauth_travelport_accessgroup: str
        :param travelport_plus_session_id: Travelport Plus Session ID used to maintain an established agency session
        :type travelport_plus_session_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(EMDListResponseWrapper, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'identifier',
            'emd_query_update_emd',
            'trace_id',
            'xauth_travelport_accessgroup',
            'travelport_plus_session_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_emd" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['identifier']:
            _path_params['Identifier'] = _params['identifier']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['trace_id']:
            _header_params['TraceId'] = _params['trace_id']

        if _params['xauth_travelport_accessgroup']:
            _header_params['XAUTH_TRAVELPORT_ACCESSGROUP'] = _params['xauth_travelport_accessgroup']

        if _params['travelport_plus_session_id']:
            _header_params['TravelportPlusSessionID'] = _params['travelport_plus_session_id']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['emd_query_update_emd'] is not None:
            _body_params = _params['emd_query_update_emd']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {
            '200': "EMDListResponseWrapper",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '402': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
        }

        return self.api_client.call_api(
            '/emds/{Identifier}', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
