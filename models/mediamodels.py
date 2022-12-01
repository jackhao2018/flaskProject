from exts import db

class MediaModel(db.Model):
    __tablename__ = "media"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    mtime = db.Column(db.DateTime)
    addr = db.Column(db.String(30))
    type = db.Column(db.Integer)

    def keys(self):
        return 'id', 'title','mtime', 'addr', 'type'

    def __getitem__(self, item):
        return getattr(self, item)

    def to_dict(self):
        return {i.name: getattr(self, i.name) for i in self.__table__.columns}

