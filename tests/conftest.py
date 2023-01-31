import pytest

from Applications.GUI_API_multisearching import GitRepoSigns

from Applications import git_token_crypt


@pytest.fixture
def dummy_gui_api():
    user = GitRepoSigns()
    user.auth_user = git_token_crypt.username
    user.auth_token = git_token_crypt.user_token
    return user
