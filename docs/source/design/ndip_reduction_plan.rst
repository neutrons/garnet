.. _ndip_reduction_plan:

======================
NDIP - Reduction Plan
======================

Reduction Plan Form fields:

.. list-table:: Title
   :widths: 25 25 50
   :header-rows: 1

   * - Field
     - Type
     - Mandatory
   * - Reduction Plan
     - string: validate for filepath usage
     - yes
   * - Instrument
     - string for dropdown list
     - yes
   * - Wavelength
     - positive float
     - yes
   * - Wavelength Band
     - 2 numbers: positive float min<max
     - yes
   * - Grouping
     - string for dropdown list
     - yes
   * - UB Matrix
     - string filepath
     - yes
   * - Detector Callibration
     - string filepath
     - no
   * - Tube Callibration
     - string filepath
     - no
   * - Flux
     - string filepath
     - no
   * - Solid Angle
     - string filepath
     - no
   * - Mask
     - string filepath
     - no
   * - Background
     - string filepath
     - no
   * - Reduction Plan filled
     - string filepath
     - yes
   * - offset
     - integer number >= 0
     - no
   * - elastic
     - bool: false
     - no
   * - IPTS
     - number: check if the folder exists
     - yes
   * - Run Ranges
     - number: check if the files exist
     - yes
   * - Experiment number in IPTS
     - number: check if the file exists
     - yes

all files are checked whether they exist and have the correct extension.
