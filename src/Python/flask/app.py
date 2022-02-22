from flask import Flask, jsonify, request, make_response, render_template
from definitions.passenger import Passenger
import json,util
import iris

app = Flask(__name__) 
app.secret_key = "abc222"

# ----------------------------------------------------------------
### CRUD FOR TITANIC_TABLE.PASSENGER
# ----------------------------------------------------------------
@app.route("/")
def index():
    
    content = util.get_dashboard_stats()
    return render_template('index.html', content = content)

@app.route("/notebook")
def notebook():
    return render_template('notebook.html')    
    
@app.route("/processes")
def processes():
    iris.cls("Embedded.Utils").SetNameSpace("USER")
    statement = iris.sql.exec(util.get_sql_stat("processes")) 
    df = statement.dataframe()
    my_data=json.loads(df.to_json(orient="split"))["data"]
    my_cols=[{"title": str(col)} for col in json.loads(df.to_json(orient="split"))["columns"]]   
    ftitle = "Processes"
    fheading = "Currently runnung processes"
    content = util.get_sidebar_stats()
    return render_template('tablesdata.html',  ftitle = ftitle, fheading = fheading, my_data = my_data, my_cols = my_cols, content = content)    

@app.route("/messages")
def messages():
    iris.cls("Embedded.Utils").SetNameSpace("USER")
    statement = iris.sql.exec(util.get_sql_stat("messages")) 
    df = statement.dataframe()
    my_data=json.loads(df.to_json(orient="split"))["data"]
    my_cols=[{"title": str(col)} for col in json.loads(df.to_json(orient="split"))["columns"]]
    ftitle = "Messages"
    fheading = "Production Messages"
    content = util.get_sidebar_stats()
    return render_template('tablesdata.html',  ftitle = ftitle, fheading = fheading, my_data = my_data, my_cols = my_cols, content = content)        
   
@app.route("/securityusers")
def securityusers():
    iris.cls("Embedded.Utils").SetNameSpace("%SYS")
    statement = iris.sql.exec(util.get_sql_stat("securityusers")) 
    df = statement.dataframe()
    my_data=json.loads(df.to_json(orient="split"))["data"]
    my_cols=[{"title": str(col)} for col in json.loads(df.to_json(orient="split"))["columns"]]
    ftitle = "Users"
    fheading = "Security Users"
    content = util.get_sidebar_stats()
    return render_template('tablesdata.html',  ftitle = ftitle, fheading = fheading, my_data = my_data, my_cols = my_cols, content = content)        

@app.route("/securityapps")
def securityapps():
    iris.cls("Embedded.Utils").SetNameSpace("%SYS")
    statement = iris.sql.exec(util.get_sql_stat("securityapps")) 
    df = statement.dataframe()
    my_data=json.loads(df.to_json(orient="split"))["data"]
    my_cols=[{"title": str(col)} for col in json.loads(df.to_json(orient="split"))["columns"]]
    ftitle = "Applications"
    fheading = "Created Applications"
    content = util.get_sidebar_stats()
    return render_template('tablesdata.html',  ftitle = ftitle, fheading = fheading, my_data = my_data, my_cols = my_cols, content = content)        

@app.route("/elassert")
def elassert():
    iris.cls("Embedded.Utils").SetNameSpace("USER")
    statement = iris.sql.exec(util.get_sql_stat("elassert"))  
    df = statement.dataframe()
    my_data=json.loads(df.to_json(orient="split"))["data"]
    my_cols=[{"title": str(col)} for col in json.loads(df.to_json(orient="split"))["columns"]]
    ftitle = "Assert"
    fheading = "Event Log Assert"
    content = util.get_sidebar_stats()
    return render_template('tablesdata.html',  ftitle = ftitle, fheading = fheading, my_data = my_data, my_cols = my_cols, content = content)        

@app.route("/elerror")
def elerror():
    iris.cls("Embedded.Utils").SetNameSpace("USER")
    statement = iris.sql.exec(util.get_sql_stat("elerror"))  
    df = statement.dataframe()
    my_data=json.loads(df.to_json(orient="split"))["data"]
    my_cols=[{"title": str(col)} for col in json.loads(df.to_json(orient="split"))["columns"]]
    ftitle = "Error"
    fheading = "Event Log Error"
    content = util.get_sidebar_stats()
    return render_template('tablesdata.html',  ftitle = ftitle, fheading = fheading, my_data = my_data, my_cols = my_cols, content = content)        

