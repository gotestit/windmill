#   Copyright (c) 2006 Open Source Applications Foundation
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


import os, sys
import windmill

def configure_global_settings():
    # Get local config
    
    if os.environ.has_key('WINDMILL_CONFIG_FILE'):
        sys.path.insert(0, os.path.dirname(os.path.abspath(os.environ['WINDMILL_CONFIG_FILE'])))
        local_settings = __import__(os.path.basename(os.path.abspath(os.environ['WINDMILL_CONFIG_FILE'])))
        sys.path.remove(os.path.dirname(os.path.abspath(os.environ['WINDMILL_CONFIG_FILE'])))
    else:
        try:
            import windmill_settings as local_settings
        except:
            local_settings = object()
            
    windmill.settings = windmill.conf.configure_settings(local_settings)
    
    
def runserver(cmd_options):
    import windmill
    
    if cmd_options.has_key('daemon'):
        httpd, httpd_thread, loggers, console_log_handler = windmill.bin.run_server.run_threaded()
        httpd_thread.setDaemon(True)
    else:
        httpd, loggers = windmill.bin.run_server.setup_server(windmill.settings['CONSOLE_LOG_LEVEL'])
        try:
            httpd.serve_until()
        except KeyboardInterrupt:
            while httpd.is_alive() is True:
                httpd.server_stop()
                httpd.socket.close()
                time.sleep(1)
            sys.exit()
    
def shell(cmd_options):
    import windmill
    if cmd_options['debug'] is True:
        import pdb
    
    httpd, httpd_thread, loggers, console_log_handler = windmill.bin.run_server.run_threaded(windmill.settings['CONSOLE_LOG_LEVEL'])
    
    # setup all usefull objects
    jsonrpc_client = windmill.tools.make_jsonrpc_client()
    xmlrpc_client = windmill.tools.make_xmlrpc_client()

    if hasattr(windmill.tools.dev_environment, 'IPyShell') is True and \
       cmd_options['usecode'] is False:
        import IPython
        shell = IPython.Shell.IPShell(user_ns=locals(), shell_class=windmill.tools.dev_environment.IPyShell)
        shell.IP.httpd = httpd
        shell.IP.httpd_thread = httpd_thread
        shell.mainloop()
    else:
        try:
            import code
            code.interact(local=locals())    
        except KeyboardInterrupt:
            while httpd_thread.isAlive() is True:
                httpd.server_stop()
                httpd.socket.close()
                time.sleep(1)
            sys.exit()
    
    
action_mapping = {'shell':shell, 'runserver':runserver}

def loglevel(value):
    import logging
    level = getattr(logging, value)
    windmill.settings['CONSOLE_LOG_LEVEL'] = getattr(logging, value)
    return level
    
def debug(value):
    import logging
    windmill.settings['CONSOLE_LOG_LEVEL'] = getattr(logging, 'DEBUG')

cmd_parse_mapping = {'loglevel':loglevel, 'debug':debug}

def parse_commands():
    
    action = sys.argv[1]
    sys.argv.pop(0)
    sys.argv.pop(0)
    # Set defaults
    cmd_options = {'debug':False, 'usecode':False}
    for option in sys.argv:
        if option.startswith('http'):
            windmill.settings.TEST_URL = option
            key = False
        elif option.find('=') is not -1:
            key, value = option.split('=')
            cmd_options[key] = value
        else:
            key = option
            cmd_options[key] = True
            
        if cmd_parse_mapping.has_key(key):
            cmd_options[key] = cmd_parse_mapping[key](cmd_options[key])
    
    return action, cmd_options
    

if __name__ == "__main__":
    import windmill
    configure_global_settings()
    action, cmd_options = parse_commands()
    
    action_mapping[action](cmd_options)
    
    








