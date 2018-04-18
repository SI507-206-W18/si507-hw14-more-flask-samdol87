import json
from datetime import datetime


GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id = 0

def init(app):
    global entries, next_id
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        if int(entries[0]["id"]) > next_id:
            next_id = int(entries[0]["id"])+1
        f.close()
    except:
        print('Couldn\'t open', GUESTBOOK_ENTRIES_FILE)
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    entry = {"author": name, "text": text, "timestamp": time_string, "id": str(next_id)}
    entries.insert(0, entry) ## add to front of list
    next_id += 1
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def delete_entry(id):
    global entries, GUESTBOOK_ENTRIES_FILE, next_id
    pointer = {}
    for e in entries:
        if id == e["id"]:
            pointer = e
    entries.remove(pointer)
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not re-write entries to file.")
