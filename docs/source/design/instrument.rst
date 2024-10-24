.. _instrument:

Instrument Model
=======================

IN PROGRESS

The Instrument model is described in `Data Dictionary Instrument Configuration <https://ornlrse.clm.ibmcloud.com/rm/web#action=com.ibm.rdm.web.pages.showArtifactPage&artifactURI=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Fresources%2FTX_gl6-gMwZEe6kustJDRk6kQ&componentURI=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Frm-projects%2F_DADVIOHJEeyU5_2AJWnXOQ%2Fcomponents%2F_DEP4oOHJEeyU5_2AJWnXOQ&vvc.configuration=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Fcm%2Fstream%2F_DEcs8OHJEeyU5_2AJWnXOQ>`_.

The BaseInstrumentModel defines each physical instrument and the InstrumentInfoModel defines the configuration settings used for one or more experiments.

.. mermaid::

 classDiagram
    BaseInstrumentModel <|-- InstrumentInfoModel
    InstrumentInfoModel "1" *--"1" InstrumentProjectionRunSchema
    InstrumentInfoModel "1" *--"N<=3" InstrumentGoniometerAngleModel

    class BaseInstrumentModel{
        <<Abstract>>
        +String facility
        +String filesystem_name
        +String reference_name
        +create()

    }

    class InstrumentInfoModel{
        +String state_info
        +List~Number~[1|2] wavelength
        +String raw_file_format
        +List~InstrumentGoniometerAngleModel~ goniometer_settings
        +InstrumentProjectionRunSchema run_schema
        +create()

    }

    class InstrumentGoniometerAngleModel{
        +String name
        +String reference_name
        +List~Number~[3] direction
        +Number sense
        +Bool used_in_goniometer_setting
        +get_angle_field_name()
    }
    class InstrumentProjectionRunSchema{
        +grouping_field
        +run_number_field
        +scale_field
    }

The InstrumentInfo is created from the InstrumentConfiguration Settings. Based on the information, we can create the following instruments:
    * SNAP
    * CORELLI
    * TOPAZ
    * MANDI
    * WAND2
    * DEMAND

The InstrumentInfoModel model captures the changes in the configuration parameters for a specific instrument, e.g. DEMAND can have two InstrumentInfoObjects
with different parameters. The state_info (optionally) includes the description of the change/upgrade for that instrument.

.. mermaid::

    classDiagram
        InstrumentInfoModel <|-- SNAPInfo
        InstrumentInfoModel <|-- CORELLIInfo
        InstrumentInfoModel <|-- TOPAZInfo
        InstrumentInfoModel <|-- MANDIInfo
        InstrumentInfoModel <|-- WAND2Info
        InstrumentInfoModel <|-- DEMANDInfo

        class InstrumentInfoModel{
            <>
        }

        class SNAPInfo{
            <>
        }
        class CORELLIInfo{
            <>
        }
        class TOPAZInfo{
            <>
        }
        class MANDIInfo{
            <>
        }
        class WAND2Info{
            <>
        }
        class DEMANDInfo{
            <>
        }
