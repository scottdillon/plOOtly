from itertools import cycle
import plotly.graph_objs as go


class MarkerTips(object):
    """
    Describe line weights
    """
    ULTRA_FINE_TIP = 1
    FINE_TIP = 3
    MEDIUM = 5
    BOLD = 8
    HEAVYWEIGHT = 10


class Colors(object):
    """
    Seaborn default colors
    """
    BLUE = 'rgba(76,  114, 176, 1.0)'
    GREEN = 'rgba(85,  168, 104, 1.0)'
    RED = 'rgba(196,  78,  82, 1.0)'
    PURPLE = 'rgba(129, 114, 178, 1.0)'
    YELLOW = 'rgba(204, 185, 116, 1.0)'
    TURQUOISE = 'rgba(100, 181, 205, 1.0)'
    BLACK = 'rgba(  0,   0,   0, 1.0)'

    def __init__(self):
        self._seaborn_colors = [self.RED, self.BLUE, self.GREEN, self.PURPLE, self.YELLOW, self.TURQUOISE]
        self._seaborn_cycle = cycle(self._seaborn_colors)

    @property
    def seaborn_cycle(self):
        return next(self._seaborn_cycle)


class LineType(object):
    """
    Line options: [solid | dashed | dot]
    """
    DASHED = 'dash'
    DOT    = 'dot'
    SOLID  = 'solid'

    def __init__(self):
        self.linetypes = [self.SOLID, self.DASHED, self.DOT]


class Mode(object):
    """
     line mode, lines, markers or lines and markers
    """
    LINES_ONLY    = 'lines'
    MARKERS_ONLY  = 'markers'
    LINES_MARKERS = 'lines+markers'

    def __init__(self):
        all_linemodes = [self.LINES_ONLY, self.LINES_MARKERS, self.MARKERS_ONLY]
        linemodes = [self.LINES_ONLY, self.LINES_MARKERS]


class LineShape(object):
    """
    Line shape determines if a trace is connected with straight lines between data points or whether those
    lines are splines or step functions, etc. Only linear and spline types are implemented here.
    """
    LINEAR = 'linear'
    SPLINE = 'spline'

    def __init__(self):
        self._line_shapes = cycle([self.LINEAR, self.SPLINE])

    @property
    def line_shapes(self):
        return next(self._line_shapes)


