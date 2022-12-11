from exts import db

class FigureSkatingModel(db.Model):
    __tablename__ = "figureSkating"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    rules = db.Column(db.Date)

    @property
    def keys(self):
        return 'id', 'name', 'rules'

    def __getitem__(self, item):
        return getattr(self, item)

    def to_dict(self):
        return {i.name: getattr(self, i.name) for i in self.__table__.columns}
