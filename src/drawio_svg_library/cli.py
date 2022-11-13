import pathlib
from typing import List
import xml.etree.ElementTree as ET

import typer

from drawio_svg_library import core


app = typer.Typer()


@app.command()
def cli(
    input: List[str] = typer.Argument(..., help="Input SVG files"),
    output: str = typer.Option(
        "./library.xml", "--output", "-o", help="The output file."
    ),
    add_css: bool = typer.Option(
        False, "--css", "-c", help="Add CSS classes to SVG tags."
    ),
    namespace: str = typer.Option(
        "http://www.w3.org/2000/svg",
        "--namespace",
        "-n",
        help="Specify the XML namespace for the input SVGs.",
    ),
    tag: str = typer.Option(
        "path", "--tag", "-t", help="Specify the XML tag where css classes are added."
    ),
):
    """Generate a draw.io / diagrams.net library from SVGs"""
    icons = {}

    for filepath in input:
        name = pathlib.Path(filepath).stem

        svg = core.parse_svg(filepath, namespace="http://www.w3.org/2000/svg")

        if add_css:
            if namespace:
                tag = f"{{{namespace}}}{tag}"
            svg = core.add_css_to_tag(svg, tag=tag)

        uri = core.generate_svg_uri(svg)

        mxgraphmodel = core.generate_mxgraphmodel(uri)

        deflated_model = core.deflate_and_base64_encode(ET.tostring(mxgraphmodel))

        icons[name] = deflated_model

    library = core.generate_library(icons)
    library.write(output)


if __name__ == "__main__":
    app()
