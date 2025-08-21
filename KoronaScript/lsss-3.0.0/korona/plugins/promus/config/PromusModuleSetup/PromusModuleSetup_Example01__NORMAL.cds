<?xml version="1.0" encoding="UTF-8"?>

<ModuleContainer version="4">
   <modules>
      <module name="CommentModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LineBreak">false</parameter>
            <parameter name="Label"/>
            <parameter name="Comment">MS70 transducer is usually not set, so here it is set to 7.5 m. The module is not supposed to be there in future PROMUS module setups.</parameter>
         </parameters>
      </module>
      <module name="TransducerDepthModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="TransducerDepth">7.5</parameter>
         </parameters>
      </module>
      <module name="CommentModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LineBreak">false</parameter>
            <parameter name="Label"/>
            <parameter name="Comment">New 2015.05.17: Dept restriction in DataReductionPromus</parameter>
         </parameters>
      </module>
      <module name="DataReductionPromus">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="MinRange">20</parameter>
            <parameter name="MaxRange">1000</parameter>
            <parameter name="MinHorizontal">0</parameter>
            <parameter name="MaxHorizontal">1000</parameter>
            <parameter name="HorizontalCut">Sample center</parameter>
            <parameter name="MinDepth">4</parameter>
            <parameter name="MaxDepth">1000</parameter>
            <parameter name="DepthCut">Sample extent</parameter>
            <parameter name="BeamWidthScaling">1.5</parameter>
            <parameter name="MinFan">1</parameter>
            <parameter name="MaxFan">20</parameter>
            <parameter name="MinVertFan">1</parameter>
            <parameter name="MaxVertFan">25</parameter>
         </parameters>
      </module>
      <module name="CommentModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LineBreak">true</parameter>
            <parameter name="VerticalSpace">8</parameter>
            <parameter name="Label">NOISE REMOVAL:</parameter>
            <parameter name="Comment">First DataReductionModule intended to remove data that is always bad. First MedianSpikeModule is supposed to remove "spike walls", e.g.
