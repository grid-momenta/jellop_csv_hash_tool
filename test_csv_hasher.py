import pytest, sys
import csv_hasher as SUT
from unittest.mock import patch


class TestHashCsv:
    def test_hash_csv(s):
        # slow test
        assert SUT.hash_csv("./test_data/CSV-1-short.csv", "sha1")

    def test_it_fails_with_no_path(s):
        with pytest.raises(Exception):
            assert SUT.hash_csv("", "sha1")

    def test_main_error_on_invalit_file(s, capsys, monkeypatch):
        monkeypatch.setattr("sys.argv", ["me", "x", "sha1"])
        assert SUT.main() == 1
        captured = capsys.readouterr()
        assert "Bad CSV path" in captured.out

    def test_main_error_on_invalid_hash(s, capsys):
        with patch.object(sys, "argv", ["me", "./test_data/CSV-1-short.csv", "blah"]):
            assert SUT.main() == 1
            captured = capsys.readouterr()
            assert "Bad hash type" in captured.out

    def test_main_prints_location_to_saved_file(s, capsys, monkeypatch):
        monkeypatch.setattr("sys.argv", ["me", "./test_data/CSV-1-short.csv", "sha1"])

        SUT.main()
        captured = capsys.readouterr()
        assert "File saved to: " in captured.out
