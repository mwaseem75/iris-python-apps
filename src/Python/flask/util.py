import iris
#get sql statements based passed id
def get_sql_stat( id ):
	if id == 'processes':
		statement = '''
        SELECT ID, NameSpace, Routine, LinesExecuted, GlobalReferences, 
               state, PidExternal, UserName, ClientIPAddress FROM %SYS.ProcessQuery ORDER BY NameSpace desc        
        '''
	elif id == 'messages':
		statement = '''
        SELECT 
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
		ID, AccountNeverExpires, AutheEnabled, ChangePassword, CreateDateTime AS DateCreated, Enabled, ExpirationDate, Flags, Name
		FROM Security.Users'''
	elif id == 'securityapps':
		statement =  '''SELECT 
		ID, AutheEnabled, AutoCompile, CSPZENEnabled, CSRFToken, CookiePath, DeepSeeEnabled, Description, DispatchClass, Enabled, Name, NameLowerCase, NameSpace
		FROM Security.Applications'''            
	elif id == 'elassert':
		statement = "SELECT id, configname,job,messageid,sessionid,sourceclass,	sourcemethod,text,timelogged FROM Ens_Util.Log where type = 1"
	elif id == 'elerror':
		statement = "SELECT id, configname,job,messageid,sessionid,sourceclass,	sourcemethod,text,timelogged FROM Ens_Util.Log where type = 2"
	elif id == 'elwarning':
		statement = "SELECT id, configname,job,messageid,sessionid,sourceclass,	sourcemethod,text,timelogged FROM Ens_Util.Log where type = 3"
	elif id == 'elinfo':
		statement = "SELECT id, configname,job,messageid,sessionid,sourceclass,	sourcemethod,text,timelogged FROM Ens_Util.Log where type = 4"
	elif id == 'eltrace':
		statement = "SELECT id, configname,job,messageid,sessionid,sourceclass,	sourcemethod,text,timelogged FROM Ens_Util.Log where type = 5"
	elif id == 'elalert':
		statement = "SELECT id, configname,job,messageid,sessionid,sourceclass,	sourcemethod,text,timelogged FROM Ens_Util.Log where type = 6"
	
	return statement	

#Get dashboard statistics
def get_dashboard_stats( ):
	iris.cls("Embedded.Utils").SetNameSpace("%SYS")
	ref = iris.cls("SYS.Stats.Dashboard").Sample()

	statement = iris.sql.exec('SELECT count(*) as tot FROM Security.Users')
	df = statement.dataframe()
	tot_usr = df.iloc[0]['tot']

	statement = iris.sql.exec('SELECT count(*) as tot FROM Security.Applications')
	df = statement.dataframe()
	tot_apps = df.iloc[0]['tot']

	iris.cls("Embedded.Utils").SetNameSpace("USER")
	#Get total processes
	statement = iris.sql.exec('SELECT count(*) as tot FROM %SYS.ProcessQuery')
	df = statement.dataframe()
	tot_pro = df.iloc[0]['tot']

	statement = iris.sql.exec('SELECT count(*) as tot FROM Ens.MessageHeader')
	df = statement.dataframe()
	tot_msg = df.iloc[0]['tot']
	
	statement = iris.sql.exec('SELECT count(*) as tot FROM Ens_Util.Log')
	df = statement.dataframe()
	tot_ev = df.iloc[0]['tot']

	statement = iris.sql.exec('SELECT count(*) as tot FROM Ens_Util.Log where type = 1')
	df = statement.dataframe()
	tot_ev_assert = int(df.iloc[0]['tot'])
	
	statement = iris.sql.exec('SELECT count(*) as tot FROM Ens_Util.Log where type = 2')
	df = statement.dataframe()
	tot_ev_error = int(df.iloc[0]['tot'])
	
	statement = iris.sql.exec('SELECT count(*) as tot FROM Ens_Util.Log where type = 3')
	df = statement.dataframe()
	tot_ev_warning = int(df.iloc[0]['tot'])
	
	statement = iris.sql.exec('SELECT count(*) as tot FROM Ens_Util.Log where type = 4')
	df = statement.dataframe()
	tot_ev_info= int(df.iloc[0]['tot'])
	
	statement = iris.sql.exec('SELECT count(*) as tot FROM Ens_Util.Log where type = 5')
	df = statement.dataframe()
	tot_ev_trace = int(df.iloc[0]['tot'])
	
	statement = iris.sql.exec('SELECT count(*) as tot FROM Ens_Util.Log where type = 6')
	df = statement.dataframe()
	tot_ev_alert = int(df.iloc[0]['tot'])

	last_backup = ref.LastBackup
	
	#check if variable is empty
	if not last_backup:
		last_backup = "Never"

	content = {
		'ApplicationErrors':ref.ApplicationErrors,
		'CSPSessions':ref.CSPSessions,
		'CacheEfficiency':ref.CacheEfficiency,
		'DatabaseSpace' : ref.DatabaseSpace,
		'DiskReads' : ref.DiskReads,
		'DiskWrites' : ref.DiskWrites,
		'ECPAppServer' : ref.ECPAppServer,
		'ECPAppSrvRate' : ref.ECPAppSrvRate,
		'ECPDataServer' : ref.ECPDataServer,
		'ECPDataSrvRate' : ref.ECPDataSrvRate,
		'GloRefs' : ref.GloRefs,
		'GloRefsPerSec' : ref.GloRefsPerSec,
		'GloSets' : ref.GloSets,
		'JournalEntries' : ref.JournalEntries,
		'JournalSpace' : ref.JournalSpace,
		'JournalStatus' : ref.JournalStatus,
		'LastBackup' : last_backup,
		'LicenseCurrent' : ref.LicenseCurrent,
		'LicenseCurrentPct' : ref.LicenseCurrentPct,
		'LicenseHigh' : ref.LicenseHigh,
		'LicenseHighPct' : ref.LicenseHighPct,
		'LicenseLimit' : ref.LicenseLimit,
		'LicenseType' : ref.LicenseType,
		'LockTable' : ref.LockTable,
		'LogicalReads' : ref.LogicalReads,
		'Processes' : ref.Processes,
		'RouRefs' : ref.RouRefs,
		'SeriousAlerts' : ref.SeriousAlerts,
		'ShadowServer' : ref.ShadowServer,
		'ShadowSource' : ref.ShadowSource,
		'SystemUpTime' : ref.SystemUpTime,
		'WriteDaemon' :  ref.WriteDaemon,
		'tot_pro'	: tot_pro,
		'tot_msg'	: tot_msg,
		'tot_usr'	: tot_usr,
		'tot_apps'	: tot_apps,
		'tot_ev' : tot_ev,
		'tot_ev_assert' : tot_ev_assert,
		'tot_ev_error' : tot_ev_error,
		'tot_ev_warning' : tot_ev_warning,
		'tot_ev_info' : tot_ev_info,
		'tot_ev_trace' : tot_ev_trace,
		'tot_ev_alert' : tot_ev_alert

		}

	return content

