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
        +handle_oncat_connection()
        +handle_datasource_filepath(filepath)
        +handle_instrument_selection(instrument)
        +handle_experiment_selection(experiment)
        +update_grouped_runs(experiment, use_cached_runs=True)
        +handle_run_selection(run_range)
    }


The M-V-P interactions are described and grouped by major functionality:

DataSource Initialization - Connect to OnCat

.. mermaid::

    sequenceDiagram
        participant View
        participant Presenter
        participant Model

        Note over View,Model: Handle OnCat Connection
        Note over View,Model: Login
        View->>Presenter: User provides credentials
        Presenter->>View: Get user credentials
        Presenter->>Model: Send user credentials
        Note right of Model: Store pyoncat agent
        Model->>Presenter: Return pyoncat agent

        Note over View,Model: Get connection status
        Presenter->>Model: Get pyoncat agent
        Model->>Presenter: Return pyoncat agent
        Presenter->>View: Display oncat connection status


DataSource Initialization - Absolute Path

.. mermaid::

    sequenceDiagram
        participant View
        participant Presenter
        participant Model

        Note over View,Model: Handle Datasource Filepath
        View->>Presenter: User selects file folder
        Presenter->>View: Get filepath
        Presenter->>Model: Send filepath
        Note right of Model: Store filepath
        Note right of Model: Generate and Store instrument
        Note right of Model: Generate and Store experiment
        Model->>Presenter: Return instrument and experiment
        Presenter->>View: Display instrument
        Presenter->>View: Display experiment
        Note over View,Model: Show grouped runs (see below)

Data fetch and display

.. mermaid::

    sequenceDiagram
        participant View
        participant Presenter
        participant Model

        Note over View,Model: Handle Instrument Selection
        View->>Presenter: User selects instrument
        Presenter->>View: Get instrument
        Presenter->>Model: Send instrument
        Note right of Model: Store instrument

        Note over View,Model: Show experiments
        Presenter->>Model: Get experiments for instrument
        Note right of Model: Get experiment from OnCat, if it does not exist
        Presenter->>View: Display experiments

        Note over View,Model: Handle Experiment Selection
        View->>Presenter: User selects experiment
        Presenter->>View: Get experiment
        Presenter->>Model: Send experiment
        Note right of Model: Store experiment
        Note right of Model: Generate and Store data source filepath
        Model->>Presenter: Return data source filepath
        Presenter->>View: Display data source filepath

        Note over View,Model: Update Grouped Runs
        Presenter->>Model: Get grouped runs for an experiment
        Note right of Model: Get runs from OnCat, if they do not exist
        Note right of Model: Store run data and group runs by group field
        Model->>Presenter: Return grouped runs for an experiment
        Presenter->>View: Display grouped runs

        Note over View,Model: Handle Run Selection
        View->>Presenter: User sets run range
        Presenter->>View: Get run range
        Presenter->>Model: Send run range
        Note right of Model: Calculate plot data
        Model->>Presenter: Return calculated plot data
        Presenter->>View: Display plot

Refresh IPTS Runs

.. mermaid::

    sequenceDiagram
        participant View
        participant Presenter
        participant Model

        Note over View,Model: Update Grouped Runs
        View->>Presenter: User clicks the  "Refresh IPTS Runs" button
        Presenter->>Model: Get grouped runs for an experiment
        Note right of Model: Get runs from OnCat
        Note right of Model: Store run data and group runs by group field
        Model->>Presenter: Return grouped runs for an experiment
        Presenter->>View: Display grouped runs (see above)
