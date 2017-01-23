from sqlalchemy.schema import Column
from sqlalchemy.types import DateTime
from datetime import datetime

from ..database import db
from ..mixins import CRUDModel
from ..currency_mixin import CurrencyMixin

class Transaction(CurrencyMixin, CRUDModel):
    __tablename__ = "transactions"
    time = Column(DateTime, nullable=False)

    def __init__(self, currency={}):
        for k, v in currency.iteritems():
            setattr(self, k, v)
        self.time = datetime.now()