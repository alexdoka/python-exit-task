Script goal is capturing and counting tags from the site. You can either
use terminal version or UI. There is possibility to use aliases for
sites (you can edit it in file **synonims.yaml**)

1 step.
~~~~~~~

First step is creating Db for tags.

.. code:: bash

   tagcounter.py --createdb

2 step
~~~~~~

To use terminal version (to load tags info to DB), you can run commans
like:

.. code:: bash

   tagcounter.py --get google.com  
   # or if use alias
   tagcounter.py --get tut

.. _step-1:

3 step
~~~~~~

To show info from DB use :

.. code:: bash

   tagcounter.py --show google.com  
   # or if use alias
   tagcounter.py --show tut

If you run script without parameters, program will start with UI, with
the same functionality.
