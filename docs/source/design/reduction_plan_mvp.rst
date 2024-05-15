.. _reduction_plan_mvp:

Reduction Plan Model-View-Presenter
========================================

The data, graphical interface and functionality components related to the first step
-- Reduction Plan Screen -- are described here. The related code
is organized in the Model-View-Presenter pattern.


ReductionPlanListModel
------------------------------

The Model is described in detail:

.. mermaid::

    classDiagram
        ReductionPlanTabModel "1" -->"1" ReductionPlanListModel
        ReductionPlanTabModel "1" -->"1" PyOnCatModel
        ReductionPlanListModel "1" o--"N" ReductionPlanModel
        ReductionPlanModel "N" -->"1" InstrumentInfoModel
        PyOnCatModel "1" -->"1" InstrumentInfoModel

        class ReductionPlanListModel{
            -String:selected_plan
            -List~ReductionPlanModel~ reduction_plan_list
            +add_reduction_plan()
            +remove_reduction_plan()
            +get_selected_plan()
            +set_selected_plan()
            +get_plans()

        }

        class ReductionPlanTabModel{
            +ReductionPlanListModel reduction_plan_list
            +PyOnCatModel pyoncat_data
            +add_instrument()
            +get_instrument()
        }


        class ReductionPlanModel{
            <>
        }

        class PyOnCatModel{
            <>
        }


The ReductionPlanListModel model contains the user's reduction plans and the one selected for
data reduction in further steps (ReductionPlanModel). Additionally, it maintains the list
of the instruments (InstrumentInfoModel) generated during the reduction plan creation process per user's selections.
Finally the runs of experiments with their fields based on the selected instrument and OnCat-related
information are stored (PyOnCatModel), too.
The selected plan (ReductionPlanModel) is passed for the next step.

There are a lot of dependencies on the selected instrument. We might have to consider a way to enforce user to select instrument,
before they continue with any other parameter.

ReductionPlanTab
--------------------

The View is described below:

