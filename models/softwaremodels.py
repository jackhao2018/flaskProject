from exts import db
from sqlalchemy.dialects.mysql import LONGTEXT


class SoftwareModel(db.Model):
    __tablename__ = "software_info"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    softName = db.Column(db.String(50), nullable=False)
    softDesc = db.Column(db.String(1000))
    softSize = db.Column(db.String(10))
    softURL = db.Column(db.String(1000))
    softLanguage = db.Column(db.String(10), comment='软件语言')
    issue = db.Column(db.String(10))
    copyright = db.Column(db.String(100))
    baiduLink = db.Column(db.String(200))
    baiduLinkPwd = db.Column(db.String(10))
    aliyunLink = db.Column(db.String(200))
    aliyunLinkPwd = db.Column(db.String(10))
    kuakeLink = db.Column(db.String(200))
    kuakeLinkPwd = db.Column(db.String(200))
    install = db.Column(LONGTEXT)
    feature = db.Column(LONGTEXT)
    mtime = db.Column(db.DateTime)

    def keys(self):
        return 'id', 'softName', 'softDesc', 'softSize',' softLanguage', 'issue', 'copyright', 'baiduLink', 'softURL',\
            'baiduLinkPwd', 'aliyunLink', 'aliyunLinkPwd', 'kuakeLink', 'kuakeLinkPwd', 'install', 'feature', 'mtime'

    def __getitem__(self, item):
        return getattr(self, item)

    def to_dict(self):
        return {i.name: getattr(self, i.name) for i in self.__table__.columns}
