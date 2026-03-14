"""BitBlock package for fixed-size bit manipulation.

This package provides the BitBlock class for working with fixed-size blocks
of bits, with support for bit-level operations and conversions.
"""

# Import the public class from its module
from .bitblock import BitBlock

# Define the public API
__all__ = ['BitBlock']

def __dir__():
    """Allow tab completion to show only public members."""
    return __all__