class ShortSymbols(object):
    """
    A short enumeration of shapes. All of the shaped can be imported from the symbols.py file.
    """
    CIRCLE       = 0
    SQUARE       = 1
    DIAMOND      = 2
    CROSS        = 3
    X            = 4
    PENTAGON     = 13
    HEXAGON      = 14
    STAR         = 17
    CROSS_CIRCLE = 27

    def __init__(self):
        self._marker_shapes = cycle([self.CIRCLE, self.SQUARE, self.DIAMOND, self.CROSS, self.X,
                              self.PENTAGON, self.HEXAGON, self.STAR, self.CROSS_CIRCLE])

    @property
    def marker_shapes(self):
        return next(self._marker_shapes)

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

    @staticmethod
    def check_markercolor(markeredgecolor, markerfacecolor, color):
        """
        If either the marker color and marker edge color is None, make it the same as the line color.
        :param markeredgecolor: the color of the outline of the markers
        :param markerfacecolor: the color of the face of the markers
        :param color: the line color of the trace
        :return:
        """
        if not markerfacecolor and color:
            markerfacecolor = color

        if not markeredgecolor and color:
            markeredgecolor = color

        if not color and markerfacecolor:
            color = markerfacecolor

        return markeredgecolor, markerfacecolor, color

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

    # @staticmethod
    # def check_marker(marker=None, msymbol=None, markersize=None, markercolor=None, lineweight=None):
    #     """
    #     If a prebuilt Marker object is already provided, then use that. If not, build one and return the Marker object
    #     :param marker:
    #     :param msymbol:
    #     :param markersize:
    #     :param markercolor:
    #     :param lineweight:
    #     :return:
    #     """
    #     if marker:
    #         return marker
    #     else:
    #         markerline = MarkerLine(width=lineweight, color=markercolor)
    #         return Marker(symbol=msymbol, size=markersize, color=markercolor, line=markerline)

    def scatter(self, *args, **kwargs):
        return self._return_scatter_obj(*args, **kwargs)

    def line(self, *args, **kwargs):
        return self._return_scatter_obj(*args, mode=Mode.LINES_MARKERS, **kwargs)

    def _return_scatter_obj(self, x=None, y=None, color=None, markerfacecolor=None, markeredgecolor=None, markeredgewidth=None,
                            mode=Mode.MARKERS_ONLY, lw=None, ls=LineType.SOLID, symbol=None, markersize=None, lineshape=None,
                            showlegend=True, connectgaps=True, name=None, opacity=1.0):
        """
        Creates and returns a plotly Scatter object with appropriate arguments placed into the Scatter object internal
        dictionary/attributes. If no markercolor or size is given the color and size of the line is used instead.

        :param x: The x axis values.
        :param y: y axis values to plot.
        :param color: line (and marker) color.
        :param markerfacecolor: marker color.
        :param markeredgecolor: the color of the marker lines. Not the facecolor of the marker.
        :param markeredgewidth: the width of the marker edge line
        :param mode: line mode 'lines' | 'lines+markers'
        :param lw: line width in pixels
        :param ls: line dash type ['solid' | 'dash' | 'dot' ]
        :param symbol: marker symbol. An Integer value starting at 0. Adding 100 only shows the outline,
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
        mec, mfc, c = self.check_markercolor(markeredgecolor, markerfacecolor, color)
        markerwidth = self.check_markersize(markeredgewidth, lw)

        markerline = MarkerLine(width=markerwidth, color=mec)
        marker = Marker(line=markerline, symbol=symbol, size=markersize, color=mfc)
        line = Line(color=c, width=lw, dash=ls, shape=lineshape)
        scatter = go.Scatter(marker=marker, line=line)

        scatter.x = x
        scatter.y = y
        scatter.mode = mode
        # scatter.marker = self.check_marker(marker, symbol, markersize, markercolor, lw)

        scatter.showlegend = showlegend
        scatter.connectgaps = connectgaps
        scatter.name = name
        scatter.opacity = opacity
        return scatter


sc = Colors()
tips = MarkerTips()
s = ShortSymbols()
shape = LineShape()
lt = LineType()
"""
Pre-defined marker dicts for assigning to the Scatter object.
"""
marker_blue      = Marker(color=sc.BLUE, line=MarkerLine(color=sc.BLUE, width=MarkerTips.FINE_TIP), size=MarkerTips.FINE_TIP, symbol=s.CIRCLE)
marker_red       = Marker(color=sc.RED, line=MarkerLine(color=sc.RED, width=MarkerTips.FINE_TIP), size=MarkerTips.FINE_TIP, symbol=s.CIRCLE)
marker_green     = Marker(color=sc.GREEN, line=MarkerLine(color=sc.GREEN, width=MarkerTips.FINE_TIP), size=MarkerTips.FINE_TIP, symbol=s.CIRCLE)
marker_purple    = Marker(color=sc.PURPLE, line=MarkerLine(color=sc.PURPLE, width=MarkerTips.FINE_TIP), size=MarkerTips.FINE_TIP, symbol=s.CIRCLE)
marker_yellow    = Marker(color=sc.YELLOW, line=MarkerLine(color=sc.YELLOW, width=MarkerTips.FINE_TIP), size=MarkerTips.FINE_TIP, symbol=s.CIRCLE)
marker_turquoise = Marker(color=sc.TURQUOISE, line=MarkerLine(color=sc.TURQUOISE, width=MarkerTips.FINE_TIP), size=MarkerTips.FINE_TIP, symbol=s.CIRCLE)


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
line_blue      = Line(color=sc.BLUE,      dash=LineType.SOLID, width=MarkerTips.MEDIUM, shape=LineShape.LINEAR)
line_red       = Line(color=sc.RED,       dash=LineType.SOLID, width=MarkerTips.MEDIUM, shape=LineShape.LINEAR)
line_green     = Line(color=sc.GREEN,     dash=LineType.SOLID, width=MarkerTips.MEDIUM, shape=LineShape.LINEAR)
line_purple    = Line(color=sc.PURPLE,    dash=LineType.SOLID, width=MarkerTips.MEDIUM, shape=LineShape.LINEAR)
line_yellow    = Line(color=sc.YELLOW,    dash=LineType.SOLID, width=MarkerTips.MEDIUM, shape=LineShape.LINEAR)
line_turquoise = Line(color=sc.TURQUOISE, dash=LineType.SOLID, width=MarkerTips.MEDIUM, shape=LineShape.LINEAR)

lines = {
    'blue'      : line_blue,
    'red'       : line_red,
    'green'     : line_green,
    'purple'    : line_purple,
    'yellow'    : line_yellow,
    'turquoise' : line_turquoise
}

# Preset scatter lines
blue_solid_scatter_line      = go.Scatter(marker=marker_blue,       line=line_blue,      mode=Mode.LINES_ONLY)
blue_dashed_scatter_line     = go.Scatter(marker=marker_blue,       line=line_blue,      mode=Mode.LINES_ONLY)
green_solid_scatter_line     = go.Scatter(marker=marker_green,      line=line_green,     mode=Mode.LINES_ONLY)
green_dashed_scatter_line    = go.Scatter(marker=marker_green,      line=line_green,     mode=Mode.LINES_ONLY)
red_solid_scatter_line       = go.Scatter(marker=marker_red,        line=line_red,       mode=Mode.LINES_ONLY)
red_dashed_scatter_line      = go.Scatter(marker=marker_red,        line=line_red,       mode=Mode.LINES_ONLY)
purple_solid_scatter_line    = go.Scatter(marker=marker_purple,     line=line_purple,    mode=Mode.LINES_ONLY)
purple_dashed_scatter_line   = go.Scatter(marker=marker_purple,     line=line_purple,    mode=Mode.LINES_ONLY)
yellow_solid_scatter_line    = go.Scatter(marker=marker_yellow,     line=line_yellow,    mode=Mode.LINES_ONLY)
yellow_dashed_scatter_line   = go.Scatter(marker=marker_yellow,     line=line_yellow,    mode=Mode.LINES_ONLY)
turquoise_solid_scatter_line = go.Scatter(marker=marker_turquoise,  line=line_turquoise, mode=Mode.LINES_ONLY)
turqiose_dashed_scatter_line = go.Scatter(marker=marker_turquoise,  line=line_turquoise, mode=Mode.LINES_ONLY)


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