import asyncio
import time


def test_get_api_status_code(dummy_gui_api):
    assert dummy_gui_api.get_api().status_code == 200

def test_get_api_response(dummy_gui_api):
    assert type(dummy_gui_api.get_api().json()[0]) is dict

def test_get_api_check_if_user_in_github(dummy_gui_api):
    if dummy_gui_api.get_api() != None:
        return True
    else:
        raise ValueError('User not in Github')

def test_performance_get_api(dummy_gui_api):
    start_time = time.time()
    asyncio.run(dummy_gui_api.get_api_async_way())
    end_time = time.time()
    assert end_time - start_time < 1
# @mock.patch('Github_API.Application.GUI_API_worked.requests.get')
# def test_get_api_response_some(mock_requests_get):
#     mock_requests_get.return_value = mock.Mock(**{'status_code': 200, 'json.return_value': {'name': 'Api_Github'}})
#     assert GitRepoSigns().get_api().status_code == 200


