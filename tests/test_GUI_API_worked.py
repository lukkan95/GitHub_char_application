import asyncio
import time


def test_get_api_status_code(dummy_gui_api):
    dummy_gui_api.en_user_git['text'] = 'Trickest'
    assert 'trickest' in asyncio.run(dummy_gui_api.get_api_async_way(dummy_gui_api.en_user_git['text']))[0].keys()

def test_get_api_async_way_if_user_in_github(dummy_gui_api):
    assert len(dummy_gui_api.send_request_and_store_data('Trickest')) == 1

def test_get_api_async_way_if_user_not_in_github(dummy_gui_api):
    assert dummy_gui_api.send_request_and_store_data('daads213fasv') is None
    assert dummy_gui_api.user_not_found['text'] == 'User is not in Github'

def test_performance_get_api(dummy_gui_api):
    users_string = 'Trickest,OverCookedAgain,lukkan95,AzeemIdrisi,LocalSend,fathyb,z4nzu,lencx,hwchase17,dwelle,' \
                  'ad1992,' \
                 'lipis,cclauss,0mp,PragmaTwice,sasumner,SinghRajenM,ea-rus,ZoranPandovski,George3d6'
    start_time = time.time()
    dummy_gui_api.send_request_and_store_data(users_string)
    end_time = time.time()
    time_length = end_time - start_time
    print(f' Time taken to make 20 requests: {time_length} sec.')
    assert time_length < 1
# @mock.patch('Github_API.Application.GUI_API_worked.requests.get')
# def test_get_api_response_some(mock_requests_get):
#     mock_requests_get.return_value = mock.Mock(**{'status_code': 200, 'json.return_value': {'name': 'Api_Github'}})
#     assert GitRepoSigns().get_api().status_code == 200


