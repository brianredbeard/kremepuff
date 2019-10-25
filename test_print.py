import escpos.printer

p = escpos.printer.Serial('/dev/ttyUSB0')
p.text("Hello World\n")
#p.barcode('1324354657680', 'EAN13', 64, 2, '', '')
p.barcode('4006381333931', 'EAN13', 64, 2, '', '')
p.qr('stuff/things', ec=escpos.escpos.QR_ECLEVEL_H, center=True, size=8)

p.cut()
