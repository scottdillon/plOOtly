from itertools import cycle
import plotly.graph_objs as go

MRKR_PIXELS = 3

LINE_ULTRA_FINE_TIP = 1
LINE_FINE_TIP = 3
LINE_MEDIUM = 5
LINE_BOLD = 8
LINE_HEAVYWEIGHT = 10

BLUE      = 'rgba(76,  114, 176, 1.0)'
GREEN     = 'rgba(85,  168, 104, 1.0)'
RED       = 'rgba(196,  78,  82, 1.0)'
PURPLE    = 'rgba(129, 114, 178, 1.0)'
YELLOW    = 'rgba(204, 185, 116, 1.0)'
TURQUOISE = 'rgba(100, 181, 205, 1.0)'
BLACK     = 'rgba(  0,   0,   0, 1.0)'

# Seaborn default colors
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
all_linemodes = [ LINES_ONLY, LINES_MARKERS, MARKERS_ONLY]
linemodes = [LINES_ONLY, LINES_MARKERS]

# Line shapes
LINEAR = 'linear'
SPLINE = 'spline'

# Straight line segments or curved spline segments.
line_shapes = [LINEAR, SPLINE]

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

"""
A short enumeration of shapes. All of the shaped can be imported from the symbols.py file."""
marker_shapes = [CIRCLE, SQUARE, DIAMOND, CROSS, X, PENTAGON, HEXAGON, STAR, CROSS_CIRCLE]


class Marker(dict):
    """
    Takes in a dictionary object or a list of keywords and assigns them all to attributes so that go.Scatter.marker
    dict objects are accessible via attributes instead of going through

    Credit: http://stackoverflow.com/a/14620633/3255269
    """
    def __init__(self, *args, **kwargs):
        super(Marker, self).__init__(*args, **kwargs)
        self.__dict__ = self

class Line(dict):
    """
    Takes in a dictionary object or a list of keywords and assigns them all to attributes so that go.Scatter.line
    dict objects are accessible via attributes instead of going through

    Credit: http://stackoverflow.com/a/14620633/3255269
    """
    def __init__(self, *args, **kwargs):
        super(Line, self).__init__(*args, **kwargs)
        self.__dict__ = self

class MarkerLine(dict):
    """
    Takes in a dictionary object or a list of keywords and assigns them all to attributes so that go.Scatter.marker.line
    dict objects are accessible via attributes instead of going through

    Credit: http://stackoverflow.com/a/14620633/3255269
    """
    def __init__(self, *args, **kwargs):
        super(MarkerLine, self).__init__(*args, **kwargs)
        self.__dict__ = self


class ScatterFactory(dict):
    """
    Produces a plotly.graph_objs.Scatter object given the passed arguments which are put into the Scatter
    obj dictionary.
    """
    def __init__(self, *args, **kwargs):
        """
        Right now, the objects in __init__ are not used. The idea is to provide some premade custom defaults for marker
        settings or line settings and simply cycle through the colors.
        """
        super(ScatterFactory, self).__init__(*args, **kwargs)
        self.marker_options = cycle(marker_shapes)
        self.colors_options = cycle(seaborn_colors)
        self.line_type_options = cycle(linetypes)
        self.line_modes_options = cycle(linemodes)

    @staticmethod
    def check_markercolor(markerlinecolor, markerfacecolor, linecolor):
        """
        IF marker color is None, make it the same as the linecolor.
        :param markercolor:
        :return:
        """
        if markerfacecolor or markerlinecolor:
            if markerfacecolor:
                print("MArker face color {} was used".format(markerfacecolor))
                return markerfacecolor
            else:
                print("Marker line color {} was used".format(markerlinecolor))
                return markerlinecolor
        else:
            print("the linecolor {} was used".format(linecolor))
            return linecolor

    @staticmethod
    def check_markersize(markersize, lineweight):
        """
        If markersize is None, make it the same as the lineweight.
        :param markersize:
        :return:
        """
        if markersize:
            return markersize
        else:
            return lineweight

    @staticmethod
    def check_marker(marker=None, msymbol=None, markersize=None, markercolor=None, lineweight=None):
        """
        If a prebuilt Marker object is already provided, then use that. If not, build one and return the Marker object
        :param marker:
        :param msymbol:
        :param markersize:
        :param markercolor:
        :param lineweight:
        :return:
        """
        if marker:
            return marker
        else:
            markerline = MarkerLine(width=lineweight, color=markercolor)
            return Marker(symbol=msymbol, size=markersize, color=markercolor, line=markerline)

    def scatter(self, *args, **kwargs):
        return self._return_scatter_obj(*args, **kwargs)

    def line(self, *args, **kwargs):
        return self._return_scatter_obj(*args, mode=LINES_MARKERS, **kwargs)

    def _return_scatter_obj(self, x=None, y=None, linecolor=None, markerfacecolor=None, markerlinecolor=None, mode=MARKERS_ONLY, lineweight=None,
                dash=None, msymbol=None, markersize=None, lineshape=None, showlegend=True, connectgaps=True,
                name=None, opacity=1.0):
        """
        Creates and returns a plotly Scatter object with appropriate arguments placed into the Scatter object internal
        dictionary/attributes. If no markercolor or size is given the color and size of the line is used instead.

        :param x: The x asix values.
        :param y: y axis values to plot.
        :param linecolor: line (and marker) color.
        :param markerfacecolor: marker color.
        :param markerlinecolor: the color of the marker lines. Not the facecolor of the marker.
        :param mode: line mode 'lines' | 'lines+markers'
        :param lineweight: line width in pixels
        :param dash: line dash type ['solid' | 'dash' | 'dot' ]
        :param msymbol: marker symbol. An Integer value starting at 0. Adding 100 only shows the outline,
            adding 200
        :param markersize: marker size in pixels
        :param lineshape: line shape. Should the line be a straight line between data points or a spline. There
            are other step functions too. See repo cheatsheet for more info.
        :param showlegend: Boolean indicating whether to add the series to the legend. Does not hide the entire legend.
        :param connectgaps: Boolean to connect the gaps between missing data or not.
        :param name: What you want the series name to be in the legend and hover text.
        :param opacity: alpha value of the trace.
        :return: Returns a newly instantiated plotly.graph_objs.Scatter object with appropriate dictionary/attribute
            entries.
        """
        markercolor = self.check_markercolor(markerlinecolor, markerfacecolor, linecolor)
        markersize = self.check_markersize(markersize, lineweight)

        markerline = MarkerLine(width=lineweight, color=markerlinecolor)
        marker = Marker(line=markerline, symbol=msymbol, size=markersize, color=markerfacecolor)
        line = Line(color=linecolor, width=lineweight, dash=dash, shape=lineshape)
        scatter = go.Scatter(marker=marker, line=line)

        scatter.x = x
        scatter.y = y
        scatter.mode = mode
        scatter.marker = self.check_marker(marker, msymbol, markersize, markercolor, lineweight)

        scatter.showlegend = showlegend
        scatter.connectgaps = connectgaps
        scatter.name=name
        scatter.opacity = opacity
        return scatter



