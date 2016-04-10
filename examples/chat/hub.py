import networkzero as nw0

#
# If the hub is already running in another process, drop out
#
hub = nw0.discover("chat-hub", 3)
if hub is not None:
    raise SystemExit("Hub is already running on %s" % hub)

hub = nw0.advertise("chat-hub")
updates = nw0.advertise("chat-updates")
while True:
    action, params = nw0.wait_for_message(hub, autoreply=True)
    print("Action: %s, Params: %s" % (action, params))
    nw0.send_notification(updates, action, params)
