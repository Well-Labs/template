from dash import Dash, dcc, html, page_container, page_registry
import dash_design_kit as ddk

app = Dash(__name__, suppress_callback_exceptions = True, use_pages=True)

server = app.server

app.layout = ddk.App([
    ddk.Header([
        ddk.Logo(src=app.get_relative_path('/assets/logo.png')),
        ddk.Title('Well Labs'),
        ddk.Menu([
            html.Div(
                dcc.Link(
                    f"{page['name']}", href=page["relative_path"]
                )
            )
            for page in page_registry.values()
        ])
    ]),
    html.Div(page_container)
])

if __name__ == '__main__':
    app.run(
        debug=True,
        )
