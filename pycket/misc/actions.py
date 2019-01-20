from pycket.common.enums import Action
from pycket.common.common import msg_dlg, write_config
from pycket.misc.paths import MAIL_CFG, MAIN_CFG
from PyQt5.QtWidgets import QMessageBox


def execute_action(action: Action, app_pw=None):
    ok = None
    try:
        if action is Action.Notify:
            from pycket.forms.notify import NotifyForm
            ok = not NotifyForm().exec_()
            print("Notify!!")
        elif action is Action.Mail:
            from pycket.scripts.sendmail import SendMail
            if app_pw is not None:
                try:
                    mail = SendMail(app_pw, MAIL_CFG)
                    mail.send()
                    print("Sent Mail")
                    ok = True
                except Exception as ex:  # TODO: Handle exception better (too generic)
                    msg_dlg("Mail error", "An error occurred while sending mail", icon=QMessageBox.Critical,
                            details="\n-".join(list(map(str, ex.args))))
                    ok = False
        else:
            from configparser import ConfigParser
            from subprocess import run, PIPE, Popen
            from shlex import split
            config = ConfigParser()
            config.read(MAIN_CFG)   # To get commands
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
            try:
                sp = Popen(split(command), stderr=PIPE)
                _, std_err = sp.communicate()
                if sp.returncode != 0:
                    msg_dlg("Could not %s" % action.name, icon=QMessageBox.Critical,
                            details="%s\nReturn Code: %s" % (std_err.decode(), sp.returncode))
                ok = not sp.returncode
            except FileNotFoundError as ex:
                msg_dlg("Could not %s" % action.name, "Command not found", icon=QMessageBox.Critical,
                        details="%s\nReturn Code: %s" % (ex.args[1], ex.args[0]))
                ok = False
    finally:
        return ok
