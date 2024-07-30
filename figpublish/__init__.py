from plotly.graph_objects import Figure

FONT_FAMILY = "Computer Modern"
FONT_COLOR = "black"
LINE_WIDTH = 1


def publication_styles(fig: Figure) -> Figure:
    """Generic stylings applied to make a plot look publication-ready."""
    return (
        Figure(fig)
        .update_layout(
            {
                "template": "plotly_white",
                "font": {
                    "family": FONT_FAMILY,
                    "color": FONT_COLOR,
                    "size": 12,
                },
                "legend": {
                    "bordercolor": "Black",
                    "borderwidth": LINE_WIDTH,
                    "title_font_family": FONT_FAMILY,
                    "font": {
                        "family": FONT_FAMILY,
                        "color": FONT_COLOR,
                        "size": 12,
                    },
                },
            }
        )
        .update_xaxes(showline=True, linewidth=LINE_WIDTH, linecolor="black")
        .update_yaxes(showline=True, linewidth=LINE_WIDTH, linecolor="black")
    )
