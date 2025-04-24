from sqlalchemy.orm import Session

class CRUDBase:
    def __init__(self, session: Session):
        self.session = session

    def create(self, model, **kwargs):
        instance = model(**kwargs)
        self.session.add(instance)
        self.session.refresh(instance)
        self.session.commit()
        return instance

    def read(self, model, **kwargs):
        result = self.session.query(model).filter_by(**kwargs).first()
        if not result:
            raise ValueError(f"Instance of {model.__name__} not found with {kwargs}")
        return result

    def get_all(self, model):
        return self.session.query(model).all()

    def update(self, instance, **kwargs):
        for key, value in kwargs.items():
            setattr(instance, key, value)
        self.session.commit()
        return instance

    def delete(self, instance):
        self.session.delete(instance)
        self.session.commit()
