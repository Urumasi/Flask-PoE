from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from sqlalchemy import desc

from .database import db

class CurrencyMixin(object):
    id = Column(Integer, primary_key=True)
    alt = Column(String(16))
    fusing = Column(String(16))
    alch = Column(String(16))
    chaos = Column(String(16))
    gcp = Column(String(16))
    exalt = Column(String(16))
    chroma = Column(String(16))
    jew = Column(String(16))
    chance = Column(String(16))
    chisel = Column(String(16))
    scour = Column(String(16))
    blessed = Column(String(16))
    regret = Column(String(16))
    regal = Column(String(16))
    divine = Column(String(16))
    vaal = Column(String(16))
    wisdom = Column(String(16))
    portal = Column(String(16))
    scrap = Column(String(16))
    whetstone = Column(String(16))
    bauble = Column(String(16))
    trans = Column(String(16))
    aug = Column(String(16))
    mirror = Column(String(16))
    eternal = Column(String(16))
    perandus = Column(String(16))

    @classmethod
    def get_latest(cls):
        o = db.session.query(cls).order_by(desc(cls.id)).first()
        if o is None:
            return cls()
        return o
