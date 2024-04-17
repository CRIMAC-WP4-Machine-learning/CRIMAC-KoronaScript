import KoronaScript.Modules as ksm
import KoronaScript as ks
import os
import sys

ksi = ks.KoronaScript(TransducerRanges = "examples/TransducerRanges.xml")

# Add the pulsecompression module and write to nc

ksi.add(ksm.TsDetection(Active = "true",
                        DetectorType = "PEAK",
                        MinTS = "-66",
                        PulseLengthDeterminationLevel = "6",
                        MinEchoLength = "0.01",
                        MaxEchoLength = "1.8",
                        MaxGainCompensation = "6",
                        DoPhaseDeviationCheck = "true",
                        MaxPhaseDevSteps = "8",
                        MaxDepth = "40"))

ksi.write()
ksi.run(src = sys.argv[1], dst = sys.argv[2])
