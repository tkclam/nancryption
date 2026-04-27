"""Encode float32 payloads into float64 quiet NaN values and decode them."""

import numpy as np

QUIET_NAN_MASK = np.uint64(0x7FF8_0000_0000_0000)

__all__ = ["nancrypt", "nandecrypt"]


def nancrypt(a: np.ndarray) -> np.ndarray:
    """Pack float32 payload bits into quiet NaN float64 values."""
    return (QUIET_NAN_MASK | np.astype(a, np.float32, copy=False).view(np.uint32)).view(np.float64)


def nandecrypt(arr: np.ndarray) -> np.ndarray:
    """Recover the embedded float32 payload from encoded float64 values."""
    if arr.dtype != np.float64:
        raise TypeError("Input must be a float64 array")
    return arr.view(np.uint64).astype(np.uint32).view(np.float32)
