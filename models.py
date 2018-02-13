from app import db
import enum


class ClientChoice(enum.Enum):
    ClientA = 'ClientA'
    ClientB = 'ClientB'
    ClientC = 'Clientc'


class TargetAreaChoice(enum.Enum):
    Policies = 'Policies'
    Billing = 'Billing'
    Claims = 'Claims'
    Reports = 'Reports'


class Features(db.Model):
    __table_args__ = {'extend_existing': True}
    ClientPriority = db.Column(db.Integer, primary_key =True, autoincrement =True)
    Title = db.Column(db.String(100), unique=True)
    Description = db.Column(db.String(1000))
    Client = db.Column(db.Enum(ClientChoice), nullable=False)
    TargetDate = db.Column(db.String(20))
    TargetArea = db.Column(db.Enum(TargetAreaChoice), nullable=False)

    def __repr__(self):
        return '<Title: {self.Title}>'
