from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the Corina_Trackerv2.ipynb directory with bokeh server"""
    Popen(["panel", "serve", "Corina_Trackerv2.ipynb", "--allow-websocket-origin=*"])
