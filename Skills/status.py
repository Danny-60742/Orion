import socket

def get_status():
    try:
      socket.create_connection(("google.com", 80), timeout=3)
      return "🟢 ONLINE"
    except Exception as e:
      print(e)
      return "🔴 OFFLINE"
