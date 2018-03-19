# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['Production']


class Production:
    __metaclass__ = PoolMeta
    __name__ = 'production'

    @classmethod
    def assign_try(cls, productions):
        for production in productions:
            for move in production.inputs:
                lot_required = ('production'
                        in [t.code for t in move.product.lot_required]
                    or move.product.lot_is_required(move.from_location,
                        move.to_location))
                if move.allow_split_lot_expiry and lot_required:
                    move._split_by_lot_expiry()
        return super(Production, cls).assign_try(productions)
