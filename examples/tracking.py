# Tracking example

# Below is the korona steps for tracking on individual frequencies

# The data we need to get out is the calibrated pulse compressed samples
# that belongs to each track and then calculate the TS(f)


'''
<?xml version="1.0" encoding="UTF-8"?>

<ConfigFiles context="Korona">
   <parameter name="ModuleConfiguration" ref="CfsDirectory">KoronaModuleSetup_Tracking.cds</parameter>
   <parameter name="Categorization" ref="CfsDirectory">categorization.xml</parameter>
   <parameter name="HorizontalTransducerOffsets" ref="CfsDirectory">HorizontalTransducerOffsets.xml</parameter>
   <parameter name="VerticalTransducerOffsets" ref="CfsDirectory">VerticalTransducerOffsets.xml</parameter>
   <parameter name="TransducerRanges" ref="CfsDirectory">TransducerRanges.xml</parameter>
   <parameter name="Plankton" ref="CfsDirectory">Plankton.xml</parameter>
   <parameter name="BroadbandNotchFilters" ref="CfsDirectory">BroadbandNotchFilters.xml</parameter>
   <parameter name="PulseCompressionFilters" ref="CfsDirectory">PulseCompressionFilters.xml</parameter>
   <parameter name="BroadbandSplitterBands" ref="CfsDirectory">BroadbandSplitterBands.xml</parameter>
   <parameter name="Towfish"/>
</ConfigFiles>


<?xml version="1.0" encoding="UTF-8"?>

<ModuleContainer version="4">
   <modules>
      <module name="CommentModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LineBreak">false</parameter>
            <parameter name="Label">Tracking setup:</parameter>
            <parameter name="Comment"/>
         </parameters>
      </module>
      <module name="EmptyPingRemovalModule">
         <parameters>
            <parameter name="Active">true</parameter>
         </parameters>
      </module>
      <module name="DataReductionModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="BlindZone">false</parameter>
            <parameter name="MinRange">14</parameter>
            <parameter name="MinDepth"/>
            <parameter name="TransducerRange">false</parameter>
            <parameter name="MaxRange">26</parameter>
            <parameter name="MaxDepth"/>
         </parameters>
      </module>
      <module name="TrackingModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="TrackerType">SED</parameter>
            <parameter name="kHz">333</parameter>
            <parameter name="PlatformMotionType">Floating</parameter>
            <parameter name="MinTS">-50</parameter>
            <parameter name="PulseLengthDeterminationLevel">5</parameter>
            <parameter name="MinEchoLength">0.005</parameter>
            <parameter name="MaxEchoLength">0.15</parameter>
            <parameter name="MaxGainCompensation">9</parameter>
            <parameter name="DoPhaseDeviationCheck">false</parameter>
            <parameter name="MaxPhaseDevSteps">10</parameter>
            <parameter name="MaxTS">-10</parameter>
            <parameter name="MaxDepth">27</parameter>
            <parameter name="MaxAlongshipAngle">5</parameter>
            <parameter name="MaxAthwartshipAngle">5</parameter>
            <parameter name="InitiationGateFunction">
               <parameter name="Alpha">2.8</parameter>
               <parameter name="Beta">2.8</parameter>
               <parameter name="Range">0.1</parameter>
               <parameter name="TS">20</parameter>
            </parameter>
            <parameter name="InitiationMinLength">1</parameter>
            <parameter name="GateFunction">
               <parameter name="Alpha">2.8</parameter>
               <parameter name="Beta">2.8</parameter>
               <parameter name="Range">0.1</parameter>
               <parameter name="TS">20</parameter>
            </parameter>
            <parameter name="AlphaBetaEstimator">
               <parameter name="Alpha">0.9</parameter>
               <parameter name="Beta">0.1</parameter>
            </parameter>
            <parameter name="MaxMissingPings">4</parameter>
            <parameter name="MaxMissingSamples">2</parameter>
            <parameter name="MaxMissingPingsFraction">0.7</parameter>
            <parameter name="MinTrackLength">10</parameter>
            <parameter name="MinSampleToLengthFraction">1</parameter>
         </parameters>
      </module>
      <module name="TrackingModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="TrackerType">SED</parameter>
            <parameter name="kHz">200</parameter>
            <parameter name="PlatformMotionType">Floating</parameter>
            <parameter name="MinTS">-50</parameter>
            <parameter name="PulseLengthDeterminationLevel">9</parameter>
            <parameter name="MinEchoLength">0.005</parameter>
            <parameter name="MaxEchoLength">0.15</parameter>
            <parameter name="MaxGainCompensation">9</parameter>
            <parameter name="DoPhaseDeviationCheck">false</parameter>
            <parameter name="MaxPhaseDevSteps">10</parameter>
            <parameter name="MaxTS">-10</parameter>
            <parameter name="MaxDepth">27</parameter>
            <parameter name="MaxAlongshipAngle">7</parameter>
            <parameter name="MaxAthwartshipAngle">7</parameter>
            <parameter name="InitiationGateFunction">
               <parameter name="Alpha">2.8</parameter>
               <parameter name="Beta">2.8</parameter>
               <parameter name="Range">0.1</parameter>
               <parameter name="TS">20</parameter>
            </parameter>
            <parameter name="InitiationMinLength">1</parameter>
            <parameter name="GateFunction">
               <parameter name="Alpha">2.8</parameter>
               <parameter name="Beta">2.8</parameter>
               <parameter name="Range">0.1</parameter>
               <parameter name="TS">20</parameter>
            </parameter>
            <parameter name="AlphaBetaEstimator">
               <parameter name="Alpha">0.9</parameter>
               <parameter name="Beta">0.1</parameter>
            </parameter>
            <parameter name="MaxMissingPings">1</parameter>
            <parameter name="MaxMissingSamples">1</parameter>
            <parameter name="MaxMissingPingsFraction">0.7</parameter>
            <parameter name="MinTrackLength">10</parameter>
            <parameter name="MinSampleToLengthFraction">1</parameter>
         </parameters>
      </module>
      <module name="TrackingModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="TrackerType">SED</parameter>
            <parameter name="kHz">120</parameter>
            <parameter name="PlatformMotionType">Floating</parameter>
            <parameter name="MinTS">-50</parameter>
            <parameter name="PulseLengthDeterminationLevel">5</parameter>
            <parameter name="MinEchoLength">0.005</parameter>
            <parameter name="MaxEchoLength">0.15</parameter>
            <parameter name="MaxGainCompensation">9</parameter>
            <parameter name="DoPhaseDeviationCheck">false</parameter>
            <parameter name="MaxPhaseDevSteps">10</parameter>
            <parameter name="MaxTS">-10</parameter>
            <parameter name="MaxDepth">27</parameter>
            <parameter name="MaxAlongshipAngle">5</parameter>
            <parameter name="MaxAthwartshipAngle">5</parameter>
            <parameter name="InitiationGateFunction">
               <parameter name="Alpha">2.8</parameter>
               <parameter name="Beta">2.8</parameter>
               <parameter name="Range">0.1</parameter>
               <parameter name="TS">20</parameter>
            </parameter>
            <parameter name="InitiationMinLength">1</parameter>
            <parameter name="GateFunction">
               <parameter name="Alpha">2.8</parameter>
               <parameter name="Beta">2.8</parameter>
               <parameter name="Range">0.1</parameter>
               <parameter name="TS">20</parameter>
            </parameter>
            <parameter name="AlphaBetaEstimator">
               <parameter name="Alpha">0.9</parameter>
               <parameter name="Beta">0.1</parameter>
            </parameter>
            <parameter name="MaxMissingPings">4</parameter>
            <parameter name="MaxMissingSamples">2</parameter>
            <parameter name="MaxMissingPingsFraction">0.7</parameter>
            <parameter name="MinTrackLength">10</parameter>
            <parameter name="MinSampleToLengthFraction">1</parameter>
         </parameters>
      </module>
      <module name="TrackingModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="TrackerType">SED</parameter>
            <parameter name="kHz">70</parameter>
            <parameter name="PlatformMotionType">Floating</parameter>
            <parameter name="MinTS">-50</parameter>
            <parameter name="PulseLengthDeterminationLevel">5</parameter>
            <parameter name="MinEchoLength">0.005</parameter>
            <parameter name="MaxEchoLength">0.15</parameter>
            <parameter name="MaxGainCompensation">9</parameter>
            <parameter name="DoPhaseDeviationCheck">false</parameter>
            <parameter name="MaxPhaseDevSteps">10</parameter>
            <parameter name="MaxTS">-10</parameter>
            <parameter name="MaxDepth">27</parameter>
            <parameter name="MaxAlongshipAngle">5</parameter>
            <parameter name="MaxAthwartshipAngle">5</parameter>
            <parameter name="InitiationGateFunction">
               <parameter name="Alpha">2.8</parameter>
               <parameter name="Beta">2.8</parameter>
               <parameter name="Range">0.05</parameter>
               <parameter name="TS">20</parameter>
            </parameter>
            <parameter name="InitiationMinLength">2</parameter>
            <parameter name="GateFunction">
               <parameter name="Alpha">2.8</parameter>
               <parameter name="Beta">2.8</parameter>
               <parameter name="Range">0.1</parameter>
               <parameter name="TS">20</parameter>
            </parameter>
            <parameter name="AlphaBetaEstimator">
               <parameter name="Alpha">0.9</parameter>
               <parameter name="Beta">0.1</parameter>
            </parameter>
            <parameter name="MaxMissingPings">4</parameter>
            <parameter name="MaxMissingSamples">2</parameter>
            <parameter name="MaxMissingPingsFraction">0.7</parameter>
            <parameter name="MinTrackLength">10</parameter>
            <parameter name="MinSampleToLengthFraction">1</parameter>
         </parameters>
      </module>
      <module name="TrackingModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="TrackerType">SED</parameter>
            <parameter name="kHz">38</parameter>
            <parameter name="PlatformMotionType">Floating</parameter>
            <parameter name="MinTS">-50</parameter>
            <parameter name="PulseLengthDeterminationLevel">5</parameter>
            <parameter name="MinEchoLength">0.005</parameter>
            <parameter name="MaxEchoLength">1.5</parameter>
            <parameter name="MaxGainCompensation">9</parameter>
            <parameter name="DoPhaseDeviationCheck">false</parameter>
            <parameter name="MaxPhaseDevSteps">8</parameter>
            <parameter name="MaxTS">-10</parameter>
            <parameter name="MaxDepth">27</parameter>
            <parameter name="MaxAlongshipAngle">5</parameter>
            <parameter name="MaxAthwartshipAngle">5</parameter>
            <parameter name="InitiationGateFunction">
               <parameter name="Alpha">2.8</parameter>
               <parameter name="Beta">2.8</parameter>
               <parameter name="Range">0.1</parameter>
               <parameter name="TS">20</parameter>
            </parameter>
            <parameter name="InitiationMinLength">1</parameter>
            <parameter name="GateFunction">
               <parameter name="Alpha">2.8</parameter>
               <parameter name="Beta">2.8</parameter>
               <parameter name="Range">0.1</parameter>
               <parameter name="TS">20</parameter>
            </parameter>
            <parameter name="AlphaBetaEstimator">
               <parameter name="Alpha">0.9</parameter>
               <parameter name="Beta">0.1</parameter>
            </parameter>
            <parameter name="MaxMissingPings">4</parameter>
            <parameter name="MaxMissingSamples">2</parameter>
            <parameter name="MaxMissingPingsFraction">0.7</parameter>
            <parameter name="MinTrackLength">10</parameter>
            <parameter name="MinSampleToLengthFraction">1</parameter>
         </parameters>
      </module>
      <module name="TsDetectionModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="DetectorType">PEAK</parameter>
            <parameter name="MinTS">-50</parameter>
            <parameter name="PulseLengthDeterminationLevel">6</parameter>
            <parameter name="MinEchoLength">0.005</parameter>
            <parameter name="MaxEchoLength">0.15</parameter>
            <parameter name="MaxGainCompensation">4</parameter>
            <parameter name="DoPhaseDeviationCheck">false</parameter>
            <parameter name="MaxPhaseDevSteps">8</parameter>
            <parameter name="MaxDepth">300</parameter>
         </parameters>
      </module>
   </modules>
</ModuleContainer>
'''
