<?xml version="1.0" encoding="UTF-8"?>

<ModuleContainer version="4">
   <modules>
      <module name="BeamModeFilterModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="TypeToKeep">VERTICAL</parameter>
         </parameters>
      </module>
      <module name="ChannelRemovalModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="Channels">1,2,3,8,9</parameter>
            <parameter name="ChannelsFromEnd"/>
            <parameter name="Frequencies"/>
            <parameter name="DataType"/>
            <parameter name="TransmitMode"/>
            <parameter name="KeepSpecified">true</parameter>
         </parameters>
      </module>
      <module name="ComplexToRealModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="ComputeAngles">true</parameter>
            <parameter name="KeepBroadband">false</parameter>
         </parameters>
      </module>
   </modules>
</ModuleContainer>