.. mermaid::

    classDiagram
        ReductionPlanTab "1" -->"1" ReductionPlanTasksWidget
        ReductionPlanTab "1" -->"1" ReductionPlanWidget
        ReductionPlanTasksWidget "1" -->"1" ReductionPlanListWidget
        ReductionPlanWidget "1" -->"1" RunsWidget
        ReductionPlanWidget "1" -->"1" InstrumentDataWidget
        ReductionPlanWidget "1" -->"1" DataSourceWidget
        ReductionPlanWidget "1" -->"1" NormalizationWidget
        ReductionPlanWidget "1" -->"1" CalibrationWidget
        ReductionPlanWidget "1" -->"1" BaseButton
        ReductionPlanWidget "1" -->"1" BtnFileWidget
        ReductionPlanWidget "1" -->"1" SaveBtnFileWidget
        DataSourceWidget"1" -->"1" PyOnCatBtnFileWidget
        PyOnCatBtnFileWidget"1" --|>"1" BtnFileWidget
        SaveBtnFileWidget"1" --|>"1" BtnFileWidget
        CalibrationWidget "1" o--"2" BtnFileWidget
        NormalizationWidget "1" o--"4" BtnFileWidget

        class ReductionPlanTab{
            -Signal~str~:error_message_signal
            +ReductionPlanTasksWidget:reduction_plan_tasks
            +ReductionPlanWidget:reduction_plan
            +send_error_message()
            -show_error_message()
            +QStatusBar:status_bar
        }

        class ReductionPlanTasksWidget{
            +ReductionPlanListWidget:reduction_plan_list
            +QButton:load
            +QButton:create
            +QLabel:selected_reduction_plan
            +display_selected_reduction_plan()
            +load_reduction_plan()
            +create_reduction_plan()
            +clear_fields()
        }

        class ReductionPlanListWidget{
            <<QListWidget>>
            +String:reduction_plan_name
            -String:reduction_plan_id
            -QMenu:menu
            +QAction:copy
            +QAction:edit
            +QAction:delete
            +copy_reduction_plan()
            +edit_reduction_plan()
            +delete_reduction_plan()
            +get_plot_data()
        }

        class ReductionPlanWidget{
            -String:reduction_plan_id
            +QLabel:name_display
            +QLineEdit:name
            +QLabel:instrument_display
            +QComboBox:instrument
            +DataSourceWidget:data_source
            +RunsWidget:runs
            +InstrumentDataWidget:instrument
            +CalibrationWidget:calibration
            +BtnFileWidget: ub
            +QLabel:grouping_display
            +QComboBox:grouping
            +VanadiumWidget:vanadium
            +SaveBtnFileWidget:reduction_plan_save
            +BaseButton:reduction_plan_btn
            +create_reduction_plan()
            +update_data_for_instrument()
            +display_fields_for_instrument()
            +display_grouping_choices_for_instrument()

        }

        class BaseButton{
            <<QButton>>
            -List~String~:invalid_fields
            -activate_btn()
            -deactivate_btn()
            +add_invalid_field()
            +remove_invalid_field()
        }

        class DataSourceWidget{
            +QLabel:oncat_connection_status
            +PyOnCatQButton: oncat_login_btn
            +PyOnCatBtnFileWidget:oncat_filepath
            +display_oncat_connection_status()
            +validate_full_path_format()
        }

        class RunsWidget{
            +QLabel:ipts_display
            +QComboBox:ipts
            +QButton:ipts_refresh
            +QTableWidget:grouped_runs
            +QLabel:run_range_display
            +QLineEdit:run_range
            +Mantidqt:run_plot
            +display_experiments_for_instrument()
            +display_grouped_runs_for_experiment()
            +display_plot_data()
            +get_selected_run_range()
            +get_selected_experiment()
            +validate_run_ranges_format()
        }


        class InstrumentDataWidget{
            +QLabel:elastic_display
            +QCheckBox:elastic
            +QLabel:offset_display
            +QLineEdit:offset
            +QLabel:goniometer_table_display
            +QTableWidget:goniometer_table
            +QLabel:wavelength_display
            +QLineEdit~1|2~:wavelength
            +display_goniometer_table_for_instrument()
            +display_wavelength_for_instrument()
        }


        class CalibrationWidget{
            +BtnFileWidget: detector
            +BtnFileWidget: tube
        }


        class NormalizationWidget{
            +BtnFileWidget: flux
            +BtnFileWidget: solid_angle
            +BtnFileWidget: mask
            +BtnFileWidget: background
        }

        class PyOnCatBtnFileWidget{
            <<BtnFileWidget>>
            +update_full_path()
        }


        class SaveBtnFileWidget{
            <<BtnFileWidget>>
            +create_starting_folder()
        }

        class BtnFileWidget{
            -String: starting_path
            -String: starts_with
            -String: extension
            +QLabel: filename_display
            +QLineEdit:full_path
            +QButton-QFileDialog: file_browse_btn
            +get_full_path()
            +sync_full_path()
            +validate_file_extension()
            +set_starting_path()
            +show()
            +hide()
        }

The wireframe for the above class diagram is here: `Garnet Wireframe <https://balsamiq.cloud/sd2jtfw/prbeb2l/r2278>`_.

All validation related to invalid and required fields for the reduction plan submit (Add/Edit) button
are added here:

    #. required parameters; all fields marked with * in the wireframe are required for the reduction plan creation: name, instrument (InstrumentInfoModel), experiment, run_ranges, wavelength, grouping, reduction_plan_file and ipts_experiment_number only for DEMAND
    #. run range format
    #. wavelength format
    #. file path format of every file in: datasource, calibration, vanadium and ub and reduction plan file sections

Instrument-specific fields:

    There are certain fields that are hidden/displayed for specific instruments. Their visibility is handled at the time of the Instrument selection.
    These are the following:

        #. detector_filepath displayed for SNAP, CORELLI, TOPAZ and MANDI.
        #. tube_filepath displayed only for CORELLI.
        #. elastic displayed only for CORELLI.
        #. offset displayed only for CORELLI.
        #. ipts_experiment_number displayed only for DEMAND.
        #. wavelength (band) 2nd field displayed only for SNAP, CORELLI, TOPAZ, MANDI.

