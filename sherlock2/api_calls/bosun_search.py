import requests
from numpy import average

#proxy information, will move later. 
proxies = {
    'http': 'socks5h://127.0.0.1:10000',
    'https': 'socks5h://127.0.0.1:10000'
}

params = (
    ('filterCloud', 'true'),
)


def get_customer_data(cid,proxies=None,time_range='5m',did='*',type='count',proxyid='100.default.110'):

    data_from_boson = {}
  
    cid = f'cid=iliteral_or({cid})'
    did = f'did=wildcard({did})'
    proxyid = f'proxyid=iliteral_or({proxyid})'
    # proxyid = 'proxyid=wildcard(*)'
    type = f'type=iliteral_or({type})'
    
    #get data in from bosun
    data = f'(q("sum:rate{{counter,,1}}:chf.proxy_FlowsIn{{{type},{cid},{did},{proxyid}}}", "{time_range}", ""))'
    response = requests.post('https://bosun.iad1.kentik.com/api/expr', data=data,proxies=proxies).json()
    
    
    #get data out from bosun
    data_out = f'(q("sum:rate{{counter,,1}}:chf.proxy_FlowsOut{{{type},{cid},{did},{proxyid}}}", "{time_range}", ""))'
    response_out = requests.post('https://bosun.iad1.kentik.com/api/expr', data=data_out,proxies=proxies).json()
    
    # print(response)

    for device in response['Results']:
        device_id = device['Group']['did']
        values = device['Value']

        data_from_boson.update({device_id:{'All Results':list(values.values())}})

    for device in response_out['Results']:
        device_id_out = device['Group']['did']
        values_out = device['Value']

        data_from_boson[device_id_out]['data_out'] = list(values_out.values())
        

    def round_num(num):
        num = str(round(num,2))
        return num

    for device_id in data_from_boson:


        data_from_boson[device_id]['max_flows'] = round_num(max(data_from_boson[device_id]['All Results']))
        data_from_boson[device_id]['min_flows'] = round_num(min(data_from_boson[device_id]['All Results']))
        data_from_boson[device_id]['average'] = round_num(average(data_from_boson[device_id]['All Results']))
        data_from_boson[device_id]['total_flows'] = round_num(sum(data_from_boson[device_id]['All Results']))  
        
    for device_id in data_from_boson:


        data_from_boson[device_id]['max_flows_out'] = round_num(max(data_from_boson[device_id]['data_out']))
        data_from_boson[device_id]['min_flows_out'] = round_num(min(data_from_boson[device_id]['data_out']))
        data_from_boson[device_id]['average_out'] = round_num(average(data_from_boson[device_id]['data_out']))
        data_from_boson[device_id]['total_out'] = round_num(sum(data_from_boson[device_id]['data_out']))



    return data_from_boson
