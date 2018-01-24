from random import choice
from pyknow import *


class Wasserstand(Fact):
    pass


class Wasserdruck(Fact):
    pass


class Wasserentnahme(Fact):
    pass


class Sonne(Fact):
    pass


class Regen(Fact):
    pass


class Niederschlag(Fact):
    pass


class Wasserknappheit(Fact):
    pass


class WasserContainer(KnowledgeEngine):
    @Rule(Wasserstand(stand='niedrig'))
    def wasserstand_niedrig(self):
        print('wasserstand_niedrig')
        self.declare(Wasserdruck(druck='niedrig'))

    @Rule(Wasserstand(stand='hoch') & Wasserentnahme(stand='klein'))
    def wasserstand_hoch(self):
        print('wasserstand_hoch')
        self.declare(Wasserdruck(druck='hoch'))

    @Rule(Wasserentnahme(entnahme='groß'))
    def wasserentnahme_groß(self):
        print('wasserentnahme_groß')
        self.declare(Wasserdruck(druck='niedrig'))

    @Rule(Sonne(scheint=True))
    def sonne_scheint(self):
        print('sonne_scheint')
        self.declare(Wasserentnahme(entnahme='groß'))

    @Rule(Regen(regnet=True))
    def regen_regnet(self):
        print('regen_regnet')
        self.declare(Wasserentnahme(entnahme='klein'))

    @Rule(Niederschlag(niederschlag='ergiebig'))
    def niederschlag_ergiebig(self):
        print('niederschlag_ergiebig')
        self.declare(Wasserstand(stand='hoch'))

    @Rule(Niederschlag(niederschlag='gering'))
    def niederschlag_gering(self):
        print('niederschlag_gering')
        self.declare(Wasserstand(stand='niedrig'))

    @Rule(Wasserstand(stand='niedrig') & Wasserentnahme(entnahme='groß'))
    def wasserknappheit(self):
        print('wasserknappheit')
        self.declare(Wasserknappheit(knapp=True))


def a():
    print('a')
    engine = WasserContainer()
    engine.reset()
    engine.declare()
    engine.run()


def b():
    print('b')
    engine = WasserContainer()
    engine.reset()
    engine.declare(Sonne(scheint=True))
    engine.run()


def c():
    print('c')
    engine = WasserContainer()
    engine.reset()
    engine.declare(*[Regen(regnet=True), Niederschlag(niederschlag='ergiebig')])
    engine.run()


def d():
    print('c')
    engine = WasserContainer()
    engine.reset()
    engine.declare(*[Sonne(scheint=True), Niederschlag(niederschlag='ergiebig')])
    engine.run()


if __name__ == "__main__":
    d()