#Get sidebar statistics
def get_sidebar_stats( ):
	iris.cls("Embedded.Utils").SetNameSpace("%SYS")

	statement = iris.sql.exec('SELECT count(*) as tot FROM Security.Users')
	df = statement.dataframe()
	tot_usr = df.iloc[0]['tot']

	statement = iris.sql.exec('SELECT count(*) as tot FROM Security.Applications')
	df = statement.dataframe()
	tot_apps = df.iloc[0]['tot']

	iris.cls("Embedded.Utils").SetNameSpace("USER")
	#Get total processes
	statement = iris.sql.exec('SELECT count(*) as tot FROM %SYS.ProcessQuery')
	df = statement.dataframe()
	tot_pro = df.iloc[0]['tot']

	statement = iris.sql.exec('SELECT count(*) as tot FROM Ens.MessageHeader')
	df = statement.dataframe()
	tot_msg = df.iloc[0]['tot']
	
	statement = iris.sql.exec('SELECT count(*) as tot FROM Ens_Util.Log')
	df = statement.dataframe()
	tot_ev = df.iloc[0]['tot']

	statement = iris.sql.exec('SELECT count(*) as tot FROM Ens_Util.Log where type = 1')
	df = statement.dataframe()
	tot_ev_assert = int(df.iloc[0]['tot'])
	
	statement = iris.sql.exec('SELECT count(*) as tot FROM Ens_Util.Log where type = 2')
	df = statement.dataframe()
	tot_ev_error = int(df.iloc[0]['tot'])
	
	statement = iris.sql.exec('SELECT count(*) as tot FROM Ens_Util.Log where type = 3')
	df = statement.dataframe()
	tot_ev_warning = int(df.iloc[0]['tot'])
	
	statement = iris.sql.exec('SELECT count(*) as tot FROM Ens_Util.Log where type = 4')
	df = statement.dataframe()
	tot_ev_info= int(df.iloc[0]['tot'])
	
	statement = iris.sql.exec('SELECT count(*) as tot FROM Ens_Util.Log where type = 5')
	df = statement.dataframe()
	tot_ev_trace = int(df.iloc[0]['tot'])
	
	statement = iris.sql.exec('SELECT count(*) as tot FROM Ens_Util.Log where type = 6')
	df = statement.dataframe()
	tot_ev_alert = int(df.iloc[0]['tot'])

	content = {	
		'tot_pro'	: tot_pro,
		'tot_msg'	: tot_msg,
		'tot_usr'	: tot_usr,
		'tot_apps'	: tot_apps,
		'tot_ev' : tot_ev,
		'tot_ev_assert' : tot_ev_assert,
		'tot_ev_error' : tot_ev_error,
		'tot_ev_warning' : tot_ev_warning,
		'tot_ev_info' : tot_ev_info,
		'tot_ev_trace' : tot_ev_trace,
		'tot_ev_alert' : tot_ev_alert
		}

	return content