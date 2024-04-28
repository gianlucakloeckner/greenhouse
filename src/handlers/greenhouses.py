from src.config import db
from src.models.greenhouse import Greenhouse


class GreenhouseManager:
    def __init__(self):
        self.db = db
        self.collection = "greenhouses"

    def create_greenhouse(self, model):
        doc = db.collection(self.collection).document(str(model.id)).get()
        if doc.exists:
            print("Duplicate Key Found. {}".format(doc.get('slug')))
            return False

        doc = self.db.collection(self.collection).document(
            str(model.name)).set(model.dict())
        if not doc:
            raise ("document not saved")
        return True

    def get_greenhouse(self, document):
        doc = db.collection(self.collection).document(document).get()
        if doc.exists:
            return doc.to_dict()
        else:
            raise ("No Details Found")

    def update_greenhouse(self, document, model):
        doc_ref = db.collection(self.collection).document(
            document).update(model.dict())
        if not doc_ref:
            raise ("document not saved")
        return True

    def delete_greenhouse(self, document):
        doc_ref = db.collection(self.collection).document(document).delete()
        return True

    def get_all_greenhouses(self):
        docs = db.collection(self.collection).stream()
        users_list = [doc.to_dict() for doc in docs]
        return users_list
