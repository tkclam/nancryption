# nancryption

[![CI](https://github.com/tkclam/nancryption/actions/workflows/ci.yml/badge.svg)](https://github.com/tkclam/nancryption/actions/workflows/ci.yml)
[![PyPI version](https://img.shields.io/pypi/v/nancryption.svg)](https://pypi.org/project/nancryption/)
[![Python versions](https://img.shields.io/pypi/pyversions/nancryption.svg)](https://pypi.org/project/nancryption/)
[![License: MIT](https://img.shields.io/github/license/tkclam/nancryption)](https://github.com/tkclam/nancryption/blob/main/LICENSE)

nancryption encodes float32 values into float64 quiet-NaN bit patterns and
decodes them back again. This is useful when you need to smuggle a 32-bit
payload through a float64-only path while still tagging values as NaN.

## Install

```bash
uv sync
```

## Quick Start

```python
import numpy as np
from nancryption import nancrypt, nandecrypt

payload = np.array([1.0, -2.5, np.pi], dtype=np.float32)
encoded = nancrypt(payload)
decoded = nandecrypt(encoded)

print(encoded.dtype)  # float64
print(np.isnan(encoded).all()) # True
print(np.array_equal(decoded, payload)) # True
```

## API

- `nancrypt(a: np.ndarray) -> np.ndarray`
	Encodes float32 payload bits into float64 quiet NaN values.
- `nandecrypt(arr: np.ndarray) -> np.ndarray`
	Recovers the embedded float32 payload from encoded float64 values.

## Development

Run tests:

```bash
uv run pytest
```