In case the selected reduction plan is in an invalid state, the next steps buttons/tabs are deactivated.
A reduction plan is created only and only if it is in a valid state.
In any other case, the user has to fix the parameters.

Tab Navigation:

    #. If the user has *not* provided a ub matrix filepath in the reduction plan, only the second Tab (UB Matrix/Peak) is activated.
    #. If the user has provided a ub matrix filepath, all Tabs are activated.

ReductionPlanTabPresenter
------------------------------

The Presenter is described below. It is connected with one model and view.

.. mermaid::

 classDiagram
    class ReductionPlanTabPresenter{
        -ReductionPlanTabModel:model
        -ReductionPlanTab:view
        (reduction plan related)
        +handle_new_reduction_plan()
        +handle_submit_reduction_plan(reduction_plan_parameters)
        +get_starting_path_for_reduction_plan(instrument,experiment)
        +handle_load_reduction_plan(reduction_plan_file)
        +handle_copy_reduction_plan_parameters(reduction_plan_id)
        +handle_edit_reduction_plan(reduction_plan_id)
        +handle_delete_reduction_plan(reduction_plan_id)

        (pyoncat related)
        +handle_oncat_connection()
        +handle_datasource_filepath(filepath)
        +handle_instrument_selection(instrument)
        +handle_experiment_selection(experiment)
        +handle_run_selection(run_range)
        +update_grouped_runs(experiment, use_cached_runs=True)

    }

All the functions orchestrate the interaction between the view and the model.
First, the ReductionPlanModel and then the PyOnCat related functionality are defined.
Most of them are triggered by a User's action on the View, e.g. by clicking a button and then
the related function is called, where the majority of the flow between M-V is coordinated.
The details are presented in the next section.

In the first screen various functionality and states are accomplished:

    * List of Reduction Plans
    * Create a Reduction Plan
    * Edit a Reduction Plan
    * Copy the Parameters of a Reduction Plan
    * Delete a Reduction Plan
    * Show the selected Reduction Plan

The selected_reduction_plan (name) label in the View should always be in sync with the selected_plan (id) in the Model side.
The selected_plan field stores the unique identifier (id) of the selected (current) valid ReductionPlan object that the User can see.

To distinsguish between the states: Create and Edit, we check the selected_plan field in ReductionPlanListModel.
    * If there is no selected plan, we are in Create state. Users need to provide a unique filepath in this state, else a Warning Message pop-up <File already exists. Do you want to override it?>.
    * If there is a selected plan, we are in Edit state. Users cannot update the filepath in this state.

Additionally, the following functionality related to experimentdat data is accomplished through PyOnCat:
    * OnCat connection
    * Read the same metadata as OnCat, without connecting, by going through the files of a user-specified folder
    * List of Experiments per Selected Instrument(s)
    * List of Runs per Selected Experiment(s)
    * Run meta data retrieval for every Run of the Selected Experiment(s)
    * Group Runs per specific field and display them
    * Retrieve grouped run per users trigger-button
    * Plot creation based on the Runs' meta data

Details are described  here  :ref:`PyOnCatModelMVP <pyoncat_mvp>`.

.. _reduction_mvpi:

M-V-P Interactions
--------------------

The M-V-P interactions are described and grouped by functionality:

#. Create a new reduction plan button: handle_new_reduction_plan()

    .. mermaid::

        sequenceDiagram
            participant View
            participant Presenter
            participant Model
            Note over View,Model: New Reduction Plan
            View->>Presenter: User clicks the "Create new Reduction Plan" button
            Presenter->>View: Clear all parameters of the reduction plan screen
            Presenter->>Model: Unselect current reduction plan
            Note right of Model: Update selected plan id ("")
            Model->>Presenter: Return status
            Presenter->>View: Return status
            Note left of View: Status Success Message <Create a new reduction plan.> (timeout=5sec)

    When the user first lands in the page, the Tab is in this mode, too.
    The success message is displayed in the status bar to indicate that the user is in the "Create mode" state.
    Success messages will disappear after 5 seconds.

