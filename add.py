from openpyxl import Workbook

# Data provided with "PKT" removed
data = [
    (1, "KURVI", "10"),
    (2, "3 LAKSHMI", "5"),
    (3, "LAKSHMI", "1"),
    (4, "DELUXE LAKSHMI", "5"),
    (7, "2 SOUND", "5"),
    (8, "FLOWER POTS", "3"),
    (20, "CHIT PUT", "3"),
    (21, "DARLING DANCER", "1"),
    (22, "PHOTO FLASH CANDLE", "2"),
    (24, "TWINKLING", "8"),
    (26, "RED BIJILI", "5"),
    (28, "BIJLI GOLD", "5"),
    (30, "28 CHORAS", "4"),
    (31, "28 GIANT", "5"),
    (32, "56 GIANT", "4"),
    (37, "200 WALA", "5"),
    (38, "1000 WALA", "2"),
    (47, "BABY ROCKET", "2"),
    (50, "PHOTO FLASH", "3"),
    (54, "FANCY POPS", "1"),
    (55, "FEATHER POPS", "1"),
    (58, "CHOTTA FANCY", "2"),
    (65, "7 SHOT", "2"),
    (66, "12 SHOT", "1"),
    (80, "10CM GREEN", "4"),
    (88, "15CM GREEN", "4"),
    (94, "PEACOCK", "1"),
    (95, "RAIN COLOUR", "1"),
    (97, "HELICOPTER BATTLE", "1"),
    (98, "TIN BEER", "1"),
    (100, "DRONE", "1"),
    (118, "OLD IS GOLD", "1"),
    (119, "MONEY BANK", "2"),
    (116, "4X4 WHEEL", "1"),
]

# Create a new workbook and select the active sheet
wb = Workbook()
ws = wb.active

# Add column headers
ws.append(["ID", "Name", "Quantity"])

# Insert data into the sheet
for row in data:
    ws.append(row)

# Save the workbook
wb.save("fireworks_data.xlsx")

print("Data inserted successfully into 'fireworks_data.xlsx'")
