"""Tests for the data_handler component"""
import pytest
import yahoo_finance

# NOTE: It seems like on certain versions an exception is raised
# but on others we just get no data back


@pytest.mark.xfail
def test_invalid_ticker():
    """Tests handling of invalid tickers"""
    from tradingsystem.data_handler import yf_downloader as yf
    res = yf.main('refhurwefhurwefhwe', '2006-02-12', '2016-02-12')
    assert len(res) > 0


@pytest.mark.xfail
def test_invalid_start_date():
    """Invalid start date, passing in as int"""
    res = yf.main('WMT', 2006, '2016-02-12')
    assert len(res) > 0


@pytest.mark.xfail
def test_invalid_end_date():
    """Invalid end date, passing in too large a month"""
    res = yf.main('WMT', '2006-02-12', '2016-32-12')
    assert len(res) > 0


@pytest.mark.xfail()
def test_invalid_date_order():
    # Start date comes after end date
    res = yf.main('WMT', '2016-02-12', '2016-02-12')
    assert len(res) > 0


def test_downloader():
    """Check if we can download data correctly"""
    from tradingsystem.data_handler import yf_downloader as yf
    # Valid case
    res = yf.main('WMT', '2006-02-12', '2016-02-12')
    assert len(res) > 0
