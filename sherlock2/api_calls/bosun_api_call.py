


def show_bosun_query(cid,time_range='5m',did='*',type='count',proxyid='100.default.110'):


  
    cid = f'cid=iliteral_or({cid})'
    did = f'did=wildcard({did})'
    proxyid = f'proxyid=iliteral_or({proxyid})'
    type = f'type=iliteral_or({type})'
    
    #get data in from bosun
    data = f'(q("sum:rate{{counter,,1}}:chf.proxy_FlowsIn{{{type},{cid},{did},{proxyid}}}", "{time_range}", ""))'

    
    
    #get data out from bosun
    data_out = f'(q("sum:rate{{counter,,1}}:chf.proxy_FlowsOut{{{type},{cid},{did},{proxyid}}}", "{time_range}", ""))'

    data_from_boson = {
        "bosun_in": data,
        "bosun_out":data_out

    }


    return data_from_boson
