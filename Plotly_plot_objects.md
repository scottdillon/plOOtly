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



# [Layout](https://plot.ly/python/reference/#layout)

### [orientation](https://plot.ly/python/reference/#layout-orientation)
An angle. Works only on polar plots by rotating the plot by the given angle.

### [paper_bgcolor](https://plot.ly/python/reference/#layout-paper_bgcolor)
default:#fff. Sets the color of the paper where the graph is drawn

### [width](https://plot.ly/python/reference/#layout-width)
Default:700. Width of the plot area in pixels.

### [showlegend](https://plot.ly/python/reference/#layout-showlegend)
### [separators](https://plot.ly/python/reference/#layout-separators)







### [scene](https://plot.ly/python/reference/#layout-scene)
A dict which helps describe the layout of a 3D plot. The scene can have
xaxis, yaxis, zaxis, width and margin headings which determine the tick labels, font and axis
colors, etc.

ToDo: Fill in scene keys
### [scene[domain]](https://plot.ly/python/reference/#layout-scene-domain)
a dict

### [scene[domain][x]]()
A list. The vertical domain of the scene.

### [scene[domain][y]]()
A list.
### [scene[dragmode]](https://plot.ly/python/reference/#layout-scene-dragmode)
Enumerated list of strings which determine how the plot interacts with the mouse click and drag.
['orbit' | 'turntable' | 'zoom' | 'pan']
### [scene[yaxis]](https://plot.ly/python/reference/#layout-scene-yaxis)
A dict containing keys describing the yaxis attributes.
### [scene[yaxis][showexponent]](https://plot.ly/python/reference/#layout-scene-yaxis-showexponent)
Enumerated String. Either all exponents show beside their significands or the first, last or
none do.
[ all | first | last | none ]
### [scene[yaxis][showticklabels]](https://plot.ly/python/reference/#layout-scene-yaxis-showticklabels)
Boolean
### [scene[yaxis][ticksuffix]](https://plot.ly/python/reference/#layout-scene-yaxis-ticksuffix)
A string. Add a suffix to the tick labels. Instead of '5', it can be '5 ft'.
### [scene[yaxis][color]](https://plot.ly/python/reference/#layout-scene-yaxis-color)
Sets the colors for a objects associated with this axis at once. That would be the
line, font, tick and grid colors. Grid color can be lightened by blending with background.
Individual piece colors take priority over this.
### [scene[yaxis][categoryarray]](https://plot.ly/python/reference/#layout-scene-yaxis-categoryarray)
### [scene[yaxis][categoryorder]](https://plot.ly/python/reference/#layout-scene-yaxis-categoryorder)
### [scene[yaxis][showticksuffix]](https://plot.ly/python/reference/#layout-scene-yaxis-showticksuffix)
### [scene[yaxis][gridwidth]](https://plot.ly/python/reference/#layout-scene-yaxis-gridwidth)
### [scene[yaxis][titlefont]](https://plot.ly/python/reference/#layout-scene-yaxis-titlefont)
dict
### [scene[yaxis][titlefont][color]](https://plot.ly/python/reference/#layout-scene-yaxis-titlefont-color)
### [scene[yaxis][titlefont][size]](https://plot.ly/python/reference/#layout-scene-yaxis-titlefont-size)
### [scene[yaxis][titlefont][family]](https://plot.ly/python/reference/#layout-scene-yaxis-titlefont-family)
### [scene[yaxis][linecolor]](https://plot.ly/python/reference/#layout-scene-yaxis-linecolor)
### [margin](https://plot.ly/python/reference/#layout-margin)
a dict describing margin information on the layout.
### [margin[b]](https://plot.ly/python/reference/#layout-margin-b)
Default: 80. Set the bottom margin in pixels.
### [margin[l]](https://plot.ly/python/reference/#layout-margin-l)
Default: 80. Set the left margin in pixels.
### [margin[t]](https://plot.ly/python/reference/#layout-margin-t)
Default: 80. Set the top margin in pixels.
### [margin[r]](https://plot.ly/python/reference/#layout-margin-r)
Default: 80. Set the right margin in pixels.
### [margin[pad]](https://plot.ly/python/reference/#layout-margin-pad)
Default: 0. Set the amount of padding between the plotting area and the axis lines.
### [margin[autoexpand]](https://plot.ly/python/reference/#layout-margin-autoexpand)
Default: True

