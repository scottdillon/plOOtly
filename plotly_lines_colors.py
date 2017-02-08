import plotly.graph_objs as go

BLUE      = 'rgba(76,  114, 176, 1.0)'
GREEN     = 'rgba(85,  168, 104, 1.0)'
RED       = 'rgba(196,  78,  82, 1.0)'
PURPLE    = 'rgba(129, 114, 178, 1.0)'
YELLOW    = 'rgba(204, 185, 116, 1.0)'
TURQUOISE = 'rgba(100, 181, 205, 1.0)'
BLACK     = 'RGBA(  0,   0,   0, 1.0)'

seaborn_colors = [BLUE, GREEN, RED, PURPLE, YELLOW, TURQUOISE]

dashed = 'dash'
dot    = 'dot'

lines_only    = 'lines'
markers_only  = 'markers'
lines_markers = 'lines+markers'

blue_marker      = dict(color=BLUE,      line=dict(color=BLUE,      width=6), size=6, symbol='circle')
red_marker       = dict(color=RED,       line=dict(color=RED,       width=6), size=6, symbol='circle')
green_marker     = dict(color=GREEN,     line=dict(color=GREEN,     width=6), size=6, symbol='circle')
purple_marker    = dict(color=PURPLE,    line=dict(color=PURPLE,    width=6), size=6, symbol='circle')
yellow_marker    = dict(color=YELLOW,    line=dict(color=YELLOW,    width=6), size=6, symbol='circle')
turquoise_marker = dict(color=TURQUOISE, line=dict(color=TURQUOISE, width=6), size=6, symbol='circle')

blue_solid_scatter_line      = go.Scatter(marker=blue_marker,      line=dict(width=4),     mode=lines_only)
blue_dashed_scatter_line     = go.Scatter(marker=blue_marker,      line=dict(dash=dashed), mode=lines_only)
green_solid_scatter_line     = go.Scatter(marker=green_marker,     line=dict(width=4),     mode=lines_only)
green_dashed_scatter_line    = go.Scatter(marker=green_marker,     line=dict(dash=dashed), mode=lines_only)
red_solid_scatter_line       = go.Scatter(marker=red_marker,       line=dict(width=4),     mode=lines_only)
red_dashed_scatter_line      = go.Scatter(marker=red_marker,       line=dict(dash=dashed), mode=lines_only)
purple_solid_scatter_line    = go.Scatter(marker=purple_marker,    line=dict(width=4),     mode=lines_only)
purple_dashed_scatter_line   = go.Scatter(marker=purple_marker,    line=dict(dash=dashed), mode=lines_only)
yellow_solid_scatter_line    = go.Scatter(marker=yellow_marker,    line=dict(width=4),     mode=lines_only)
yellow_dashed_scatter_line   = go.Scatter(marker=yellow_marker,    line=dict(dash=dashed), mode=lines_only)
turquoise_solid_scatter_line = go.Scatter(marker=turquoise_marker, line=dict(width=4),     mode=lines_only)
turqiose_dashed_scatter_line = go.Scatter(marker=turquoise_marker, line=dict(dash=dashed), mode=lines_only)

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