import requests


class DeviceSearch:
    def __init__(self, kentik_email,kentik_api_token, customer_id, cookie):
        self.url = f'https://portal.kentik.com/api/sudo/companies/{customer_id}'
        self.cookies = {'kentikPortalv2.sid': f"{str(cookie)}"}
        self.headers = {
                'content-type': 'application/json',
                'X-CH-Auth-Email': kentik_email,
                'X-CH-Auth-API-Token': kentik_api_token,
        }
        self.data_back = ''
    
    def get_device_data(self):
        
        response = requests.get(self.url, headers=self.headers, cookies=self.cookies)
        if response.status_code != 200:
            
            return response.text
     
        return response.json()



    def create_plan_object(self, data_back):

        plan_object = {}
        for plan in data_back['plans']:
            plan_id = plan['id']
            max_fps = plan['max_fps']
            
            try:
                plan_fps = plan['metadata']['pakFps']
                plan_type = plan['metadata']['type']
            except:
                plan_fps = '0'
                plan_type = 'none'
            plan_object[plan_id] = {
                    "max_fps":max_fps,
                    "plan_type":plan_type,
                    "plan_fps":plan_fps,
                    "plan_id":plan_id
                }

        return plan_object

    def create_device_objects(self, plan_object, data_back):


            devices = []
            for device in data_back['devices']:
                device_id = device['id']
                device_name = device['device_name']
                device_date = device['cdate']
                plan_id = device['plan_id']
                max_flows = plan_object[plan_id]['max_fps']
                plan_type = plan_object[plan_id]['plan_type']
                plan_fps = plan_object[plan_id]['plan_fps']
                device_description = device['device_description']
                device_sample_rate = device['device_sample_rate']
                dates = device_date.split("T")
                device_date = dates[0]
                
                device_object = {device_id:{
                    'device_id':device_id,
                    'name':device_name,
                    'date_added':device_date,
                    'plan_id': plan_id,
                    'max_fps':max_flows,
                    'type':device_description,
                    'sample_rate':device_sample_rate,
                    'plan_type': plan_type,
                    'plan_fps':plan_fps
                }}
                devices.append(device_object)
            return devices