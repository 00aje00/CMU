from os import system

import requests


def test_basic():
    """Test basic API endpoint."""
    response = requests.get("http://localhost:8080/")
    assert response.status_code == 200        
    assert response.json() == {"message": "This is the main endpoint to the cheese rating API."}

def test_data():
    """Test that the data is loaded correctly."""
    response = requests.get("http://localhost:8080/cheese/")
    assert response.status_code == 200
    assert len(response.json()) == 1741

def test_local_dev():
    """Test that the local bind mount feature is active."""
    response = requests.get("http://localhost:8080/color/")
    assert response.status_code == 200
    assert response.json() == {"color": "green"}

    system("sed -i.bak 's/green/yellow/g' api/color.json")
    system("sleep 1")
    response = requests.get("http://localhost:8080/color/")
    assert response.status_code == 200
    print(response.json())
    assert response.json() == {"color": "yellow"}

    system("mv api/color.json.bak api/color.json")
