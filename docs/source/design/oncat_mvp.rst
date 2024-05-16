.. _pyoncat_mvp:

PyOnCat Model-View-Presenter
==============================

IN PROGRESS

The data, graphical interface and functionality components related to OnCat are described here. The related code
is organized in Model-View-Presenter pattern.

PyOnCat
--------

The Model is described in detail :ref:`PyOnCatModel <pyoncat>`.

View related to PyOnCat
------------------------

The ReductionPlanWidget contains only elements relevant to pyoncat data.

.. mermaid::

 classDiagram
    ReductionPlanWidget "1" -->"1" RunsWidget
    ReductionPlanWidget "1" -->"1" DataSourceWidget

    class ReductionPlanWidget{
        +QLabel:instrument_display
        +QComboBox:instrument
        +DataSourceWidget:data_source
        +RunsWidget:runs
    }

    class DataSourceWidget{
        +QLabel:oncat_connection_status
        +PyOnCatQButton: oncat_login_btn
        +QLabel:full_path_display
        +QButton-QFileDialog: file_browse_btn
        +get_user_credentials()
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

Presenter related to PyOnCat
-----------------------------

The Presenter is described below.

.. mermaid::

 classDiagram
    class OnCatDataPresenter{
       -model
       -view
        +login(username,password)
        +handle_oncat_connection(username,password)
        +handle_datasource_filepath(filepath)
        +handle_instrument_selection(instrument)
        +handle_experiment_selection(experiment)
        +update_grouped_runs(use_cached_runs=True)
        +handle_run_selection(run_range)
    }

Through this component that can is part of the ReductionPlanTab, the users retrieve data about experiments and runs
by either connecting to OnCat or navigating to a directory in their local environment (directory format). The
following are supported and their interactions afre described in detail in the next section:

    * OnCat connection/login dialog
    * Access data with OnCat and by going through the files of a user-specified folder
    * List of Experiments per instrument with and without OnCat connection
    * List of Runs per experiment with and without OnCat connection
    * Run meta data retrieval with and without OnCat connection
    * Group run per specific field and display them
    * Retrieve grouped run per user's trigger-button
    * Plot creation based on the run meta data, when user is connected to OnCat

The experiments and runs are retrieved and saved on User-requested base on the current instrument and experiment selection.
The danger here, would be that if the user, keeps selecting instrument and experiments, the data will be stored in the backed and thus increasing the application's memory usage.

..  _oncat_mvpi:


M-V-P Interactions
--------------------

The M-V-P interactions are described and grouped by major functionality:

#. DataSource Initialization - Connect to OnCat: handle_oncat_connection(username, password)

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


#. DataSource Initialization - Absolute Path: handle_datasource_filepath(filepath)
    Note: The instrument should already be selected.

    #. FileBrowser
        .. mermaid::

            sequenceDiagram
                participant View
                participant Presenter
                participant Model

                Note over View,Model: Handle Datasource Filepath
                View->>Presenter: User selects file folder
                Note left of View: Validate filepath format
                Presenter->>View: Get filepath
                Presenter->>Model: Send filepath
                Note right of Model: Store filepath
                Note right of Model: Generate and Store experiment
                Model->>Presenter: Return experiment
                Presenter->>View: Display experiment
                Note over View,Model: Show grouped runs (see below)

    #. Filepath Type
        .. mermaid::

            sequenceDiagram
                participant View
                participant Presenter
                participant Model

                Note over View,Model: Handle Datasource Filepath
                View->>Presenter: User types file folder
                Note left of View: Validate filepath format
                Presenter->>View: Get filepath
                Presenter->>Model: Send filepath
                Note right of Model: Store filepath
                Note right of Model: Generate and Store experiment
                Model->>Presenter: Return experiment
                Presenter->>View: Display experiment
                Note over View,Model: Show grouped runs (see below)


#. Data fetch - Select Instrument: handle_instrument_selection(instrument) (partial flow). See :ref:`handle_instrument_selection <reduction_mvpi>` for the full flow

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


#. Data fetch - Select Experiment: handle_experiment_selection(experiment) (partial flow). See :ref:`handle_experiment_selection <reduction_mvpi>` for the full flow

    Users can retrieve runs either from OnCat or from a directory by reading each file separately. The later
    might be memory and/or cpu intensive. We will have to include some TimeoutError exception or similar to avoid having the program hanging.
    In that case the runs table will be empty.

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

            Note over View,Model: Update Grouped Runs (update_grouped_runs(use_cached_runs=True))
            Presenter->>Model: Get grouped runs for an experiment
            Note right of Model: Get runs from OnCat/filepath folder, if they do not exist
            Note right of Model: Store run data and group runs by group field
            Model->>Presenter: Return grouped runs for an experiment
            Presenter->>View: Display grouped runs


#. Data fetch - Select Run Range: handle_run_selection(run_range)
    The plot is calculated and displayed only when the user is connected to OnCat, else it is left empty.

    .. mermaid::

        sequenceDiagram
            participant View
            participant Presenter
            participant Model
            Note over View,Model: Handle Run Selection
            View->>Presenter: User sets run range
            Note left of View: Validate run range
            Presenter->>View: Get run range
            Presenter->>Model: Send run range
            Note right of Model: Calculate plot data
            Model->>Presenter: Return calculated plot data
            Presenter->>View: Display plot


#. Data fetch - Refresh IPTS Runs: update_grouped_runs(use_cached_runs=False)

    .. mermaid::

        sequenceDiagram
            participant View
            participant Presenter
            participant Model

            Note over View,Model: Update Grouped Runs
            View->>Presenter: User clicks the  "Refresh IPTS Runs" button
            Presenter->>Model: Get grouped runs for an experiment
            Note right of Model: Get runs from OnCat/filepath folder
            Note right of Model: Store run data and group runs by group field
            Model->>Presenter: Return grouped runs for an experiment
            Presenter->>View: Display grouped runs (see above)
