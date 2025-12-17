import pytest
import math
from unittest.mock import patch
from nist import bit_frequency_test, consecutive_bits_test, long_sequence_test


def test_bit_frequency_basic():
    sequence = "10101010"
    p_value = bit_frequency_test(sequence)
    assert math.isclose(p_value, 1.0, rel_tol=1e-5)


@pytest.mark.parametrize("invalid_input, error_type, match_msg", [
    (12345, TypeError, "Sequence must be string"),
    ("", ValueError, "Void string"),
    ("102abc", ValueError, "String must include only '0' and '1'"),
])
def test_bit_frequency_errors(invalid_input, error_type, match_msg):
    with pytest.raises(error_type, match=match_msg):
        bit_frequency_test(invalid_input)


@pytest.mark.parametrize("sequence", [
    "10101010",
    "11110000",
])
def test_consecutive_bits_logic(sequence):
    result = consecutive_bits_test(sequence)
    assert isinstance(result, float)
    assert 0.0 <= result <= 1.0


def test_consecutive_bits_short_sequence():
    with pytest.raises(ValueError, match="Sequence length must be at least 2 bits"):
        consecutive_bits_test("1")


def test_long_sequence_with_mock():
    sequence = "1100100111001001"
    probabilities = [0.2, 0.3, 0.3, 0.2]

    with patch('nist.gammainc') as mock_gamma:
        mock_gamma.return_value = 0.5
        result = long_sequence_test(sequence, probabilities, block_size=8)
        assert result == 0.5
        mock_gamma.assert_called_once()


def test_long_sequence_block_error():
    with pytest.raises(ValueError, match="Length must be a multiple of the block size"):
        long_sequence_test("101", [0.1] * 4, block_size=8)