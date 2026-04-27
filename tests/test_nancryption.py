import numpy as np
import pytest

from nancryption import nancrypt, nandecrypt


def test_roundtrip_preserves_float32_bits() -> None:
    payload = np.array([0.0, -0.0, 1.5, -2.25, np.pi], dtype=np.float32)

    encoded = nancrypt(payload)
    decoded = nandecrypt(encoded)

    assert encoded.dtype == np.float64
    assert np.isnan(encoded).all()
    assert np.array_equal(decoded.view(np.uint32), payload.view(np.uint32))


def test_nandecrypt_requires_float64_input() -> None:
    bad_input = np.array([1.0, 2.0], dtype=np.float32)

    with pytest.raises(TypeError, match="float64"):
        nandecrypt(bad_input)
