var urlParams = new URLSearchParams(window.location.search);

function todays_date() {
  var today = new Date();
  var dd = today.getDate();
  var mm = today.getMonth() + 1;
  var yyyy = today.getFullYear();
  if (dd < 10) dd = '0' + dd
  if (mm < 10) mm = '0' + mm
  return yyyy + "-" + mm + "-" + dd;
}

var start = urlParams.get('start') || "2018-01-01"
var end = urlParams.get('end') || todays_date()

var margin = {top: 30, right: 30, bottom: 100, left: 100};
var width = 1000 - margin.left - margin.right;
var height = 500 - margin.top - margin.bottom;

var parseTime = d3.timeParse("%Y-%m-%d");

var x = d3.scaleTime().range([0, width]);
var y = d3.scaleLinear().range([height, 0]);

var line = d3.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.value); });

var svg = d3.select(".container")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

d3.json("/net_worth?start=" + start + "&end=" + end, function(error, data) {
  if (error) throw error;

  data.forEach(function(d) {
      d.date = parseTime(d.date);
      d.value = +d.value;
  });

  x.domain(d3.extent(data, function(d) { return d.date; }));
  y.domain([0, d3.max(data, function(d) { return d.value; })]);

  svg.append("path")
      .data([data])
      .attr("class", "line")
      .attr("d", line);

  svg.append("g")
      .attr("class", "axis")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x)
      .tickFormat(d3.timeFormat("%Y-%m-%d")))
      .selectAll("text")
      .style("text-anchor", "end")
      .attr("dx", "-.8em")
      .attr("dy", ".15em")
      .attr("transform", "rotate(-65)");

  svg.append("g")
      .attr("class", "axis")
      .call(d3.axisLeft(y));
});
