.. _crevass-api:

API Reference
*****************
Here you can find documentation on all classes and their methods in Surround.

.. _assembler:   

Assembler
========

.. autodata:: crevass.assembler.Assembler
    :no-value:

    .. automethod:: crevass.assembler.Assembler.init_assembler
    .. automethod:: crevass.assembler.Assembler.run
    .. automethod:: crevass.assembler.Assembler.set_config
    .. automethod:: crevass.assembler.Assembler.set_stages
    .. automethod:: crevass.assembler.Assembler.set_finaliser
    .. automethod:: crevass.assembler.Assembler.set_metrics


.. automodule:: surround

BaseConfig
==========
    
.. autodata:: surround.config.BaseConfig       
    :no-value:

SurroundConfig
==============

.. autodata:: surround.config.SurroundConfig       
    :no-value:

@config
=======

.. autodecorator:: surround.config.config

load_config
===========

.. autofunction:: surround.config.load_config
 
State                              
=====
                
.. autoclass:: surround.State        
    :members:                   

.. automodule:: surround.stage

Stage
=====
    
.. autoclass:: surround.stage.Stage
    :members:

Estimator
=========

.. autoclass:: surround.stage.Estimator
    :members:

Runner
=======
.. autoclass:: surround.runners.Runner  
    :members:

