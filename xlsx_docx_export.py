import csv
import docx
from docx.shared import Pt


def xlsx_xprt(name: str, header: list, data: list) -> None:
    """Saves the read information from the database as an excel table"""

    with open(f"{name}.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        writer.writerows(data)


def docx_xprt(name:str, data: list) -> None:
    """Saves the read information from the database as a docx document"""

    doc = docx.Document()
    style = doc.styles["Normal"]
    style.font.name = "Arial"
    style.font.size = Pt(14)
    for d in data:
        doc.add_paragraph(d)
    doc.save(f"{name}.docx")