@app.route("/elwarning")
def elwarning():
    statement = iris.sql.exec(util.get_sql_stat("elwarning")) 
    df = statement.dataframe()
    my_data=json.loads(df.to_json(orient="split"))["data"]
    my_cols=[{"title": str(col)} for col in json.loads(df.to_json(orient="split"))["columns"]]
    ftitle = "Warning"
    fheading = "Event Log Warning"
    content = util.get_sidebar_stats()
    return render_template('tablesdata.html',  ftitle = ftitle, fheading = fheading, my_data = my_data, my_cols = my_cols, content = content)        
    
@app.route("/elinfo")
def elinfo():
    statement = iris.sql.exec(util.get_sql_stat("elinfo")) 
    df = statement.dataframe()
    my_data=json.loads(df.to_json(orient="split"))["data"]
    my_cols=[{"title": str(col)} for col in json.loads(df.to_json(orient="split"))["columns"]]
    ftitle = "Info"
    fheading = "Event Log Info"
    content = util.get_sidebar_stats()
    return render_template('tablesdata.html',  ftitle = ftitle, fheading = fheading, my_data = my_data, my_cols = my_cols, content = content)       

@app.route("/eltrace")
def eltrace():
    statement = iris.sql.exec(util.get_sql_stat("eltrace")) 
    df = statement.dataframe()
    my_data=json.loads(df.to_json(orient="split"))["data"]
    my_cols=[{"title": str(col)} for col in json.loads(df.to_json(orient="split"))["columns"]]
    ftitle = "Trace"
    fheading = "Event Log Trace"
    content = util.get_sidebar_stats()
    return render_template('tablesdata.html',  ftitle = ftitle, fheading = fheading, my_data = my_data, my_cols = my_cols, content = content)        

@app.route("/elevent")
def elevent():
    statement = iris.sql.exec(util.get_sql_stat("elalert")) 
    df = statement.dataframe()
    my_data=json.loads(df.to_json(orient="split"))["data"]
    my_cols=[{"title": str(col)} for col in json.loads(df.to_json(orient="split"))["columns"]]
    ftitle = "Alert"
    fheading = "Event Log Alert"
    content = util.get_sidebar_stats()
    return render_template('tablesdata.html',  ftitle = ftitle, fheading = fheading, my_data = my_data, my_cols = my_cols, content = content)        


# GET all passengers
@app.route("/api/passengers")
def getAllPassengers():
    payload = {}
    payload['passengers'] = []
    tp = {}
    name = request.args.get('name')
    currPage = request.args.get('currPage')
    pageSize = request.args.get('pageSize')
    if name is not None:
        # If search by name 
        query = "SELECT ID FROM Titanic_Table.Passenger WHERE name %STARTSWITH ?"
        rs = iris.sql.exec(query, name)
        for i in rs:
            # We create an iris object
            tp = iris.ref(1)
            # We get the json in a string
            iris.cls("Titanic.Table.Passenger")._OpenId(i[0])._JSONExportToString(tp)
            # We normalize the string to get it in python
            tp = iris.cls("%String").Normalize(tp)
            # We load the string in a dict
            tp = json.loads(tp)
            # We add the id
            tp['passengerId'] = i[0]
            payload['passengers'].append(tp)
    else:
        currPage = int(currPage) if currPage is not None else 1
        pageSize = int(pageSize) if pageSize is not None else 10
        tFrom = ((currPage -1 ) * pageSize)+1
        tTo = tFrom + (pageSize-1)
        query = """
                SELECT * FROM 
                    (
                        SELECT ID,
                            ROW_NUMBER() OVER (ORDER By ID ASC) rn
                        FROM Titanic_Table.Passenger
                    ) tmp
                WHERE rn between {} and {}
                ORDER By ID ASC
                """.format(tFrom,tTo)
        rs = iris.sql.exec(query)
        for i in rs:
            # We create an iris object
            tp = iris.ref(1)
            # We get the json in a string
            iris.cls("Titanic.Table.Passenger")._OpenId(i[0])._JSONExportToString(tp)
            # We normalize the string to get it in python
            tp = iris.cls("%String").Normalize(tp)
            # We load the string in a dict
            tp = json.loads(tp)
            # We add the id
            tp['passengerId'] = i[0]
            payload['passengers'].append(tp)
    # Getting the total number of passengers
    rs = iris.sql.exec("SELECT COUNT(*) FROM Titanic_Table.Passenger")
    payload['total'] = rs.__next__()[0]
    payload['query'] = query
    return jsonify(payload)

