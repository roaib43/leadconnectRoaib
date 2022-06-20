import pytest
import json

@pytest.fixture
def ui_locators():
    with open('../config/locators.json', 'r') as json_data_file:
        locators_data_json = json_data_file.read()
    locators_data = json.loads(locators_data_json)
    return locators_data