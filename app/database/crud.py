class CRUDBase:
    def __init__(self, session):
        self.session = session

    def create(self, model, **kwargs):
        instance = model(**kwargs)
        self.session.add(instance)
        self.session.commit()
        instance.refresh()
        return instance

    def read(self, model, **kwargs):
        result = self.session.query(model).filter_by(**kwargs).first()
        if not result:
            raise ValueError(f"Instance of {model.__name__} not found with {kwargs}")
        return result

    def update(self, instance, **kwargs):
        for key, value in kwargs.items():
            setattr(instance, key, value)
        self.session.commit()
        return instance

    def delete(self, instance):
        self.session.delete(instance)
        self.session.commit()