#. Create/Edit a reduction plan - Submit button: handle_submit_reduction_plan(reduction_plan_parameters)

    .. mermaid::

        sequenceDiagram
            participant View
            participant Presenter
            participant Model

            Note over View,Model: a. Save Reduction Plan - (Create)
            View->>Presenter: User clicks the "Add/Edit" button
            Presenter->>View: Gather the reduction plan parameters
            Presenter->>Model: Send the reduction plan parameters
            Note right of Model: Validate the parameters, unique filepath for new reduction plan
            Note right of Model: Create new reduction plan
            Note right of Model: Create new reduction plan file and store the reduction plan parameters
            Note right of Model: Add the reduction plan in the reduction plan list
            Note right of Model: Set curent plan as selected (selected_plan=<id>)
            Model->>Presenter: Return reduction plan
            Presenter->>View: Update reduction plan list table with new item(id,name)
            Note left of View: Display selected plan label

            Note over View,Model: b. Save Reduction Plan - (Edit)
            View->>Presenter: User clicks the "Add/Edit" button
            Presenter->>View: Gather the reduction plan parameters
            Presenter->>Model: Send the reduction plan parameters
            Note right of Model: Validate the parameters
            Note right of Model: Edit selected reduction plan with parameters
            Note right of Model: Edit the reduction plan file with the reduction plan parameters
            Model->>Presenter: Return reduction plan
            Presenter->>View: Update reduction plan list table item, if name changed
            Note left of View: Display selected plan label, if name changed

#. Get the starting folder path for the reduction plan: get_starting_path_for_reduction_plan(instrument,experiment)

    .. mermaid::

        sequenceDiagram
            participant View
            participant Presenter
            participant Model

            Note over View,Model: Create Recommended Reduction Plan Folder File
            View->>Presenter: User clicks the "Reduction Plan FilePath Select" button
            Presenter->>View: Gather instrument and experiment
            Presenter->>Model: Send the instrument and experiment
            Note right of Model: Create the filepath format </<facility>/<instrument>/shared/<ipts>/garnet>, from parameters and instrument configurations
            Note right of Model: Create the garnet folder in the filepath, if it does not exist
            Model->>Presenter: Return the full filepath
            Presenter->>View: Set the starting path of the FileBrowser dialog
            Note left of View: Display the path in the filesystem to the user

    If the user has selected an instrument and experiment, then the recommended starting path for saving the reduction plan file is at:
    /<facility>/<instrument>/shared/<ipts>/garnet. The garnet folder needs to be created, if it does not exist.
    If the user has not selected an instrument yet, a default option should appear.

#. Load a reduction plan from file: handle_load_reduction_plan(reduction_plan_file)
    #. Valid case

        .. mermaid::

            sequenceDiagram
                participant View
                participant Presenter
                participant Model

                Note over View,Model: Load a reduction plan
                View->>Presenter: User clicks the "Load Reduction Plan" button and selects a file
                Presenter->>View: Get the filepath
                Presenter->>Model: Send the filepath
                Note right of Model: Read the parameters from the file
                Note right of Model: Validate the parameters
                Note right of Model: Create new reduction plan
                Note right of Model: Add the reduction plan in the reduction plan list
                Note right of Model: Set curent plan as selected
                Model->>Presenter: Return reduction plan
                Presenter->>View: Update reduction plan parameters and list table
                Note left of View: Display parameters
                Note left of View: Display selected plan label
                Note over View,Model: Edit reduction plan flow

    #. Invalid case - Invalid parameter values

        .. mermaid::

            sequenceDiagram
                participant View
                participant Presenter
                participant Model

                Note over View,Model: Load a reduction plan
                View->>Presenter: User clicks the "Load Reduction Plan" button and selects a file
                Presenter->>View: Get the filepath
                Presenter->>Model: Send the filepath
                Note right of Model: Read the parameters from the file
                Note right of Model: Validate the parameters
                Note right of Model: Create Error Message
                Note right of Model: Set curent plan as selected("")
                Model->>Presenter: Return error message
                Presenter->>View: Show error message
                Note left of View: Information Message <The reduction plan was not saved. Please correct the issue and save it.>
                Note left of View: Display parameter validation
                Note over View,Model: Create reduction plan flow

    #. Invalid case - Missing parameter fields (keys) or file is already loaded

        .. mermaid::

            sequenceDiagram
                participant View
                participant Presenter
                participant Model

                Note over View,Model: Load a reduction plan
                View->>Presenter: User clicks the "Load Reduction Plan" button and selects a file
                Presenter->>View: Get the filepath
                Presenter->>Model: Send the filepath
                Note right of Model: Read the parameters from the file
                Note right of Model: Validate the parameters
                Note right of Model: Create Error Message
                Model->>Presenter: Return error message
                Presenter->>View: Show error message
                Note left of View: Error Message <The reduction plan was not loaded. Corrupted file schema.>

