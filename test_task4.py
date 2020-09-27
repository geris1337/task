import os, pytest, subprocess
from os import listdir
from os.path import isfile, join

def prepare():
    multilist = []
    files = [f for f in listdir('data') if isfile(join('data', f))]

    for item in files:
        if item.endswith("input.txt"):
            inputfile = 'data/' + item
            outputfile = 'data/' + item.replace("input.txt", "processed.txt")
            subprocess.call(['python3', 'upper_case_file.py', '--input-file', inputfile, '--output-file', outputfile])
	    # Prepare comparison file multilist
            first = "data/%s" % (item.replace("input.txt", "processed.txt")),
            second = "data/%s" % (item.replace("input.txt", "output.txt")),
            multilist += list(zip(first, second))

    return multilist

@pytest.mark.parametrize("filepath", prepare())
def test_min(filepath):
    with open(filepath[0], 'r') as file1:
        data1 = file1.read().replace('\r\n', '\n').replace('\n', '')
    with open(filepath[1], 'r') as file2:
        data2 = file2.read().replace('\r\n', '\n').replace('\n', '')
    
    assert data1 == data2
