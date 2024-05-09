.. _ndip_reduction_plan:

======================
NDIP - Reduction Plan
======================

In this page, functionality related to the parameters of the Reduction Plan is handled. A reduction plan contains a set of parameters that are necessary to perform data reduction in the later steps/tabs. The ReductionPlan object is used to retrieve information along with any additional parameters. Thus, the ReductionPlan object is visible in every tab/step.

Overall, users can:
   * create a Reduction Plan
   * edit a Reduction Plan
   * create a new Reduction Plan from the parameters of the one displayed in Edit state
   * load a Reduction Plan from an exisiting file

Fields
--------

Below are the fields for creating/editing a Reduction Plan. They are grouped into two categories:
   * the main fields
   * the fields that are applicable only for the related instrument

In the latter case, they are only displayed when the associated instrument is selected by the user.

.. list-table:: Reduction Plan - Main Fields
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Type
     - Value Origin
     - Additional validation
     - Mandatory
   * - Reduction Plan
     - String
     -
     - filepath usage
     - yes
   * - Instrument
     - String
     - predefined choices from available instrument
     -
     - yes
   * - IPTS
     - Integer
     -
     - valid/existing filepath
     - yes
   * - Run Ranges
     - Comma-separated numbers and number ranges
     -
     - valid/existing filepath
     - yes
   * - Wavelength
     - Float
     - default value from instrument configuration
     - positive
     - yes
   * - Grouping
     - String
     - predefined choices from instrument configuration
     -
     - yes
   * - UB Matrix
     - String
     -
     - valid/existing filepath
     - yes
   * - Flux
     - String
     -
     - valid/existing filepath
     - no
   * - Solid Angle
     - String
     -
     - valid/existing filepath
     - no
   * - Mask
     - String
     -
     - valid/existing filepath
     - no
   * - Background
     - String
     -
     - valid/existing filepath
     - no
   * - Reduction Plan file
     - String
     -
     - valid/non-existing filepath
     - yes

.. list-table:: Reduction Plan - Instrument-specific fields
   :widths: 20 20 20 20 20 10
   :header-rows: 1

   * - Field
     - Type
     - Value Origin
     - Additional validation
     - Mandatory
     - Instruments
   * - Detector Callibration
     - String
     -
     - valid/existing filepath
     - no
     - SNAP, CORELLI, TOPAZ, MANDI
   * - Tube Callibration
     - String
     -
     - valid/existing filepath
     - no
     - CORELLI
   * - Experiment number in IPTS
     - Integer
     -
     - valid/existing filepath
     - yes
     - DEMAND
   * - Elastic
     - Bool
     - default false
     -
     - yes
     - CORELLI
   * - Offset
     - Float
     -
     -
     - no
     - CORELLI
   * - Wavelength Band
     - Float 2 numbers (min, max)
     - default values from instrument configuration
     - positive, min<max
     - yes
     - SNAP, CORELLI, TOPAZ, MANDI

In case detector and tube calibration are both hidden, the whole calibration section can be hidden, too.

Field Interactions
-------------------

* When the user selects an instrument, besides showing/hidding the above fields, data are retrieved from the instrument's configuration (example here: `Data Dictionary Instrument Configuration <https://ornlrse.clm.ibmcloud.com/rm/web#action=com.ibm.rdm.web.pages.showArtifactPage&artifactURI=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Fresources%2FTX_gl6-gMwZEe6kustJDRk6kQ&componentURI=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Frm-projects%2F_DADVIOHJEeyU5_2AJWnXOQ%2Fcomponents%2F_DEP4oOHJEeyU5_2AJWnXOQ&vvc.configuration=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Fcm%2Fstream%2F_DEcs8OHJEeyU5_2AJWnXOQ>`_):
   * Wavelength/Wavelength default value
   * Grouping dropdown choices
   * Detector, Tube, Flux, Solid Angle, Mask and Background starting folder filepaths for the filebrowser

* When the user selects (an instrument and) an experiment (ipts), then the recommended starting path for saving the reduction plan file is at: /<facility>/<instrument>/shared/<ipts>/garnet. The garnet folder needs to be created, if it does not exist.

Note: If the user has not selected an instrument yet, a default option should appear for every fileselect field.

Validation
----------

The following validations occur before the Reduction Plan creation:
   * required fields
   * field types
   * for files: filepath format, whether the files exist and have the correct extension
   * the run range files exist in the instrument/experiment filepath.
   * the IPTS folder exists in the instrument filepath
   * the reduction plan filepath is unique. In case of a new reduction plan with an exisiting filepath, a warning popup message is displayed to the user to ask whether they want to override the existing one.

Some of them are checked in the backend, while others are checked on the client side (before form submission) to provide an initial check.

Backend validations can include:
   * validations through Mantid algorithms
   * accesing the filesystem, e.g. file exists
   * reduction plan exceptions

Client side validation can include:
   * required fields
   * field types
   * filepath format
   * run range format
   * wavelength min < max

All required fields are marked with *\** on the left and "(required)" on the right to their label (name).
In case a field becomes invalid, it is marked with a red background border around the field box. A small error message appears below the field, too.
Additionally, the associated functionality of the button is deactivated (form is not submitted) until all the fields are valid and the required fields are filled-in.

After the form is submitted, any/all error from backend validation can appear as error message pop-up.

Create
-------

The user can land here from the menu item Reduction Plan-->Create or from the Home Page *Create Reduction Plan* button.
In this case all fields are empty.The associated wireframe is here:
`Garnet Wireframe Reduction Plan Create - Landing <https://share.balsamiq.com/c/ky236EHRwQatwHKMrYmGPp.png>`_.

As the user fills-in the form and selects the instrument other fields appear in the locations shows here: `Garnet Wireframe Reduction Plan Create - All Fields <https://share.balsamiq.com/c/k3kzkVXknAMdUExZWBGToq.png>`_.

Validations occured as described above. An additional validation rule here, is to check whether the user selects an exisiting (reduction plan) instead of a new one. A warning appears whether they would like to continue or not.
After a successfull form submission (*Save* button) a new ReductionPlan is created and the view is switched to Edit mode (Reduction Plan Edit page) for the newly-created reduction plan.

Edit
-----

The user can land here from the Home Page by selecting a recent reduction plan or through the *Reduction Plan* button from Normalization and Integration Pages.
The reduction plan parameters are shown and populated. The associated wireframe is displayed here:
`Garnet Wireframe Reduction Plan Edit <https://share.balsamiq.com/c/b1Hyb5ohybzsMdWKMa39gf.png>`_.
Regarding the instrument-specific fields, only the ones associated to the reduction plan's instrument are displayed with their values. The rest stay hidden.

Besides saving the plan, users can select to save a copy of an existing Reduction Plan, by selecting the "Save As" option. This button appears only in "Edit" mode.

Submission
-----------

* *Save* In order to save the reduction plan, the users click the *Save* button on the bottom of the form. Following the validation rules, the parameters are gathered and sent to the backend to create/edit the reduction plan.
* *Save As* In order to save a copy of the reduction plan parameters in a new file, the users click the *Save As* button on the bottom of the form. Following the validation rules, the parameters are gathered and sent to the backend to create the reduction plan. An additional validation rule here, is to check whether the user selects an exisiting (reduction plan) instead of a new one. A warning appears whether they would like to continue or not.


Load Reduction Plan - Browse
-------------------------------

In order to load a Reduction Plan file, the users click the associated *Browse* button. The filebrowser appears and users select a file.
A new ReductionPlan object is created in memory, the parameters are populated in the Reduction Plan Form and the view is switched to Edit mode (Reduction Plan Edit page).
