from itertools import cycle
import plotly.graph_objs as go


class MarkerTips(object):
    """
    Describe line weights
    """
    ULTRA_FINE_TIP = 1
    FINE_TIP       = 3
    MEDIUM         = 5
    BOLD           = 8
    HEAVYWEIGHT    = 10


class Colors(object):
    """
    Seaborn default colors
    """
    BLUE      = 'rgba(76,  114, 176, 1.0)'
    GREEN     = 'rgba(85,  168, 104, 1.0)'
    RED       = 'rgba(196,  78,  82, 1.0)'
    PURPLE    = 'rgba(129, 114, 178, 1.0)'
    YELLOW    = 'rgba(204, 185, 116, 1.0)'
    TURQUOISE = 'rgba(100, 181, 205, 1.0)'
    BLACK     = 'rgba(  0,   0,   0, 1.0)'
    LIGHT_GRAY= 'rbga(240, 240, 240, 1.0)'

    def __init__(self):
        self._seaborn_colors = [self.RED, self.BLUE, self.GREEN, self.PURPLE, self.YELLOW, self.TURQUOISE]
        self._seaborn_cycle = cycle(self._seaborn_colors)

    @property
    def seaborn_colors(self):
        return self._seaborn_cycle

    def next_color(self):
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
    def check_markeredgewidth(markeredgewidth, lineweight):
        """
        Assume that the markeredgewidth should be the same as the lineweight if it was not passed explicitly.
        :param markeredgewidth: The size in pixels of the marker.
        :param lineweight: the thickness in pixels of the line connecting data points.
        :return:
        """
        if markeredgewidth or markeredgewidth == 0:
            return markeredgewidth
        else:
            return lineweight

    def scatter(self, *args, **kwargs):
        return self._return_scatter_obj(*args, **kwargs)

    def line(self, *args, **kwargs):
        mode = kwargs.pop('mode', Mode.LINES_MARKERS)
        return self._return_scatter_obj(*args, mode=mode, **kwargs)

    def _return_scatter_obj(self, x=None, y=None, color=None, markerfacecolor=None, markeredgecolor=None, markeredgewidth=None,
                            mode=Mode.MARKERS_ONLY, lw=None, ls=LineType.SOLID, symbol=None, markersize=None, lineshape=None,
                            showlegend=True, connectgaps=True, name=None, opacity=1.0):
        """
        Creates and returns a plotly Scatter object with appropriate arguments placed into the Scatter object internal
        dictionary/attributes. If no markercolor or size is given the color and size of the line is used instead.

        * All parameters are optional *

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
        markerwidth = self.check_markeredgewidth(markeredgewidth, lw)

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


class Axis(dict):
    """

    """
    def __init__(self, *args, **kwargs):
        super(Axis, self).__init__(*args, **kwargs)
        self.__dict__ = self


class Xaxis(Axis):
    """
    This class might not be necessary if I don't have to label everything
    X or Y in the Axis class
    """
    def __init__(self, *args, gridlines='x', **kwargs):
        super(Xaxis, self).__init__(*args, **kwargs)
        self.showgrid = None
        self._showgrid = gridlines

    @property
    def _showgrid(self):
        return self.showgrid

    @_showgrid.setter
    def _showgrid(self, gridlines):
        if 'x' in gridlines.lower():
            self.showgrid = True
        else:
            self.showgrid = False


class Yaxis(Axis):
    """
    This class might not be necessary if I don't have to label everything
    X or Y in the Axis class
    """
    def __init__(self, *args, gridlines='y', **kwargs):
        super(Yaxis, self).__init__(*args, **kwargs)
        self.showgrid = None
        self._showgrid = gridlines

    @property
    def _showgrid(self):
        return self.showgrid

    @_showgrid.setter
    def _showgrid(self, gridlines):
        if 'y' in gridlines.lower():
            self.showgrid = True
        else:
            self.showgrid = False


class LOMargin(go.Margin):
    """
    Margin object for the layout. Accepts parameters for l, b, t, r
    :param l: the left margin in pixels.
    :param r: right margin in pixels
    :param t: top margin value in pixels
    :param b: bottom margin value in pixels.
    :param pad: padding in pixels between margins and plot area
    """
    def __init__(self, *args, l=50, t=50, r=50, b=50, padding=None, ae=False, **kwargs):
        super(LOMargin, self).__init__(*args, **kwargs)
        self.t = t
        self.r = r
        self.b = b
        self.l = l
        self.pad = padding
        self.autoexpand = ae


class Annotation(dict):
    """
    Annotation object
    """
    def __init__(self, *args, **kwargs):
        super(Annotation, self).__init__(*args, **kwargs)
        self.__dict__ = self


class Legend(dict):
    """

    """
    def __init__(self, *args, **kwargs):
        super(Legend, self).__init__(*args, **kwargs)
        self.__dict__ = self


class Layout(dict):
    """
    plOOtly version of a layout object.
    """
    def __init__(self, *args, **kwargs):
        super(Layout, self).__init__(*args, **kwargs)
        self.__dict__ = self


class Data(dict):
    """

    """
    def __init__(self, *args, **kwargs):
        super(Data, self).__init__(*args, **kwargs)
        self.__dict__ = self


class Figure(dict):
    """

    """
    def __init__(self, *args, **kwargs):
        super(Figure, self).__init__(*args, **kwargs)
        self.__dict__ = self


class PlotFactory(object):
    """
    Simple factory that returns go.Figure, go.Layout and go.Data
    objects.
    """
    def __init__(self):
        self.__dict__ = self
        pass

    def __new__(self, *args, width=None, height=None, plot_color=None, paper_color=None,
                 gridlines='xy', annotations=[], showlegend=True, margin=None, **kwargs):
        xaxis = Xaxis(gridlines=gridlines)
        yaxis = Yaxis(gridlines=gridlines)

        figure = go.Figure()
        layout = go.Layout(xaxis=xaxis, yaxis=yaxis, plot_bgcolor=plot_color, annotations=annotations,
                           paper_bgcolor=paper_color, width=width, height=height, showlegend=showlegend,
                           margin=margin)
        data = go.Data()

        return figure, layout, data

# report_layout = Layout()
# report_layout['plot_bgcolor'] = 'rgba(240, 240, 240, 1.0)'
# report_layout['xaxis']['show_grid'] = False
# report_layout['yaxis']['show_grid'] = False
# report_layout['xaxis']['nticks'] = 0
# report_layout['yaxis']['nticks'] = 0
# report_layout['xaxis']['showline'] = 0
# report_layout['yaxis']['showline'] = 0


sc    = Colors()
tips  = MarkerTips()
s     = ShortSymbols()
shape = LineShape()
lt    = LineType()
"""
Pre-defined marker dicts for assigning to the Scatter object.
"""
marker_blue      = Marker(color=sc.BLUE,      line=MarkerLine(color=sc.BLUE,      width=MarkerTips.FINE_TIP), size=MarkerTips.FINE_TIP, symbol=s.CIRCLE)
marker_red       = Marker(color=sc.RED,       line=MarkerLine(color=sc.RED,       width=MarkerTips.FINE_TIP), size=MarkerTips.FINE_TIP, symbol=s.CIRCLE)
marker_green     = Marker(color=sc.GREEN,     line=MarkerLine(color=sc.GREEN,     width=MarkerTips.FINE_TIP), size=MarkerTips.FINE_TIP, symbol=s.CIRCLE)
marker_purple    = Marker(color=sc.PURPLE,    line=MarkerLine(color=sc.PURPLE,    width=MarkerTips.FINE_TIP), size=MarkerTips.FINE_TIP, symbol=s.CIRCLE)
marker_yellow    = Marker(color=sc.YELLOW,    line=MarkerLine(color=sc.YELLOW,    width=MarkerTips.FINE_TIP), size=MarkerTips.FINE_TIP, symbol=s.CIRCLE)
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
blue_solid_scatter_line       = go.Scatter(marker=marker_blue,       line=line_blue,      mode=Mode.LINES_ONLY)
blue_dashed_scatter_line      = go.Scatter(marker=marker_blue,       line=line_blue,      mode=Mode.LINES_ONLY)
green_solid_scatter_line      = go.Scatter(marker=marker_green,      line=line_green,     mode=Mode.LINES_ONLY)
green_dashed_scatter_line     = go.Scatter(marker=marker_green,      line=line_green,     mode=Mode.LINES_ONLY)
red_solid_scatter_line        = go.Scatter(marker=marker_red,        line=line_red,       mode=Mode.LINES_ONLY)
red_dashed_scatter_line       = go.Scatter(marker=marker_red,        line=line_red,       mode=Mode.LINES_ONLY)
purple_solid_scatter_line     = go.Scatter(marker=marker_purple,     line=line_purple,    mode=Mode.LINES_ONLY)
purple_dashed_scatter_line    = go.Scatter(marker=marker_purple,     line=line_purple,    mode=Mode.LINES_ONLY)
yellow_solid_scatter_line     = go.Scatter(marker=marker_yellow,     line=line_yellow,    mode=Mode.LINES_ONLY)
yellow_dashed_scatter_line    = go.Scatter(marker=marker_yellow,     line=line_yellow,    mode=Mode.LINES_ONLY)
turquoise_solid_scatter_line  = go.Scatter(marker=marker_turquoise,  line=line_turquoise, mode=Mode.LINES_ONLY)
turquoise_dashed_scatter_line = go.Scatter(marker=marker_turquoise,  line=line_turquoise, mode=Mode.LINES_ONLY)


line_cycle = {'solid': [red_solid_scatter_line,
                        blue_solid_scatter_line,
                        green_solid_scatter_line,
                        purple_solid_scatter_line,
                        yellow_solid_scatter_line,
                        turquoise_solid_scatter_line],
              'dashed': [red_dashed_scatter_line,
                         blue_dashed_scatter_line,
                         green_dashed_scatter_line,
                         purple_dashed_scatter_line,
                         yellow_dashed_scatter_line,
                         turquoise_dashed_scatter_line]
              }