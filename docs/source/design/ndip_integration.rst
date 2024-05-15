.. _ndip_integration:

===================
NDIP - Integration
===================

In this page, users can perform Integration, by using the current Reduction Plan and the additional parameters defined here.

Overall, users can:
   * create Integration parameters in a Reduction Plan
   * edit the Integration parameters of a Reduction plan from  the ReductionPlan object or file (memory or disk)
   * run the Integration data reduction process
   * launch an external tool for analyzing the data further

Fields
--------

Below are the fields for integration

.. list-table:: Integration - Fields
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Type
     - Value Origin
     - Additional validation
     - Mandatory
   * - Cell
     - String
     - predefined options from backend
     -
     - yes
   * - Centering Symbol
     - String
     - predefined options from backend
     -
     - yes
   * - Minimum D-Spacing
     - Float
     -
     - >0
     - yes
   * - Peak Radius
     - Float
     -
     - >0 and <1
     - yes
   * - Minimum Modulation D-Spacing
     - Float
     -
     - >=Minimum D-Spacing
     - no
   * - Maximum Order
     - Integer
     - default: 0
     - >=0 and <10
     - yes
   * - Modular Vectors X3
     - (Float, Float, Float)
     - default mod_vectors[]: [[0,0,0],[0,0,0],[0,0,0]]
     - non co-linear
     - yes
   * - CrossTerms
     - Boolean
     - default: false
     -
     - yes

Cell options from configuration settings in the backend:
    * Monoclinic
    * Triclinic
    * Orthorhombic
    * Tetragonal
    * Rhombohedral
    * Hexagonal
    * Cubic

Centering options from configuration settings in the backend:
    * P
    * I
    * F
    * R(obv)
    * R(rev)
    * A
    * B
    * C

Inter-Field Validations
------------------------

The following field validations that involve pairs of fields are checked from the client side.

MaxOrder-CrossTerms Combined Validation. If any of the fields change their inter-field validation rules should be checked. Invalid case:
    * CrossTerms = True and MaxOrder=0

In the invalid case, both MaxOrder and CrossTerms border colors become (invalid) red.

MaxOrder-ModVectors Combined Validation. If any of the fields change their inter-field validation rules should be checked. Invalid cases:
    * ModVectors[0][0] = ModVectors[0][1] = .. = ModVectors[2][2] = 0 and MaxOrder !=0
    * at least 1 ModVectors[i][j] != 0 and MaxOrder =0

In the invalid cases, both MaxOrder and ModVectors table border colors become (invalid) red.

Validation
----------

Regarding validation, same rules about styling, form submission, success/error mesages, client side vs. server side validation and messages apply here, as the Reduction Plan.

Client side validation can include:
   * required fields
   * field types
   * minimum d-spacing limits
   * minimum modulation d-spacing limits
   * peak radius limits
   * maximum order limits

Additionally, when the user does not have a Reduction Plan, yet, and they land on this page, an error message ("*Please create a Reduction Plan first*") below the submission buttons should appear.
The buttons' functionalities (*Save All & Run Integration*, *Save Only Integration Parameters*) are deactivated as the rest client side validations. The menu item on the left should be replaced to "Create Reduction Plan".
*Launch tool* button is visible and active anytime.

Server side validation can include:
   * filepath/directory for integration data
   * integration exception
   * modvectors non colinear

Submission
-----------

* *Save All & Run Integration* button: When the user clicks the button, garnet runs the integration process and produces results. Both ReductionPlan object and file are updated with the integration parameters and Results filepaths. The Results block is updated with the generated files and their root directory. A success message (n=5s) is displayed: "*Reduction Plan is updated with the Integration Parameters and Results.*"
* *Save Only Integration Parameters* button: When the user clicks the button, the peaks integration parameters (cell unit parameters, modulation and results=[]) are saved in the ReductionPlan object and corresponding file. A success message (n=5s) is displayed: "*Reduction Plan is updated with the Integration Parameters.*" below the button. The Results block becomes empty.
* *Launch Analysis tool* button.  When the user clicks this button, a new page appears with the analysis tool. This is a new tool. Requirement for this: TBD.

If the user runs integration and there is an existing directory/filenames, a warning message appears asking the user: "*The current files in the directory <directory> will be overwritten. Do you want to continue?*" (option to not show this message again). If the user selects to continue the files will be overwritten, else nothing will happen.

Create Integration Parameters
-------------------------------

The first time the user lands in the page with a Reduction Plan created/loaded in memory and no integration parameters exist in the plan, default parameters are displayed as shown here: `Wireframe Integration Landing <https://share.balsamiq.com/c/2rnrpk1RrjzyriAhcSPJe6.png>`_.

Edit Integration Parameters
-------------------------------

If the existing Reduction Plan contains valid Integration parameters, then they are shown in the web form over the default values.
They are accesed from the ReductionPlan object first and then from the Reduction Plan file.
The Results block with the directory and files should appear, too (`Wireframe Integration Edit <https://share.balsamiq.com/c/1VCWAsEXBR5vTkmHs722ir.png>`_).


If the fields are not valid:
   * Invalid parameter values. An information message is displayed to the user: "*The integration parameters have some mistakes in the Reduction Plan. Please correct the issue and save it.*". The parameters are populated in the form with their validation messages/colors.
   * Missing parameter fields (keys). An error message is displayed to the user: "*The integration parameters were not loaded. Please fill them in.*" . The default integration parameters values should appear in this case.

If the Results exist, they should be populated, too.
