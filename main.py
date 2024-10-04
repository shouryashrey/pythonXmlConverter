import xml.etree.ElementTree as ET
from difflib import HtmlDiff

def parse_xml(file_path):
    """Parse XML file into ElementTree."""
    try:
        tree = ET.parse(file_path)
        return tree.getroot()
    except Exception as e:
        print(f"Error parsing XML file {file_path}: {e}")
        return None

def compare_xml_files(file1, file2):
    """Compare two XML files and return the differences as a string."""
    root1 = parse_xml(file1)
    root2 = parse_xml(file2)

    if root1 is None or root2 is None:
        return None

    # Convert XML elements to strings for line-by-line comparison
    xml1_str = ET.tostring(root1, encoding='unicode')
    xml2_str = ET.tostring(root2, encoding='unicode')

    xml1_lines = xml1_str.splitlines()
    xml2_lines = xml2_str.splitlines()

    # Use HtmlDiff from difflib to get the differences in HTML format
    differ = HtmlDiff()
    html_diff = differ.make_file(xml1_lines, xml2_lines, file1, file2)

    return html_diff

def save_diff_as_html(html_diff, output_file):
    """Save the HTML diff as a file."""
    with open(output_file, 'w') as f:
        f.write(html_diff)
    print(f"HTML difference saved as {output_file}")

# Paths to the XML files you want to compare
file1 = 'assets/file1.xml'
file2 = 'assets/file2.xml'
output_html = 'output/xml_diff.html'

# Generate the difference in HTML format and save it
html_diff = compare_xml_files(file1, file2)
if html_diff:
    save_diff_as_html(html_diff, output_html)
