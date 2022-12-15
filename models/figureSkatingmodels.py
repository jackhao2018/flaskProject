from exts import db
from sqlalchemy.dialects.mysql import LONGTEXT
class FigureSkatingModel(db.Model):
    __tablename__ = "figureSkating"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(LONGTEXT)
    tag = db.Column(db.String(20))
    rules = db.Column(LONGTEXT)

    @property
    def keys(self):
        return 'id', 'name', 'tag', 'rules'

    def __getitem__(self, item):
        return getattr(self, item)

    def to_dict(self):
        return {i.name: getattr(self, i.name) for i in self.__table__.columns}
