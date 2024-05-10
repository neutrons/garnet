.. _ndip_normalization:

======================
NDIP - Normalization
======================

In this page, users can perform Normalization, by using the current Reduction Plan and the additional parameters defined here.

Overall, users can:
   * create Normalization parameters in a Reduction Plan
   * edit Normalization parameters of a Reduction plan
   * run the Normalization data reduction process
   * launch an external tool for analyzing the data further

Fields
--------

Below are the fields for normalization

.. list-table:: Normalization - Fields
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Type
     - Value Origin
     - Additional validation
     - Mandatory
   * - Projection X3
     - List of 3 Float
     - projections[]: [[1,0,0],[0,1,0],[0,0,1]]
     - non co-linear
     - yes
   * - Extern (Min, Max) X3
     - (Float, Float)
     - (-6,6)
     - Min < Max
     - yes
   * - Number of Bins X3
     - Integer
     - bins[]: [201,201,201]
     - bins[i]>=1, bins[0]+bins[1]+bins[2] <= 1000
     - yes
   * - Operations
     - String
     - default: None, predefined choices(2)
     -
     - no
   * - Crystal System
     - String
     - predefined choices from operations
     -
     - conditionally yes
   * - Group
     - String
     - predefined choices from crystal system
     -
     - conditionally yes

The Crystal System and Group fields are hidden and empty, when Operations value is None.
If the Operations Value is Space Group or Point Group, both become mandatory fields.

Field Interactions
-------------------

* When the user selects an Operations value (Space Group or Point Group), besides showing/hidding the above fields, data are retrieved for Crystal System dropdown choices depending on the operations selected value.
* When the user selects a Crystal System value, data are retrieved for Group dropdown choices depending on the Crystal System selected value.
* When the user updates the extends min[i] or extends max[i] or number of bins[i], the bins size[i] is updated following this formula:
   bins_size[i] = (max[i]- min[i])/(bins[i]-1)

Validation
----------

Regarding validation, same rules regarding styling, form submission, client side vs. server side validation and messages apply here, as the Reduction Plan.

Client side validation can include here:
   * required fields
   * field types
   * extends min <max
   * number of bins min value and collective max value
   * projection comma-separated float number format

Additionally, when the user does not have a Reduction Plan, yet, and they land on this page, an error message below the submission buttons should appear.
The buttons functionality is deactivated as the rest client side validations. The menu item on the left should be replaced to "Create Reduction Plan" and the message should say:"*Please create a Reduction Plan first*".

Backend validation can include here:
   * projection non colinear
   * filepath/directory for normalization data
   * normalization exception

Create Normalization Parameters
-------------------------------

The first time the user lands in the Page with a Reduction Plan created/loaded in memory and no normalization parameters exist in the plan, default parameters are displayed as shown here: `Wireframe Normalization Landing <https://share.balsamiq.com/c/4Lay4JCqNoCP3PTdrWqhYz.png>`_.

Edit Normalization Parameters
-------------------------------

If the existing Reduction Plan contains Normalization parameters, then they are shown in the web form over the default values.
The Results block with the directory and files should appear, too (`Wireframe Normalization Edit <https://share.balsamiq.com/c/f4PDmyWoYfbSYPtxjxuJgt.png>`_).


If the fields are not valid:
   * Invalid parameter values. An information message is displayed to the user: "*The normalization parameters have some mistakes in the Reduction Plan. Please correct the issue and save it.*". The parameters are populated in the form with their validation messages/colors.
   * Missing parameter fields (keys). An error message is displayed to the user: "*The normalization parameters were not loaded. Please fill them in.*" . The default normalization parameters values should appear in this case.

The above error messages appear below the submission buttons.

If the user runs the Reduction Plan and there is an existing directory/filenames, a warning message appears asking the user: "*The current files in the directory <directory> will be overwritten. Do you want to continue?*". If the user selects to continue the files will be overwritten, else nothing will happen.
