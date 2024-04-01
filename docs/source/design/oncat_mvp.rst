OnCat Model-View-Presenter Schema
========================================

Related APIS:

- experiment_list: oncat.Experiment.list(facility=<facility>, instrument=<instrument>)
- experiment_info: oncat.Experiment.retrieve(experiment=<experiment>,facility=<facility>, instrument=<instrument>)
- data_files: oncat.Datafile.list(facility=<facility>, instrument=<instrument>, experiment=<experiment>, projection=<projection>, exts=<ext>)



MVP diagram

Model diagram : link to OncatSchema diagram

View diagram

.. mermaid::

 classDiagram
    ReductionPlanWidget "1" -->"1" RunsWidget
    ReductionPlanWidget "1" -->"1" GoniometerWavelengthWidget

    class ReductionPlanWidget{
        +QLabel:oncat_connection_status
        +PyOnCatQButton: oncat_login_btn
        +QLabel:instrument_display
        +QComboBox:instrument
        +RunsWidget:runs
        +GoniometerWavelengthWidget:goniometer
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
    }


    class GoniometerWavelengthWidget{
        +QLabel:goniometer_table_display
        +QTableWidget:goniometer_table
        +QLabel:wavelength_display
        +QLineEdit~1|2~:wavelength
    }




Presenter diagram (it can just be part of the HomePresenter)

.. mermaid::

 classDiagram
    OnCatDataPresenter "1" -->"1" ReductionPlanWidget
    OnCatDataPresenter "1" -->"1" OnCatModel
    class OnCatDataPresenter{
       -OnCatModel:model
       -ReductionPlanWidget:view
       +login(username,password)
       +get_connection_status()
       +set_instrument(instrument)
       +set_selected_experiment(experiment)
       +get_experiments()
       +get_grouped_runs()
       +get_plot_data(run_range)
    }
    class ReductionPlanWidget{
        +QLabel:oncat_connection_status
        +PyOnCatQButton: oncat_login_btn
        +QLabel:instrument_display
        +QComboBox:instrument
        +RunsWidget:runs
        +GoniometerWavelengthWidget:goniometer
    }
    class OnCatModel{
        +InstrumentModel instrument
        +ExperimentModel selected_experiment
        -Pyoncat:ONCat oncat_agent
        +List~ExperimentModel~ experiment_list
    }


flow

.. mermaid::

    flowchart TB
        subgraph View        
            display_oncat_connection_status
            display_experiments
            display_grouped_runs
            display_plot_data
            get_selected_instrument
            get_selected_run
        end
        
        subgraph Presenter
        handle_connection_status
            set_instrument
            set_selected_experiment
            get_experiments
            get_grouped_runs
            get_plot_data
        end
        subgraph Model
            get_pyoncat_agent
            set_experiment
            set_instrument
        end
        handle_connection_status-->get_pyoncat_agent
        handle_connection_status-->display_oncat_connection_status




set_selected_experiment-->set_experiment
set_selected_instrument-->set_instrument        
set_selected_instrument-->set_selected_experiment
get_selected_instrument-->set_instrument