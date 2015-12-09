from Testing.makerequest import makerequest
from plone import api
from zope.component.hooks import setHooks
from zope.component.hooks import setSite
import Zope2
import logging
import sys
import transaction

log = logging.getLogger()


class ConsoleScript(object):
    def __call__(self, config_file, run_as):
        Zope2.Startup.run.configure(config_file)
        self.app = makerequest(Zope2.app())
        setHooks()
        self.portal = self.app.objectValues('Plone Site')[0]
        setSite(self.portal)

        log.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        log.addHandler(handler)

        with api.env.adopt_user(username=run_as):
            self.run()
        transaction.commit()

    def run(self):
        raise NotImplementedError
