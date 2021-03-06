import sys
import os
sys.path.append(os.path.join(sys.path[0],'interfaces'))
from fog05.interfaces.States import State
from fog05.interfaces.EntityInstance import EntityInstance

class LXDEntityInstance(EntityInstance):

    def __init__(self, uuid, name, networks, image, user_file, ssh_key, storage, profiles, entity_uuid):

        super(LXDEntityInstance, self).__init__(uuid, entity_uuid)
        self.name = name
        self.networks = networks
        self.image = image
        self.user_file = user_file
        self.ssh_key = ssh_key
        self.storage = storage
        self.profiles = profiles
        self.conf = None

    def on_configured(self, configuration):
        self.conf = configuration
        self.state = State.CONFIGURED

    def on_clean(self):
        self.state = State.DEFINED

    def on_start(self):
        self.state = State.RUNNING
    
    def on_stop(self):
        self.state = State.CONFIGURED

    def on_pause(self):
        self.state = State.PAUSED

    def on_resume(self):
        self.state = State.RUNNING

    def __str__(self):
        return "Name : {0} UUID: {1}".format(self.name, self.uuid)
