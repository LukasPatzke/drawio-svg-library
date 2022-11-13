import base64
import zlib
import json
import xml.etree.ElementTree as ET


def parse_svg(filepath: str, namespace: str) -> ET.ElementTree:
    """Read a svg from a file and parse the xml"""
    ET.register_namespace("", namespace)
    return ET.parse(filepath)


def add_css_to_tag(svg: ET.ElementTree, tag: str, color="#000000") -> ET.ElementTree:
    """Add a css class to every xml tag in the svg
    and a css fill property with the given color for every generated class."""
    root = svg.getroot()

    style = ET.Element("style")
    style.set("type", "text/css")
    style.text = ""

    for index, path in enumerate(root.iter(tag)):
        path.set("class", f"path{index}")
        style.text += f".path{index}{{fill:{color};}}"

    root.append(style)
    return svg


def generate_svg_uri(svg: ET.ElementTree) -> str:
    """
    Generate a svg uri for a given svg.

    Use base64 encoding, but do not include the ;base64
    The ; conflicts with the style syntax in diagrams.net
    """
    string = ET.tostring(svg.getroot())
    return "data:image/svg+xml," + base64.b64encode(string).decode("ascii")


def format_cell_style(style_dict: "dict[str, str]") -> str:
    """Format a dict of style properties to a string"""
    combined_properties = ["=".join(prop) for prop in style_dict.items()]
    return ";".join(combined_properties)


def generate_mxgraphmodel(svg_uri: str) -> ET.Element:
    """Generate the MxGraphModel XML"""
    mxGraphModel = ET.Element("mxGraphModel")
    root = ET.SubElement(mxGraphModel, "root")

    cell0 = ET.SubElement(root, "mxCell")
    cell0.set("id", "0")
    cell1 = ET.SubElement(root, "mxCell")
    cell1.set("id", "1")
    cell1.set("parent", "0")

    cell = ET.SubElement(root, "mxCell")
    cell.set("id", "2")
    cell.set("parent", "1")
    cell.set("vertex", "1")
    cell.set("value", "")

    style = {
        "shape": "image",
        "verticalLabelPosition": "bottom",
        "labelBackgroundColor": "#ffffff",
        "verticalAlign": "top",
        "aspect": "fixed",
        "imageAspect": "0",
        "image": svg_uri,
        "editableCssRules": ".*",
    }

    cell.set("style", format_cell_style(style))

    geometry = ET.SubElement(cell, "mxGeometry")
    geometry.set("width", "40")
    geometry.set("height", "40")
    geometry.set("as", "geometry")

    return mxGraphModel


def deflate_and_base64_encode(string_val: bytes) -> bytes:
    """
    Deflate a string with zlib and base64 encode the result
    https://stackoverflow.com/q/1089662
    https://drawio-app.com/extracting-the-xml-from-mxfiles/
    """
    zlibbed_str = zlib.compress(string_val)
    compressed_string = zlibbed_str[2:-4]
    return base64.b64encode(compressed_string)


def generate_library(icons: "dict[str, bytes]") -> ET.ElementTree:
    """Build the library XML for a gevien set of icons"""
    library_config = []

    for name, icon in icons.items():
        library_config.append(
            {
                "xml": icon.decode("ascii"),
                "w": 40,
                "h": 40,
                "aspect": "fixed",
                "title": name,
            }
        )
    library_config.sort(key=lambda x: x.get("title"))
    library_json = json.dumps(library_config)

    mxlibrary = ET.Element("mxlibrary")
    mxlibrary.text = library_json

    return ET.ElementTree(mxlibrary)

