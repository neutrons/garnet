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
        ReductionPlanTabModel "1" o--"N<=6" InstrumentModel
        ReductionPlanListModel "1" o--"N" ReductionPlanModel
        ReductionPlanModel "1" -->"1" InstrumentModel
        PyOnCatModel "1" -->"1" InstrumentModel

        class ReductionPlanListModel{
            -String:selected_plan
            -List~ReductionPlanModel~ reduction_plan_list
            +add_reduction_plan()
            +remove_reduction_plan()
            +get_selected_plan()
            +set_selected_plan()
            +get_plans()
            +validate_reduction_plan_names_unique()

        }

        class ReductionPlanTabModel{
            +ReductionPlanListModel reduction_plan_list
            +List~InstrumentModel~ instrument_list
            +PyOnCatModel pyoncat_data
            +add_instrument()
            +get_instrument()
        }

        class InstrumentModel{
            <>
        }

        class ReductionPlanModel{
            <>
        }

        class PyOnCatModel{
            <>
        }


The ReductionPlanListModel model contains the user's reduction plans and the one selected for
data reduction in further steps (ReductionPlanListModel). Additionally, it maintains the list
of the instruments (InstrumentModel) generated during the reduction plan creation process per user's selections.
Finally the runs of experiments with their fields based on the selected instrument and OnCat-related
information are stored (PyOnCatModel), too.
The selected plan (ReductionPlanModel) is passed for the next step.

