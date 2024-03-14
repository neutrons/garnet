Reduction Plan
===================

The schema of the Reduction Plan is described in `Data Dictionary Reduction Plan <https://ornlrse.clm.ibmcloud.com/rm/web#action=com.ibm.rdm.web.pages.showArtifactPage&artifactURI=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Fresources%2FTX_FsGEMM9tEe6kustJDRk6kQ&vvc.configuration=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Fcm%2Fstream%2F_DEcs8OHJEeyU5_2AJWnXOQ&componentURI=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Frm-projects%2F_DADVIOHJEeyU5_2AJWnXOQ%2Fcomponents%2F_DEP4oOHJEeyU5_2AJWnXOQ>`_.
Every parameter below is collected during the reduction plan creation, besides ub_matrix and peaks_ws
that are calculated during the UB Matrix/Peaks Finding step.

.. mermaid::

 classDiagram
    ReductionPlanModel "1" --> "1" InstrumentModel
    ReductionPlanModel "1" --> "1" CalibrationModel
    ReductionPlanModel "1" -->"1" NormalizationModel

    class ReductionPlanModel{
        +String name
        +String run_ranges
        +List~number~ wavelength
        +String mask_filename
        +String background_filename
        +String grouping
        +String reduction_plan_filename
        +Mantid:OrientedLattice ub_matrix
        +Mantid:PeaksWorkspace peaks_ws
    }
    class InstrumentModel{
        +String name
        +(TBD) settings
    }
    class CalibrationModel{
        +String detector_filename
        +String tube_filename
    }
    class NormalizationModel{
        +String flux_filename
        +String solid_angle_filename
    }

|