import requests

# use log files and args

class RequestHandler:
    def __init__(self):
        self.headers = {'User-Agent':'OTW-Open Doors bot'}
        self.redirect_codes = [301, 302, 307, 308]

    def _send_head(self, url):
        return requests.head(url=url, headers=self.headers)
    
    def status_code_handler(self, url):
        return_dict = {'original_url':url, 'status_code':'', 'redirect_location':''}
        status = self._send_head(url)
        if staus.status_code in self.redirect_codes:
            return_dict.update({'redirect_location':status.headers['location']})
        return_dict.update({'status_code':status.status_code})