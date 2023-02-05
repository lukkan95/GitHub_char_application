import pytest

from Applications.GUI_API_multisearching import GitRepoSigns

from Applications import git_acc_data


@pytest.fixture
def dummy_gui_api():
    user = GitRepoSigns()
    user.auth_user = git_acc_data.username
    user.auth_token = git_acc_data.user_token
    return user