#. Copy the parameters of a reduction plan: handle_copy_reduction_plan_parameters(reduction_plan_id)

    .. mermaid::

        sequenceDiagram
            participant View
            participant Presenter
            participant Model

            Note over View,Model: Copy reduction plan parameters
            View->>Presenter: User right-clicks on a reduction plan the "Copy" button
            Presenter->>View: Get the reduction plan name
            Presenter->>Model: Send the reduction plan name
            Note right of Model: Read the parameters of the reduction plan
            Note right of Model: Update selected plan id (selected_plan="")
            Model->>Presenter: Return the parameters
            Presenter->>View: Update the parameters
            Presenter->>View: Update the reduction name to <name> Clone (unique)
            Note left of View: Status Success Message <Create a new reduction plan.> (timeout=5sec)
            Note over View,Model: Create reduction plan flow

    This is a "Create" state variation with initial parameters filled in from another Reduction Plan.
    The reduction plan name and filepath need to be updated from the user to create the cloned reduction plan.

#. Select/Edit a reduction plan - Button: handle_edit_reduction_plan(reduction_plan_id)

    .. mermaid::

        sequenceDiagram
            participant View
            participant Presenter
            participant Model

            Note over View,Model: Edit reduction plan parameters
            View->>Presenter: User left-clicks on a reduction plan
            Presenter->>View: Get the reduction plan id
            Presenter->>Model: Send the reduction plan id
            Note right of Model: Read the parameters of the reduction plan
            Note right of Model: Update selected plan id to current (selected_plan=<id>)
            Model->>Presenter: Return the parameters
            Presenter->>View: Update the parameters
            Note left of View: Display selected plan label
            Note over View,Model: Edit reduction plan flow

#. Delete a reduction plan - Button: handle_delete_reduction_plan(reduction_plan_id)

    .. mermaid::

        sequenceDiagram
            participant View
            participant Presenter
            participant Model

            Note over View,Model: Delete a reduction plan
            View->>Presenter: User right-clicks on a reduction plan the "Delete" button
            Note left of View: Info Message <Do you want to delete the file from the folder?>
            Presenter->>View: Get the reduction plan id
            Presenter->>Model: Send the reduction plan id
            Note right of Model: Remove the reduction plan from the list
            Note right of Model: Remove the reduction plan file, if selected yes
            Note right of Model: Update selected plan to "", if this is the current one
            Model->> Presenter: Return status
            Presenter->>View: Update reduction plan list table
            Presenter->> View: Update selected plan label, if this is the current one

#. Connect to OnCat: handle_oncat_connection(username, password). See :ref:`handle_oncat_connection <oncat_mvpi>` .

#. DataSource Absolute Path: handle_datasource_filepath(filepath). See :ref:`handle_datasource_filepath <oncat_mvpi>` .


