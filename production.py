# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta, Pool

__all__ = ['Production']


class Production(metaclass=PoolMeta):
    __name__ = 'production'

    @classmethod
    def assign_try(cls, productions):
        Move = Pool().get('stock.move')
        moves = []
        for production in productions:
            for move in production.inputs:
                if move.product.lot_required:
                    lot_required = ('production' in [
                        t for t in move.product.lot_required])
                else:
                    lot_required = (move.product.lot_is_required(
                            move.from_location, move.to_location))
                if move.allow_split_lot_expiry and lot_required:
                    moves.append(move)
        Move._split_by_lot_expiry(moves, assign=True)
        return super(Production, cls).assign_try(productions)
