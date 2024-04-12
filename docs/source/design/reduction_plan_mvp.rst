.. _reduction_plan_mvp:

Reduction Plan Model-View-Presenter
========================================

The data, graphical interface and functionality components related to the first step
-- Reduction Plan Screen -- are described here. The related code
is organized in the Model-View-Presenter pattern.

The Model is described in detail:


.. mermaid::

    classDiagram
        ReductionPlanTabModel "1" -->"1" InstrumentListModel
        ReductionPlanTabModel "1" -->"1" ReductionPlanListModel
        ReductionPlanTabModel "1" -->"1" PyOnCatModel
        InstrumentListModel "1" o--"N<=6" InstrumentModel
        ReductionPlanListModel "1" o--"N" ReductionPlanModel
        ReductionPlanModel "1" -->"1" InstrumentModel
        PyOnCatModel "1" -->"1" InstrumentModel

        class ReductionPlanListModel{
            -Number:selected_plan_index
            -List~ReductionPlanModel~ reduction_plan_list
            +add_reduction_plan()
            +remove_reduction_plan()
            +get_selected_plan()
            +set_selected_plan()
            +get_plans()
        }

        class InstrumentListModel{
            -List~InstrumentModel~ instrument_list
            +add_instrument()
            +get_instrument()
        }


        class ReductionPlanTabModel{
            ReductionPlanListModel reduction_plan_list
            InstrumentListModel instrument_list
            PyOnCatModel pyoncat_data
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
            +QLabel:grouping_display
            +QComboBox:grouping
            +VanadiumWidget:vanadium
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
            +validate_run_ranges()
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
            +validate_detector()
            +validate_tube()
        }


        class NormalizationWidget{
            +BtnFileWidget: flux
            +BtnFileWidget: solid_angle
            +BtnFileWidget: mask
            +BtnFileWidget: background
            +validate_flux()
            +validate_solid_angle()
            +validate_mask()
            +validate_background()
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
            +validate_file()
            +set_starting_path_for_instrument()
            +show()
            +hide()
        }

The Presenter is described below. It is connected with one model and view.

.. mermaid::

 classDiagram
    class ReductionPlanTabPresenter{
        -model
        -view
        %%reduction plan related
        -update_reduction_plan_list()

        +new_reduction_plan()
        +submit_reduction_plan()
        +load_reduction_plan()
        +copy_reduction_plan_parameters()
        +edit_reduction_plan()
        +select_reduction_plan()
        +delete_reduction_plan()

        %%pyoncat related
        +handle_oncat_connection()
        +handle_datasource_filepath(filepath)
        +handle_instrument_selection(instrument) %%more
        +handle_experiment_selection(experiment)
        +update_grouped_runs(experiment, use_cached_runs=True)
        +handle_run_selection(run_range)
    }



instrument and reduction plan relationships??



View-only interactions
paths before button activation?

The M-V-P interactions are described and grouped by functionality:

Create a new reduction plan button

.. mermaid::

    sequenceDiagram
        participant View
        participant Presenter
        participant Model

        Note over View,Model: New Reduction Plan
        View->>Presenter: User clicks the "Create new Reduction Plan" button
        Note left of View: Clear all parameters of the reduction plan screen
        Presenter->>Model: Unselect current reduction plan
        Note right of Model: Update selected plan index (-1)


Create/Edit a reduction plan - Submit button

.. mermaid::

    sequenceDiagram
        participant View
        participant Presenter
        participant Model

        Note over View,Model: Save Reduction Plan - (Create)
        View->>Presenter: User clicks the "Add/Edit" button
        Presenter->>View: Gather the reduction plan parameters
        Presenter->>Model: Send the reduction plan parameters
        Note right of Model: New reduction plan
        Note right of Model: Create new reduction plan
        Note right of Model: Add the reduction plan in the reduction plan list
        Note right of Model: Set curent plan as selected
        Model->>Presenter: Return reduction plan and index id
        Presenter->>View: Update reduction plan list table

        Note over View,Model: Save Reduction Plan - (Edit)
        View->>Presenter: User clicks the "Add/Edit" button
        Presenter->>View: Gather the reduction plan parameters
        Presenter->>Model: Send the reduction plan parameters
        Note right of Model: Edit selected reduction plan with parameters
       

Load a reduction plan from file

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
        Note over View,Model: Save Reduction Plan - (Create) New reduction plan (see above)



Select a reduction plan 
Note: The order of the reduction plan on the widget is the same as the order of
the reduction plan list on the model side

.. mermaid::

    sequenceDiagram
        participant View
        participant Presenter
        participant Model

        Note over View,Model: Select reduction
        View->>Presenter: User left-clicks on a reduction plan
        Presenter->>View: Get the reduction plan name,index
        Presenter->>Model: Send the reduction plan name,index
        Note right of Model: Set curent plan as selected

Copy the parameters of a reduction plan 

.. mermaid::

    sequenceDiagram
        participant View
        participant Presenter
        participant Model

        Note over View,Model: Copy reduction plan parameters
        View->>Presenter: User right-clicks on a reduction plan the "Copy" button
        Presenter->>View: Get the reduction plan name,index
        Presenter->>Model: Send the reduction plan name,index
        Note right of Model: Read the parameters of the reduction plan
        Note right of Model: Update selected plan index (-1)
        Model->>Presenter: Return the parameters
        Presenter->>View: Display the parameters


Edit a reduction plan - Button

.. mermaid::

    sequenceDiagram
        participant View
        participant Presenter
        participant Model

        Note over View,Model: Edit reduction plan parameters
        View->>Presenter: User right-clicks on a reduction plan the "Edit" button
        Presenter->>View: Get the reduction plan name,index
        Presenter->>Model: Send the reduction plan name,index
        Note right of Model: Read the parameters of the reduction plan
        Note right of Model: Update selected plan index to current
        Model->>Presenter: Return the parameters
        Presenter->>View: Display the parameters


Delete a reduction plan - Button

.. mermaid::

    sequenceDiagram
        participant View
        participant Presenter
        participant Model

        Note over View,Model: Delete a reduction plan
        View->>Presenter: User right-clicks on a reduction plan the "Delete" button
        Note left of View: Info Message <Do you wan to delete the file from the folder?>
        Presenter->>View: Get the reduction plan name,index
        Presenter->>Model: Send the reduction plan name,index
        Note right of Model: Delete the reduction plan
        Note right of Model: Remove the reduction plan from the list
        Note right of Model: update selected plan index


Error message flow

.. mermaid::

    sequenceDiagram
        participant View
        participant Presenter
        participant Model

        Note over View,Model: New Reduction Plan
        View->>Presenter: User clicks the "Create new Reduction Plan" button
        Note left of View: Clear all parameters of the reduction plan screen
        Presenter->>Model: Unselect current reduction plan
        Note right of Model: Update selected plan index (-1)

