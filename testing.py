from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.models import ColumnDataSource
from jinja2 import Template

source = ColumnDataSource(data=dict(x=[1, 2, 3],
                                    y=[3, 2, 1]),
                          name='my-data-source')

p = figure()
l1 = p.line("x", "y", source=source)

# copied and modified default file.html template used for e.g. `file_html`
html_template = Template("""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>{{ title|e if title else "Bokeh Plot" }}</title>
        {{ bokeh_css }}
        {{ bokeh_js }}
        <style>
          html {
            width: 100%;
            height: 100%;
          }
          body {
            width: 90%;
            height: 100%;
            margin: auto;
          }
        </style>
        <script>
            function change_ds_value(name, idx, value) {
                var ds = Bokeh.documents[0].get_model_by_name('my-data-source');
                ds.data[name][idx] = value;
                ds.change.emit();
            }
        </script>
    </head>
    <body>
        <div>
            {{ plot_div|indent(8) }}
            {{ plot_script|indent(8) }}
            <input type='range' min='-5' max='5'
                   onchange='change_ds_value("x", 1, this.value)'/>
            <input type='range' min='-5' max='5'
                   onchange='change_ds_value("y", 1, this.value)'/>
        </div>
    </body>
</html>
""")

html = file_html(p, CDN, template=html_template)
with open('test.html', 'wt') as f:
    f.write(html)