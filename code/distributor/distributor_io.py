# In-built libraries
import re
import os

# Try to import Excel writing library
try:
    import xlwt
    has_xlwt = True
except ImportError as e:
    print "[Error] Error importing xlwt module. Write-to-excel functionality via '-e'/'--excel' will be disabled."
    print "[Error] xlwt module can be installed via 'pip install xlwt' on *nix and https://pypi.python.org/pypi/xlwt/0.7.2"\
          " on Win"
    print "[Error] Error message: ", e
    has_xlwt = False

def output_to_file(data, fname, func_str):
    # Write resulting 2d detection data to file fname.dat

    if not is_valid_fname(fname):
        print "[Error] Invalid filename:", fname
        print "[Error] Please use only lower and upper alphanumerics, full stop, underscore and hyphen."
        print "[Error] Data not written to file."
        return False

    fname = "data/" + fname + ".dat"

    if os.path.isfile(fname):
        response = str(raw_input("[Warning] Chosen output file already exists. Overwrite? "))
        if response.lower() in ("yes", "y"):
            print "Continuing..."
        elif response.lower() in ("no", "n"):
            print "Aborting..."
            exit(2)
        else:
            print "[Error] Unrecognised response. Aborting..."
            exit(3)

    with open(fname, "w") as output_file:
        output_file.write("Detector Readings\n")
        for value in data:
            output_file.write("%f\n" % value)

    return True

def output_to_excel(data, fname, func_str):
    # Write resulting 2d detection data to excel spreadsheet fname.xlsx

    if not is_valid_fname(fname):
        print "[Error] Invalid filename:", fname
        print "[Error] Please use only lower and upper alphanumerics, full stop, underscore and hyphen."
        print "[Error] Data not written to Excel spreadsheet."
        return False

    if not has_xlwt:
        print "[Error] xlwt library not found. Excel capabilities not present.",
        print "[Error] File not written to Excel spreadsheet."

        return False

    fname = "data/" + fname + ".xlsx"
    row_limit = 65536 # Fundamental Excel limit

    if os.path.isfile(fname):
        response = str(raw_input("[Warning] Chosen output file already exists. Overwrite? "))
        if response.lower() in ("yes", "y"):
            print "Continuing..."
        elif response.lower() in ("no", "n"):
            print "Aborting..."
            exit(2)
        else:
            print "[Error] Unrecognised response. Aborting..."
            exit(3)

    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("Random {} distribution".format(func_str))

    bold_style = xlwt.easyxf("font: bold 1")

    col_title = "Random {} distribution".format(func_str)

    sheet.write(0, 0, col_title, bold_style)

    sheet.col(0).width = 300*(len(col_title) + 1)

    for i in range(len(data)):
        if i == row_limit - 1:
            print "[Warning] Excel row limit of {} reached. Finishing prematurely.".format(row_limit)
            # Consider changing the phrasing here...

            workbook.save(fname)
            return True

        sheet.write(i+1, 0, data[i])

    workbook.save(fname)

    return True
    
def is_valid_fname(fname):
    # Check that fname is a valid pathname (i.e. contains only alphanumerics, 
    # full stop, underscore or hyphen)

    if re.search(r'[^A-Za-z0-9._-]', fname):
        return False
    else:
        return True