#. Select Instrument: handle_instrument_selection(instrument)

    .. mermaid::

        sequenceDiagram
            participant View
            participant Presenter
            participant Model

            Note over View,Model: Select instrument
            View->>Presenter: User selects instrument
            Presenter->>View: Get instrument
            Presenter->>Model: Send instrument
            Note right of Model: Create new instrument, if it does not exist
            Note right of Model: Add new instrument in instrument_list, if it does not exist
            Note right of Model: Store instrument in PyOnCat
            Note right of Model: Get goniometer data from instrument's configuration
            Note right of Model: Get wavelength data from instrument's configuration
            Note right of Model: Get grouping choices from instrument's configuration
            Note right of Model: Get calibration detector and tube data from instrument's configuration
            Note right of Model: Get/Create starting directory paths for calibation, vanadium, background and mask from instrument's configuration
            Note over View,Model: Show data
            Model->>Presenter: Return experiments, goniometer, wavelength and calibration data for instrument
            Presenter->>Model: Get experiments, goniometer, wavelength and calibration data for instrument
            Presenter->>View: Display data for instrument
            Note left of View: Show experiments
            Note left of View: Show grouping
            Note left of View: Update goniometer table and wavelength data
            Note left of View: Display/Hide calibration detector and tube fields
            Note left of View: Set starting directory paths for calibation, vanadium, background and mask


    The starting directory paths of the filebrowser dialogs for the following are updated:

        * for calibration section: /<facility>/<instrument>/shared/calibration
        * for vanadium and mask section: /<facility>/<instrument>/shared/Vanadium
        * for background: /<facility>/<instrument>/shared/Background/

    The starting paths for calibration, vanadium background and mask sections are retrieved from the Instrument Configuration Settings. No folder creation occurs in this case.


#. Select Experiment: handle_experiment_selection(experiment).

    .. mermaid::

        sequenceDiagram
            participant View
            participant Presenter
            participant Model
            Note over View,Model: Handle Experiment Selection
            View->>Presenter: User selects experiment
            Presenter->>View: Get experiment
            Presenter->>Model: Send experiment
            Note right of Model: Store experiment
            Note right of Model: Generate and Store data source filepath
            Model->>Presenter: Return data source filepath
            Presenter->>View: Display data source filepath
            Note left of View: Create/Set starting directory paths for UB Matrix

            Note over View,Model: Update Grouped Runs (update_grouped_runs(use_cached_runs=True))
            Presenter->>Model: Get grouped runs for an experiment
            Note right of Model: Get runs from OnCat/filepath folder, if they do not exist
            Note right of Model: Store run data and group runs by group field
            Model->>Presenter: Return grouped runs for an experiment
            Presenter->>View: Display grouped runs

    The starting path format for UB matrix: /<facility>/<instrument>/IPTS-<experiment>/shared

#. Select Run Range: handle_run_selection(run_range) See :ref:`handle_run_selection <oncat_mvpi>` .

#. Refresh IPTS Runs: update_grouped_runs(use_cached_runs=False) See :ref:`update_grouped_runs <oncat_mvpi>` .


#. Warning message flow from Model

    .. mermaid::

        sequenceDiagram
            participant View
            participant Presenter
            participant Model

            Note over View,Model: Error detected during data processing
            Note right of Model: Create Warning message
            Model->>Presenter: Send warning message
            Presenter->>View: Send warning message
            Note left of View: Show warning message
            Presenter->>View: Get user input
            Presenter->>Model: Send user input
            Note right of Model: Continue or Interrupt flow

    A warning message pop-up appears during the normal workflow to ask the user whether they want to proceed with the worflow or interrup.
        * If the user chooses to continue, then the warning is disregarded and the worflow continues.
        * If the user chooses to stop, the workflow is interrupted and the users returns to the previous state.


#. Error message flow from Model

    .. mermaid::

        sequenceDiagram
            participant View
            participant Presenter
            participant Model

            Note over View,Model: Error detected during data processing
            Note right of Model: Create error message
            Model->>Presenter: Send error message
            Presenter->>View: Send error message
            Note left of View: Show error message

    Error and warning messages are pop-up messages.
