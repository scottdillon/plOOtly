import plotly
import plotly.graph_objs as go
import plotly_config.plotly_lines_colors as plc
import plotly_config.symbols as symbols

sf = plc.ScatterFactory()

markerline = plc.MarkerLine(color=plc.TURQUOISE, width=plc.MRKR_PIXELS)
print("1:{}".format(markerline))
marker = plc.Marker(symbol=symbols.circle, size=20, line=markerline, color=plc.BLUE)
print("2:{}".format(markerline))
line = plc.Line(color=plc.RED, width=plc.LINE_MEDIUM)
print("3:{}".format(markerline))

trace0 = sf.scatter(markerfacecolor=plc.TURQUOISE, markerwidth=plc.MRKR_PIXELS, symbol=symbols.circle, markersize=plc.LINE_MEDIUM,
                    )
# print("4:{}".format(trace0))
trace0.line = line
trace0.marker.line = markerline

trace0.x=[1, 2, 3, 4]
trace0.y=[10, 15, 13, 17]

data = go.Data([trace0])

plotly.offline.plot(figure_or_data=data, filename = 'output_files/basic-line.html',
                    include_plotlyjs=True, show_link=False)