"""
Pre-defined marker dicts for assigning to the Scatter object.
"""
marker_blue      = Marker(color=BLUE,      line=MarkerLine(color=BLUE,      width=MRKR_PIXELS), size=MRKR_PIXELS, symbol=CIRCLE)
marker_red       = Marker(color=RED,       line=MarkerLine(color=RED,       width=MRKR_PIXELS), size=MRKR_PIXELS, symbol=CIRCLE)
marker_green     = Marker(color=GREEN,     line=MarkerLine(color=GREEN,     width=MRKR_PIXELS), size=MRKR_PIXELS, symbol=CIRCLE)
marker_purple    = Marker(color=PURPLE,    line=MarkerLine(color=PURPLE,    width=MRKR_PIXELS), size=MRKR_PIXELS, symbol=CIRCLE)
marker_yellow    = Marker(color=YELLOW,    line=MarkerLine(color=YELLOW,    width=MRKR_PIXELS), size=MRKR_PIXELS, symbol=CIRCLE)
marker_turquoise = Marker(color=TURQUOISE, line=MarkerLine(color=TURQUOISE, width=MRKR_PIXELS), size=MRKR_PIXELS, symbol=CIRCLE)


markers = {
    'blue'      : marker_blue,
    'red'       : marker_red,
    'green'     : marker_green,
    'purple'    : marker_purple,
    'yellow'    : marker_yellow,
    'turquoise' : marker_turquoise
    }

"""
Line dictionaries for Scatter objects. These can be used directly for the line attribute of the Scatter object and 
thereby skipping the dictionary definition.
"""
line_blue      = Line(color=BLUE,      dash=SOLID, width=LINE_MEDIUM, shape=LINEAR)
line_red       = Line(color=RED,       dash=SOLID, width=LINE_MEDIUM, shape=LINEAR)
line_green     = Line(color=GREEN,     dash=SOLID, width=LINE_MEDIUM, shape=LINEAR)
line_purple    = Line(color=PURPLE,    dash=SOLID, width=LINE_MEDIUM, shape=LINEAR)
line_yellow    = Line(color=YELLOW,    dash=SOLID, width=LINE_MEDIUM, shape=LINEAR)
line_turquoise = Line(color=TURQUOISE, dash=SOLID, width=LINE_MEDIUM, shape=LINEAR)

lines = {
    'blue'      : line_blue,
    'red'       : line_red,
    'green'     : line_green,
    'purple'    : line_purple,
    'yellow'    : line_yellow,
    'turquoise' : line_turquoise
}

# Preset scatter lines
blue_solid_scatter_line      = go.Scatter(marker=marker_blue,       line=line_blue,      mode=LINES_ONLY)
blue_dashed_scatter_line     = go.Scatter(marker=marker_blue,       line=line_blue,      mode=LINES_ONLY)
green_solid_scatter_line     = go.Scatter(marker=marker_green,      line=line_green,     mode=LINES_ONLY)
green_dashed_scatter_line    = go.Scatter(marker=marker_green,      line=line_green,     mode=LINES_ONLY)
red_solid_scatter_line       = go.Scatter(marker=marker_red,        line=line_red,       mode=LINES_ONLY)
red_dashed_scatter_line      = go.Scatter(marker=marker_red,        line=line_red,       mode=LINES_ONLY)
purple_solid_scatter_line    = go.Scatter(marker=marker_purple,     line=line_purple,    mode=LINES_ONLY)
purple_dashed_scatter_line   = go.Scatter(marker=marker_purple,     line=line_purple,    mode=LINES_ONLY)
yellow_solid_scatter_line    = go.Scatter(marker=marker_yellow,     line=line_yellow,    mode=LINES_ONLY)
yellow_dashed_scatter_line   = go.Scatter(marker=marker_yellow,     line=line_yellow,    mode=LINES_ONLY)
turquoise_solid_scatter_line = go.Scatter(marker=marker_turquoise,  line=line_turquoise, mode=LINES_ONLY)
turqiose_dashed_scatter_line = go.Scatter(marker=marker_turquoise,  line=line_turquoise, mode=LINES_ONLY)


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