spikes due to external sonars. Second MedianSpikeModule is supposed to remove "spike beams", i.e. one beam that is much stronger than
the surrounding 9 beams.
The SpotNoiseModule is used to remove single bad samples.</parameter>
         </parameters>
      </module>
      <module name="MedianSpikeFilterModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LogarithmicValues">true</parameter>
            <parameter name="ShowDetails">true</parameter>
            <parameter name="OnlyLast">false</parameter>
            <parameter name="ChannelsToProcess">-1</parameter>
            <parameter name="AutomaticDepthRange">false</parameter>
            <parameter name="StartDepth">-10</parameter>
            <parameter name="EndDepth">1000</parameter>
            <parameter name="SpikeThreshold">-45</parameter>
            <parameter name="TotalDelta">20</parameter>
            <parameter name="WindowMedianSearchHeight">0</parameter>
            <parameter name="WindowMedianHorizontalSearchWidth">0</parameter>
            <parameter name="WindowMedianVerticalSearchWidth">0</parameter>
            <parameter name="Debug">false</parameter>
            <parameter name="ValidFanRange">
               <parameter name="min">19</parameter>
               <parameter name="max">20</parameter>
            </parameter>
         </parameters>
      </module>
      <module name="MedianSpikeFilterModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LogarithmicValues">true</parameter>
            <parameter name="ShowDetails">true</parameter>
            <parameter name="OnlyLast">false</parameter>
            <parameter name="ChannelsToProcess">-1</parameter>
            <parameter name="AutomaticDepthRange">false</parameter>
            <parameter name="StartDepth">-10</parameter>
            <parameter name="EndDepth">1000</parameter>
            <parameter name="SpikeThreshold">-45</parameter>
            <parameter name="TotalDelta">15</parameter>
            <parameter name="WindowMedianSearchHeight">10</parameter>
            <parameter name="WindowMedianHorizontalSearchWidth">0</parameter>
            <parameter name="WindowMedianVerticalSearchWidth">0</parameter>
            <parameter name="Debug">true</parameter>
            <parameter name="ValidFanRange">
               <parameter name="min">1</parameter>
               <parameter name="max">20</parameter>
            </parameter>
         </parameters>
      </module>
      <module name="MedianSpikeFilterModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LogarithmicValues">true</parameter>
            <parameter name="ShowDetails">true</parameter>
            <parameter name="OnlyLast">false</parameter>
            <parameter name="ChannelsToProcess">-1</parameter>
            <parameter name="AutomaticDepthRange">false</parameter>
            <parameter name="StartDepth">-10</parameter>
            <parameter name="EndDepth">1000</parameter>
            <parameter name="SpikeThreshold">-45</parameter>
            <parameter name="TotalDelta">15</parameter>
            <parameter name="WindowMedianSearchHeight">0</parameter>
            <parameter name="WindowMedianHorizontalSearchWidth">1</parameter>
            <parameter name="WindowMedianVerticalSearchWidth">1</parameter>
            <parameter name="Debug">false</parameter>
            <parameter name="ValidFanRange">
               <parameter name="min">1</parameter>
               <parameter name="max">20</parameter>
            </parameter>
         </parameters>
      </module>
      <module name="SpotNoiseModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LogarithmicValues">true</parameter>
            <parameter name="ShowDetails">true</parameter>
            <parameter name="OnlyLast">false</parameter>
            <parameter name="ChannelsToProcess">-1</parameter>
            <parameter name="AutomaticDepthRange">false</parameter>
            <parameter name="StartDepth">-10</parameter>
            <parameter name="EndDepth">2500</parameter>
            <parameter name="Delta">15</parameter>
            <parameter name="Debug">false</parameter>
         </parameters>
      </module>
      <module name="NoiseMedianQuantificationModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="PingHistory">3</parameter>
            <parameter name="NoiseSamplesPerBeam">300</parameter>
            <parameter name="DetectionDistance">175</parameter>
            <parameter name="InnermostDistance">false</parameter>
         </parameters>
      </module>
      <module name="CommentModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LineBreak">false</parameter>
            <parameter name="Label"/>
            <parameter name="Comment">The BeamSmootherModule smooths data along the beam. This is done to make estimation of ambient noise more sable and reliable. The
