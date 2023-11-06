from datetime import datetime

_current_log_file = ""

def log(message):
    global _current_log_file
    
    if _current_log_file == "":
      _current_log_file = datetime.now().strftime("%m-%d-%Y %H-%M") + ".txt"
   
    with open(_current_log_file, "a+") as log_file:
        log_file.write(message + "\n\n\n")
    
def set_log_file(name):
  global _current_log_file
  _current_log_file = name + ".txt"
