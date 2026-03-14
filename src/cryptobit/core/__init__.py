"""cryptobit.core

Core components of the cryptobit library.
"""

from .bitblock import BitBlock

# Define the public API
__all__ = ['BitBlock']

def __dir__():
    """Allow tab completion to show only public members."""
    return __all__