from enums import Action


def execute(action: Action):
    if action is Action.Shutdown:
        print("Shutdown!!")
    elif action is Action.Reboot:
        print("Reboot!!")
    elif action is Action.Lock:
        print("Lock screen!!")
    elif action is Action.Suspend:
        print("Suspend!!")
    elif action is Action.Hibernate:
        print("Hibernate!!")
    elif action is Action.Notify:
        print("Notify!!")
    elif action is Action.Execute:
        print("Execute!!")
    elif action is Action.Mail:
        print("Send Mail!!")