import asyncio
import time
from Applications import git_acc_data

def test_get_api_response_and_entry_compatibility(dummy_gui_api):
    dummy_gui_api.en_user_git['text'] = 'Trickest'
    assert 'trickest' in asyncio.run(dummy_gui_api.get_api_async_way(dummy_gui_api.en_user_git['text']))[0].keys()

def test_user_not_in_github_single_search(dummy_gui_api):
    dummy_gui_api.en_user_git['text'] = 'daads213fasv'
    dummy_gui_api.send_request_and_store_data(dummy_gui_api.en_user_git['text'])
    assert dummy_gui_api.user_not_found['text'] == 'User is not in Github'

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

def test_user_username_and_token(dummy_gui_api):
    assert dummy_gui_api.auth_user == git_acc_data.username
    assert dummy_gui_api.auth_token == git_acc_data.user_token





