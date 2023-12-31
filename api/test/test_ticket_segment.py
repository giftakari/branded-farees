# coding: utf-8

"""
    Akaris Travels Air

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 11.10.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import openapi_client
from openapi_client.models.ticket_segment import TicketSegment  # noqa: E501
from openapi_client.rest import ApiException

class TestTicketSegment(unittest.TestCase):
    """TicketSegment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TicketSegment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TicketSegment`
        """
        model = openapi_client.models.ticket_segment.TicketSegment()  # noqa: E501
        if include_optional :
            return TicketSegment(
                type = 'TicketSegment', 
                sequence = 56, 
                class_of_service = 'Cu0', 
                fare_basis_code = 'if you buy a super expensive business class ticket, it may have the fare code J', 
                status = 'CheckedIn', 
                carrier = 'DAL', 
                number = 'BA2490', 
                departure = openapi_client.models.departure.Departure(
                    @type = 'DepartureDetail', 
                    location = 'Texas', 
                    date = 'Tue Oct 13 10:00:00 AEST 11', 
                    time = '04:45 PM', ), 
                arrival = openapi_client.models.arrival.Arrival(
                    @type = 'ArrivalDetail', 
                    location = 'Texas', 
                    date = 'Tue Oct 13 10:00:00 AEST 11', 
                    time = '04:45 PM', ), 
                flight_status_code = 'AF  AA Advantage ticket', 
                valid_date_range = openapi_client.models.date_range.DateRange(
                    start = 'Fri Mar 03 11:00:00 AEDT 2023', 
                    end = 'Fri Mar 03 11:00:00 AEDT 2023', ), 
                ticket_baggage = openapi_client.models.ticket_baggage.TicketBaggage(
                    @type = 'TicketBaggage', 
                    quantity = 2, 
                    measurement = Small checked suitcases usually are 23-24 inches on the longest size, medium ones 25-27 inches, and large ones in 28-32 inches, ), 
                connection_ind = True
            )
        else :
            return TicketSegment(
                carrier = 'DAL',
                number = 'BA2490',
                departure = openapi_client.models.departure.Departure(
                    @type = 'DepartureDetail', 
                    location = 'Texas', 
                    date = 'Tue Oct 13 10:00:00 AEST 11', 
                    time = '04:45 PM', ),
                arrival = openapi_client.models.arrival.Arrival(
                    @type = 'ArrivalDetail', 
                    location = 'Texas', 
                    date = 'Tue Oct 13 10:00:00 AEST 11', 
                    time = '04:45 PM', ),
                flight_status_code = 'AF  AA Advantage ticket',
                valid_date_range = openapi_client.models.date_range.DateRange(
                    start = 'Fri Mar 03 11:00:00 AEDT 2023', 
                    end = 'Fri Mar 03 11:00:00 AEDT 2023', ),
                ticket_baggage = openapi_client.models.ticket_baggage.TicketBaggage(
                    @type = 'TicketBaggage', 
                    quantity = 2, 
                    measurement = Small checked suitcases usually are 23-24 inches on the longest size, medium ones 25-27 inches, and large ones in 28-32 inches, ),
        )
        """

    def testTicketSegment(self):
        """Test TicketSegment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
