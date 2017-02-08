from itertools import cycle
import plotly.graph_objs as go

BLUE      = 'rgba(76,  114, 176, 1.0)'
GREEN     = 'rgba(85,  168, 104, 1.0)'
RED       = 'rgba(196,  78,  82, 1.0)'
PURPLE    = 'rgba(129, 114, 178, 1.0)'
YELLOW    = 'rgba(204, 185, 116, 1.0)'
TURQUOISE = 'rgba(100, 181, 205, 1.0)'
BLACK     = 'rgba(  0,   0,   0, 1.0)'

# Seaborn colors
seaborn_colors = [RED, BLUE, GREEN, PURPLE, YELLOW, TURQUOISE]

DASHED = 'dash'
DOT    = 'dot'
SOLID  = 'solid'
# Line dash options
linetypes = [ SOLID, DASHED, DOT]

LINES_ONLY    = 'lines'
MARKERS_ONLY  = 'markers'
LINES_MARKERS = 'lines+markers'

# line mode, lines, markers or lines and markers
linemode = [ LINES_ONLY, LINES_MARKERS]

# Line shapes
LINEAR = 'linear'
SPLINE = 'spline'

# Straight line segments or curved spline segments.
line_shape = [ LINEAR, SPLINE ]

# Marker Symbols
CIRCLE       = 0
SQUARE       = 1
DIAMOND      = 2
CROSS        = 3
X            = 4
PENTAGON     = 13
HEXAGON      = 14
STAR         = 17
CROSS_CIRCLE = 27

# A short enumeration of marker shapes
marker_shape = [CIRCLE, SQUARE, DIAMOND, CROSS, X, PENTAGON, HEXAGON, STAR, CROSS_CIRCLE]

marker_blue = dict(color=BLUE,      line=dict(color=BLUE,      width=6), size=6, symbol=CIRCLE)
marker_red  = dict(color=RED,       line=dict(color=RED,       width=6), size=6, symbol=CIRCLE)
marker_green = dict(color=GREEN,     line=dict(color=GREEN,     width=6), size=6, symbol=CIRCLE)
marker_purple = dict(color=PURPLE,    line=dict(color=PURPLE,    width=6), size=6, symbol=CIRCLE)
marker_yellow = dict(color=YELLOW,    line=dict(color=YELLOW,    width=6), size=6, symbol=CIRCLE)
marker_turquoise = dict(color=TURQUOISE, line=dict(color=TURQUOISE, width=6), size=6, symbol=CIRCLE)


markers = {
    'blue': marker_blue,
    'red' : marker_red,
    'green' : marker_green,
    'purple': marker_purple,
    'yellow' : marker_yellow,
    'turquoise' : marker_turquoise
    }

line_blue = dict(color=BLUE, dash=SOLID, width=2, shape=LINEAR)
line_red = dict(color=RED, dash=SOLID, width=2, shape=LINEAR)
line_green = dict(color=GREEN, dash=SOLID, width=2, shape=LINEAR)
line_purple = dict(color=PURPLE, dash=SOLID, width=2, shape=LINEAR)
line_yellow = dict(color=YELLOW, dash=SOLID, width=2, shape=LINEAR)
line_turquoise = dict(color=TURQUOISE, dash=SOLID, width=2, shape=LINEAR)

lines = {
    'blue': line_blue,
    'red': line_red,
    'green': line_green,
    'purple': line_purple,
    'yellow': line_yellow,
    'turquoise': line_turquoise
}

blue_solid_scatter_line      = go.Scatter(marker=marker_blue, line=line_blue, mode=LINES_ONLY)
blue_dashed_scatter_line     = go.Scatter(marker=marker_blue, line=line_blue, mode=LINES_ONLY)
green_solid_scatter_line     = go.Scatter(marker=marker_green, line=line_green, mode=LINES_ONLY)
green_dashed_scatter_line    = go.Scatter(marker=marker_green, line=line_green, mode=LINES_ONLY)
red_solid_scatter_line       = go.Scatter(marker=marker_red, line=line_red, mode=LINES_ONLY)
red_dashed_scatter_line      = go.Scatter(marker=marker_red, line=line_red, mode=LINES_ONLY)
purple_solid_scatter_line    = go.Scatter(marker=marker_purple, line=line_purple, mode=LINES_ONLY)
purple_dashed_scatter_line   = go.Scatter(marker=marker_purple, line=line_purple, mode=LINES_ONLY)
yellow_solid_scatter_line    = go.Scatter(marker=marker_yellow, line=line_yellow, mode=LINES_ONLY)
yellow_dashed_scatter_line   = go.Scatter(marker=marker_yellow, line=line_yellow, mode=LINES_ONLY)
turquoise_solid_scatter_line = go.Scatter(marker=marker_turquoise, line=line_turquoise, mode=LINES_ONLY)
turqiose_dashed_scatter_line = go.Scatter(marker=marker_turquoise, line=line_turquoise, mode=LINES_ONLY)

class ScatterFactory(object):
    def __init__(self):
        self.markers = cycle(marker_shape)
        self.colors = cycle(seaborn_colors)
        self.line_types = cycle(linetypes)
        self.line_modes = cycle(linemode)

    def __new__(self, x=None, y=None, linecolor=None, markercolor=None, mode=None, lineweight=None,
                dash=None, msymbol=None, markersize=None, lineshape=None, showlegend=True):
        """
        :param x: The x asix values.
        :param y: y axis values to plot.
        :param linecolor: line and marker color.
        :param markercolor: marker color.
        :param mode: line mode 'lines' | 'lines+markers'
        :param lineweight: line width in pixels
        :param dash: line dash type ['solid' | 'dash' | 'dot' ]
        :param msymbol: marker symbol. An Integer value starting at 0. Adding 100 only shows the outline,
            adding 200
        :param markersize: marker size in pixels
        :param lineshape: line shape. Should the line be a straight line between data points or a spline. There
            are other step functions too. See repo cheatsheet for more info.
        :return: Returns a newly instantiated plotly.graph_objs.Scatter object with appropriate dictionary/attribute
            entries.
        """

        if not markersize:
            markersize = lineweight
        if not markercolor:
            markercolor = linecolor

        scatter = go.Scatter()
        scatter.line['color'] = linecolor
        scatter.line['width'] = lineweight
        scatter.line['dash'] = dash
        scatter.line['shape'] = lineshape
        scatter.mode = mode
        scatter.marker['symbol'] = msymbol
        scatter.marker['size'] = markersize
        scatter.marker['color'] = markercolor
        scatter.marker['line']['color'] = markercolor
        scatter.marker['line']['width'] = lineweight
        scatter.showlegend = showlegend
        return scatter


line_cycle = {'solid':[red_solid_scatter_line,
                       blue_solid_scatter_line,
                       green_solid_scatter_line,
                       purple_solid_scatter_line,
                       yellow_solid_scatter_line,
                       turquoise_solid_scatter_line],
              'dashed':[red_dashed_scatter_line,
                        blue_dashed_scatter_line,
                        green_dashed_scatter_line,
                        purple_dashed_scatter_line,
                        yellow_dashed_scatter_line,
                        turqiose_dashed_scatter_line]
              }