NoiseMedianQuantificationModule calculates the noise from the current ping, hte NoiseAcceptanceModule compares the quantified noise with
previous estimated noise stored in files, and the NoiseRemoverModule removes ambient noise for each beam.
**** Standard settings on NoiseAcceptanceModule is 0.25 - 4. The current settings are 1 - 1, i.e. noise ia always removed according to files! *****</parameter>
         </parameters>
      </module>
      <module name="BeamSmootherModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="BeamKernelType">gaussian</parameter>
            <parameter name="BeamKernelWidth">8</parameter>
         </parameters>
      </module>
      <module name="NoiseAcceptanceModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="NoiseFraction">
               <parameter name="min">0.5</parameter>
               <parameter name="max">2</parameter>
            </parameter>
            <parameter name="UseFileNoiseFile">false</parameter>
            <parameter name="UseDayNoiseFile">false</parameter>
            <parameter name="UseSurveyNoiseFile">true</parameter>
            <parameter name="UseSurveyLowNoiseFile">true</parameter>
         </parameters>
      </module>
      <module name="NoiseRemoverModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="RemoveNoiseFromStart">true</parameter>
            <parameter name="MaxBufferSize">10</parameter>
         </parameters>
      </module>
      <module name="CommentModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LineBreak">true</parameter>
            <parameter name="VerticalSpace">8</parameter>
            <parameter name="Label">SPIKE NOISE REMOVAL:</parameter>
            <parameter name="Comment">The three following MedianSpikeFilterModules are to remove fans (first), beams after along-beam smoothing (second)
 "time noise" (first), i.e. a ping which is bad, and then beams that are bad.</parameter>
         </parameters>
      </module>
      <module name="MedianSpikeFilterModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LogarithmicValues">true</parameter>
            <parameter name="ShowDetails">true</parameter>
            <parameter name="OnlyLast">false</parameter>
            <parameter name="ChannelsToProcess">-1</parameter>
            <parameter name="AutomaticDepthRange">false</parameter>
            <parameter name="StartDepth">-10</parameter>
            <parameter name="EndDepth">1000</parameter>
            <parameter name="SpikeThreshold">-70</parameter>
            <parameter name="TotalDelta">20</parameter>
            <parameter name="WindowMedianSearchHeight">0</parameter>
            <parameter name="WindowMedianHorizontalSearchWidth">0</parameter>
            <parameter name="WindowMedianVerticalSearchWidth">2</parameter>
            <parameter name="Debug">false</parameter>
            <parameter name="ValidFanRange">
               <parameter name="min">1</parameter>
               <parameter name="max">20</parameter>
            </parameter>
         </parameters>
      </module>
      <module name="MedianSpikeFilterModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LogarithmicValues">true</parameter>
            <parameter name="ShowDetails">true</parameter>
            <parameter name="OnlyLast">false</parameter>
            <parameter name="ChannelsToProcess">-1</parameter>
            <parameter name="AutomaticDepthRange">false</parameter>
            <parameter name="StartDepth">-10</parameter>
            <parameter name="EndDepth">1000</parameter>
            <parameter name="SpikeThreshold">-70</parameter>
            <parameter name="TotalDelta">20</parameter>
            <parameter name="WindowMedianSearchHeight">0</parameter>
            <parameter name="WindowMedianHorizontalSearchWidth">1</parameter>
            <parameter name="WindowMedianVerticalSearchWidth">1</parameter>
            <parameter name="Debug">false</parameter>
            <parameter name="ValidFanRange">
               <parameter name="min">1</parameter>
               <parameter name="max">20</parameter>
            </parameter>
         </parameters>
      </module>
      <module name="MedianSpikeFilterModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LogarithmicValues">true</parameter>
            <parameter name="ShowDetails">true</parameter>
            <parameter name="OnlyLast">false</parameter>
            <parameter name="ChannelsToProcess">-1</parameter>
            <parameter name="AutomaticDepthRange">false</parameter>
            <parameter name="StartDepth">-10</parameter>
            <parameter name="EndDepth">1000</parameter>
            <parameter name="SpikeThreshold">-70</parameter>
            <parameter name="TotalDelta">20</parameter>
            <parameter name="WindowMedianSearchHeight">1</parameter>
            <parameter name="WindowMedianHorizontalSearchWidth">1</parameter>
            <parameter name="WindowMedianVerticalSearchWidth">1</parameter>
            <parameter name="Debug">false</parameter>
            <parameter name="ValidFanRange">
               <parameter name="min">1</parameter>
               <parameter name="max">20</parameter>
            </parameter>
         </parameters>
      </module>
      <module name="CommentModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LineBreak">false</parameter>
            <parameter name="Label"/>
            <parameter name="Comment">New MedianFilterSpikeModule to remove time-noise only: the threshold is very large!!!</parameter>
         </parameters>
      </module>
      <module name="MedianSpikeFilterModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LogarithmicValues">true</parameter>
            <parameter name="ShowDetails">true</parameter>
            <parameter name="OnlyLast">false</parameter>
            <parameter name="ChannelsToProcess">-1</parameter>
            <parameter name="AutomaticDepthRange">true</parameter>
            <parameter name="StartDepth">10</parameter>
            <parameter name="EndDepth">1000</parameter>
            <parameter name="SpikeThreshold">-120</parameter>
            <parameter name="TotalDelta">50</parameter>
            <parameter name="WindowMedianSearchHeight">0</parameter>
            <parameter name="WindowMedianHorizontalSearchWidth">0</parameter>
            <parameter name="WindowMedianVerticalSearchWidth">0</parameter>
            <parameter name="Debug">false</parameter>
            <parameter name="ValidFanRange">
               <parameter name="min">1</parameter>
               <parameter name="max">20</parameter>
            </parameter>
         </parameters>
      </module>
      <module name="CommentModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LineBreak">false</parameter>
            <parameter name="Label"/>
            <parameter name="Comment">The two ThresholdModules are there to clamp remaining measurements to realistic values</parameter>
         </parameters>
      </module>
      <module name="ThresholdModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LogarithmicValues">true</parameter>
            <parameter name="ShowDetails">true</parameter>
            <parameter name="OnlyLast">false</parameter>
            <parameter name="ChannelsToProcess">-1</parameter>
            <parameter name="AutomaticDepthRange">false</parameter>
            <parameter name="StartDepth">-10</parameter>
            <parameter name="EndDepth">1000</parameter>
            <parameter name="Threshold">-70</parameter>
            <parameter name="CutBelow">true</parameter>
            <parameter name="CutAbove">false</parameter>
            <parameter name="BelowVal">-120</parameter>
            <parameter name="AboveVal">-120</parameter>
         </parameters>
      </module>
      <module name="ThresholdModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LogarithmicValues">true</parameter>
            <parameter name="ShowDetails">true</parameter>
            <parameter name="OnlyLast">false</parameter>
            <parameter name="ChannelsToProcess">-1</parameter>
            <parameter name="AutomaticDepthRange">false</parameter>
            <parameter name="StartDepth">-10</parameter>
            <parameter name="EndDepth">1000</parameter>
            <parameter name="Threshold">-5</parameter>
            <parameter name="CutBelow">false</parameter>
            <parameter name="CutAbove">true</parameter>
            <parameter name="BelowVal">-120</parameter>
            <parameter name="AboveVal">-120</parameter>
         </parameters>
      </module>
      <module name="CommentModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LineBreak">true</parameter>
            <parameter name="VerticalSpace">8</parameter>
            <parameter name="Label">DATA REDUCTION (geometrical):</parameter>
            <parameter name="Comment">The following DataReductionModule could have been earlier in the ModuleSetup, but is placed as late as possible due to the
