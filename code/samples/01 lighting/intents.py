from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import geocoder
import random
import requests
import philhues

app = Flask(__name__)
ask = Ask(app, '/')

bridge_ip = "192.168.0.10"

""" These functions handle what are essentially the beginning and end of the main use case of the skill."""
@ask.launch
def start_session():
    """ This function is what initializes the application."""
    welcome_msg = render_template('welcome')
    return question(welcome_msg)

@ask.intent("ListGroups")
def listGroups():
    bridge = philhues.Bridge(ip=bridge_ip)
    groups = bridge.get_group()
    group_names = []
    group_count = 0
    for idnumber, info in groups.items():
        group_names.append(info['name'])
        group_count += 1
    if not group_count:
        return statement("You have not set up any groups yet.")

    ret_statement =  "You have %d groups called %s" % (group_count, ",".join(group_names))
    return statement(ret_statement)

@ask.intent("ListLights")
def listLights():
    bridge = philhues.Bridge(ip=bridge_ip)
    num_lights = len(bridge.get_light_objects())
    if num_lights != 0:
        session.attributes['numLights'] = num_lights
        return question("Woah, Darkness has taken over.").reprompt("Shall I turn on the lights?")
    else:
        session.attributes['numLights'] = num_lights
        return statement("You have %d lights enabled in the house!" % num_lights)

@ask.intent("ListScenes")
def listScenes():
    # TODO
    return

@ask.intent("DiscoMode")
def discoMode():
    # color temp between 154 to 500
    import time, random
    bridge = philhues.Bridge(ip=bridge_ip)
    lights = bridge.get_light_objects()
    iter_cnt = 1
    while iter_cnt < 300: # fav magic number 
        for light in lights:
            light.colortemp(random.randint(154, 500))
            light.Brightness(random.randint(0, 254))
            light.Saturation(random.randint(0, 254))
            light.hue(random.randint(0, 65535))
            time.sleep(1)
        time.sleep(1)
        iter_cnt += 1
    return question("That was fun").reprompt("Want me to continue?")

@ask.intent("ControlLights")
def controlLights(Lights, Brightness):
    bridge = philhues.Bridge(ip=bridge_ip)
    all_lights = bridge.get_light_objects()
    for light in all_lights:
        if light.light_id in Lights:
            light.Brightness = Brightness
    return statement("Thy wish is my command, O master.")