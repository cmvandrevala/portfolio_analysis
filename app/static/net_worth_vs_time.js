var ctx = document.getElementById("net-worth-vs-time");

$.get( "/net_worth?start=2018-01-01&end=2018-02-02", function( data ) {
  new tauCharts.Chart({
      data: data,
      type: 'line',
      x: 'date',
      y: 'value',
      color: 'net-worth'
  }).renderTo(ctx);;
});
