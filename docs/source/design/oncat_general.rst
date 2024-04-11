.. _pyoncat_general:

PyOnCat General Model
=======================

This is a generalization of :ref:`PyOnCatSchema <pyoncat>`, in case it can be used for other applications other than garnet that want to achieve a similar functionality.

The detailed Instrument model is found here :ref:`Intrument <instrument>`.

Related APIS:

- experiment_list: oncat.Experiment.list(facility=<facility>, instrument=<instrument>)
- experiment_info: oncat.Experiment.retrieve(experiment=<experiment>,facility=<facility>, instrument=<instrument>)
- data_files: oncat.Datafile.list(facility=<facility>, instrument=<instrument>, experiment=<experiment>, projection=<projection>, exts=<ext>)


.. mermaid::

 classDiagram
    PyOnCatModel "1" o--"N" ExperimentModel
    ExperimentModel "1" o--"N" RunModel
    PyOnCatModel "1" -->"1" InstrumentModel
    RunModel "1" *--"N<=170" ProjectionFieldKeyValueModel

    class PyOnCatModel{
        +InstrumentModel instrument
        -PyOnCat:ONCat oncat_agent
        +String data_source_filepath
        +List~ExperimentModel~ experiment_list
        +ExperimentModel selected_experiment
        +get_experiments()
    }

    class InstrumentModel{
        <>
    }


    class ExperimentModel{
        +String ipts_number
        +List~RunModel~ run_list
        +get_run_list()
    }

    class RunModel{
        +String run_number
        +List~ProjectionFieldKeyValueModel~ fields
        +get_run_data()

    }
    class ProjectionFieldKeyValueModel{
        +String field_key
        +String field_value
    }