### [xaxis](https://plot.ly/python/reference/#layout-xaxis)
a dict of xaxis attributes.
### [xaxis[showexponent]](https://plot.ly/python/reference/#layout-xaxis-showexponent)
### [xaxis[showticklabels]](https://plot.ly/python/reference/#layout-xaxis-showticklabels)
### [xaxis[color]](https://plot.ly/python/reference/#layout-xaxis-color)
### [xaxis[categoryarray]](https://plot.ly/python/reference/#layout-xaxis-categoryarray)
### [xaxis[showticksuffix]](https://plot.ly/python/reference/#layout-xaxis-showticksuffix)
### [xaxis[titlefont]](https://plot.ly/python/reference/#layout-xaxis-titlefont)
### [xaxis[titlefont][color]]()
### [xaxis[titlefont][family]]()
### [xaxis[titlefont][size]]()
### [xaxis[linecolor]](https://plot.ly/python/reference/#layout-xaxis-linecolor)
### [xaxis[mirror]](https://plot.ly/python/reference/#layout-xaxis-mirror)
### [xaxis[tickvalssrc]](https://plot.ly/python/reference/#layout-xaxis-tickvalssrc)
### [xaxis[nticks]](https://plot.ly/python/reference/#layout-xaxis-nticks)
### [xaxis[linewidth]](https://plot.ly/python/reference/#layout-xaxis-linewidth)
### [xaxis[autorange]](https://plot.ly/python/reference/#layout-xaxis-autorange)
### [xaxis[ticktextsrc]](https://plot.ly/python/reference/#layout-xaxis-ticktextsrc)
### [xaxis[tickprefix]](https://plot.ly/python/reference/#layout-xaxis-tickprefix)
### [xaxis[position]](https://plot.ly/python/reference/#layout-xaxis-position)
### [xaxis[tickformat]](https://plot.ly/python/reference/#layout-xaxis-tickformat)
### [xaxis[tickmode]](https://plot.ly/python/reference/#layout-xaxis-tickmode)
### [xaxis[title]]()
### [xaxis[ticks]]()
### [xaxis[overlaying]]()
### [xaxis[rangemode]]()
### [xaxis[showtickprefix]]()
### [xaxis[zeroline]]()
### [xaxis[domain]]()
### [xaxis[gridcolor]]()
### [xaxis[type]]()
### [xaxis[rangeselector]](https://plot.ly/python/reference/#layout-xaxis-rangeselector)
dict
### [xaxis[rangeselector][bordercolor]]()
### [xaxis[rangeselector][yanchor]]()
### [xaxis[rangeselector][xanchor]]()
### [xaxis[rangeselector][bgcolor]]()
### [xaxis[rangeselector][buttons]](https://plot.ly/python/reference/#layout-xaxis-rangeselector-buttons)
### [xaxis[rangeselector][buttons][count]]()
### [xaxis[rangeselector][buttons][stepmode]]()
### [xaxis[rangeselector][buttons][label]]()
### [xaxis[rangeselector][buttons][step]]()
### [xaxis[rangeselector][visible]]()
### [xaxis[rangeselector][activecolor]]()
### [xaxis[rangeselector][borderwidth]]()
### [xaxis[rangeselector][y]]()
### [xaxis[rangeselector][x]]()
### [xaxis[rangeselector][font]]()
### [xaxis[rangeselector][font][color]]()
### [xaxis[rangeselector][font][family]]()
### [xaxis[rangeselector][font][size]]()
### [xaxis[separatethousands]](https://plot.ly/python/reference/#layout-xaxis-separatethousands)
### [xaxis[zerolinewidth]]()
### [xaxis[ticklen]]()
### [xaxis[categoryorder]]()
### [xaxis[hoverformat]]()
### [xaxis[ticksuffix]]()
### [xaxis[fixedrange]]()
### [xaxis[showline]]()
### [xaxis[ticktext]]()
### [xaxis[showgrid]]()
### [xaxis[tickvals]]()
### [xaxis[tickfont]](https://plot.ly/python/reference/#layout-xaxis-tickfont)
### [xaxis[tickfont][color]]()
### [xaxis[tickfont][family]]()
### [xaxis[tickfont][size]]()
### [xaxis[tickwidth]]()
### [xaxis[tick0]]()
### [xaxis[tickangle]]()
### [xaxis[gridwidth]]()
### [xaxis[dtick]]()
### [xaxis[side]]()
### [xaxis[zerolinecolor]]()
### [xaxis[range]]()
### [xaxis[categoryarraysrc]]()
### [xaxis[calendar]]()
### [xaxis[tickcolor]]()
### [xaxis[rangeslider]](https://plot.ly/python/reference/#layout-xaxis-rangeslider)
### [xaxis[rangeslider][bordercolor]]()
### [xaxis[rangeslider][visible]]()
### [xaxis[rangeslider][thickness]]()
### [xaxis[rangeslider][bgcolor]]()
### [xaxis[rangeslider][range]]()
### [xaxis[rangeslider][borderwidth]]()
### [xaxis[anchor]]()
### [xaxis[exponentformat]]()
### [mapbox](https://plot.ly/python/reference/#layout-mapbox)
### [direction]()
For polar plots

