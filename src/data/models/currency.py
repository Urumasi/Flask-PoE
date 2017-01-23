from ..currency_mixin import CurrencyMixin
from ..mixins import CRUDModel

class Alt(CurrencyMixin, CRUDModel):
    __tablename__ = "c_alt"
    name = "Orb of Alteration"
    alt_name = "alt"
    cid = 1

class Fusing(CurrencyMixin, CRUDModel):
    __tablename__ = 'c_fusing'
    name = "Orb of Fusing"
    alt_name = "fusing"
    cid = 2

class Alchemy(CurrencyMixin, CRUDModel):
    __tablename__ = "c_alch"
    name = "Orb of Alchemy"
    alt_name = "alch"
    cid = 3

class Chaos(CurrencyMixin, CRUDModel):
    __tablename__ = "c_chaos"
    name = "Chaos Orb"
    alt_name = "chaos"
    cid = 4

class GCP(CurrencyMixin, CRUDModel):
    __tablename__ = "c_gcp"
    name = "Gemcutter's Prism"
    alt_name = "gcp"
    cid = 5

class Exalt(CurrencyMixin, CRUDModel):
    __tablename__ = "c_exalt"
    name = "Exalted Orb"
    alt_name = "exalt"
    cid = 6

class Chroma(CurrencyMixin, CRUDModel):
    __tablename__ = "c_chroma"
    name = "Chromatic Orb"
    alt_name = "chroma"
    cid = 7

class Jew(CurrencyMixin, CRUDModel):
    __tablename__ = "c_jew"
    name = "Jeweller's Orb"
    alt_name = "jew"
    cid = 8

class Chance(CurrencyMixin, CRUDModel):
    __tablename__ = "c_chance"
    name = "Orb of Chance"
    alt_name = "chance"
    cid = 9

class Chisel(CurrencyMixin, CRUDModel):
    __tablename__ = "c_chisel"
    name = "Cartographer's Chisel"
    alt_name = "chisel"
    cid = 10

class Scour(CurrencyMixin, CRUDModel):
    __tablename__ = "c_scour"
    name = "Orb of Scouring"
    alt_name = "scour"
    cid = 11

class Blessed(CurrencyMixin, CRUDModel):
    __tablename__ = "c_blessed"
    name = "Blessed Orb"
    alt_name = "blessed"
    cid = 12

class Regret(CurrencyMixin, CRUDModel):
    __tablename__ = "c_regret"
    name = "Orb of Regret"
    alt_name = "regret"
    cid = 13

class Regal(CurrencyMixin, CRUDModel):
    __tablename__ = "c_regal"
    name = "Regal Orb"
    alt_name = "regal"
    cid = 14

class Divine(CurrencyMixin, CRUDModel):
    __tablename__ = "c_divine"
    name = "Divine Orb"
    alt_name = "divine"
    cid = 15

class Vaal(CurrencyMixin, CRUDModel):
    __tablename__ = "c_vaal"
    name = "Vaal Orb"
    alt_name = "vaal"
    cid = 16

class Wisdom(CurrencyMixin, CRUDModel):
    __tablename__ = "c_wisdom"
    name = "Scroll of Wisdom"
    alt_name = "wisdom"
    cid = 17

class Portal(CurrencyMixin, CRUDModel):
    __tablename__ = "c_portal"
    name = "Portal Scroll"
    alt_name = "portal"
    cid = 18

class Scrap(CurrencyMixin, CRUDModel):
    __tablename__ = "c_scrap"
    name = "Armourer's Scrap"
    alt_name = "scrap"
    cid = 19

class Whetstone(CurrencyMixin, CRUDModel):
    __tablename__ = "c_whetstone"
    name = "Blacksmith's Whetstone"
    alt_name = "whetstone"
    cid = 20

class Bauble(CurrencyMixin, CRUDModel):
    __tablename__ = "c_bauble"
    name = "Glassblower's Bauble"
    alt_name = "bauble"
    cid = 21

class Trans(CurrencyMixin, CRUDModel):
    __tablename__ = "c_trans"
    name = "Orb of Transmutation"
    alt_name = "trans"
    cid = 22

class Aug(CurrencyMixin, CRUDModel):
    __tablename__ = "c_aug"
    name = "Orb of Augmentation"
    alt_name = "aug"
    cid = 23

class Mirror(CurrencyMixin, CRUDModel):
    __tablename__ = "c_mirror"
    name = "Mirror of Kalandra"
    alt_name = "mirror"
    cid = 24

class Eternal(CurrencyMixin, CRUDModel):
    __tablename__ = "c_eternal"
    name = "Eternal Orb"
    alt_name = "eternal"
    cid = 25

class Perandus(CurrencyMixin, CRUDModel):
    __tablename__ = "c_perandus"
    name = "Perandus Coin"
    alt_name = "perandus"
    cid = 26

CurrencyTypes = [Alt, Fusing, Alchemy, Chaos, GCP, Exalt, Chroma, Jew, Chance, Chisel, Scour, Blessed, Regret, Regal, Divine, Vaal, Wisdom, Portal, Scrap, Whetstone, Bauble, Trans, Aug, Mirror, Eternal, Perandus]