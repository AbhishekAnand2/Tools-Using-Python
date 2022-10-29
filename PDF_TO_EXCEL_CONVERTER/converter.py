import tabula
import openpyxl

df = tabula.read_pdf(r"C:\Users\as196\Downloads\DBO323PAIDINVOICEOCT22.pdf", pages = 1)[0]
print("Converting......")
tabula.convert_into(r"C:\Users\as196\Downloads\DBO323PAIDINVOICEOCT22.pdf", r"C:\Users\as196\Downloads\DBO323PAIDINVOICEOCT22.csv", output_format="csv", pages=1)
print("Converted......")