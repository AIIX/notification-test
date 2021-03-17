from mycroft.skills.core import MycroftSkill, intent_handler, intent_file_handler

class NotificationTestSkill(MycroftSkill):
    
    def __init__(self):
        super(NotificationTestSkill, self).__init__(name="NotificationTestSkill")
    
    def initialize(self):
        self.add_event("notif-test.aiix.send_sticky", self.notif_send_sticky)

    @intent_file_handler("notif.intent")
    def notif_send_default(self, message):
        self.gui.show_notification("Received A Sample Notification, This Is Sample Content!", action="notif-test.aiix.send_sticky")
    
    def notif_send_sticky(self, message):
        self.gui.show_notification("Received A Sample Sticky Notification, This Is Sample Content!", noticetype="sticky")
        
    
def create_skill():
    return NotificationTestSkill()
