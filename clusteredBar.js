$(document).ready(function() {

    var TITLE = 'Popular Track name by streams in USA/Canada, 2021-22';
  
    // `false` for vertical column chart, `true` for horizontal bar chart
    var HORIZONTAL = false;
  
      // `false` for individual bars, `true` for stacked bars
    var STACKED = false;  
    
    // Which column defines 'bucket' names?// column name
    // var LABELS = 'track_name'; (this is the original option) 
    var LABELS = 'artist_names';
  
    // For each column representing a data series, define its name and color
    var SERIES = [  
      {
        column: 'USA  Stream',
        name: 'Total Streams In USA ',
        color: 'red'
      },
      {
        column: 'Canada -Streams',
        name: 'Total Streams In Canada',
        color: 'blue'
      }
    //   {
    //     column: 'loudness',
    //     name: 'Loudness',
    //     color: 'blue'
    //   }
    ];
  
    // x-axis label and label in tooltip
    var X_AXIS = 'Track Name';
  
    // y-axis label, label in tooltip
    var Y_AXIS = 'Total Number of Streams';
  
    // `true` to show the grid, `false` to hide
    var SHOW_GRID = true; 
  
    // `true` to show the legend, `false` to hide
    var SHOW_LEGEND = true; 
  
    // Read data file with random string generated by current time
    // to bypass browser cache, and create chart
    $.get('https://raw.githubusercontent.com/trvrbrdgs/Spotify_project/main/clusterBar1.csv', {'_': $.now()}, function(csvString) {
  
      var rows = Papa.parse(csvString, {header: true}).data;
  
      var datasets = SERIES.map(function(el) {
        return {
          label: el.name,
          labelDirty: el.column,
          backgroundColor: el.color,
          data: []
        }
      });
  
      rows.map(function(row) {
        datasets.map(function(d) {
          d.data.push(row[d.labelDirty])
        })
      });
  
          var barChartData = {
        labels: rows.map(function(el) { return el[LABELS] }),
              datasets: datasets
      };
  
      var ctx = document.getElementById('container').getContext('2d');
  
      new Chart(ctx, {
        type: HORIZONTAL ? 'horizontalBar' : 'bar',
        data: barChartData,
        
        options: {
          title: {
            display: true,
            text: TITLE,
            fontSize: 14,
          },
          legend: {
            display: SHOW_LEGEND,
          },
          scales: {
            xAxes: [{
              stacked: STACKED,
              scaleLabel: {
                display: X_AXIS !== '',
                labelString: X_AXIS
              },
              gridLines: {
                display: SHOW_GRID,
              }
            //   ticks: {
            //     beginAtZero: true,
            //     callback: function(value, index, values) {
            //       return value.toLocaleString();
            //     }
            //   }
            }],
            yAxes: [{
              stacked: STACKED,
              beginAtZero: true,
              scaleLabel: {
                display: Y_AXIS !== '',
                labelString: Y_AXIS
              },
              gridLines: {
                display: SHOW_GRID,
              }
            //   ticks: {
            //     beginAtZero: true,
            //     callback: function(value, index, values) {
            //       return value.toLocaleString()
            //     }
            //   }
            }]
          }
        //   tooltips: {
        //     displayColors: false,
        //     callbacks: {
        //       label: function(tooltipItem, all) {
        //         return all.datasets[tooltipItem.datasetIndex].label
        //           + ': ' + tooltipItem.yLabel;
        //       }
        //     }
        //   }
        }
      });
  
    });
  
  });