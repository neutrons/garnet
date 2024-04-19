.. _reduction_plan:

Reduction Plan Model
=======================

The Reduction Plan is described in `Data Dictionary Reduction Plan <https://ornlrse.clm.ibmcloud.com/rm/web#action=com.ibm.rdm.web.pages.showArtifactPage&artifactURI=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Fresources%2FTX_FsGEMM9tEe6kustJDRk6kQ&vvc.configuration=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Fcm%2Fstream%2F_DEcs8OHJEeyU5_2AJWnXOQ&componentURI=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Frm-projects%2F_DADVIOHJEeyU5_2AJWnXOQ%2Fcomponents%2F_DEP4oOHJEeyU5_2AJWnXOQ>`_.
Every parameter below is collected during the reduction plan creation, besides ub_matrix that is calculated during the UB Matrix/Peaks Finding step.

The detailed Instrument model is found here :ref:`Intrument <instrument>`.

.. mermaid::

 classDiagram
    ReductionPlanModel "N" -->"1" InstrumentModel
    ReductionPlanModel "1" *--"1" CalibrationModel
    ReductionPlanModel "1" *--"1" NormalizationModel

    class ReductionPlanModel{
        -String reduction_plan_id
        +String reduction_plan_name
        +InstrumentModel instrument
        +String experiment
        +String run_range
        +String mask_filepath
        +String background_filepath
        +String grouping
        +String reduction_plan_filepath
        +String data_source_filepath
        +CalibrationModel calibration
        +NormalizationModel vanadium
        +Mantid:OrientedLattice ub_matrix
        +get()
        +create()
        +edit()
        +delete()
        //(backend validation rules)
        +validate_mask()
        +validate_background()
        +validate_run_ranges()
        +reduction_plan_filepath()
    }

    class InstrumentModel{
        <>
    }


    class CalibrationModel{
        +String detector_filepath
        +String tube_filepath
        +get()
        +create()
        +edit()
        +delete()
        //(backend validation rules)
        +validate_detector()
        +validate_tube()
    }

    class NormalizationModel{
        +String flux_filepath
        +String solid_angle_filepath
        +get()
        +create()
        +edit()
        +delete()
        //(backend validation rules)
        +validate_flux()
        +validate_solid_angle()
    }

The above validation functions check the following before the Reduction Plan creation:

    * whether the files exist and have the correct extension
    * the run range files exist in the instrument/experiment filepath.
    * the reduction plan filepath is unique. In case of a new reduction plan with an exisiting filepath warning message is sent to the user to ask whether they want to override the existing one.

The reduction_plan_id is created and assigned during the Reduction Plan creation. It is a unique identifier that is passed along with the reduction plan name and any other necessary parameters between View and Model.

In case any of the above do not pass, an error message is sent and displayed to the user.

Below is the expected schema for the Reduction Plan saved in a file:

.. mermaid::

    classDiagram
        class ReductionPlanFile{
            +String Instrument
            +Number Experiment
            +String Run_Range
            +String Grouping
            +String UBFile
            +String VanadiumFile
            +String BackgroundFile
            +String FluxFile
            +String MaskFile
            +String DetectorCalibration
            +String TubeCalibration
        }

* If the data fields and values are correct, a new reduction plan object is created and its values are send and displayed to the user.

* If the data values are missing or invalid, a reduction plan object is not created. The parameters are sent and displayed to the user to fix them. A corresponding error message is displayed to promt the user to edit the parameters and then save the reduction plan.

* If data keys (fields) are missing, the file is considered corrupted. No parameters are loaded andan error message is sent and displayed to the user.
