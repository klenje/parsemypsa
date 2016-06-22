#!/usr/bin/env python

import logging
import sys
import pytest

from parsemypsa import main


def test_argparse():
    # Clear args
    sys.argv.clear()
    # First is program name
    sys.argv.append("parseMyPSA")
    # Then positional arguments
    sys.argv.append("aa.trip")
    args = main.option_parser()
    assert args.input_file == "aa.trip"

def test_setup_logging():
    # Clear args
    sys.argv.clear()
    # First is program name
    sys.argv.append("parseMyPSA")
    # Then positional arguments
    sys.argv.append("aa.trip")
    # Then optional argiments
    sys.argv.append("--log-level=DEBUG")
    args = main.option_parser()
    assert args.log_level == "DEBUG"
    main.setup_logging(args)
    assert logging.getLogger().isEnabledFor(logging.DEBUG)


def test_setup_logging_invalid_value():
    # Clear args
    sys.argv.clear()
    # First is program name
    sys.argv.append("parseMyPSA")
    # Then positional arguments
    sys.argv.append("aa.trip")
    # Then optional argiments
    sys.argv.append("--log-level=DUMMY")
    args = main.option_parser()
    assert args.log_level == "DUMMY"
    with pytest.raises(ValueError):
        main.setup_logging(args)
        assert not logging.getLogger().isEnabledFor(logging.DEBUG)


def test_version():
    # Clear args
    sys.argv.clear()
    # First is program name
    sys.argv.append("parseMyPSA")
    sys.argv.append("--version")
    with pytest.raises(SystemExit) as excinfo:
        main.main()
        assert excinfo.code == 0
