from project import db, app


class SharingTypeVO(db.Model):
    __tablename__ = 'sharingTypemaster'
    sharingTypeId = db.Column('sharingTypeId', db.Integer, primary_key=True, autoincrement=True)
    sharingTypeName = db.Column('sharingTypeName', db.String(100))

    def as_dict(self):
        return {
            'sharingTypeId': self.sharingTypeId,
            'sharingTypeName': self.sharingTypeName,

        }


# db.create_all()
with app.app_context():
    db.create_all()
