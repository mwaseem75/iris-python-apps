/// Routing Rule
/// Business process for resultVer Production
/// Given an incoming transform message and forward to operations
Class resultVer.ResultsRule Extends Ens.Rule.Definition
{

Parameter RuleAssistClass = "EnsLib.HL7.MsgRouter.RuleAssist";

XData RuleDefinition [ XMLNamespace = "http://www.intersystems.com/rule" ]
{
<ruleDefinition alias="" context="EnsLib.HL7.MsgRouter.RoutingEngine" production="resultVer.Production">
<ruleSet name="RoutingRule2" effectiveBegin="" effectiveEnd="">
<rule name="" disabled="false">
<constraint name="docCategory" value="2.5"></constraint>
<constraint name="docName" value="ORU_R01"></constraint>
<when condition="1">
<send transform="" target="ToNormalResultsFile"></send>
<return></return>
</when>
</rule>
</ruleSet>
</ruleDefinition>
}

}
