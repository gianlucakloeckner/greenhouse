from src.config import db
from src.models.plant import Plant


class PlantManager:

    def __init__(self):
        self.db = db
        self.collection = "plants"

    def create_plant(self, model):
        doc_ref = db.collection(self.collection).document(str(model.id))
        doc_ref.set(model.dict())
        return True

    def get_plant(self, plant_id):
        doc_ref = db.collection(self.collection).document(plant_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            raise ValueError("Plant not found")

    def update_plant(self, plant_id, model):
        doc_ref = db.collection(self.collection).document(plant_id)
        doc_ref.update(model.dict())
        return True

    def delete_plant(self, plant_id):
        doc_ref = db.collection(self.collection).document(plant_id)
        doc_ref.delete()
        return True

    def get_plants_by_greenhouse(self, greenhouse_id):
        query = db.collection(self.collection).where(
            "greenhouse_id", "==", greenhouse_id)
        docs = query.stream()
        plants_list = [doc.to_dict() for doc in docs]
        return plants_list
