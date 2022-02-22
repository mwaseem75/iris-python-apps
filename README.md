## Summary
IRIS Dashboard build by using embedded python with the help of [**Python Flask Web Framework**](https://flask.palletsprojects.com/). 
Application also demonostrates some of the Python funtionality like Data Science, Data Plotting, Data Visualizaion and QR Code generation. 

## Application Layout
#### Dashboard
![image](https://user-images.githubusercontent.com/18219467/155088357-86a81518-fe6d-4bfc-87d8-c957e32fb6a1.png)
#### Tables Data
![image](https://user-images.githubusercontent.com/18219467/155088531-ccf33a2d-f7e5-4d2e-b2be-089595a101d5.png)
#### Plotting with Python matplotlib library
![image](https://user-images.githubusercontent.com/18219467/155135340-93a791cc-e193-47de-bbf5-645c9968bc7a.png)

## Features
* Resposive bootstrap IRIS Dasboard.
* View dashboard details along with interoperability events log and messages.
* Python plotting from IRIS
* Use of [**Jupyter Notebook**](https://jupyter.org/)
* Introduction to Data Science, Data Plotting and Data Visulization.
* QR Code generator from python.

## Recommendation 
 * Read related documentations [Embedded Python Overview](https://docs.intersystems.com/iris20212/csp/docbook/DocBook.UI.Page.cls?KEY=AFL_epython).

## Installation
1. Clone/git pull the repo into any local directory

```
git clone https://github.com/mwaseem75/iris-python-apps.git
```

2. Open a Docker terminal in this directory and run:

```
docker-compose build
```

3. Run the IRIS container:

```
docker-compose up -d 
```

To run the application Navigate to http://localhost:4040 

## Credits
This application is derived from the below iris-python-examples template by @Guillaume Rongier 
https://openexchange.intersystems.com/package/iris-python-examples

