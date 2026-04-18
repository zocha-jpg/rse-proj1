import pytest
import pint
from shrek_units import to_shreks, ureg

def test_one_meter_is_correct_shreks():
    result = to_shreks(1 * ureg.meter).magnitude
    assert result == pytest.approx(1 / 2.43)

def test_mass_rejected_by_to_shreks():
    with pytest.raises(pint.DimensionalityError):
        to_shreks(5 * ureg.kilogram)