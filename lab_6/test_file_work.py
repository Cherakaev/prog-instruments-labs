import pytest
import json
from unittest.mock import patch, mock_open
from file_work import read_json, read_txt, write_results


def test_read_json_success():
    valid_data = {
        "cpp_file": "main.cpp",
        "java_file": "Main.java",
        "probabilities": [0.1, 0.2, 0.3]
    }
    with patch("builtins.open", mock_open(read_data=json.dumps(valid_data))):
        cpp, java, probs = read_json("config.json")
        assert cpp == "main.cpp"
        assert probs == [0.1, 0.2, 0.3]


def test_read_json_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError, match="JSON file not found"):
            read_json("missing.json")


def test_read_json_invalid_format():
    with patch("builtins.open", mock_open(read_data="{bad_json")):
        with pytest.raises(ValueError, match="Invalid JSON format"):
            read_json("bad.json")


@pytest.mark.parametrize("missing_data", [
    {"java_file": "J", "probabilities": []},
    {"cpp_file": "C", "java_file": "J"}
])
def test_read_json_missing_keys(missing_data):
    with patch("builtins.open", mock_open(read_data=json.dumps(missing_data))):
        with pytest.raises(KeyError, match="Missing required key"):
            read_json("config.json")


def test_read_txt_success():
    with patch("builtins.open", mock_open(read_data="  hello  ")):
        assert read_txt("data.txt") == "hello"


def test_write_results_content():
    m = mock_open()
    with patch("builtins.open", m):
        write_results(0.5, 0.6, 0.1, 0.2, 0.9, 0.8, "out.txt")

    m.assert_called_once_with("out.txt", 'w', encoding='utf-8')
    handle = m()
    handle.write.assert_called()
    args, _ = handle.write.call_args
    assert "C++: 0.500000" in args[0]


def test_write_results_permission_error(capsys):
    with patch("builtins.open", side_effect=PermissionError):
        write_results(0, 0, 0, 0, 0, 0, "readonly.txt")
        captured = capsys.readouterr()
        assert "Error: acces denied" in captured.out