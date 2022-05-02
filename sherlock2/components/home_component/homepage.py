from dash import  html,dcc


homepage = html.Div(
    [
        html.H2("Welcome to Sherlock", className="display-4"),
        html.Hr(),
        html.P(
            "You can use this tool to find FPS information about your customers."
        ),

        dcc.Markdown('''


## Introduction

Sherlock is a Python app that can present the state of the 'flow world' for customers of kentik. 

The goal is to combine answers to common questions into a single output. Some examples of these questions would be: 

- What percent of a license is a customer using on average? 
- Is my customer downsampling? If so, how often? 
- How many flows are being downsampled total vs on average?
- What license level should I be selling here?

---

## Getting Started 

### Libraries 

Sherlock is written entirely in Python. This is because it is a scientific fact that Python is the best programming language. 

[Dash](https://dash.plotly.com/introduction) is the main library used to build Sherlock. If your interested in modifying this app or building you own I would also reccomend checking out [plotly](https://plotly.com/python/getting-started/) and [pandas](https://pandas.pydata.org/docs/). 

### Running Sherlock

The requirement.txt file contains all the packages needed to run this app. First step is to install all the packages with the following command. 

You can use [virtualenv](https://docs.python.org/3/library/venv.html) if you don't want to install these packeages globably. 

```
pip3 install -r requirements.txt
```

After installing the packages start the app with 

```
python3 app.py
```

If things didn't blow up you should see the following output in your terminal. 

```
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on

```

### Proxy

Since Sherlock is not hosted on the same network as Bosun the API calls must be proxies through the VPN. My guess this is going to be the #1 issue people run into as they try this system out. 

I have only tested this using SwitchyOmega, so if your using something else you made need to adjust the procy variable in /api_calls/bosun_search.py. 

For my testing these variables line up with the SwitchyOmega settings. If your using a different port or protocol to VPN into Kentik, Your Milleage May Vary. Please please please if there is a more consistent way to do this suggest it!

```python

proxies = {
    'http': 'socks5h://127.0.0.1:10000',
    'https': 'socks5h://127.0.0.1:10000'
}

```

 '''),


html.Img(src="../../assets/switchy.png", className="proxy-image"),

dcc.Markdown('''

---
## Navigation 

Sherlock has two different search cabilities. Bosun Search, which only uses the Bosun API, and Enriched Search which uses both the Bosun API and the Kentik API. 

## Bosun Search 

Within the Bosun Search tab plug in the Customer ID number, select a time range, and hit search. 
After the query completes you are presented with a table and graph showing the data. 

#### Bosun Queries

The Bosun search makes two queries to the Bosun api in order to gather results, you can find the queries in /api_calls/bosun_search.py to see how they are built. 

Below are some example queries Sherlock would make, the difference between them is Query 1 looks for flows coming inbound (pre-downsample) and Query 2 looks for flows going outbound (post-downsample).

The results of these queries are then compared to show how much a customer is being downsampled per device. 

```python
# Query 1 (FlowsIn)

q("sum:rate{counter,,1}:chf.proxy_FlowsIn{type=iliteral_or(count),cid=iliteral_or(80549),did=wildcard(*),proxyid=iliteral_or(100.default.110)}", "1h", "")

# Query 2 (FlowsOut)

q("sum:rate{counter,,1}:chf.proxy_FlowsOut{type=iliteral_or(count),cid=iliteral_or(80549),did=wildcard(*),proxyid=iliteral_or(100.default.110)}", "1h", "")

```

## Enriched Search 

The enriched search combines the Bosun Queries from the previous example with the results of a couple API calls to the customers portal. 

In addition to providing a email address and API token you may have to adjust the customer portal to allow Sherlock to pull the required information down. 

### API Calls

You can find the api calls used in this search under /api_calls/kentik_search.py. 

The first api call gathers a mapping of Plan IDs and Max Flow rates for each plan. 

The second gathers information about the customer devices

- Sample Rate 
- Device Name 
- Plan ID (compared with first API call to get max flow rates)
- Date the device was added to Kentik
    

```python
# API call 1

requests.get('https://portal.kentik.com/api/ui/setup/plans', headers=headers).json()

#API call 2

requests.get('https://portal.kentik.com/api/ui/devices', headers=headers, params=params).json()

```
---

## FAQ

*I downloaded the report, started it, but the searches are not working, whats wrong?*

Well, I'm a bad developer, so the error handling is pretty terrible. I would suggest looking at a few things. 

Considerations would be : 

- If Bosun Search is failing, then everything will fail. The biggest reason that Bosun search would fail is because you aren't VPNed in, or the API call isn't being proxies correctly. 

- If the Bosun search IS working and the Enriched Search is failing. The most likely reason (aside from you fat fingering the Email / API token) would be that you have not allowed Sherlocks IP access to the customers account. (Menu - > Settings - > ACL)


*The script pukes all over itsef when I try to start it, whats wrong?*

If this is the case the python output is going to be your best bet for figuring out whats going on. 





        ''')

    ],

    id = "page-content")