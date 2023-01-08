import pytest

from Applications.GUI_API_worked import GitRepoSigns


@pytest.fixture
def dummy_gui_api():
    return GitRepoSigns()
