Production: Split input moves by available Lots expiry dates
============================================================

Assign automatically the Lot, taking in account the expiry dates, to the input
moves of a production for the products configured to require lots on
production.

The available lots are ordered by expiry dates and assigned starting by the one
with the nearest expiry date and splitting the input move when necessary.
