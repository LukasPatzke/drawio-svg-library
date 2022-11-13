# Drawio SVG Library

[![PyPI - Version](https://img.shields.io/pypi/v/drawio-svg-library.svg)](https://pypi.org/project/drawio-svg-library)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/drawio-svg-library.svg)](https://pypi.org/project/drawio-svg-library)

This tools allows the conversion of SVGs into a draw.io / diagrams.net library. Supports colorable SVGs.

---

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install drawio-svg-library
```

## CLI

```
drawio-svg-library --help

 Usage: drawio-svg-library [OPTIONS] INPUT...

 Generate a draw.io / diagrams.net library from SVGs

╭─ Arguments ────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    input      INPUT...  Input SVG files [default: None] [required]                                                       │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --output              -o      TEXT  The output file. [default: ./library.xml]                                              │
│ --css                 -c            Add CSS classes to SVG tags.                                                           │
│ --namespace           -n      TEXT  Specify the XML namespace for the input SVGs. [default: http://www.w3.org/2000/svg]    │
│ --tag                 -t      TEXT  Specify the XML tag where css classes are added. [default: path]                       │
│ --install-completion                Install completion for the current shell.                                              │
│ --show-completion                   Show completion for the current shell, to copy it or customize the installation.       │
│ --help                              Show this message and exit.                                                            │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## What it does

### CSS classes

To be able to set the fill colours of an SVG in diagram.net, every element needs a CSS class
and the SVG needs an embedde CSS style with these classes (see https://www.diagrams.net/doc/faq/svg-edit-colours).

Use the option `--css` to enable the injection off a CSS class for every SVG tag specified via `--tag` (defaults to `path`).

Example input:

```xml
<?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 17.1.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 20 20" enable-background="new 0 0 20 20" xml:space="preserve">
<g id="add_1_">
	<g>
		<path fill-rule="evenodd" clip-rule="evenodd" d="M10,0C4.48,0,0,4.48,0,10c0,5.52,4.48,10,10,10s10-4.48,10-10
			C20,4.48,15.52,0,10,0z M10,18c-4.42,0-8-3.58-8-8s3.58-8,8-8s8,3.58,8,8S14.42,18,10,18z M15,9h-4V5c0-0.55-0.45-1-1-1
			S9,4.45,9,5v4H5c-0.55,0-1,0.45-1,1c0,0.55,0.45,1,1,1h4v4c0,0.55,0.45,1,1,1s1-0.45,1-1v-4h4c0.55,0,1-0.45,1-1
			C16,9.45,15.55,9,15,9z"/>
	</g>
</g>
</svg>
```

Example output:

```xml
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" id="Layer_1" x="0px" y="0px" viewBox="0 0 20 20" enable-background="new 0 0 20 20" xml:space="preserve">
<g id="add_1_">
	<g>
		<path fill-rule="evenodd" clip-rule="evenodd" d="M10,0C4.48,0,0,4.48,0,10c0,5.52,4.48,10,10,10s10-4.48,10-10
            C20,4.48,15.52,0,10,0z M10,18c-4.42,0-8-3.58-8-8s3.58-8,8-8s8,3.58,8,8S14.42,18,10,18z M15,9h-4V5c0-0.55-0.45-1-1-1
            S9,4.45,9,5v4H5c-0.55,0-1,0.45-1,1c0,0.55,0.45,1,1,1h4v4c0,0.55,0.45,1,1,1s1-0.45,1-1v-4h4c0.55,0,1-0.45,1-1
            C16,9.45,15.55,9,15,9z" class="path0" />
	</g>
</g>
<style type="text/css">.path0{fill:#000000;}</style></svg>
```

### Data uri

Generate a svg uri for the given svg. Uses base64 encoding, but does not include `;base64` in the MIME type.
The `;` conflicts with the style syntax in diagrams.net.

Example output:

```
data:image/svg+xml,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHg9IjBweCIgeT0iMHB4IiB2aWV3Qm94PSIwIDAgMjAgMjAiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDIwIDIwIiB4bWw6c3BhY2U9InByZXNlcnZlIj4KPGcgaWQ9ImFkZF8xXyI+Cgk8Zz4KCQk8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEwLDBDNC40OCwwLDAsNC40OCwwLDEwYzAsNS41Miw0LjQ4LDEwLDEwLDEwczEwLTQuNDgsMTAtMTAgICAgQzIwLDQuNDgsMTUuNTIsMCwxMCwweiBNMTAsMThjLTQuNDIsMC04LTMuNTgtOC04czMuNTgtOCw4LThzOCwzLjU4LDgsOFMxNC40MiwxOCwxMCwxOHogTTE1LDloLTRWNWMwLTAuNTUtMC40NS0xLTEtMSAgICBTOSw0LjQ1LDksNXY0SDVjLTAuNTUsMC0xLDAuNDUtMSwxYzAsMC41NSwwLjQ1LDEsMSwxaDR2NGMwLDAuNTUsMC40NSwxLDEsMXMxLTAuNDUsMS0xdi00aDRjMC41NSwwLDEtMC40NSwxLTEgICAgQzE2LDkuNDUsMTUuNTUsOSwxNSw5eiIgY2xhc3M9InBhdGgwIiAvPgoJPC9nPgo8L2c+CjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+LnBhdGgwe2ZpbGw6IzAwMDAwMDt9PC9zdHlsZT48L3N2Zz4=
```

### Styles

Generates a draw.io style JSON. Adds `"editableCssRules": ".*"` to add GUI support for the change of the CSS colors.

```json
{
  "shape": "image",
  "verticalLabelPosition": "bottom",
  "labelBackgroundColor": "#ffffff",
  "verticalAlign": "top",
  "aspect": "fixed",
  "imageAspect": 0,
  "image": "data:image/svg+xml,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHg9IjBweCIgeT0iMHB4IiB2aWV3Qm94PSIwIDAgMjAgMjAiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDIwIDIwIiB4bWw6c3BhY2U9InByZXNlcnZlIj4KPGcgaWQ9ImFkZF8xXyI+Cgk8Zz4KCQk8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEwLDBDNC40OCwwLDAsNC40OCwwLDEwYzAsNS41Miw0LjQ4LDEwLDEwLDEwczEwLTQuNDgsMTAtMTAgICAgQzIwLDQuNDgsMTUuNTIsMCwxMCwweiBNMTAsMThjLTQuNDIsMC04LTMuNTgtOC04czMuNTgtOCw4LThzOCwzLjU4LDgsOFMxNC40MiwxOCwxMCwxOHogTTE1LDloLTRWNWMwLTAuNTUtMC40NS0xLTEtMSAgICBTOSw0LjQ1LDksNXY0SDVjLTAuNTUsMC0xLDAuNDUtMSwxYzAsMC41NSwwLjQ1LDEsMSwxaDR2NGMwLDAuNTUsMC40NSwxLDEsMXMxLTAuNDUsMS0xdi00aDRjMC41NSwwLDEtMC40NSwxLTEgICAgQzE2LDkuNDUsMTUuNTUsOSwxNSw5eiIgY2xhc3M9InBhdGgwIiAvPgoJPC9nPgo8L2c+CjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+LnBhdGgwe2ZpbGw6IzAwMDAwMDt9PC9zdHlsZT48L3N2Zz4=",
  "editableCssRules": ".*"
}
```

### MxGraphModel

Generates the XML for the `MxGraphModel`. For some reason three intances of `mxCell` are needed.

Example output:

```xml
<mxGraphModel>
    <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="2" parent="1" vertex="1" value="" style="shape=image;verticalLabelPosition=bottom;labelBackgroundColor=#ffffff;verticalAlign=top;aspect=fixed;imageAspect=0;image=data:image/svg+xml,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHg9IjBweCIgeT0iMHB4IiB2aWV3Qm94PSIwIDAgMjAgMjAiIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDIwIDIwIiB4bWw6c3BhY2U9InByZXNlcnZlIj4KPGcgaWQ9ImFkZF8xXyI+Cgk8Zz4KCQk8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEwLDBDNC40OCwwLDAsNC40OCwwLDEwYzAsNS41Miw0LjQ4LDEwLDEwLDEwczEwLTQuNDgsMTAtMTAgICAgQzIwLDQuNDgsMTUuNTIsMCwxMCwweiBNMTAsMThjLTQuNDIsMC04LTMuNTgtOC04czMuNTgtOCw4LThzOCwzLjU4LDgsOFMxNC40MiwxOCwxMCwxOHogTTE1LDloLTRWNWMwLTAuNTUtMC40NS0xLTEtMSAgICBTOSw0LjQ1LDksNXY0SDVjLTAuNTUsMC0xLDAuNDUtMSwxYzAsMC41NSwwLjQ1LDEsMSwxaDR2NGMwLDAuNTUsMC40NSwxLDEsMXMxLTAuNDUsMS0xdi00aDRjMC41NSwwLDEtMC40NSwxLTEgICAgQzE2LDkuNDUsMTUuNTUsOSwxNSw5eiIgY2xhc3M9InBhdGgwIiAvPgoJPC9nPgo8L2c+CjxzdHlsZSB0eXBlPSJ0ZXh0L2NzcyI+LnBhdGgwe2ZpbGw6IzAwMDAwMDt9PC9zdHlsZT48L3N2Zz4=;editableCssRules=.*">
            <mxGeometry width="40" height="40" as="geometry" />
        </mxCell>
    </root>
</mxGraphModel>
```

### XML deflation

draw.io uses compressed XML using zlib (see https://drawio-app.com/extracting-the-xml-from-mxfiles/).

Example output:

```
bVRtk6I4EP4rU963m6sbRNzSc9gqXhzEBdQBBfkWIRuiQSwTJfLrt4GZ2dqqo6orD91Pd56kOv1aSueKLoVf5Zh9f71Wlfj+WkoLM/ZEc32gDJ5e/nAMB08XdMVn8T8x9XcMaHd8FVj2ELEb1geDJy4eDAAv0AXrtEQEz1oazRDz0AGzdcWpoNVZP1RCVOWMtU4TZSdyrW7n3KpYddX/+tl9X5kGo+Ssi+oyQ/yCM6H/pBLns6680XuU/k/PkUD/dfCF38mzLNk/60Wgpg9TO8TyljUKRYt3JbOruzfKR/ljPPIf43tWZnf/aNS+NW3yMqPuImXZObgcVG3qHuc3P3QJijdT9yQLHO8eSTMHDoGYWWPLJThSqL8wNZeaKop3o0051dahW7u2QaBua9R1drd9vORpOKT7OLimo+U9j8endbi8pUlGfMsAvtsbbfXW37KRWezV7dQ9m480CUBTytyj9mPtZL2e8u2Uvk1k8nCfLXKapI32w9qcJpnzpiDLLFEsuZcshwcHapQ7NY3H99TZgJaAo8QQ2XnHU9CeJik7lNNTCmdJbYVG0bz2bNMOLE1ZWTVgg//G83rfwH+oDX1aK95xo7W+T8saWKPNLbAJ9yNDgBHXMsimcSH+6d/egsjlvlVLsBpTMwAe+Itjn9vGFM2LfOARsQKcNZ+4Bn/RwNp4xy3sTfjqzZetPtAjV31NuVpUBM4x9GxWedF7HMQ+6DKgxlb4wA1CRXrRXPhhq8+MVmF3FuCfeJDsldDeHT/4rRYJdwC6IDesZXt+qDEMQriPLmfOWz+y39XA8euO2+W1+9Syiye+7OrZ4Ie9c6oowD9+1bHn4osfzT/ubK6Cnj6nu7MtB50SOGNMXbJXZZGN/LY/itwh0DfGfU2q5dqanmGdeGr2bB1lky8Y9J2p4MRk0G9KmhSKpwZNBn3jfeRiNb0cnPqb28A7sFsT03X7HtrcSJt4I3hHjabPcE4FOjBscf5+Y5jr//49aMeEg6sSi+vjqaa5KPSBBvOjwJQUoseI6wPywekmy0s/WgD0Y+nlj1n1Cw==
```

### Library JSON

Generates a JSON with all the icon XMLs.

Example output:

```json
[
  {
    "xml": "bVRtk6I4EP4rU963m6sbRNzSc9gqXhzEBdQBBfkWIRuiQSwTJfLrt4GZ2dqqo6orD91Pd56kOv1aSueKLoVf5Zh9f71Wlfj+WkoLM/ZEc32gDJ5e/nAMB08XdMVn8T8x9XcMaHd8FVj2ELEb1geDJy4eDAAv0AXrtEQEz1oazRDz0AGzdcWpoNVZP1RCVOWMtU4TZSdyrW7n3KpYddX/+tl9X5kGo+Ssi+oyQ/yCM6H/pBLns6680XuU/k/PkUD/dfCF38mzLNk/60Wgpg9TO8TyljUKRYt3JbOruzfKR/ljPPIf43tWZnf/aNS+NW3yMqPuImXZObgcVG3qHuc3P3QJijdT9yQLHO8eSTMHDoGYWWPLJThSqL8wNZeaKop3o0051dahW7u2QaBua9R1drd9vORpOKT7OLimo+U9j8endbi8pUlGfMsAvtsbbfXW37KRWezV7dQ9m480CUBTytyj9mPtZL2e8u2Uvk1k8nCfLXKapI32w9qcJpnzpiDLLFEsuZcshwcHapQ7NY3H99TZgJaAo8QQ2XnHU9CeJik7lNNTCmdJbYVG0bz2bNMOLE1ZWTVgg//G83rfwH+oDX1aK95xo7W+T8saWKPNLbAJ9yNDgBHXMsimcSH+6d/egsjlvlVLsBpTMwAe+Itjn9vGFM2LfOARsQKcNZ+4Bn/RwNp4xy3sTfjqzZetPtAjV31NuVpUBM4x9GxWedF7HMQ+6DKgxlb4wA1CRXrRXPhhq8+MVmF3FuCfeJDsldDeHT/4rRYJdwC6IDesZXt+qDEMQriPLmfOWz+y39XA8euO2+W1+9Syiye+7OrZ4Ie9c6oowD9+1bHn4osfzT/ubK6Cnj6nu7MtB50SOGNMXbJXZZGN/LY/itwh0DfGfU2q5dqanmGdeGr2bB1lky8Y9J2p4MRk0G9KmhSKpwZNBn3jfeRiNb0cnPqb28A7sFsT03X7HtrcSJt4I3hHjabPcE4FOjBscf5+Y5jr//49aMeEg6sSi+vjqaa5KPSBBvOjwJQUoseI6wPywekmy0s/WgD0Y+nlj1n1Cw==",
    "w": 310,
    "h": 310,
    "aspect": "fixed",
    "title": "add"
  }
]
```

### Library XML

Embedds the library JSON in a simple XML structure. The result can be imported as a library in draw.io.

Example output:

```xml
<mxlibrary>
[
    {
        "xml": "bVRtk6I4EP4rU963m6sbRNzSc9gqXhzEBdQBBfkWIRuiQSwTJfLrt4GZ2dqqo6orD91Pd56kOv1aSueKLoVf5Zh9f71Wlfj+WkoLM/ZEc32gDJ5e/nAMB08XdMVn8T8x9XcMaHd8FVj2ELEb1geDJy4eDAAv0AXrtEQEz1oazRDz0AGzdcWpoNVZP1RCVOWMtU4TZSdyrW7n3KpYddX/+tl9X5kGo+Ssi+oyQ/yCM6H/pBLns6680XuU/k/PkUD/dfCF38mzLNk/60Wgpg9TO8TyljUKRYt3JbOruzfKR/ljPPIf43tWZnf/aNS+NW3yMqPuImXZObgcVG3qHuc3P3QJijdT9yQLHO8eSTMHDoGYWWPLJThSqL8wNZeaKop3o0051dahW7u2QaBua9R1drd9vORpOKT7OLimo+U9j8endbi8pUlGfMsAvtsbbfXW37KRWezV7dQ9m480CUBTytyj9mPtZL2e8u2Uvk1k8nCfLXKapI32w9qcJpnzpiDLLFEsuZcshwcHapQ7NY3H99TZgJaAo8QQ2XnHU9CeJik7lNNTCmdJbYVG0bz2bNMOLE1ZWTVgg//G83rfwH+oDX1aK95xo7W+T8saWKPNLbAJ9yNDgBHXMsimcSH+6d/egsjlvlVLsBpTMwAe+Itjn9vGFM2LfOARsQKcNZ+4Bn/RwNp4xy3sTfjqzZetPtAjV31NuVpUBM4x9GxWedF7HMQ+6DKgxlb4wA1CRXrRXPhhq8+MVmF3FuCfeJDsldDeHT/4rRYJdwC6IDesZXt+qDEMQriPLmfOWz+y39XA8euO2+W1+9Syiye+7OrZ4Ie9c6oowD9+1bHn4osfzT/ubK6Cnj6nu7MtB50SOGNMXbJXZZGN/LY/itwh0DfGfU2q5dqanmGdeGr2bB1lky8Y9J2p4MRk0G9KmhSKpwZNBn3jfeRiNb0cnPqb28A7sFsT03X7HtrcSJt4I3hHjabPcE4FOjBscf5+Y5jr//49aMeEg6sSi+vjqaa5KPSBBvOjwJQUoseI6wPywekmy0s/WgD0Y+nlj1n1Cw==",
        "w": 310,
        "h": 310,
        "aspect": "fixed",
        "title": "add",
    }
]
</mxlibrary>
```

## License

`drawio-svg-library` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
