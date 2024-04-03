.. _pyocat_mvp:

PyOnCat Model-View-Presenter
========================================

The data, graphical interface and functionality components related to OnCat are described here. The related code
is organized in Model-View-Presenter pattern.

The Model is described in detail :ref:`PyOnCatSchema <pyoncat>`.
The View is described below:

(The ReductionPlanWidget contains only elements relevant to pyoncat data.)

.. mermaid::

 classDiagram
    ReductionPlanWidget "1" -->"1" RunsWidget
    ReductionPlanWidget "1" -->"1" GoniometerWavelengthWidget
    ReductionPlanWidget "1" -->"1" DataSourceWidget

    class ReductionPlanWidget{
        +QLabel:instrument_display
        +QComboBox:instrument
        +DataSourceWidget:data_source
        +RunsWidget:runs
        +GoniometerWavelengthWidget:goniometer
    }

    class DataSourceWidget{
        +QLabel:oncat_connection_status
        +PyOnCatQButton: oncat_login_btn
        +QLabel:full_path_display
        +QButton-QFileDialog: file_browse_btn
        +get_user_credentials()
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
        +display_experiments()
        +display_grouped_runs()
        +display_plot_data()
        +get_selected_run_range()
        +get_selected_experiment()
    }


    class GoniometerWavelengthWidget{
        +QLabel:goniometer_table_display
        +QTableWidget:goniometer_table
        +QLabel:wavelength_display
        +QLineEdit~1|2~:wavelength
    }




The Presenter is described below. It is connected with one model and view.

.. mermaid::

 classDiagram
    class OnCatDataPresenter{
       -model
       -view
        +login(username,password)
        +handle_connection_status()
        +set_data_source_filepath(filepath)
        +set_instrument(instrument)
        +show_experiments(instrument)
        +set_experiment(experiment)
        +show_grouped_runs(instrument,experiments)
        +set_run_range(run_range)
        +show_plot()
    }


The M-V-P interactions are described and grouped by functionality:

DataSource Initialization - Connect to OnCat

.. mermaid::

    sequenceDiagram
        participant View
        participant Presenter
        participant Model

        Note over View,Model: Login
        View->>Presenter: User provides credentials
        Presenter->>View: Get user credentials
        Presenter->>Model: Send user credentials
        Note right of Model: Store pyoncat agent
        Model->>Presenter: Return pyoncat agent

        Note over View,Model: Handle oncat connection status
        Presenter->>Model: Get pyoncat agent
        Model->>Presenter: Return pyoncat agent
        Presenter->>View: Display oncat connection status


DataSource Initialization - Absolute Path

.. mermaid::

    sequenceDiagram
        participant View
        participant Presenter
        participant Model

        Note over View,Model: Set Data Source FilePath
        View->>Presenter: User selects file folder
        Presenter->>View: Get filepath
        Presenter->>Model: Send filepath
        Note right of Model: Store filepath


Data fetch and display

.. mermaid::

    sequenceDiagram
        participant View
        participant Presenter
        participant Model

        Note over View,Model: Set Instrument
        View->>Presenter: User selects instrument
        Presenter->>View: Get instrument
        Presenter->>Model: Send instrument
        Note right of Model: Store instrument

        Note over View,Model: Show experiments
        Presenter->>Model: Get experiments for instrument
        Presenter->>View: Display experiments

        Note over View,Model: Set experiment
        View->>Presenter: User selects experiment
        Presenter->>View: Get experiment
        Presenter->>Model: Send experiment
        Note right of Model: Store experiment

        Note over View,Model: Show grouped runs
        Presenter->>Model: Get grouped runs for an experiment
        Note right of Model: Get run data and group runs by group field
        Model->>Presenter: Return grouped runs for an experiment
        Presenter->>View: Display grouped runs

        Note over View,Model: Set run range
        View->>Presenter: User sets run range
        Presenter->>View: Get run range
        Presenter->>Model: Send run range
        Note right of Model: Store run range

        Note over View,Model: Show run-plot
        Presenter->>Model: Get calculated plot data
        Note right of Model: Calculate plot data
        Model->>Presenter: Return calculated plot data
        Presenter->>View: Display plot
