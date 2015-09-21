function renderGraph() {
    var w = 600;                        //width
    var h = 500;                        //height
    var padding = {top: 40, right: 40, bottom: 40, left: 40};
    var dataset;
    //Set up stack method
    var stack = d3.layout.stack();

    var svg = d3.select("#cool-graph").append("svg:svg") //SELECT BY ID
        .attr("width", w)
        .attr("height", h)
        .append("svg:g")
        .attr("transform", "translate(" + p[3] + "," + (h - p[2]) + ")");

    d3.json('stats_app/summary', function (json) {
        dataset = json;

        //Data, stacked
        stack(dataset);

    });

}

renderGraph();