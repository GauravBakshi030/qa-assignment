import requests
import pytest
import time

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_status():
    res = requests.get(f"{BASE_URL}/posts")
    assert res.status_code == 200

def test_response_time():
    start = time.time()
    res = requests.get(f"{BASE_URL}/posts")
    end = time.time()
    assert (end - start) < 2

@pytest.mark.parametrize("endpoint", ["posts", "comments", "users"])
def test_endpoints(endpoint):
    res = requests.get(f"{BASE_URL}/{endpoint}")
    assert res.status_code == 200