## Plotly Cheatsheet

First, you'll need to import the graph objects:
``` Python
import plotly.graph_objs as go
```
Then, you can place the data into plot series objects such as go.Scatter, go.Bar, etc.

``` Python
trace1 = go.Scatter(
                    x = iterable,
                    y = iterable,
                    mode = 'lines+markers',
                    name = iterable,
                    text = iterable
                    marker = dict(
                        size = 10,
                        symbol = 'circle',
                        color = 'rgba(152, 0, 0, .8)',
                        colorscale = 'Viridis',
                        line = dict(
                            width = 2,
                            color = 'rgba(10, 10, 10, 0.5)'
                            )
                     )
                    textposition : 'top left',
                    hoverinfo : 'x', 'y',
                    line = dict()
                    )
```

## [go.Scatter attributes](https://plot.ly/python/reference/#scatter)

### [x](https://plot.ly/python/reference/#scatter-x)
A data iterable. Some sort of number or categorical iterable to use for the x axis. a pd.DataFrame.Index object will work just fine.

### [y](https://plot.ly/python/reference/#scatter-y)
Some sort of numerical iterable to plot on the y axis. A pandas dataframe column or Series will work just fine.

### [mode](https://plot.ly/python/reference/#scatter-mode)
Do you want lines, markers or both? Select one from ['lines', 'markers', 'lines+markers']

### [name](https://plot.ly/python/reference/#scatter-name)
This is the name of the trace that will be shown in the legend. Typically the name of your data series.

### [text](https://plot.ly/python/reference/#scatter-text)
This attribute is an iterable of the same length as the x or y attribute iterables.
The values of the iterable will be appended to the hover text.

### [marker](https://plot.ly/python/reference/#scatter-marker)
This is a dictionary object. Assigning a scalar object such as a string or integer will break  your plot. Probably in a way that you see the plot but don't see the trace on the plot. All following keywords for this dict object will have the keyword in a dict['keyword'] notation to indicate it is still part of the marker dict object.

### [marker['size']](https://plot.ly/python/reference/#scatter-marker-size)
Default size is 6. Sets the marker size in pixels.

### [marker['sizemode']](https://plot.ly/python/reference/#scatter-marker-sizemode)
Only works if marker.size is set to a numerical array type. Does the value in the array refer to the value of the area or the diameter.
type: enumerated: "diameter" | "area"

### [marker['symbol']](https://plot.ly/python/reference/#scatter-marker-symbol)
Lots of marker options to choose from here. Can be text or a text numeral which correspond to the same symbol. Ex.: "0" | "circle" is the same thing. Adding "100" to the number will change the marker from a filled to open marker. Adding "200" appends a "dot" to the marker name and adding "300" appends an "open-dot" to the symbol name.
One thing to note is that despite what is shown on the plotly website, the numbers are integers and not strings.
Valid string values and corresponding numbers:

"circle" : 0

"circle-open" : 100

"circle-dot" : 200

"circle-open-dot" : 300

### [marker['color']](https://plot.ly/python/reference/#scatter-marker-color)
Set this using the notation "rgba(234,252, 123, 0.5)" or hsl notation. You don't have to include an alpha number but why not.

### [marker['cmin']](https://plot.ly/python/reference/#scatter-marker-cmin)

### [marker['cmax']](https://plot.ly/python/reference/#scatter-marker-cmax)

