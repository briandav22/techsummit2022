import pandas as pd 
import json

def round_num(num):
    num = str(round(num,2))
    return num

def dropnested(alist):
    outputdict = {}
    for dic in alist:
        for key, value in dic.items():
            if isinstance(value, dict):
                for k2, v2, in value.items():
                    outputdict[k2] = outputdict.get(k2, []) + [v2]
            else:
                outputdict[key] = outputdict.get(key, []) + [value]
    return outputdict    

def enriched_fig(bosun_data,kentik_data, time_range):


    hours = time_range.split('h')[0]
    enriched_devices = []


    for device in kentik_data:

        device_id = list(device.keys())[0]
        
        #[7][3][1][7][1]
        if device_id in bosun_data:
            try:
            #flows in 
                max_flows_in = float(bosun_data[device_id]['max_flows']) 
                min_flows = float(bosun_data[device_id]['min_flows']) 
                average_flows = float(bosun_data[device_id]['average'])  
                total_in = float(bosun_data[device_id]['total_flows']) 

                #flows out
                max_flows_out = float(bosun_data[device_id]['max_flows_out']) 
                min_out = float(bosun_data[device_id]['min_flows_out']) 
                average_out = float(bosun_data[device_id]['average_out'])
                total_out = float(bosun_data[device_id]['total_out']) 

                max_flows = float(device[device_id]['max_fps'])
                fp_plan_fps = device[device_id]['plan_fps']
                plan_type = device[device_id]['plan_type']

                #number of results for each exporter in 
                data_points = len(bosun_data[device_id]['All Results'])
                times_over = []

                for time_series in bosun_data[device_id]['All Results']:
                    
                    if time_series > max_flows:
                        times_over.append(1)

                data_points_over = len(times_over)



                if len(times_over) > 1: 
                    if plan_type == 'flowpak':
                        # print('in flow pak')
                        # print(plan_type)
                        device[device_id]['fp_min_percent'] =  round_num(min_flows/fp_plan_fps)
                        device[device_id]['fp_avg_percent'] =  round_num(average_flows/fp_plan_fps)
                        device[device_id]['fp_max_percent'] =  round_num(max_flows_in/fp_plan_fps)
                        device[device_id]['time_over'] = 0
                        device[device_id]['average_utilization'] = 0

                    else:
                        # print('not in flowpak')
                        # print(plan_type)
                        device[device_id]['fp_min_percent'] =  0
                        device[device_id]['fp_avg_percent'] =  0
                        device[device_id]['fp_max_percent'] =  0
                        device[device_id]['time_over'] = round_num(data_points_over/data_points)
                        device[device_id]['average_utilization'] = round_num(float(average_flows)/float(max_flows))
                
                else:
                    if plan_type == 'flowpak':

                        device[device_id]['fp_min_percent'] =  round_num(float(min_flows)/float(fp_plan_fps))
                        device[device_id]['fp_avg_percent'] =  round_num(float(average_flows)/float(fp_plan_fps))
                        device[device_id]['fp_max_percent'] =  round_num(float(max_flows_in)/float(fp_plan_fps))
                        device[device_id]['time_over'] = 0
                        device[device_id]['average_utilization'] = 0 
                    else:
                        # print('in the else')
                        # print(plan_type)
                        device[device_id]['time_over'] = 0
                        device[device_id]['average_utilization'] = round_num(float(average_flows)/float(max_flows))
                        device[device_id]['fp_min_percent'] =  0
                        device[device_id]['fp_avg_percent'] =  0
                        device[device_id]['fp_max_percent'] =  0

                #flows in labeled 
                device[device_id]['max_flows_in'] = max_flows_in
                device[device_id]['max_flows_out'] = max_flows_out
                
                device[device_id]['average_flows_in'] = average_flows
                device[device_id]['average_out'] = average_out
                
                #flows out labeled
                device[device_id]['min_flows_in'] = min_flows
                device[device_id]['min_flows_out'] = min_out
                device[device_id]['total_flows_in'] = total_in
                device[device_id]['total_flows_out'] = total_out
                device[device_id]['total_dropped'] = round_num(float(total_in) - float(total_out))
                device[device_id]['sending_flows'] = 'True'

                enriched_devices.append(device)
            except Exception as e:
                print(device)
                print(e)
                pass
        else:
                max_flows_in = 0 
                min_flows = 0
                average_flows = 0 
                total_in = 0

                #flows out
                max_flows_out = 0
                min_out = 0
                average_out = 0
                total_out = 0
                device[device_id]['max_flows_in'] = max_flows_in
                device[device_id]['max_flows_out'] = max_flows_out
                device[device_id]['average_flows_in'] = average_flows
                device[device_id]['average_out'] = average_out
                device[device_id]['time_over'] = 0
                device[device_id]['average_utilization'] = 0
                device[device_id]['fp_min_percent'] =  0
                device[device_id]['fp_avg_percent'] =  0
                device[device_id]['fp_max_percent'] =  0
                #flows out labeled
                device[device_id]['min_flows_in'] = min_flows
                device[device_id]['min_flows_out'] = min_out
                device[device_id]['total_flows_in'] = total_in
                device[device_id]['total_flows_out'] = total_out
                device[device_id]['total_dropped'] = 0
                device[device_id]['sending_flows'] = 'False'
                enriched_devices.append(device)

    final = dropnested(enriched_devices)

    # print(json.dumps(final, indent=4))
 
    df = pd.DataFrame(final)

    df['total_dropped'] = df['total_dropped'].astype('float64')
    df['sample_rate'] = df['sample_rate'].astype('int')
    df['average_utilization'] = df['average_utilization'].astype('float64')
    df['time_over'] = df['time_over'].astype('float64')
    df['total_dropped'] = df['total_dropped'].astype('float64')
    df['date_added'] = pd.to_datetime(df['date_added'])




    df = df.reindex(['device_id','name','plan_type','total_dropped','sending_flows','time_over','max_fps','average_utilization', 'fp_min_percent', 'fp_avg_percent',
       'fp_max_percent','date_added', 'plan_id', 'type',
       'sample_rate',  'plan_fps', 
       'max_flows_in', 'max_flows_out', 'average_flows_in',
       'average_out', 'min_flows_in', 'min_flows_out', 'total_flows_in',
       'total_flows_out'], axis=1)

    df.to_csv('data.csv')    
    
    return df