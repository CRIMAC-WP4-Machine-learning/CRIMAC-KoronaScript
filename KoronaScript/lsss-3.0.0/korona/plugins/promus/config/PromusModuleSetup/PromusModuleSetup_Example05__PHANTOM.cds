<?xml version="1.0" encoding="UTF-8"?>

<ModuleContainer version="4">
   <modules>
      <module name="DataReductionPromus">
         <parameters>
            <parameter name="Active">false</parameter>
            <parameter name="MinRange">0</parameter>
            <parameter name="MaxRange">1000</parameter>
            <parameter name="MinHorizontal">0</parameter>
            <parameter name="MaxHorizontal">1000</parameter>
            <parameter name="HorizontalCut">Sample center</parameter>
            <parameter name="MinDepth">0</parameter>
            <parameter name="MaxDepth">1000</parameter>
            <parameter name="DepthCut">Sample extent</parameter>
            <parameter name="BeamWidthScaling">1</parameter>
            <parameter name="MinFan">1</parameter>
            <parameter name="MaxFan">19</parameter>
            <parameter name="MinVertFan">1</parameter>
            <parameter name="MaxVertFan">2147483647</parameter>
         </parameters>
      </module>
      <module name="SpatialSpikeFilterModule">
         <parameters>
            <parameter name="Active">false</parameter>
            <parameter name="SpikeThreshold">-36</parameter>
            <parameter name="SpikeHeight">5</parameter>
         </parameters>
      </module>
      <module name="TemporalSpikeFilterModule">
         <parameters>
            <parameter name="Active">false</parameter>
            <parameter name="SpikeThreshold">-36</parameter>
            <parameter name="SpikeHeight">5</parameter>
         </parameters>
      </module>
      <module name="MedianSpikeFilterModule">
         <parameters>
            <parameter name="Active">false</parameter>
            <parameter name="LogarithmicValues">true</parameter>
            <parameter name="ShowDetails">true</parameter>
            <parameter name="OnlyLast">false</parameter>
            <parameter name="ChannelsToProcess">-1</parameter>
            <parameter name="AutomaticDepthRange">false</parameter>
            <parameter name="StartDepth">0</parameter>
            <parameter name="EndDepth">1000</parameter>
            <parameter name="SpikeThreshold">-38</parameter>
            <parameter name="TotalDelta">15</parameter>
            <parameter name="WindowMedianSearchHeight">10</parameter>
            <parameter name="WindowMedianHorizontalSearchWidth">0</parameter>
            <parameter name="WindowMedianVerticalSearchWidth">0</parameter>
            <parameter name="Debug">false</parameter>
            <parameter name="ValidFanRange">
               <parameter name="min">1</parameter>
               <parameter name="max">20</parameter>
            </parameter>
         </parameters>
      </module>
      <module name="MedianSpikeFilterModule">
         <parameters>
            <parameter name="Active">false</parameter>
            <parameter name="LogarithmicValues">true</parameter>
            <parameter name="ShowDetails">true</parameter>
            <parameter name="OnlyLast">false</parameter>
            <parameter name="ChannelsToProcess">-1</parameter>
            <parameter name="AutomaticDepthRange">false</parameter>
            <parameter name="StartDepth">0</parameter>
            <parameter name="EndDepth">1000</parameter>
            <parameter name="SpikeThreshold">-38</parameter>
            <parameter name="TotalDelta">15</parameter>
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
      <module name="MedianSpikeFilterModule">
         <parameters>
            <parameter name="Active">false</parameter>
            <parameter name="LogarithmicValues">true</parameter>
            <parameter name="ShowDetails">true</parameter>
            <parameter name="OnlyLast">false</parameter>
            <parameter name="ChannelsToProcess">-1</parameter>
            <parameter name="AutomaticDepthRange">false</parameter>
            <parameter name="StartDepth">0</parameter>
            <parameter name="EndDepth">1000</parameter>
            <parameter name="SpikeThreshold">-38</parameter>
            <parameter name="TotalDelta">15</parameter>
            <parameter name="WindowMedianSearchHeight">3</parameter>
            <parameter name="WindowMedianHorizontalSearchWidth">0</parameter>
            <parameter name="WindowMedianVerticalSearchWidth">0</parameter>
            <parameter name="Debug">false</parameter>
            <parameter name="ValidFanRange">
               <parameter name="min">1</parameter>
               <parameter name="max">20</parameter>
            </parameter>
         </parameters>
      </module>
      <module name="BeamSmootherModule">
         <parameters>
            <parameter name="Active">false</parameter>
            <parameter name="BeamKernelType">gaussian</parameter>
            <parameter name="BeamKernelWidth">15</parameter>
         </parameters>
      </module>
      <module name="NoiseMedianQuantificationModule">
         <parameters>
            <parameter name="Active">false</parameter>
            <parameter name="PingHistory">1</parameter>
            <parameter name="NoiseSamplesPerBeam">150</parameter>
            <parameter name="DetectionDistance">50</parameter>
            <parameter name="InnermostDistance">false</parameter>
         </parameters>
      </module>
      <module name="NoiseAcceptanceModule">
         <parameters>
            <parameter name="Active">false</parameter>
            <parameter name="NoiseFraction">
               <parameter name="min">0.25</parameter>
               <parameter name="max">4</parameter>
            </parameter>
            <parameter name="UseFileNoiseFile">true</parameter>
            <parameter name="UseDayNoiseFile">true</parameter>
            <parameter name="UseSurveyNoiseFile">true</parameter>
            <parameter name="UseSurveyLowNoiseFile">true</parameter>
         </parameters>
      </module>
      <module name="NoiseRemoverModule">
         <parameters>
            <parameter name="Active">false</parameter>
            <parameter name="RemoveNoiseFromStart">true</parameter>
            <parameter name="MaxBufferSize">10</parameter>
         </parameters>
      </module>
      <module name="MedianSpikeFilterModule">
         <parameters>
            <parameter name="Active">false</parameter>
            <parameter name="LogarithmicValues">true</parameter>
            <parameter name="ShowDetails">true</parameter>
            <parameter name="OnlyLast">false</parameter>
            <parameter name="ChannelsToProcess">-1</parameter>
            <parameter name="AutomaticDepthRange">false</parameter>
            <parameter name="StartDepth">0</parameter>
            <parameter name="EndDepth">1000</parameter>
            <parameter name="SpikeThreshold">-70</parameter>
            <parameter name="TotalDelta">10</parameter>
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
      <module name="ThresholdModule">
         <parameters>
            <parameter name="Active">false</parameter>
            <parameter name="LogarithmicValues">true</parameter>
            <parameter name="ShowDetails">true</parameter>
            <parameter name="OnlyLast">false</parameter>
            <parameter name="ChannelsToProcess">-1</parameter>
            <parameter name="AutomaticDepthRange">false</parameter>
            <parameter name="StartDepth">0</parameter>
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
            <parameter name="Active">false</parameter>
            <parameter name="LogarithmicValues">true</parameter>
            <parameter name="ShowDetails">true</parameter>
            <parameter name="OnlyLast">false</parameter>
            <parameter name="ChannelsToProcess">-1</parameter>
            <parameter name="AutomaticDepthRange">false</parameter>
            <parameter name="StartDepth">0</parameter>
            <parameter name="EndDepth">1000</parameter>
            <parameter name="Threshold">-15</parameter>
            <parameter name="CutBelow">false</parameter>
            <parameter name="CutAbove">true</parameter>
            <parameter name="BelowVal">-120</parameter>
            <parameter name="AboveVal">-120</parameter>
         </parameters>
      </module>
      <module name="MedianSpikeFilterModule">
         <parameters>
            <parameter name="Active">false</parameter>
            <parameter name="LogarithmicValues">true</parameter>
            <parameter name="ShowDetails">true</parameter>
            <parameter name="OnlyLast">false</parameter>
            <parameter name="ChannelsToProcess">-1</parameter>
            <parameter name="AutomaticDepthRange">true</parameter>
            <parameter name="StartDepth">10</parameter>
            <parameter name="EndDepth">1000</parameter>
            <parameter name="SpikeThreshold">-120</parameter>
            <parameter name="TotalDelta">15</parameter>
            <parameter name="WindowMedianSearchHeight">7</parameter>
            <parameter name="WindowMedianHorizontalSearchWidth">0</parameter>
            <parameter name="WindowMedianVerticalSearchWidth">0</parameter>
            <parameter name="Debug">false</parameter>
            <parameter name="ValidFanRange">
               <parameter name="min">1</parameter>
               <parameter name="max">20</parameter>
            </parameter>
         </parameters>
      </module>
      <module name="WriterModule">
         <parameters>
            <parameter name="Active">false</parameter>
            <parameter name="FileName"/>
            <parameter name="UseRelativeDirectory">true</parameter>
            <parameter name="RelativeDirectory">TMP</parameter>
         </parameters>
      </module>
      <module name="DataReductionPromus">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="MinRange">25</parameter>
            <parameter name="MaxRange">500</parameter>
            <parameter name="MinHorizontal">0</parameter>
            <parameter name="MaxHorizontal">1000</parameter>
            <parameter name="HorizontalCut">Sample center</parameter>
            <parameter name="MinDepth">15</parameter>
            <parameter name="MaxDepth">200</parameter>
            <parameter name="DepthCut">Sample extent</parameter>
            <parameter name="BeamWidthScaling">1</parameter>
            <parameter name="MinFan">1</parameter>
            <parameter name="MaxFan">19</parameter>
            <parameter name="MinVertFan">1</parameter>
            <parameter name="MaxVertFan">25</parameter>
         </parameters>
      </module>
      <module name="PhantomModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="BeamDirType">Vertical</parameter>
            <parameter name="VerticalPlaneAngle">277</parameter>
            <parameter name="UpperDepth">25</parameter>
            <parameter name="LowerDepth">200</parameter>
            <parameter name="InnerDist">20</parameter>
            <parameter name="OuterDist">250</parameter>
            <parameter name="StartDepth">0</parameter>
            <parameter name="X position">0</parameter>
            <parameter name="Y position">-300</parameter>
            <parameter name="Z position">0</parameter>
            <parameter name="NumBeams">10</parameter>
            <parameter name="LastBeamStartX">0</parameter>
            <parameter name="LastBeamStartY">-300</parameter>
            <parameter name="LastBeamStartZ">0</parameter>
            <parameter name="X dir">0</parameter>
            <parameter name="Y dir">0</parameter>
            <parameter name="Z dir">1</parameter>
            <parameter name="Sample distance">1</parameter>
            <parameter name="FanAggregationType">Max</parameter>
            <parameter name="FanAggregationHalfWidth">2</parameter>
         </parameters>
      </module>
      <module name="FillMissingDataModule">
         <parameters>
            <parameter name="Active">true</parameter>
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
            <parameter name="StartDepth">0</parameter>
            <parameter name="EndDepth">1000</parameter>
            <parameter name="Threshold">-57</parameter>
            <parameter name="CutBelow">true</parameter>
            <parameter name="CutAbove">false</parameter>
            <parameter name="BelowVal">-200</parameter>
            <parameter name="AboveVal">0</parameter>
         </parameters>
      </module>
      <module name="SpikeFilterModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LogarithmicValues">true</parameter>
            <parameter name="ShowDetails">true</parameter>
            <parameter name="OnlyLast">false</parameter>
            <parameter name="ChannelsToProcess">-1</parameter>
            <parameter name="AutomaticDepthRange">false</parameter>
            <parameter name="StartDepth">0</parameter>
            <parameter name="EndDepth">400</parameter>
            <parameter name="TotalDelta">15</parameter>
            <parameter name="VerticalDelta">15</parameter>
            <parameter name="Debug">false</parameter>
            <parameter name="VerticalUnit">SAMPLES</parameter>
            <parameter name="VerticalMedianSearchHeight">8</parameter>
            <parameter name="WindowMedianSearchHeight">4</parameter>
            <parameter name="VerticalMedianSearchDuration">0.9</parameter>
            <parameter name="WindowMedianSearchDuration">4.4</parameter>
            <parameter name="VerticalMedianSearchDistance">1.3</parameter>
            <parameter name="WindowMedianSearchDistance">6.6</parameter>
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
            <parameter name="StartDepth">0</parameter>
            <parameter name="EndDepth">2500</parameter>
            <parameter name="Delta">20</parameter>
            <parameter name="Debug">false</parameter>
         </parameters>
      </module>
      <module name="FiskViewDisplayModule">
         <parameters>
            <parameter name="Active">true</parameter>
         </parameters>
      </module>
   </modules>
</ModuleContainer>
