Instrument Schema
=======================

The Instrument model is described in `Data Dictionary Instrument Configuration <https://ornlrse.clm.ibmcloud.com/rm/web#action=com.ibm.rdm.web.pages.showArtifactPage&artifactURI=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Fresources%2FTX_gl6-gMwZEe6kustJDRk6kQ&componentURI=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Frm-projects%2F_DADVIOHJEeyU5_2AJWnXOQ%2Fcomponents%2F_DEP4oOHJEeyU5_2AJWnXOQ&vvc.configuration=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Fcm%2Fstream%2F_DEcs8OHJEeyU5_2AJWnXOQ>`_.

.. mermaid::

 classDiagram
    InstrumentModel "1" o--"1" ProjectionFieldModel
    InstrumentModel "1" o--"N" GoniometerAngleModel
    ProjectionFieldModel "1" o--"N" GoniometerAngleModel

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
