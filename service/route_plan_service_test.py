import unittest
from service.route_plan_service import *
from service.auth_service import DtoLoginUser, users_login
from service.test_utils import BASE_URL, headers
from faker import Faker
from datetime import datetime

fake = Faker()


class TestRoutePlanService(unittest.TestCase):
    def setUp(self):
        self.client = requests.Session()
        self.host = BASE_URL
        basic_auth_dto = DtoLoginUser(username='fdse_microservice',
                                      password='111111', verificationCode="123")
        token = users_login(self.client, basic_auth_dto, headers, BASE_URL)
        self.headers = {'Authorization': f'Bearer {token}'}

    def tearDown(self):
        self.client.close()

    def test_routeplan_welcome(self):
        response = routeplan_welcome(self.client, self.host)
        self.assertIsInstance(response, str)

    def test_get_cheapest_routes(self):
        info = RoutePlanInfo(startStation="shanghai",
                             endStation="taiyuan",
                             travelDate="5/31/2024",
                             num=777)
        response = get_cheapest_routes(self.client, info, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_get_quickest_routes(self):
        info = RoutePlanInfo(startStation="shanghai",
                             endStation="taiyuan",
                             travelDate="5/31/2024",
                             num=666)
        response = get_quickest_routes(self.client, info, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_get_min_stop_stations(self):
        info = RoutePlanInfo(startStation="shanghai",
                             endStation="taiyuan",
                             travelDate="5/31/2024",
                             num=666)
        response = get_min_stop_stations(self.client, info, self.host, self.headers)
        self.assertIsInstance(response, dict)

    def test_end2end(self):
        info = RoutePlanInfo(startStation="shanghai",
                             endStation="taiyuan",
                             travelDate="5/31/2024",
                             num=444)

        cheapest_routes = get_cheapest_routes(self.client, info, self.host, self.headers)
        self.assertIsInstance(cheapest_routes, dict)
        print("Cheapest Routes:", cheapest_routes)

        quickest_routes = get_quickest_routes(self.client, info, self.host, self.headers)
        self.assertIsInstance(quickest_routes, dict)
        print("Quickest Routes:", quickest_routes)

        min_stop_stations = get_min_stop_stations(self.client, info, self.host, self.headers)
        self.assertIsInstance(min_stop_stations, dict)
        print("Min Stop Stations:", min_stop_stations)


if __name__ == '__main__':
    unittest.main()