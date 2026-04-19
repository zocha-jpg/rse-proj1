import pint 

ureg = pint.UnitRegistry()
ureg.define('shrek = 2.43 * meter')

def to_shreks(length):
    """Convert a length quantity to shreks.

    Parameters
    ----------
    length : pint.Quantity
        A quantity with length dimensionality.

    Returns
    -------
    pint.Quantity
        The same length expressed in shreks.

    Raises
    ------
    pint.DimensionalityError
        If ``length`` is not a length quantity.
    """
    return length.to("shrek")