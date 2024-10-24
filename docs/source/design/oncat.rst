.. _pyoncat:

PyOnCat Model
===================

IN PROGRESS

The PyOnCat is described in `Data Dictionary OnCat <https://ornlrse.clm.ibmcloud.com/rm/web#action=com.ibm.rdm.web.pages.showArtifactPage&artifactURI=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Fresources%2FTX_X6q9wNStEe6uLrx4w2K0Ew&vvc.configuration=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Fcm%2Fstream%2F_DEcs8OHJEeyU5_2AJWnXOQ&componentURI=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Frm-projects%2F_DADVIOHJEeyU5_2AJWnXOQ%2Fcomponents%2F_DEP4oOHJEeyU5_2AJWnXOQ>`_ .

The detailed Instrument model is found here :ref:`Instrument <instrument>`.
Related APIS:

- experiment_list: oncat.Experiment.list(facility=<facility>, instrument=<instrument>)
- experiment_info: oncat.Experiment.retrieve(experiment=<experiment>,facility=<facility>, instrument=<instrument>)
- data_files: oncat.Datafile.list(facility=<facility>, instrument=<instrument>, experiment=<experiment>, projection=<projection>, exts=<ext>)


.. mermaid::

 classDiagram
    PyOnCatModel "1" o--"N" ExperimentModel
    ExperimentModel "1" o--"N" RunModel
    PyOnCatModel "1" -->"1" InstrumentInfoModel
    RunModel "1" *--"N<=3" GoniometerAngleKeyValueModel
    RunModel "1" *--"3" ProjectionFieldKeyValueModel

    class PyOnCatModel{
        +InstrumentInfoModel instrument
        -PyOnCat:ONCat oncat_agent
        +String data_source_filepath
        +Number selected_experiment_index
        +List~ExperimentModel~ experiment_list
        +get_experiments()
        +add_agent()
        +add_instrument()
        +select_experiment()
        +add_datasource_filepath()
    }
    class InstrumentInfoModel{
        <>
    }

    class ExperimentModel{
        +String ipts_number
        +List~RunModel~ run_list
        +get_run_list()
        +calculate_run_plot()

    }

    class RunModel{
        +String run_number
        +List~GoniometerAngleKeyValueModel~ goniometer_angles_avg
        +List~ProjectionFieldKeyValueModel~ fields
        +get_run_data()

    }
    class GoniometerAngleKeyValueModel{
        +String angle_key
        +String angle_value
    }

    class ProjectionFieldKeyValueModel{
        +String field_key
        +String field_value
    }