### [marker['colorscale']](https://plot.ly/python/reference/#scatter-marker-colorscale)
Plotly colorscales are:
['Blackbody', 'Bluered', 'Blues', 'Earth', 'Electric', 'Greens', 'Greys', 'Hot',
'Jet', 'Picnic', 'Portland', 'Rainbow', 'RdBu', 'Reds', 'Viridis', 'YlGnBu',
'YlOrRd'] as noted [here](https://community.plot.ly/t/what-colorscales-are-available-in-plotly-and-which-are-the-default/2079/2).
More info on getting colorscales from mpl is [here](https://plot.ly/python/matplotlib-colorscales/) and [here](https://plot.ly/python/cmocean-colorscales/).

### [marker['colorsrc']](https://plot.ly/python/reference/#scatter-marker-colorsrc)

### [marker['colorbar']](https://plot.ly/python/reference/#scatter-marker-colorbar)
There is a whole slew of options for this that I have not explored yet but you can manipulate details of the colorbar.

### [marker['cauto']](https://plot.ly/python/reference/#scatter-marker-cauto)

### [marker['reversescale']](https://plot.ly/python/reference/#scatter-marker-colorscale)
A boolean which does the obvious but only if the marker.color is set to a numerical array.

### [marker['opacity']](https://plot.ly/python/reference/#scatter-marker-opacity)

### [marker['autocolorscale']](https://plot.ly/python/reference/#scatter-marker-autocolorscale)

### [marker['sizemin']](https://plot.ly/python/reference/#scatter-marker-sizemin)
value >= 0. Only works if marker.size is set to an array.

### [marker['line']](https://plot.ly/python/reference/#scatter-marker-line)

### [marker['line']['width']](https://plot.ly/python/reference/#scatter-marker-line-width)

### [marker['line']['color']](https://plot.ly/python/reference/#scatter-marker-line-color)

### [marker['line']['colorsrc']](https://plot.ly/python/reference/#scatter-marker-line-colorsrc)

### [marker['line']['autocolorscale']](https://plot.ly/python/reference/#scatter-marker-autocolorscale)

### [marker['line']['cmin']](https://plot.ly/python/reference/#scatter-marker-line-cmin)

### [marker['line']['cmax']](https://plot.ly/python/reference/#scatter-marker-line-cauto)

### [marker['line']['colorscale']](https://plot.ly/python/reference/#scatter-marker-line-colorscale)
Sets the colorscale and only has an effect if `marker.line.color` is set to a numerical array. The colorscale must be an array containing arrays mapping a normalized value to an rgb, rgba, hex, hsl, hsv, or named color string. At minimum, a mapping for the lowest (0) and highest (1) values are required. For example, `[[0, 'rgb(0,0,255)', [1, 'rgb(255,0,0)']]`. To control the bounds of the colorscale in color space, use `marker.line.cmin` and `marker.line.cmax`. Alternatively, `colorscale` may be a palette name string of the following list: Greys, YlGnBu, Greens, YlOrRd, Bluered, RdBu, Reds, Blues, Picnic, Rainbow, Portland, Jet, Hot, Blackbody, Earth, Electric, Viridis

### [marker['line']['reversescale']](https://plot.ly/python/reference/#scatter-marker-line-reversescale)

### [marker['line']['widthsrc']](https://plot.ly/python/reference/#scatter-marker-line-widthsrc)

### [marker['line']['cauto']](https://plot.ly/python/reference/#scatter-marker-line-cauto)

### [line](https://plot.ly/python/reference/#scatter-line)
Sets dict keyword, value pairs for the line attributes.

### [line['simplify']](https://plot.ly/python/reference/#scatter-line-simplify)

### [line['color']](https://plot.ly/python/reference/#scatter-line-color)

### [line['smoothing']](https://plot.ly/python/reference/#scatter-line-smoothing)

### [line['dash']](https://plot.ly/python/reference/#scatter-line-dash)
Enumerated value: ['solid' | 'dash' | 'dot']. Can also be set to a dash length in pixels.
type: string

### [line['width']](https://plot.ly/python/reference/#scatter-line-width)

### [line['shape']](https://plot.ly/python/reference/#scatter-line-shape)
Default is 'linear'. This is the shape that the line connecting datapoints will have. Should it spline interpolation or be stepped? [Here are examples.](https://plot.ly/create/?fid=chelsea_lyn:8766)

### [textposition](https://plot.ly/python/reference/#scatter-textposition)
enumerated: "top left" | "top center" | "top right" | "middle left" | "middle center" | "middle right" | "bottom left" | "bottom center" | "bottom right" )
default: "middle center"
Sets the positions of the `text` elements with respects to the (x,y) coordinates.

### [hoverinfo](https://plot.ly/python/reference/#scatter-hoverinfo)
Allows you to customize the text that pops up when you hover over a datapoint or position on the chart.

### [visible](https://plot.ly/python/reference/#scatter-visible)
Default: True. Is the trace visible? If false, trace will not appear in the legend or plot. If 'legendonly', trace is not drawn but will appear in the legend.

### [hoveron](https://plot.ly/python/reference/#scatter-hoveron)

### [fill](https://plot.ly/python/reference/#scatter-fill)

### [showlegend](https://plot.ly/python/reference/#scatter-showlegend)

### [error_x](https://plot.ly/python/reference/#scatter-error_x)

### [error_y](https://plot.ly/python/reference/#scatter-error_y)

### [xaxis](https://plot.ly/python/reference/#scatter-xaxis)
### [yaxis](https://plot.ly/python/reference/#scatter-yaxis)

### [opacity](https://plot.ly/python/reference/#scatter-opacity)

### [textfont](https://plot.ly/python/reference/#scatter-textfont)

### [legendgroup](https://plot.ly/python/reference/#scatter-legendgroup)

### [fillcolor](https://plot.ly/python/reference/#scatter-fillcolor)

### [dx](https://plot.ly/python/reference/#scatter-dx)
This is the x axis increment. Use this in combination with x0 instead of setting x.

### [dy](https://plot.ly/python/reference/#scatter-dy)
This is the y axis increment. Use this in combination with y0 instead of setting y.

### [x0](https://plot.ly/python/reference/#scatter-x0)
This is the starting point for the minimum x coordinate. Use this in combination with dx instead of setting x.

### [y0](https://plot.ly/python/reference/#scatter-y0)
This is the starting point for the minimum y coordinate. Use this in combination with dy instead of setting y.

### [connectgaps](https://plot.ly/python/reference/#scatter-connectgaps)
Connect the gaps between data points with nans with a trace line?

### [ids](https://plot.ly/python/reference/#scatter-ids)
"A list of keys for object constancy of data points during animation"

I'm not exactly sure what this means as I don't do any animations. At least not yet.

### [idssrc](https://plot.ly/python/reference/#scatter-idssrc)
Sets the source reference for ids.

### [r](https://plot.ly/python/reference/#scatter-r)
Sets the radial coordinates.

type: iterable: list, pd.Series, etc.

## [Add layout attributes here](https://plot.ly/python/reference/#layout)



## Getting Fancy with Titles
[Adding HTML and links to Charts](http://help.plot.ly/adding-HTML-and-links-to-charts/)