class variables():

    class debugMode():

        def __init__(self, bool): self.debugMode = bool

        def setToBoolean(self, bool): self.debugMode = bool

        def status(self): return self.debugMode

    class mongodB():

        def token(): return "mongodb+srv://SYSADMIN:aCOpm6q1dQrX7CFv@cluster0.pwl4q.mongodb.net/test"

        def dBname(): return "portfolio"

class logs():

    class dB():

        def fetch(id_, field, item): print(f"[FETCH] : {id_}[{field}] = {item}.")

        def update(id_, field, item): print(f"[UPDATE] : {item}[{field}] = {item}.")

        def check(id_, bool): print(f"[CHECK] {id_} in dB = {bool}.")

        def delete(id_): print(f"[DELETE] {id_} deleted.")

        def creation(id_): print(f"[CREATION] {id_} was created.")