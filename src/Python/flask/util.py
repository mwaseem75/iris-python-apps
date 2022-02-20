import iris

def get_sql_stat( id ):
	if id == 'processes':
		statement = '''
        SELECT ID, NameSpace, Routine, LinesExecuted, GlobalReferences, 
               state, PidExternal, UserName, ClientIPAddress FROM %SYS.ProcessQuery        
        '''
	elif id == 'messages':
		statement = '''
        SELECT TOP 250 
		ID, 
		Banked, 
		BusinessProcessId, 
		CorrespondingMessageId, 
		Description, 
		ErrorStatus, 
		%EXTERNAL(Invocation) AS Invocation, 
		CASE IsError 
			WHEN 1 THEN 'Error' 
			ELSE 'OK' END 
			AS Error,
		MessageBodyClassName,
		MessageBodyId,
		%EXTERNAL(Priority) AS Priority,
		Resent,
		ReturnQueueName,
		SessionId,
		%EXTERNAL(SourceBusinessType) AS SourceBusinessType,
		SourceConfigName, 
		%EXTERNAL(Status) AS Status,
		SuperSession,
		%EXTERNAL(TargetBusinessType) AS TargetBusinessType,
		TargetConfigName, TargetQueueName,
		{fn LEFT(%EXTERNAL(TimeCreated),10 )} AS DateCreated,
		{fn RIGHT(%EXTERNAL(TimeCreated),12 )} AS TimeCreated, 
		{fn LEFT(%EXTERNAL(TimeProcessed),10 )} AS DateProcessed,
		{fn RIGHT(%EXTERNAL(TimeProcessed),12 )} AS TimeProcessed,  
		%EXTERNAL(Type) AS Type 
		FROM Ens.MessageHeader 
		ORDER BY SessionId DESC '''   
	elif id == 'securityusers':
		statement =  '''SELECT 
		ID, AccountNeverExpires, AutheEnabled, ChangePassword, {fn LEFT(%EXTERNAL(CreateDateTime),10 )} AS DateCreated, Enabled, ExpirationDate, Flags, Name
		FROM Security.Users'''
	elif id == 'securityapps':
		statement =  '''SELECT 
		ID, AutheEnabled, AutoCompile, CSPZENEnabled, CSRFToken, CookiePath, DeepSeeEnabled, Description, DispatchClass, Enabled, Name, NameLowerCase, NameSpace
		FROM Security.Applications'''            
	elif id == 'elinfo':
		statement = "SELECT id, configname,job,messageid,sessionid,sourceclass,	sourcemethod,text,timelogged FROM Ens_Util.Log where type = 4"
	elif id == 'elalert':
		statement = "SELECT id, configname,job,messageid,sessionid,sourceclass,	sourcemethod,text,timelogged FROM Ens_Util.Log where type = 6"
	elif id == 'elwarning':
		statement = "SELECT id, configname,job,messageid,sessionid,sourceclass,	sourcemethod,text,timelogged FROM Ens_Util.Log where type = 3"
	elif id == 'elError':
		statement = "SELECT id, configname,job,messageid,sessionid,sourceclass,	sourcemethod,text,timelogged FROM Ens_Util.Log where type = 2"
	
	
	return statement	

#Get dashboard statistics
def get_dashboard_stats( ):
	iris.cls("Embedded.Utils").SetNameSpace("%SYS")
	ref = iris.cls("SYS.Stats.Dashboard").Sample()
	aurg1 = ref.ApplicationErrors
	aurg2 = 44
	content = {'thing':aurg1,'thnig2':aurg2}
	return 3