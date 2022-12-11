from exts import db

class SchedulesModel(db.Model):
    __tablename__ = "schedules"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    mtime = db.Column(db.Date)

    @property
    def keys(self):
        return 'id', 'title', 'mtime'

    def __getitem__(self, item):
        return getattr(self, item)

    def to_dict(self):
        return {i.name: getattr(self, i.name) for i in self.__table__.columns}