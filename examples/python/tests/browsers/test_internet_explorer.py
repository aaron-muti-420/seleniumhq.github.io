import os
import subprocess
import sys

import pytest
from selenium import webdriver


@pytest.mark.skipif(sys.platform != "win32", reason="requires Windows")
def test_basic_options_win10(edge_bin):
    options = webdriver.IeOptions()
    options.attach_to_edge_chrome = True
    options.edge_executable_path = edge_bin
    driver = webdriver.Ie(options=options)

    driver.quit()


@pytest.mark.skipif(sys.platform != "win32", reason="requires Windows")
def test_basic_options_win11():
    options = webdriver.IeOptions()
    driver = webdriver.Ie(options=options)

    driver.quit()

@pytest.mark.skipif(sys.platform != "win32", reason="requires Windows")
def test_file_upload_timeout():
    options = webdriver.IeOptions()
    options.file_upload_timeout = 2000

    driver = webdriver.Ie(options=options)

    driver.quit()


@pytest.mark.skipif(sys.platform != "win32", reason="requires Windows")
def test_ensure_clean_session():
    options = webdriver.IeOptions()
    options.ensure_clean_session = True

    driver = webdriver.Ie(options=options)

    driver.quit()


@pytest.mark.skipif(sys.platform != "win32", reason="requires Windows")
def test_ignore_zoom_level():
    options = webdriver.IeOptions()
    options.ignore_zoom_level = True

    driver = webdriver.Ie(options=options)

    driver.quit()


@pytest.mark.skipif(sys.platform != "win32", reason="requires Windows")
def test_ignore_protected_mode_settings():
    options = webdriver.IeOptions()
    options.ignore_protected_mode_settings = True

    driver = webdriver.Ie(options=options)

    driver.quit()


@pytest.mark.skipif(sys.platform != "win32", reason="requires Windows")
def test_silent():
    service = webdriver.IeService(service_args=["--silent"])
    driver = webdriver.Ie(service=service)

    driver.quit()


@pytest.mark.skipif(sys.platform != "win32", reason="requires Windows")
def test_cmd_options():
    options = webdriver.IeOptions()
    options.add_argument("-private")

    driver = webdriver.Ie(options=options)

    driver.quit()

# Skipping this as it fails on Windows because the value of registry setting in 
# HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\Main\TabProcGrowth must be '0' 
@pytest.mark.skip
def test_force_create_process_api():
    options = webdriver.IeOptions()
    options.force_create_process_api = True

    driver = webdriver.Ie(options=options)

    driver.quit()


@pytest.mark.skipif(sys.platform != "win32", reason="requires Windows")
def test_log_to_file(log_path):
    service = webdriver.IeService(log_output=log_path, log_level="INFO")

    driver = webdriver.Ie(service=service)

    with open(log_path, "r") as fp:
        assert "Starting WebDriver server" in fp.readline()

    driver.quit()


@pytest.mark.skipif(sys.platform != "win32", reason="requires Windows")
def test_log_to_stdout(capfd):
    service = webdriver.IeService(log_output=subprocess.STDOUT)

    driver = webdriver.Ie(service=service)

    out, err = capfd.readouterr()
    assert "Started InternetExplorerDriver server" in out

    driver.quit()


@pytest.mark.skipif(sys.platform != "win32", reason="requires Windows")
def test_log_level(log_path):
    service = webdriver.IeService(log_output=log_path, log_level="WARN")

    driver = webdriver.Ie(service=service)

    with open(log_path, "r") as fp:
        assert "Started InternetExplorerDriver server (32-bit)" in fp.readline()

    driver.quit()


@pytest.mark.skipif(sys.platform != "win32", reason="requires Windows")
def test_supporting_files(temp_dir):
    service = webdriver.IeService(service_args=["–extract-path=" + temp_dir])

    driver = webdriver.Ie(service=service)

    driver.quit()
