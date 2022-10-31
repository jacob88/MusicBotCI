from typing import TYPE_CHECKING
from pathlib import Path
from lxml import etree

if TYPE_CHECKING:
    from lxml.etree import _ElementTree, _Element

NAMESPACES = {"pom": "http://maven.apache.org/POM/4.0.0"}


def tag_pom(version: str, file: Path):
    """Updates POM project file (pom.xml) with version string passed to command.

    Parameters
    ----------
    version : str
        _description_
    file : Path
        _description_
    """

    # Load POM project file
    parser = etree.XMLParser(ns_clean=True)
    tree: "_ElementTree" = etree.parse(file, parser)
    et: "_ElementTree" = etree.ElementTree(tree.getroot())

    # Xpath to and update version
    version_element: "_Element" = et.xpath(
        "/pom:project/pom:version",
        namespaces=NAMESPACES,
    )[0]
    version_element.text = version

    # Write updated XML tree to file
    et.write(file, pretty_print=True, xml_declaration=True, encoding="UTF-8")
