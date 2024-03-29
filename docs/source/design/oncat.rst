OnCat Schema
===================

The OnCat is described in `Data Dictionary OnCat <https://ornlrse.clm.ibmcloud.com/rm/web#action=com.ibm.rdm.web.pages.showArtifactPage&artifactURI=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Fresources%2FTX_X6q9wNStEe6uLrx4w2K0Ew&vvc.configuration=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Fcm%2Fstream%2F_DEcs8OHJEeyU5_2AJWnXOQ&componentURI=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Frm-projects%2F_DADVIOHJEeyU5_2AJWnXOQ%2Fcomponents%2F_DEP4oOHJEeyU5_2AJWnXOQ>`_

Related APIS:

- experiment_list: oncat.Experiment.list(facility=<facility>, instrument=<instrument>)
- experiment_info: oncat.Experiment.retrieve(experiment=<experiment>,facility=<facility>, instrument=<instrument>)
- data_files: oncat.Datafile.list(facility=<facility>, instrument=<instrument>, experiment=<experiment>, projection=<projection>, exts=<ext>)


.. mermaid::

 classDiagram
    OnCatModel "1" o--"N" ExperimentModel
    ExperimentModel "1" o--"N" RunModel
    OnCatModel "1" -->"1" InstrumentModel
    InstrumentModel "1" o--"1" ProjectionFieldModel
    InstrumentModel "1" o--"N" GoniometerAngleModel
    ProjectionFieldModel "1" o--"N" GoniometerAngleModel
    RunModel "1" o--"N" GoniometerAngleKeyValueModel
    GoniometerAngleModel "1" *--"1" GoniometerAngleKeyValueModel

    class OnCatModel{
        +InstrumentModel instrument
        -String user_session
        +List~ExperimentModel~ experiment_list

    }

    class InstrumentModel{
        +String facility
        +String filesystem_name
        +String reference_name
        +List~Number~[1|2] wavelength
        +String raw_file_format
        +List~GoniometerAngleModel~ goniometer_settings
        +ProjectionFieldModel run_schema

    }
    class GoniometerAngleModel{
        +String name
        +String reference_name
        +List~Number~[3] direction
        +Number sense
        +Bool used_in_goniometer_setting
        get_angle_field_name()
    }
    class ProjectionFieldModel{
        +String grouping_field_name
        +String run_number_field_name
        +String scale_field_name
        +List~GoniometerAngleModel~ goniometer_angle_field_names
    }
    class ExperimentModel{
        +String ipts_number
        +List~RunModel~ run_list
    }

    class RunModel{
        +String run_number
        +String grouping
        +String scale
        +String run_file_extension
        +List~GoniometerAngleKeyValueModel~ goniometer_angles_avg

    }
    class GoniometerAngleKeyValueModel{
        +GoniometerAngleModel angle_key
        +String angle_value
    }
