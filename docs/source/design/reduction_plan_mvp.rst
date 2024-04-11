.. _reduction_plan_mvp:

Reduction Plan Model-View-Presenter
========================================

The data, graphical interface and functionality components related to the first step
-- Reduction Plan Screen -- are described here. The related code
is organized in the Model-View-Presenter pattern.

The Model is described in detail :ref:`Reduction Plan <reduction_plan>`.
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

        +set_new_reduction_plan()
        +submit_reduction_plan()
        +load_reduction_plan()
        +copy_reduction_plan_parameters()
        +select_reduction_plan()
        +delete_reduction_plan()

        %%pyoncat related
        +handle_oncat_connection()
        +handle_datasource_filepath(filepath)
        +handle_instrument_selection(instrument)
        +handle_experiment_selection(experiment)
        +update_grouped_runs(experiment, use_cached_runs=True)
        +handle_run_selection(run_range)
    }
