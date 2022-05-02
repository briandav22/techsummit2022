import requests


class KentikAPI:
    def __init__(self, kentik_email,kentik_api_token):
        self.email = kentik_email
        self.token = kentik_api_token
        self.cookies = {'kentikPortalv2.sid': 's%3AWnEZIBeJUoCUHLV43I25ebUSr3shH-wO.ghsdbppwrx3XmxJlABGunmnUy8jK7cu9vVuqSixcXcU'}
        self.all_devices = ''
        self.plan_map = ''


    def create_device_object(self,device):
        device_name = device['device_name']
        device_description = device['device_description']
        device_date = device['created_date']
        dates = device_date.split("T")
        device_date = dates[0]
        device_plan_id = device['plan']['id']
        device_sample_rate = device['device_sample_rate']
        device_id = device['id']
        device_max_fps = self.plan_map[device_plan_id]['max_fps']
        device_plan = self.plan_map[device_plan_id]['plan_type']
        device_plan_fps = self.plan_map[device_plan_id]['plan_fps']
        device_object = {device_id:{
            'name':device_name,
            'device_id':device_id,
            'type':device_description,
            'date_added':device_date,
            'plan_type':device_plan,
            'plan_fps':device_plan_fps,
            'max_fps':device_max_fps,
            'sample_rate':device_sample_rate
        }}

        return device_object

    def get_plans(self):
        plan_map = {}
        headers = {
            'accept': 'application/json',
            'X-CH-Auth-Email': self.email,
            'X-CH-Auth-API-Token': self.token,
        }

        response = requests.get('https://portal.kentik.com/api/ui/setup/plans', headers=headers).json()

        for plan in response:
            plan_id = plan['id']
            max_fps = plan['max_fps']
            plan_type = plan['metadata']['type']
            plan_name = plan['name']
            plan_description = plan['description']
            try:
                plan_fps = plan['metadata']['pakFps']
            except:
                plan_fps = '0'
            if plan_id not in plan_map:
                plan_map[plan_id] = {
                    'id': plan_id,
                    'name': plan_name,
                    'descriptions': plan_description,
                    'max_fps':max_fps,
                    'plan_type':plan_type,
                    'plan_fps':plan_fps,

         
                }
            else: 
                plan_map[plan_id] = {
                    'id': plan_id,
                    'name': plan_name,
                    'descriptions': plan_description,
                    'max_fps':max_fps,
                    'plan_type':plan_type,
                    'plan_fps':plan_fps,
                    
         
                }    
        self.plan_map = plan_map

    def get_kentik_devices(self):
        enriched_devices = []
        
        params = (
        ('filterCloud', 'true'),
            )
        headers = {
            'accept': 'application/json',
            'X-CH-Auth-Email': self.email,
            'X-CH-Auth-API-Token': self.token,
        }


        response = requests.get('https://portal.kentik.com/api/ui/devices', headers=headers, params=params).json()

        for device in response:
            device_enriched = self.create_device_object(device)
            enriched_devices.append(device_enriched)

        return enriched_devices