### [angularaxis](https://plot.ly/python/reference/#layout-angularaxis)
### [geo]()
### [legend](https://plot.ly/python/reference/#layout-legend)
A dict.
### [legend[bordercolor]]()
### [legend[yanchor]]()
### [legend[traceorder]]()
### [legend[xanchor]]()
### [legend[orientation]]()
### [legend[tracegroupgap]]()
### [legend[bgcolor]]()
### [legend[borderwidth]]()
### [legend[y]]()
### [legend[x]]()
### [legend[font]]()
### [legend[font][color]]()
### [legend[font][family]]()
### [legend[font][size]]()
### [yaxis](https://plot.ly/python/reference/#layout-yaxis)
A dict. The same entries as xaxis.
### [updatemenus](https://plot.ly/python/reference/#layout-updatemenus)
A dict.
### [annotations](https://plot.ly/python/reference/#layout-annotations)
### [annotations[bordercolor]]()
### [annotations[yanchor]]()
### [annotations[text]]()
### [annotations[arrowsize]]()
### [annotations[textangle]]()
### [annotations[borderwidth]]()
### [annotations[yclick]]()
### [annotations[ay]]()
### [annotations[ax]]()
### [annotations[font]]()
### [annotations[font][color]]()
### [annotations[font][family]]()
### [annotations[font][size]]()
### [annotations[arrowcolor]]()
### [annotations[xref]]()
### [annotations[arrowhead]]()
### [annotations[bgcolor]]()
### [annotations[borderpad]]()
### [annotations[showarrow]]()
### [annotations[opacity]]()
### [annotations[xanchor]]()
### [annotations[axref]]()
### [annotations[ayref]]()
### [annotations[arrowwidth]]()
### [annotations[visible]]()
### [annotations[yref]]()
### [annotations[yref]]()
### [annotations[align]]()
### [annotations[clicktoshow]](https://plot.ly/python/reference/#layout-annotations-clicktoshow)
### [annotations[xclick]]()
### [annotations[y]]()
### [annotations[x]]()
### [annotations[standoff]]()
### [shapes](https://plot.ly/python/reference/#layout-shapes)
A dict.
### [shapes[opacity]]()
### [shapes[layer]]()
### [shapes[xref]]()
### [shapes[yref]]()
### [shapes[visible]]()
### [shapes[fillcolor]]()
### [shapes[path]]()
### [shapes[y1]]()
### [shapes[y0]]()
### [shapes[x1]]()
### [shapes[x0]]()
### [shapes[type]]()
### [shapes[line]]()
### [shapes[line][color]]()
### [shapes[line][width]]()
### [shapes[line][dash]]()

### [sliders](https://plot.ly/python/reference/#layout-sliders)
A dict

### [ternary]()



## Getting Fancy with Titles
[Adding HTML and links to Charts](http://help.plot.ly/adding-HTML-and-links-to-charts/)
