import uuid
import datetime

def generate_id(prefix=""):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"

def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")