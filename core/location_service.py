from repositories.location_repository import LocationRepository
from models.location import Location
from core.utils import generate_id

class LocationService:
    def __init__(self):
        self.repo = LocationRepository()

    def create_location(self, warehouse, rack, aisle, bin_code):
        location = Location(
            id=generate_id("loc"),
            warehouse=warehouse,
            rack=rack,
            aisle=aisle,
            bin_code=bin_code
        )
        self.repo.insert(location)

    def list_locations(self):
        return self.repo.load_all()

    def get_by_id(self, loc_id):
        return self.repo.find_by_id(loc_id)