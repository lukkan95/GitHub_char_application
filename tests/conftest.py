import pytest

from Applications.GUI_API_multisearching import GitRepoSigns


@pytest.fixture
def dummy_gui_api():
    return GitRepoSigns()