MedianSpikeFilter modules. It is placed before the split to the Phantom processing.</parameter>
         </parameters>
      </module>
      <module name="DataReductionPromus">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="Comment">Main purpose is to exclude beyond a range, and beyond a depth</parameter>
            <parameter name="MinRange">0</parameter>
            <parameter name="MaxRange">1000</parameter>
            <parameter name="MinHorizontal">0</parameter>
            <parameter name="MaxHorizontal">250</parameter>
            <parameter name="HorizontalCut">Sample center</parameter>
            <parameter name="MinDepth">0</parameter>
            <parameter name="MaxDepth">200</parameter>
            <parameter name="DepthCut">Sample center</parameter>
            <parameter name="BeamWidthScaling">1</parameter>
            <parameter name="MinFan">1</parameter>
            <parameter name="MaxFan">20</parameter>
            <parameter name="MinVertFan">1</parameter>
            <parameter name="MaxVertFan">25</parameter>
         </parameters>
      </module>
      <module name="CommentModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LineBreak">true</parameter>
            <parameter name="VerticalSpace">8</parameter>
            <parameter name="Label">DATA FOR PHANTOM ECHOGRAMS:</parameter>
            <parameter name="Comment">The sequence between TemporaryComputationsBeginModule and TemporaryComputationsEndModule reduce data and writes to a file used to
