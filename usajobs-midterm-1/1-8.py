import requests, json

BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"

# State codes file
state_codes = json.loads(requests.get('http://stash.compjour.org/data/usajobs/us-statecodes.json').text)

state_names = ['California','Florida','New York','Maryland']
state_results = [['State', 'Job Count']]

for state in state_names:
    atts = {"CountrySubdivision": state, 'NumberOfJobs': 1}
    resp = requests.get(BASE_USAJOBS_URL, params = atts)
    data = resp.json()['TotalJobs']
    code = "US-" + state_codes[state]
    state_results.append([code, int(data)])

# Code for generating the map
chartcode = """
<html>
  <head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
  </head>
  <body>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["geochart"]});
      google.setOnLoadCallback(drawRegionsMap);

      function drawRegionsMap() {

        var data = %s
        var datatable = google.visualization.arrayToDataTable(data);
        var options = {'region': 'US', 'width': 600, 'height': 400, 'resolution': 'provinces'};

        var chart = new google.visualization.GeoChart(document.getElementById('mychart'));

        chart.draw(datatable, options);
      }
    </script>


      <div class="container">
        <h1 style="text-align:center">Hello chart</h1>
        <div id="mychart"></div>
      </div>
  </body>
</html>
"""

htmlfile = open("1-8.html", "w")
htmlfile.write(chartcode % state_results)
htmlfile.close()