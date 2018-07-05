stockDict = { 'GM': 'General Motors',
    'CAT':'Caterpillar', 
    'EK':"Eastman Kodak" }

purchases = [ ( 'GM', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GM', 200, '1-jul-1998', 56 ) ]



for block in purchases:
    
    print(stockDict[block[0]] + ': ' + str(block[1] * block[3]))