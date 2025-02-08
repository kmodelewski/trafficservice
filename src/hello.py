from enum import Enum
from fastapi import FastAPI

app = FastAPI()


@app.get("/{name}")
def read_root(name):
    return {"Hello": name}


class TrafficIncident(str, Enum):
    accident = 'accident'
    location = 'location'
    
@app.get("/traffic/all")
def show_all_incidents(page_size: int = 10):
    return {"page_size": page_size}
    
@app.get("/traffic/{incident}")
def show_incident(incident: TrafficIncident):
    return {"incident": incident}