import os

try:
    import xlwt

    no_excel = False
except ImportError as e:
    print "Error importing xlwt module. Write-to-excel functionality via '-e'/'--excel' will be disabled."
    print "xlwt module can be installed via 'pip install xlwt' on *nix and https://pypi.python.org/pypi/xlwt/0.7.2"\
          " on Win"
    print "Error message: ", e

    no_excel = True

def output_to_file(data, fname, func_str):
    # Write resulting random data to file fname

    fname += ".dat"

    if os.path.isfile(fname):
        response = str(raw_input("Warning, chosen output file already exists. Overwrite? "))
        if response.lower() in ("yes", "y"):
            print "Continuing..."
        elif response.lower() in ("no", "n"):
            print "Aborting..."
            exit(2)
        else:
            print "Unrecognised response. Aborting..."
            exit(3)

    with open(fname, "w") as output_file:
        output_file.write("Random {} distributed numbers".format(func_str))
        for i in range(len(data)):
            output_file.write("%f\n" % data[i])

    return True

def output_to_excel(data, fname, func_str):
    # Write resulting random data to excel spreadsheet fname.xlsx

    if no_excel:
        print "xlwt library not found. Excel capabilities not present.",
        print "File not written to Excel spreadsheet."

        return False

    fname += ".xlsx"
    row_limit = 65536 # Fundamental Excel limit

    if os.path.isfile(fname):
        response = str(raw_input("Warning, chosen output file already exists. Overwrite? "))
        if response.lower() in ("yes", "y"):
            print "Continuing..."
        elif response.lower() in ("no", "n"):
            print "Aborting..."
            exit(2)
        else:
            print "Unrecognised response. Aborting..."
            exit(3)

    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Random {} distribution".format(func_str))

    bold_style = xlwt.easyxf("font: bold 1")

    col_title = "Random {} distribution".format(func_str)

    sheet.write(0, 0, col_title, bold_style)

    sheet.col(0).width = 300*(len(col_title) + 1)

    for i in range(len(data)):
        if i == row_limit-1:
            print "Excel row limit of {} reached. Finishing prematurely...".format(row_limit)
            # Consider changing the phrasing here...

            workbook.save(fname)
            return True

        sheet.write(i+1, 0, data[i])

    workbook.save(fname)

    return True