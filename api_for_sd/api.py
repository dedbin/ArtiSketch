import requests

class WebUIApi:
    def __init__(self, baseurl):
        self.baseurl = baseurl
    
    def prompt_to_image(self, prompt):
        endpoint = f"{self.baseurl}/prompt-to-image"
        payload = {"prompt": prompt}
        
        response = requests.post(endpoint, json=payload)
        if response.status_code == 200:
            image_data = response.content
            return image_data
        else:
            return None
        