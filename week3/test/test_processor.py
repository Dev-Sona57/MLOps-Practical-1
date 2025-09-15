import pytest
from processor import DataProcessor
import math

def test_mean_basic():
    p = DataProcessor([1, 2, 3, 4, 5])
    assert p.mean() == 3.0

def test_variance_basic():
    p = DataProcessor([1, 2, 3, 4, 5])
    assert math.isclose(p.variance(), 2.0, rel_tol=1e-9)

def test_empty_data():
    p = DataProcessor([])
    with pytest.raises(ValueError):
        p.mean()

def test_single_value():
    p = DataProcessor([42])
    assert p.mean() == 42
    assert p.variance() == 0.0

