<?xml version="1.0" encoding="UTF-8"?>

<ModuleContainer version="4">
   <modules>
      <module name="CommentModule">
         <parameters>
            <parameter name="Active">true</parameter>
            <parameter name="LineBreak">false</parameter>
            <parameter name="Label">COPY DATA</parameter>
            <parameter name="Comment">KORONA reads data from the source directory and writes to the destination directory. If the Write module is active, it will write to the directory specified there (in addition to the destination directory specified in the config setup).</parameter>
         </parameters>
      </module>
      <module name="WriterModule">
         <parameters>
            <parameter name="Active">false</parameter>
            <parameter name="FileName"/>
            <parameter name="UseRelativeDirectory">false</parameter>
            <parameter name="DirectoryName">F:\LSSS_DATA\S2012116_PG.O.Sars[4174]\MS70Raw</parameter>
         </parameters>
      </module>
   </modules>
</ModuleContainer>
