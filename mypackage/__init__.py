# mypackage/__init__.py
import requests

class MyPackage:
    def __init__(self, url, data):
        self.url = url
        self.data = data

    def initYojn(self):
        response = requests.post(self.url, json=self.data)
        return response.json()

    def runYojn(self, url, data):
        response = requests.post(url, json=data)
        return response.json()

    def uploadFile(self, url, file_path):
        files = {'file': open(file_path, 'rb')}
        response = requests.post(url, files=files)
        return response.json()

    def userHistory(self, url, user_id):
        params = {'userId': user_id}
        response = requests.get(url, params=params)
        return response.json()

    def updateUserFeedback(self, url, feedback):
        response = requests.put(url, json=feedback)
        return response.json()