There are a lot fo dependencies on the selected instrument. We might have to consider a way to encorfe user to select instrument,
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
        ReductionPlanWidget "1" -->"1" GoniometerWavelengthWidget
        ReductionPlanWidget "1" -->"1" DataSourceWidget
        ReductionPlanWidget "1" -->"1" NormalizationWidget
        ReductionPlanWidget "1" -->"1" CalibrationWidget
        ReductionPlanWidget "1" -->"1" BaseButton
        DataSourceWidget"1" -->"1" PyOnCatBtnFileWidget
        PyOnCatBtnFileWidget"1" --|>"1" BtnFileWidget
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
            -QMenu:menu
            +QAction:select
            +QAction:copy
            +QAction:edit
            +QAction:delete
            +select_reduction_plan()
            +copy_reduction_plan()
            +edit_reduction_plan()
            +delete_reduction_plan()
            +get_plot_data()
        }

        class ReductionPlanWidget{
            +QLabel:name_display
            +QLineEdit:name
            +QLabel:instrument_display
            +QComboBox:instrument
            +DataSourceWidget:data_source
            +RunsWidget:runs
            +GoniometerWavelengthWidget:goniometer
            +CalibrationWidget:calibration
            +QLabel:UB
            +BtnFileWidget:ubfile
            +QLabel:grouping_display
            +QComboBox:grouping
            +VanadiumWidget:vanadium
            +BaseButton:reduction_plan_btn
            +create_reduction_plan()
            +update_data_for_instrument()
            +display_fields_for_instrument()
            +display_grouping_choices_for_instrument()
            +validate_reduction_plan_names_unique()

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


        class GoniometerWavelengthWidget{
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

        class BtnFileWidget{
            +QLabel: filename
            +QLineEdit:full_path_display
            +QButton-QFileDialog: file_browse_btn
            +get_full_path()
            +validate_file_extension()
            +set_starting_path_for_instrument()
            +show()
            +hide()
        }

All validation related to invalid and required fields for the reduction plan submit (Add/Edit) button
are added here:

    #. required parameters
    #. unique name among the reduction plan list
    #. run range format
    #. datasource file path format

In case the selected reduction plan is in an invalid state, the next steps buttons/tabs are deactivated.
A reduction plan is created only and only if is in a valid state.
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
        +handle_load_reduction_plan(reduction_plan_file)
        +handle_copy_reduction_plan_parameters(reduction_plan_name)
        +handle_edit_reduction_plan(reduction_plan_name)
        +handle_select_reduction_plan(reduction_plan_name)
        +handle_delete_reduction_plan(reduction_plan_name)

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
            Note right of Model: Update selected plan name ("")
            Model->>Presenter: Return status


#. Create/Edit a reduction plan - Submit button: handle_submit_reduction_plan(reduction_plan_parameters)

    .. mermaid::

        sequenceDiagram
            participant View
            participant Presenter
            participant Model

            Note over View,Model: a. Save Reduction Plan - (Create)
            View->>Presenter: User clicks the "Add/Edit" button
            Note left of View: Filebrowser Message <Select filepath to save the reduction plan> (unique)
            Presenter->>View: Gather the reduction plan parameters
            Presenter->>Model: Send the reduction plan parameters
            Note right of Model: Validate the parameters
            Note right of Model: Create new reduction plan
            Note right of Model: Create new reduction plan file and store the reduction plan parameters
            Note right of Model: Add the reduction plan in the reduction plan list
            Note right of Model: Set curent plan as selected (selected_plan=<name>)
            Model->>Presenter: Return reduction plan
            Presenter->>View: Update reduction plan list table
            Note left of View: Display selected plan label

            Note over View,Model: b. Save Reduction Plan - (Edit)
            View->>Presenter: User clicks the "Add/Edit" button
            Note left of View: Info Message <Do you want to update the file, too?>
            Presenter->>View: Gather the reduction plan parameters
            Presenter->>Model: Send the reduction plan parameters
            Note right of Model: Validate the parameters
            Note right of Model: Edit selected reduction plan with parameters
            Note right of Model: Edit the reduction plan file with the reduction plan parameters
            Model->>Presenter: Return reduction plan
            Presenter->>View: Update reduction plan list table, if name changed
            Note left of View: Display selected plan label, if name changed


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
                Note left of View: Warning Message <The reduction plan was not saved. Please correct the issue and save it.>
                Note left of View: Display parameter validation
                Note over View,Model: Create reduction plan flow

    #. Invalid case - Missing parameter fields (keys)

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

#. Copy the parameters of a reduction plan: handle_copy_reduction_plan_parameters(reduction_plan_name)

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
            Note right of Model: Modify the new reduction plan name to <name>_<number> (unique)
            Note right of Model: Update selected plan name (selected_plan="")
            Model->>Presenter: Return the parameters
            Presenter->>View: Update the parameters
            Note over View,Model: Create reduction plan flow

#. Edit a reduction plan - Button: handle_edit_reduction_plan(reduction_plan_name)

    .. mermaid::

        sequenceDiagram
            participant View
            participant Presenter
            participant Model

            Note over View,Model: Edit reduction plan parameters
            View->>Presenter: User right-clicks on a reduction plan the "Edit" button
            Presenter->>View: Get the reduction plan name
            Presenter->>Model: Send the reduction plan name
            Note right of Model: Read the parameters of the reduction plan
            Note right of Model: Update selected plan name to current (selected_plan=<name>)
            Model->>Presenter: Return the parameters
            Presenter->>View: Update the parameters
            Note left of View: Display selected plan label

#. Select a reduction plan: handle_select_reduction_plan(reduction_plan_name)

    Note: The order of the reduction plan on the widget is the same as the order of
    the reduction plan list on the model side

    .. mermaid::

        sequenceDiagram
            participant View
            participant Presenter
            participant Model

            Note over View,Model: Select reduction
            View->>Presenter: User left-clicks on a reduction plan
            Presenter->>View: Get the reduction plan name
            Presenter->>Model: Send the reduction plan name
            Note right of Model: Set curent plan as selected (selected_plan=<name>)
            Model->>Presenter: Return status
            Note left of View: Display selected plan label


#. Delete a reduction plan - Button: handle_delete_reduction_plan(reduction_plan_name)

    .. mermaid::

        sequenceDiagram
            participant View
            participant Presenter
            participant Model

            Note over View,Model: Delete a reduction plan
            View->>Presenter: User right-clicks on a reduction plan the "Delete" button
            Note left of View: Info Message <Do you want to delete the file from the folder?>
            Presenter->>View: Get the reduction plan name
            Presenter->>Model: Send the reduction plan name
            Note right of Model: Remove the reduction plan from the list
            Note right of Model: Remove the reduction plan file, if selected yes
            Note right of Model: Update selected plan to "", if this is the current one
            Model->> Presenter: Return status
            Presenter->>View: Update reduction plan list table
            Presenter->> View: Update selected plan label, if this is the current one

#. Connect to OnCat: handle_oncat_connection(username, password). See :ref:`handle_oncat_connection <handle_oncat_connection>` .

#. DataSource Absolute Path: handle_datasource_filepath(filepath). See :ref:`handle_datasource_filepath <handle_datasource_filepath>` .


#. Select Instrument: handle_instrument_selection(instrument)
    Besides the above flow that happens when the user selects an instrument, the starting path of the filebrowser dialogs are updated as following:

        * for calibration section: /<facility>/<instrument>/shared/calibration
        * for vanadium section: /<facility>/<instrument>/shared/Vanadium

    This can happen, when the user selects a specific file. UBMatrix does not have a starting path.

    .. _handle_instrument_selection:

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
            Note over View,Model: Show data
            Model->>Presenter: Return experiments, goniometer, wavelength and calibration data for instrument
            Presenter->>Model: Get experiments, goniometer, wavelength and calibration data for instrument
            Presenter->>View: Display data for instrument
            Note left of View: Clear instrument-related fields: runs, plot,calibration and vanadium data
            Note left of View: Show experiments
            Note left of View: Show grouping
            Note left of View: Update Goniometer table and Wavelength data
            Note left of View: Display/Hide calibration detector and tube fields

#. Select Experiment: handle_experiment_selection(experiment). See :ref:`handle_experiment_selection <handle_experiment_selection>` .

#. Select Run Range: handle_run_selection(run_range) See :ref:`handle_run_selection <handle_run_selection>` .

#. Refresh IPTS Runs: update_grouped_runs(use_cached_runs=False) See :ref:`update_grouped_runs <update_grouped_runs>` .

#. Error message flow

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