# POST a new passenger
@app.route("/api/passengers", methods=["POST"])
def createPassenger():
    # Retreiving the data in request body
    passenger = request.get_json()
    query = "INSERT INTO Titanic_Table.Passenger (survived, pclass, name, sex, age, sibSp, parCh, ticket, fare, cabin, embarked) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    # Getting the new ID of the passenger
    newId = int(iris.sql.exec("SELECT MAX(ID) FROM Titanic_Table.Passenger").__next__()[0]) + 1
    try:
        iris.sql.exec(query, passenger['survived'], passenger['pclass'], passenger['name'], passenger['sex'], passenger['age'], passenger['sibSp'], passenger['parCh'], passenger['ticket'], passenger['fare'], passenger['cabin'], passenger['embarked'])
    except:
        return make_response(
            'Bad Request',
            400
        )
    payload = {
        'query': query,
        'passengerId': newId
    }
    return jsonify(payload)

# GET passenger with id
@app.route("/api/passengers/<int:id>", methods=["GET"])
def getPassenger(id):
    payload = {}
    query = "SELECT * FROM Titanic_Table.Passenger WHERE ID = ?"
    rs = iris.sql.exec(query, str(id))
    try :
        passenger = Passenger(rs.__next__()).__dict__
    except:        
        return make_response(
            'Not Found',
            204
        )
    payload['passenger'] = passenger
    payload['query'] = query
    return jsonify(payload)

# PUT to update passenger with id
@app.route("/api/passengers/<int:id>", methods=["PUT"])
def updatePassenger(id):
    # First, checking to see if the passenger exists
    query = "SELECT ID FROM Titanic_Table.Passenger WHERE ID = ?"
    rs = iris.sql.exec(query, str(id))
    try :
        rs.__next__()
    except:        
        return make_response(
            'Not Found',
            204
        )
    # Updating
    passenger = request.get_json()
    query = "UPDATE Titanic_Table.Passenger SET survived = ?, pclass = ?, name = ?, sex = ?, age = ?, sibSp = ?, parCh = ?, ticket = ?, fare = ?, cabin = ?, embarked = ? WHERE ID = ?"
    try:
        iris.sql.exec(query, passenger['survived'], passenger['pclass'], passenger['name'], passenger['sex'], passenger['age'], passenger['sibSp'], passenger['parCh'], passenger['ticket'], passenger['fare'], passenger['cabin'], passenger['embarked'], id)
    except:
        return make_response(
            'Bad Request',
            400
        )
    payload = {
        'query': query,
    }
    return jsonify(payload)

# DELETE passenger with id
@app.route("/api/passengers/<int:id>", methods=["DELETE"])
def deletePassenger(id):
    payload = {}  
    query = "DELETE FROM Titanic_Table.Passenger WHERE ID = ?"
    try:
        iris.sql.exec(query, str(id))
    except:
        return make_response(
            'Not Found',
            204
        )
    payload['query'] = query
    return jsonify(payload)



def getP():
    payload = {}
    payload['passengers'] = []
    tp = {}
    name = request.args.get('name')
    currPage = request.args.get('currPage')
    pageSize = request.args.get('pageSize')
    currPage = int(currPage) if currPage is not None else 1
    pageSize = int(pageSize) if pageSize is not None else 10
    tFrom = ((currPage -1 ) * pageSize)+1
    tTo = tFrom + (pageSize-1)
    query = """
            SELECT * FROM 
                (
                    SELECT ID,
                        ROW_NUMBER() OVER (ORDER By ID ASC) rn
                    FROM Titanic_Table.Passenger
                ) tmp
            WHERE rn between {} and {}
            ORDER By ID ASC
            """.format(tFrom,tTo)
    rs = iris.sql.exec(query)
    for i in rs:
        # We create an iris object
        tp = iris.ref(1)
        # We get the json in a string
        iris.cls("Titanic.Table.Passenger")._OpenId(i[0])._JSONExportToString(tp)
        # We normalize the string to get it in python
        tp = iris.cls("%String").Normalize(tp)
        # We load the string in a dict
        tp = json.loads(tp)
        # We add the id
        tp['passengerId'] = i[0]
        payload['passengers'].append(tp)
    # Getting the total number of passengers
    rs = iris.sql.exec("SELECT COUNT(*) FROM Titanic_Table.Passenger")
    payload['total'] = rs.__next__()[0]
    payload['query'] = query
    return jsonify(payload)



# ----------------------------------------------------------------
### MAIN PROGRAM
# ----------------------------------------------------------------

if __name__ == '__main__':
    app.run('0.0.0.0', port = "8080", debug=True)
