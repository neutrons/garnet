.. _normalization_algo:

Normalization Algorithm
=========================


.. mermaid::

    stateDiagram-v2 
        [*] --> NormalizationInput
        NormalizationInput --> NormalizationAlgorithm
        %%SaveData-->NormalizationOutputs
        NormalizationAlgorithm-->NormalizationOutputs

        state NormalizationInput{
            Prerequisite-->NormalizationUserInputs
            Prerequisite-->AdditionalInstrumentInputs?
            state Prerequisite {
                ReductionPlan
                note left of ReductionPlan
                    required fields for Normalization:
                    UBMatrix, Background, Vanadium and Flux for every instrument and 
                    Mask, Tube and Detector only for SNAP, CORELLI, TOPAZ and MANDI (Laue).
                end note            
            }  
            state NormalizationUserInputs {
                Projections 
                Extents
                Bins
                Symmetry
            }
            state AdditionalInstrumentInputs?{
                RawFilePath
            }
        }
        
        state NormalizationAlgorithm {
            
            CheckInstrumentType-->Laue
            CheckInstrumentType-->Wand2
            CheckInstrumentType-->Demand


            state Laue{
                l_load: LoadEachDataRun
                l_apply: ApplyCalibration
                l_crop:CropWorkspace
                l_ub:LoadUB
                l_qsample:ConvertToQSample
                l_background:LoadBackground
                l_hkl:NormalizeToHKL
                l_compl:CompleteRuns

                [*] --> l_load
                l_load --> l_apply
                l_apply-->l_crop
                l_crop-->l_ub
                l_ub-->l_qsample
                l_qsample-->l_background
                l_background-->l_hkl
                l_hkl-->l_load
                l_hkl-->l_compl
                l_compl-->SaveData
            }

            state Wand2{
                w_ub:LoadUB
                w_background:LoadBackground
                w_hkl:NormalizeToHKL    

                [*]-->LoadData
                LoadData-->w_ub
                w_ub-->w_background
                w_background-->w_hkl
                w_hkl-->SaveData
            }

            state Demand{
                d_load: LoadEachDataRun
                d_ub:LoadUB
                d_background:LoadBackground
                d_hkl:NormalizeToHKL  
                d_compl:CompleteRuns
                
                [*]-->d_load
                d_load-->d_ub
                d_ub-->d_background
                d_background-->d_hkl
                d_hkl-->d_load
                d_hkl-->d_compl
                d_compl-->SaveData
            }
            state SaveData{
            
                SaveUB
                SaveDataHistogram
                SaveNormHistogram
                SaveBkgDataHistogram
            }
        }
        state NormalizationOutputs{
            NormalizationUBMatrix?
            DataHistogram
            NormHistogram
            BkgDataHistogram
            BkgNormHistogram
        }

The Algorithm is executed in the Model side. In case of SNAP, CORELLI, TOPAZ, MANDI and DEMAND the runs can be calculated
in parallel.
The script is described in detail here: `Normalization Script <https://ornlrse.clm.ibmcloud.com/rm/web#action=com.ibm.rdm.web.pages.showArtifactPage&artifactURI=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Fresources%2FTX_gl6-gMwZEe6kustJDRk6kQ&componentURI=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Frm-projects%2F_DADVIOHJEeyU5_2AJWnXOQ%2Fcomponents%2F_DEP4oOHJEeyU5_2AJWnXOQ&vvc.configuration=https%3A%2F%2Fornlrse.clm.ibmcloud.com%2Frm%2Fcm%2Fstream%2F_DEcs8OHJEeyU5_2AJWnXOQ>`_.
