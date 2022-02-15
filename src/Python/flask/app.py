from flask import Flask, jsonify, request, make_response
from definitions.passenger import Passenger
import json
import iris

app = Flask(__name__)

# ----------------------------------------------------------------
### CRUD FOR TITANIC_TABLE.PASSENGER
# ----------------------------------------------------------------
@app.route("/")
def asdfhellsdfsdfo_world():
    return "<p>BismiALLAH! Test</p>"
# GET all passengers
@app.route("/api/passengers", methods=["GET"])
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


# ----------------------------------------------------------------
### MAIN PROGRAM
# ----------------------------------------------------------------

if __name__ == '__main__':
    app.run('0.0.0.0', port = "8080")