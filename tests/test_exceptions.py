"""Tests for the exceptions module."""

from __future__ import annotations

from duco.exceptions import (
    DucoConnectionError,
    DucoError,
    DucoRateLimitError,
)


class TestExceptionHierarchy:
    """Test exception class hierarchy."""

    def test_base_exception(self):
        """DucoError is the base for all exceptions."""
        err = DucoError("test")
        assert isinstance(err, Exception)
        assert str(err) == "test"

    def test_connection_error_inherits(self):
        """DucoConnectionError inherits from DucoError."""
        err = DucoConnectionError("unreachable")
        assert isinstance(err, DucoError)

    def test_rate_limit_error_inherits(self):
        """DucoRateLimitError inherits from DucoError."""
        err = DucoRateLimitError(remaining=5)
        assert isinstance(err, DucoError)


class TestRateLimitError:
    """Test DucoRateLimitError specific behavior."""

    def test_with_remaining(self):
        """Rate limit error with remaining count."""
        err = DucoRateLimitError(remaining=10)
        assert err.remaining == 10
        assert "10" in str(err)

    def test_without_remaining(self):
        """Rate limit error without remaining count."""
        err = DucoRateLimitError()
        assert err.remaining is None
        assert "rate limit" in str(err).lower()

    def test_remaining_none_explicit(self):
        """Explicit None remaining is handled."""
        err = DucoRateLimitError(remaining=None)
        assert err.remaining is None
