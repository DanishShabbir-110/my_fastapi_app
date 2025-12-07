import os
from fastapi import APIRouter
import json
router = APIRouter()

encoding_json = os.path.join(os.path.dirname(__file__), "../../../../encodings.json")

@router.get("/echo")
def echo(message: str):
    print(f"Loading encodings from: {encoding_json}")
    with open(encoding_json, "r") as file:
        encodings_data = file.read()
    print(f"Encodings data: {encodings_data}")
    return {"echo": message}

@router.get("/encodings/{person_id}")
def get_encodings_by_id(person_id: str):

    with open(encoding_json, "r") as file:
        data = json.load(file)
        target_ecodings = data.get(person_id, {})
        print(f"Encodings for {person_id}: {target_ecodings}")

    return target_ecodings

@router.get("/encodings/class/{class_name}")
def get_encodings_by_class(class_name: str):
    with open(encoding_json, "r") as file:
        data = json.load(file)
        filtered_encodings = {
            pid: details for pid, details in data.items() if details.get("class") == class_name
        }
        print(f"Encodings for class {class_name}: {filtered_encodings}")
    return filtered_encodings
