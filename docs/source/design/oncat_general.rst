PyOnCat General Model
===================

Related APIS:

- experiment_list: oncat.Experiment.list(facility=<facility>, instrument=<instrument>)
- experiment_info: oncat.Experiment.retrieve(experiment=<experiment>,facility=<facility>, instrument=<instrument>)
- data_files: oncat.Datafile.list(facility=<facility>, instrument=<instrument>, experiment=<experiment>, projection=<projection>, exts=<ext>)


.. mermaid::

 classDiagram
    OnCatModel "1" o--"N" ExperimentModel
    ExperimentModel "1" o--"N" RunModel
    OnCatModel "1" -->"1" InstrumentModel
    RunModel "1" o--"N<=170" ProjectionFieldKeyValueModel

    class OnCatModel{
        +InstrumentModel instrument
        -Pyoncat:ONCat oncat_agent
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
