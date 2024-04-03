.. _pyoncat_general:

PyOnCat General Model
=======================

This is a generalization of :ref:`PyOnCatSchema <pyoncat>`, in case it can be used for other applications other than garnet that want to achieve a similar functionality.

Related APIS:

- experiment_list: oncat.Experiment.list(facility=<facility>, instrument=<instrument>)
- experiment_info: oncat.Experiment.retrieve(experiment=<experiment>,facility=<facility>, instrument=<instrument>)
- data_files: oncat.Datafile.list(facility=<facility>, instrument=<instrument>, experiment=<experiment>, projection=<projection>, exts=<ext>)


.. mermaid::

 classDiagram
    PyOnCatModel "1" o--"N" ExperimentModel
    ExperimentModel "1" o--"N" RunModel
    PyOnCatModel "1" -->"1" InstrumentModel
    RunModel "1" o--"N<=170" ProjectionFieldKeyValueModel

    class PyOnCatModel{
        +InstrumentModel instrument
        -Pyoncat:ONCat oncat_agent
        +String data_source_filepath
        +List~ExperimentModel~ experiment_list
        +ExperimentModel selected_experiment
        +get_experiments()
    }

    class InstrumentModel{
        TBD
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
