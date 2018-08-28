from common.enums import Action
from common.common import msg_dlg
from provisional import MAIL_CFG, MAIN_CFG


def execute(action: Action, app_pw=None):
    if action is Action.Notify:
        from forms.notify import NotifyForm
        NotifyForm().exec_()
        print("Notify!!")
    elif action is Action.Mail:
        from scripts.sendmail import SendMail
        from PyQt5.QtWidgets import QMessageBox
        if app_pw is not None:
            try:
                mail = SendMail(app_pw, MAIL_CFG)
                mail.send()
                print("Sent Mail")
            except Exception as ex:
                msg_dlg("Mail error", "An error occurred while sending mail", icon=QMessageBox.Critical,
                        details="\n-".join(list(map(str, ex.args))))
    else:
        from configparser import ConfigParser
        config = ConfigParser()
        config.read(MAIN_CFG)
        command = ""
        if action is Action.Shutdown:
            command = config.get("Commands", "shutdown")
        elif action is Action.Reboot:
            command = config.get("Commands", "reboot")
        elif action is Action.CloseSession:
            command = config.get("Commands", "close_session")
        elif action is Action.Lock:
            command = config.get("Commands", "lock_screen")
        elif action is Action.Suspend:
            command = config.get("Commands", "suspend")
        elif action is Action.Hibernate:
            command = config.get("Commands", "hibernate")
        elif action is Action.Execute:
            command = config.get("Commands", "execute")
