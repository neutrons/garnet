OnCat Schema
===================

The OnCat is described in `OnCat <https://ornlrse.clm.ibmcloud.com/rm/web#action=com.ibm.rdm.web.pages.showArtifactPage&artifactURI=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Fresources%2FTX_FsGEMM9tEe6kustJDRk6kQ&vvc.configuration=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Fcm%2Fstream%2F_DEcs8OHJEeyU5_2AJWnXOQ&componentURI=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Frm-projects%2F_DADVIOHJEeyU5_2AJWnXOQ%2Fcomponents%2F_DEP4oOHJEeyU5_2AJWnXOQ>`_

Related APIS:

- experiment_list: oncat.Experiment.list(facility=<facility>, instrument=<instrument>)
- experiment_info: oncat.Experiment.retrieve(experiment=<experiment>,facility=<facility>, instrument=<instrument>)
- data_files: oncat.Datafile.list(facility=<facility>, instrument=<instrument>, experiment=<experiment>, projection=<projection>, exts=<ext>)


.. mermaid::

 classDiagram
    OnCatModel "1" --> "N" ExperimentModel
    ExperimentModel "1" --> "N" RunModel
    RunModel "1" -->"1" ProjectionFieldModel
    OnCatModel "1" -->"1" InstrumentModel

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
        +String goniometer
    }

    class ExperimentModel{
        +String ipts_number
        +List~RunModel~ run_list
    }

    class RunModel{
        +String run_number
        +List~ProjectionFieldModel fields
    }

    class ProjectionFieldModel{
        +String grouping_field_name
        +String run_number_field_name
        +String scale_field_name
        +List~String~ goniometer_angle_field_names
    }


