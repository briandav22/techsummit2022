from content import app

server = app.server
if __name__ == "__main__":
    app.run_server(debug=True,dev_tools_ui=True,dev_tools_props_check=True)