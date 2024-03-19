Reduction Plan Schema
=======================

The Reduction Plan is described in `Data Dictionary Reduction Plan <https://ornlrse.clm.ibmcloud.com/rm/web#action=com.ibm.rdm.web.pages.showArtifactPage&artifactURI=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Fresources%2FTX_FsGEMM9tEe6kustJDRk6kQ&vvc.configuration=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Fcm%2Fstream%2F_DEcs8OHJEeyU5_2AJWnXOQ&componentURI=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Frm-projects%2F_DADVIOHJEeyU5_2AJWnXOQ%2Fcomponents%2F_DEP4oOHJEeyU5_2AJWnXOQ>`_.
Every parameter below is collected during the reduction plan creation, besides ub_matrix that is calculated during the UB Matrix/Peaks Finding step.

.. mermaid::

 classDiagram
    ReductionPlanModel "1" --> "1" InstrumentModel
    ReductionPlanModel "1" --> "1" CalibrationModel
    ReductionPlanModel "1" -->"1" NormalizationModel

    class ReductionPlanModel{
        +String name
        +InstrumentModel instrument
        +String experiment
        +String run_range
        +List~number~ wavelength
        +String mask_filepath
        +String background_filepath
        +String grouping
        +String reduction_plan_filepath
        +CalibrationModel calibration
        +NormalizationModel vanadium
        +Mantid:OrientedLattice ub_matrix
    }
    class InstrumentModel{
        +String facility
        +String filesystem_name
        +String reference_name
        +List(1|2)~Number~ wavelength
        +String raw_file_format
        +String goniometer
    }
    class CalibrationModel{
        +String detector_filepath
        +String tube_filepath
    }
    class NormalizationModel{
        +String flux_filepath
        +String solid_angle_filepath
    }

|