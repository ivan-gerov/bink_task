import subprocess

import pytest
from main import task_1, task_2, task_3, task_4, task_selector

from tests.data.tasks_expected_data import TASK_1, TASK_2, TASK_3, TASK_4

TEST_DATA = "tests/data/test_dataset.csv"


def test_task_selector():
    """Tests the task selector"""
    assert task_selector("1") == task_1
    pytest.raises(ValueError, task_selector, 5)


def test_task_1():
    proc = subprocess.Popen(
        f"python main.py -t 1 -d {TEST_DATA}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    assert TASK_1 in stdout.decode()


def test_task_2():
    proc = subprocess.Popen(
        f"python main.py -t 2 -d {TEST_DATA}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    assert TASK_2[0] in stdout.decode().replace("\n", "")
    assert TASK_2[1] in stdout.decode()


def test_task_3():
    proc = subprocess.Popen(
        f"python main.py -t 3 -d {TEST_DATA}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    assert TASK_3 in stdout.decode()


def test_task_4():
    proc = subprocess.Popen(
        f"python main.py -t 4 -d {TEST_DATA}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    assert TASK_4 in stdout.decode()
