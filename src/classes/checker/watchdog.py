class watchdog(object):
    def __call__(self):
        try:
            with open('src/data/files/packages.txt','r') as f:
                for line in f.readlines():
                    line=line.strip()
                    __import__(line)
                    print(f"[src.classes.checker.watchdog] [PACKAGELOADER] Successfully loaded package: {line}")
        except Exception as e:
            print(f"[src.classes.checker.watchdog] ERROR! | Something went terribly wrong: {e}")
            return False
        return True