calculate Phantom echograms.</parameter>
         </parameters>
      </module>
      <module name="TemporaryComputationsBeginModule">
         <parameters>
            <parameter name="Active">true</parameter>
         </parameters>
      </module>
      <module name="CommentModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LineBreak">false</parameter>
            <parameter name="Label"/>
            <parameter name="Comment">To save space: keep only the fan (no 16) that is used to generate PhantomEchograms</parameter>
         </parameters>
      </module>
      <module name="DataReductionPromus">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="MinRange">20</parameter>
            <parameter name="MaxRange">400</parameter>
            <parameter name="MinHorizontal">0</parameter>
            <parameter name="MaxHorizontal">1000</parameter>
            <parameter name="HorizontalCut">Sample center</parameter>
            <parameter name="MinDepth">0</parameter>
            <parameter name="MaxDepth">200</parameter>
            <parameter name="DepthCut">Sample center</parameter>
            <parameter name="BeamWidthScaling">1</parameter>
            <parameter name="MinFan">1</parameter>
            <parameter name="MaxFan">18</parameter>
            <parameter name="MinVertFan">16</parameter>
            <parameter name="MaxVertFan">16</parameter>
         </parameters>
      </module>
      <module name="WriterModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="FileName"/>
            <parameter name="UseRelativeDirectory">true</parameter>
            <parameter name="RelativeDirectory">TMP</parameter>
         </parameters>
      </module>
      <module name="TemporaryComputationsEndModule">
         <parameters>
            <parameter name="Active">true</parameter>
         </parameters>
      </module>
      <module name="CommentModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LineBreak">true</parameter>
            <parameter name="VerticalSpace">8</parameter>
            <parameter name="Label">SCHOOL DETECTION AND COMPRESSION:</parameter>
            <parameter name="Comment">The SchoolClusterModule tries to extract schools to be visualised in the MapWindow.</parameter>
         </parameters>
      </module>
      <module name="SchoolClusterModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="NumberOfClusters">2</parameter>
            <parameter name="MinSv">-58</parameter>
            <parameter name="MaxDepth">125</parameter>
            <parameter name="MinDepth">25</parameter>
            <parameter name="IgnoreFans">2</parameter>
            <parameter name="MaxSample">10000</parameter>
            <parameter name="MinSample">20</parameter>
            <parameter name="ColorClusters">false</parameter>
            <parameter name="MinVolume">50000</parameter>
            <parameter name="ClusterSphereRatio">0.5</parameter>
            <parameter name="MinTimeSeriesLength">1</parameter>
         </parameters>
      </module>
      <module name="CommentModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LineBreak">false</parameter>
            <parameter name="Label"/>
            <parameter name="Comment">Currently, the EchoLineExtractorModule generates a bug in PROMUS: turned off</parameter>
         </parameters>
      </module>
      <module name="ThresholdEchoLineExtractor">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="Threshold">-70</parameter>
            <parameter name="MinLineLength">20</parameter>
         </parameters>
      </module>
      <module name="DepthModulePromus">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="InitialDepthGuess">160</parameter>
            <parameter name="RemoveDepthOutliers">true</parameter>
            <parameter name="IterativeFit">true</parameter>
            <parameter name="DoInterpolation">true</parameter>
            <parameter name="LogSv threshold">-50</parameter>
            <parameter name="StabilityMeasure">0.03</parameter>
            <parameter name="PulseWidthDeviation">0.1</parameter>
            <parameter name="UpperFan">10</parameter>
            <parameter name="StartDetectionRange">10</parameter>
         </parameters>
      </module>
      <module name="CommentModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LineBreak">true</parameter>
            <parameter name="VerticalSpace">8</parameter>
            <parameter name="Label">BAD PING COUNT</parameter>
            <parameter name="Comment"/>
         </parameters>
      </module>
      <module name="PromusBadPingsModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="SvThreshold">-60</parameter>
            <parameter name="WritePlotParameters">true</parameter>
            <parameter name="MaxSampleCount"/>
            <parameter name="MaxSvAverage"/>
            <parameter name="MaxVolume"/>
            <parameter name="ExcludePings">false</parameter>
            <parameter name="DeletePings">false</parameter>
         </parameters>
      </module>
   </modules>
</ModuleContainer>
