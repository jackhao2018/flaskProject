from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class FansDetailsModel(db.Model):
    __tablename__ = "fans_detail"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fans_name = db.Column(db.String(100), nullable=False)
    mtime = db.Column(db.DateTime)
    vip_type = db.Column(db.String(30))
    sign = db.Column(db.String(1000))

    def to_dict(self):
        return {i.name: getattr(self, i.name) for i in self.__table__.columns}

class ImgInfoModel(db.Model):
    __tablename__ = "img_info"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img_url = db.Column(db.String(100), nullable=False)


if __name__ == '__main__':
    db.create_all()