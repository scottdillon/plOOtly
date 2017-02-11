# Plotly_Lines_and_Colors

### Synopsis
This is a collection of helper constants, plotly.graph_obj classes and other
objects to help keep my code cleaner. Creation of scatter objects can be simplified
down to class instantiation arguments rather than creating creating complex dictionary
structures. See below for a code simplification example.

There is also included a cheatsheet for plotly.graph_objs containing an almost
full list of commonly (for me) used Scatter object attributes. I'll work
on also adding the Bar class attributes soon and if requested, I'd add more
common graph_objs.

### Motivation
I found the plotly reference docs hard to follow and keep track of what attribute
fell under what key heading like [line], [marker], [marker][line].
Instantiating plotly Scatter and Bar objects with all of the corresponding
attributes, dictionaries, colors and string objects clutters up my code.
Instead, I can instantiate from these pre-set objects to quickly and cleanly
create new Scatter objects and just assign data attributes.

### Installation
Clone the repo into a location on your path.

### Code Example
If a new ScatterFactory object is instantiated with no arguments, you'll
get a plotly.graph_objs.Scatter object with the defaults. Ex:

    import plotly.graph_objs as go
    data = []
    scat_fact = plc.ScatterFactory
    trace = scat_fact()
    trace.x = [1,2,3]
    trace.y = [1,2,3]
    data.append(trace)
    plotly.offline.iplot(data)
That example is simple and doesn't justify using this library but imagine
creating a more complex with different line styles, colors and widths and
different values for the marker style and marker line styles. How about
adding different modes and dash options?

This is a code example before I wrote plotly_lines_colors.py:

    from itertools import cycle
    import plotly
    import plotly.graph_objs as go
    data = []
    plot_title  = 'My Esoteric Plot Title'
    xaxis_label = 'Date'
    yaxis_label = 'Sliceable Height (mm)'
    layout = go.Layout(title=plot_title,
                       xaxis=dict(title=xaxis_label),
                       yaxis=dict(title=yaxis_label),
                       width=1000
                       )
    colors = cycle(pcl.seaborn_colors)

    for col in self.plot_range.columns[:-1]:
        color = next(colors)

        trace                 = go.Scatter()
        trace.x               = self.plot_range.loc[:, 'stop_week']
        trace.y               = self.plot_range.loc[:, col]
        trace.mode            = pcl.lines_only
        trace.marker['color'] = color
        trace.line['width']   = 2
        trace.name            = col

        trace_ma                 = go.Scatter()
        trace_ma.x               = self.plot_range.loc[:, 'stop_week']
        trace_ma.y               = self.plot_range.loc[:, col].rolling(4).mean()
        trace_ma.mode            = pcl.lines_only
        trace_ma.marker['color'] = color
        trace_ma.name            = col + '_4pma'
        trace_ma.line['shape']   = 'spline'
        trace_ma.line['dash']    = pcl.dashed
        trace_ma.line['width']   = 4

        data.append(trace)
        data.append(trace_ma)

    fig = go.Figure(data=data, layout=layout)
    return plotly.offline.plot(figure_or_data=fig, include_plotlyjs=False,
                               output_type='div', show_link=False)

which turns into:

    from itertools import cycle
    import plotly
    import plotly.graph_objs as go
    data = go.Data()
    plot_title =  'My Esoteric Plot Title'
    xaxis_label = 'Date'
    yaxis_label = 'Sliceable Height (mm)'
    layout = go.Layout(title=plot_title,
                       xaxis=dict(title=xaxis_label),
                       yaxis=dict(title=yaxis_label),
                       width=1000
                       )
    colors = cycle(plc.seaborn_colors)
    scat_fact = plc.ScatterFactory

    for i, col in enumerate(self.plot_range.columns[:-1]):
        color = next(colors)
        trace = scat_fact(linecolor=color, markercolor=color, lineweight=2, mode=plc.LINES_ONLY)
        trace.x = self.plot_range.loc[:, 'stop_week']
        trace.y = self.plot_range.loc[:, col]
        trace.name = col

        trace_ma = scat_fact(linecolor=color, markercolor=color, lineweight=4, dash=plc.DASHED,
                             lineshape=plc.SPLINE, mode=plc.LINES_ONLY)
        trace_ma.x = self.plot_range.loc[:, 'stop_week']
        trace_ma.y = self.plot_range.loc[:, col].rolling(4).mean()
        trace_ma.name = col + '_4pma'

        data.append(trace)
        data.append(trace_ma)

    fig = go.Figure(data=data, layout=layout)
    return plotly.offline.plot(figure_or_data=fig, include_plotlyjs=False,
                               output_type='div', show_link=False)

The pre-defined markers can be used to set the marker and it's options
rather than setting each option individually.