from src.instantiate_csv_error import InstantiateCSVError

import pytest

def test_instantiate_csv_error():
    with pytest.raises(InstantiateCSVError):
        raise InstantiateCSVError