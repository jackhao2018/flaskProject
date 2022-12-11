from exts import db

class UpdateModel(db.Model):
    __tablename__ = "updatemenu"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='菜单ID')
    menu_name = db.Column(db.String(20), comment='菜单名称')
    menu_code = db.Column(db.String(20), comment='菜单栏code')
    menu_action = db.Column(db.String(100), comment='菜单操作')
    mtime = db.Column(db.Date, comment='创建时间')

    @property
    def keys(self):
        return 'id', 'menu_name', 'menu_code', 'menu_action', 'mtime'

    def __getitem__(self, item):
        return getattr(self, item)

    def to_dict(self):
        return {i.name: getattr(self, i.name) for i in self.__table__.columns}

class UpdateChildrenModel(db.Model):
    __tablename__ = "childrenmenu"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    menu_id = db.Column(db.Integer(), comment='菜单ID')
    children_code = db.Column(db.String(50), comment='子菜单code')
    children_name = db.Column(db.String(20), comment='子菜单名称')
    children_action = db.Column(db.String(200), comment='子菜单对应地址')
    mtime = db.Column(db.Date, comment='创建时间')

    @property
    def keys(self):
        return 'id', 'menu_id', 'children_name', 'children_code', 'children_action', 'mtime'

    def __getitem__(self, item):
        return getattr(self, item)

    def to_dict(self):
        return {i.name: getattr(self, i.name) for i in self.__table__.columns}
