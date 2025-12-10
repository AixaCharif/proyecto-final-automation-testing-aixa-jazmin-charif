import requests

class APIClient:
    BASE_URL = "https://dummyjson.com"
    HEADERS = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"  
    }

    def get(self, endpoint, expected_status=200):
        response = requests.get(f"{self.BASE_URL}{endpoint}", headers=self.HEADERS)
        assert response.status_code == expected_status, \
            f"GET {endpoint} devolvió {response.status_code}"
        return response.json()

    def post(self, endpoint, data, expected_status=201):
        response = requests.post(f"{self.BASE_URL}{endpoint}", json=data, headers=self.HEADERS)
        assert response.status_code == expected_status, \
            f"POST {endpoint} devolvió {response.status_code}"
        return response.json()

    def delete(self, endpoint, expected_status=200):
        response = requests.delete(f"{self.BASE_URL}{endpoint}", headers=self.HEADERS)
        assert response.status_code == expected_status, \
            f"DELETE {endpoint} devolvió {response.status_code}"
        return response
