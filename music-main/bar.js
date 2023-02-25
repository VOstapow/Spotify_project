function makeplot() {
    d3.csv("https://raw.githubusercontent.com/skumaridev/music/main/BarChart.csv", function(data){ processData(data) } );
  
  };
  
  function processData(allRows) {
  
    console.log(allRows);
    var x = [], y = [],z=[], standard_deviation = [];
  
    for (var i=0; i<allRows.length; i++) {
      row = allRows[i];
      // a= row['month-yy']
      // a= new Date(a).toLocaleDateString('en-us', { year:"numeric", month:"short"})
      x.push( row['month-yy'] );
      y.push( row['total_streams'] );
      // z.push(row['country'])
    }
    console.log( 'X',x, 'Y',y, 'SD',standard_deviation );
    makePlotly( x, y, standard_deviation );
  }
  
  function makePlotly( x, y, z,standard_deviation ){
    var plotDiv = document.getElementById("plot");
    var traces = [{
      x: x,
      y: y,
      // text:z,
      type:'bar'
      
      
    }];
  
    Plotly.newPlot('myDiv', traces,
      {title: 'Fiscal Year Month-Over-Month Streams In North America 2021-2022'});
  };
    makeplot();