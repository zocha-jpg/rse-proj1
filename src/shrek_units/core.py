import pint 

ureg = pint.UnitRegistry()
ureg.define('shrek = 2.43 * meter')

def to_shreks(length):
    """Convert a length to shreks."""
    return length.to('shrek')