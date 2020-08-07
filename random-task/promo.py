from datetime import datetime

Now = datetime.now()


class Promo:
    """Promo Object
    arg:
    name: string
    expires: datetime

    methods:
     expired: checking validity of the promo date

    """

    def __init__(self, name, expires = Now):
        """Method for initializing a Promo object
        self.name = name
        self.expires = expires
    @property
    def expired(self):
        """ Checking the validity of the promo object

        Returns: True or False

        """
        return datetime.now() > self.expires
