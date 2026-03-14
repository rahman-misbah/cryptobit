"""Type definitions for the BitBlock module."""
from __future__ import annotations
from typing import TypeIs, Union, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .bitblock import BitBlock

type Data = Union[int, BitBlock]
type RawData = Union[Data, bytes]

def is_valid_raw_data(data: Optional[RawData], block_size: Optional[int]) -> TypeIs[RawData]:
    """Check if the input data is valid for the given block size.
    
    Args:
        data: The input data to check (can be an integer or bytes).
        block_size: The size of the block in bits.
    
    Returns:
        True if the data is valid, False otherwise.
    """
    if data is None:
        return True  # Allow None for default initialization
    
    if isinstance(data, int):
        return True
    if isinstance(data, bytes) and len(data) <= block_size // 8:
        return True
    
    # Checking for BitBlock
    if block_size is None:
        raise TypeError("Block size must be specified when validating BitBlock data.")
    
    # Late import to avoid circular dependency
    from .bitblock import BitBlock

    if isinstance(data, BitBlock) and data.block_size == block_size:
        return True
    return False

def is_valid_data(data: Data) -> TypeIs[Data]:
    """Check if the input data is valid (can be an integer or a BitBlock instance).
    
    Args:
        data: The input data to check (can be an integer or a BitBlock instance).
    
    Returns:
        True if the data is valid, False otherwise.
    """
    # Late import to avoid circular dependency
    from .bitblock import BitBlock

    return isinstance(data, (int, BitBlock))