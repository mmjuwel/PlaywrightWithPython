import pytest
from pages.homePage import HomePage
from pages.tripPage import TripPage
from utils.test_data_loader import  get_trip_test_data
import allure

TRIP_DATA = get_trip_test_data()
TEST_IDS = [data["test_id"] for data in TRIP_DATA]

class TestTrip:
   
    @pytest.mark.parametrize("trip_data", TRIP_DATA, ids=TEST_IDS)
    @allure.title("Trip Test")
    @allure.description("Test trip search by device ID and other functionalities")
    @allure.severity(allure.severity_level.NORMAL)

    def test_trip_functionality(self, authenticated_page, trip_data):
        
        home_page = HomePage(authenticated_page)
        trip_page = TripPage(authenticated_page)
        completed_trip = trip_data["number_of_completed_trips"]
        inprogress_trip = trip_data["number_of_inprogress_trips"]
        unidentified_trip = trip_data["number_of_unidentified_trips"]
        
        with allure.step("Navigate to the trip page via menu"):
            home_page.click_trip_menu()
            authenticated_page.wait_for_load_state("networkidle")

        with allure.step(f"Search for trips using device ID: {trip_data['device_id']}"):
            trip_page.search_by_device_id(trip_data["device_id"])
            authenticated_page.wait_for_load_state("networkidle")
            authenticated_page.wait_for_load_state("domcontentloaded")

        with allure.step("Verify the number of completed trips"):
            actual_completed_trip = trip_page.get_completed_trip_count()
            assert actual_completed_trip == int(completed_trip), f"Expected {completed_trip} completed trips, got {actual_completed_trip}"

        with allure.step("Verify the number of in-progress trips"):
            actual_inprogress_trip = trip_page.get_inprogress_trip_count()
            assert actual_inprogress_trip == int(inprogress_trip), f"Expected {inprogress_trip} in-progress trips, got {actual_inprogress_trip}"

        with allure.step("Verify the number of unidentified trips"):
            actual_unidentified_trip = trip_page.get_unidentified_trip_count()
            assert actual_unidentified_trip == int(unidentified_trip), f"Expected {unidentified_trip} unidentified trips, got {actual_unidentified_trip}"

        